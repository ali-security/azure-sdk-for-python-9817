# The MIT License (MIT)
# Copyright (c) Microsoft Corporation. All rights reserved.

import unittest
import uuid
from datetime import datetime, timedelta, timezone
from time import sleep
import pytest

import azure.cosmos._retry_utility as retry_utility
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
import test_config
from azure.cosmos import http_constants, DatabaseProxy
from azure.cosmos._execution_context.base_execution_context import _QueryExecutionContextBase
from azure.cosmos._execution_context.query_execution_info import _PartitionedQueryExecutionInfo
from azure.cosmos.documents import _DistinctType
from azure.cosmos.partition_key import PartitionKey


@pytest.mark.cosmosEmulator
class TestQuery(unittest.TestCase):
    """Test to ensure escaping of non-ascii characters from partition key"""

    created_db: DatabaseProxy = None
    client: cosmos_client.CosmosClient = None
    config = test_config.TestConfig
    host = config.host
    masterKey = config.masterKey
    connectionPolicy = config.connectionPolicy
    TEST_DATABASE_ID = config.TEST_DATABASE_ID

    @classmethod
    def setUpClass(cls):
        if (cls.masterKey == '[YOUR_KEY_HERE]' or
                cls.host == '[YOUR_ENDPOINT_HERE]'):
            raise Exception(
                "You must specify your Azure Cosmos account values for "
                "'masterKey' and 'host' at the top of this class to run the "
                "tests.")

        cls.client = cosmos_client.CosmosClient(cls.host, cls.masterKey)
        cls.created_db = cls.client.get_database_client(cls.TEST_DATABASE_ID)

    def test_first_and_last_slashes_trimmed_for_query_string(self):
        created_collection = self.created_db.create_container(
            "test_trimmed_slashes", PartitionKey(path="/pk"))
        doc_id = 'myId' + str(uuid.uuid4())
        document_definition = {'pk': 'pk', 'id': doc_id}
        created_collection.create_item(body=document_definition)

        query = 'SELECT * from c'
        query_iterable = created_collection.query_items(
            query=query,
            partition_key='pk'
        )
        iter_list = list(query_iterable)
        self.assertEqual(iter_list[0]['id'], doc_id)
        self.created_db.delete_container(created_collection.id)

    def test_query_change_feed_with_pk(self):
        created_collection = self.created_db.create_container("change_feed_test_" + str(uuid.uuid4()),
                                                              PartitionKey(path="/pk"))
        # The test targets partition #3
        partition_key = "pk"

        # Read change feed without passing any options
        query_iterable = created_collection.query_items_change_feed()
        iter_list = list(query_iterable)
        self.assertEqual(len(iter_list), 0)

        # Read change feed from current should return an empty list
        query_iterable = created_collection.query_items_change_feed(partition_key=partition_key)
        iter_list = list(query_iterable)
        self.assertEqual(len(iter_list), 0)
        self.assertTrue('etag' in created_collection.client_connection.last_response_headers)
        self.assertNotEqual(created_collection.client_connection.last_response_headers['etag'], '')

        # Read change feed from beginning should return an empty list
        query_iterable = created_collection.query_items_change_feed(
            is_start_from_beginning=True,
            partition_key=partition_key
        )
        iter_list = list(query_iterable)
        self.assertEqual(len(iter_list), 0)
        self.assertTrue('etag' in created_collection.client_connection.last_response_headers)
        continuation1 = created_collection.client_connection.last_response_headers['etag']
        self.assertNotEqual(continuation1, '')

        # Create a document. Read change feed should return be able to read that document
        document_definition = {'pk': 'pk', 'id': 'doc1'}
        created_collection.create_item(body=document_definition)
        query_iterable = created_collection.query_items_change_feed(
            is_start_from_beginning=True,
            partition_key=partition_key
        )
        iter_list = list(query_iterable)
        self.assertEqual(len(iter_list), 1)
        self.assertEqual(iter_list[0]['id'], 'doc1')
        self.assertTrue('etag' in created_collection.client_connection.last_response_headers)
        continuation2 = created_collection.client_connection.last_response_headers['etag']
        self.assertNotEqual(continuation2, '')
        self.assertNotEqual(continuation2, continuation1)

        # Create two new documents. Verify that change feed contains the 2 new documents
        # with page size 1 and page size 100
        document_definition = {'pk': 'pk', 'id': 'doc2'}
        created_collection.create_item(body=document_definition)
        document_definition = {'pk': 'pk', 'id': 'doc3'}
        created_collection.create_item(body=document_definition)

        for pageSize in [1, 100]:
            # verify iterator
            query_iterable = created_collection.query_items_change_feed(
                continuation=continuation2,
                max_item_count=pageSize,
                partition_key=partition_key
            )
            it = query_iterable.__iter__()
            expected_ids = 'doc2.doc3.'
            actual_ids = ''
            for item in it:
                actual_ids += item['id'] + '.'
            self.assertEqual(actual_ids, expected_ids)

            # verify by_page
            # the options is not copied, therefore it need to be restored
            query_iterable = created_collection.query_items_change_feed(
                continuation=continuation2,
                max_item_count=pageSize,
                partition_key=partition_key
            )
            count = 0
            expected_count = 2
            all_fetched_res = []
            for page in query_iterable.by_page():
                fetched_res = list(page)
                self.assertEqual(len(fetched_res), min(pageSize, expected_count - count))
                count += len(fetched_res)
                all_fetched_res.extend(fetched_res)

            actual_ids = ''
            for item in all_fetched_res:
                actual_ids += item['id'] + '.'
            self.assertEqual(actual_ids, expected_ids)

        # verify reading change feed from the beginning
        query_iterable = created_collection.query_items_change_feed(
            is_start_from_beginning=True,
            partition_key=partition_key
        )
        expected_ids = ['doc1', 'doc2', 'doc3']
        it = query_iterable.__iter__()
        for i in range(0, len(expected_ids)):
            doc = next(it)
            self.assertEqual(doc['id'], expected_ids[i])
        self.assertTrue('etag' in created_collection.client_connection.last_response_headers)
        continuation3 = created_collection.client_connection.last_response_headers['etag']

        # verify reading empty change feed
        query_iterable = created_collection.query_items_change_feed(
            continuation=continuation3,
            is_start_from_beginning=True,
            partition_key=partition_key
        )
        iter_list = list(query_iterable)
        self.assertEqual(len(iter_list), 0)
        self.created_db.delete_container(created_collection.id)

    # TODO: partition key range id 0 is relative to the way collection is created
    @pytest.mark.skip
    def test_query_change_feed_with_pk_range_id(self):
        created_collection = self.created_db.create_container("change_feed_test_" + str(uuid.uuid4()),
                                                              PartitionKey(path="/pk"))
        # The test targets partition #3
        partition_key_range_id = 0
        partitionParam = {"partition_key_range_id": partition_key_range_id}

        # Read change feed without passing any options
        query_iterable = created_collection.query_items_change_feed()
        iter_list = list(query_iterable)
        self.assertEqual(len(iter_list), 0)

        # Read change feed from current should return an empty list
        query_iterable = created_collection.query_items_change_feed(**partitionParam)
        iter_list = list(query_iterable)
        self.assertEqual(len(iter_list), 0)
        self.assertTrue('etag' in created_collection.client_connection.last_response_headers)
        self.assertNotEqual(created_collection.client_connection.last_response_headers['etag'], '')

        # Read change feed from beginning should return an empty list
        query_iterable = created_collection.query_items_change_feed(
            is_start_from_beginning=True,
            **partitionParam
        )
        iter_list = list(query_iterable)
        self.assertEqual(len(iter_list), 0)
        self.assertTrue('etag' in created_collection.client_connection.last_response_headers)
        continuation1 = created_collection.client_connection.last_response_headers['etag']
        self.assertNotEqual(continuation1, '')

        # Create a document. Read change feed should return be able to read that document
        document_definition = {'pk': 'pk', 'id': 'doc1'}
        created_collection.create_item(body=document_definition)
        query_iterable = created_collection.query_items_change_feed(
            is_start_from_beginning=True,
            **partitionParam
        )
        iter_list = list(query_iterable)
        self.assertEqual(len(iter_list), 1)
        self.assertEqual(iter_list[0]['id'], 'doc1')
        self.assertTrue('etag' in created_collection.client_connection.last_response_headers)
        continuation2 = created_collection.client_connection.last_response_headers['etag']
        self.assertNotEqual(continuation2, '')
        self.assertNotEqual(continuation2, continuation1)

        # Create two new documents. Verify that change feed contains the 2 new documents
        # with page size 1 and page size 100
        document_definition = {'pk': 'pk', 'id': 'doc2'}
        created_collection.create_item(body=document_definition)
        document_definition = {'pk': 'pk', 'id': 'doc3'}
        created_collection.create_item(body=document_definition)

        for pageSize in [1, 100]:
            # verify iterator
            query_iterable = created_collection.query_items_change_feed(
                continuation=continuation2,
                max_item_count=pageSize,
                **partitionParam
            )
            it = query_iterable.__iter__()
            expected_ids = 'doc2.doc3.'
            actual_ids = ''
            for item in it:
                actual_ids += item['id'] + '.'
            self.assertEqual(actual_ids, expected_ids)

            # verify by_page
            # the options is not copied, therefore it need to be restored
            query_iterable = created_collection.query_items_change_feed(
                continuation=continuation2,
                max_item_count=pageSize,
                **partitionParam
            )
            count = 0
            expected_count = 2
            all_fetched_res = []
            for page in query_iterable.by_page():
                fetched_res = list(page)
                self.assertEqual(len(fetched_res), min(pageSize, expected_count - count))
                count += len(fetched_res)
                all_fetched_res.extend(fetched_res)

            actual_ids = ''
            for item in all_fetched_res:
                actual_ids += item['id'] + '.'
            self.assertEqual(actual_ids, expected_ids)

        # verify reading change feed from the beginning
        query_iterable = created_collection.query_items_change_feed(
            is_start_from_beginning=True,
            **partitionParam
        )
        expected_ids = ['doc1', 'doc2', 'doc3']
        it = query_iterable.__iter__()
        for i in range(0, len(expected_ids)):
            doc = next(it)
            self.assertEqual(doc['id'], expected_ids[i])
        self.assertTrue('etag' in created_collection.client_connection.last_response_headers)
        continuation3 = created_collection.client_connection.last_response_headers['etag']

        # verify reading empty change feed
        query_iterable = created_collection.query_items_change_feed(
            continuation=continuation3,
            is_start_from_beginning=True,
            **partitionParam
        )
        iter_list = list(query_iterable)
        self.assertEqual(len(iter_list), 0)
        self.created_db.delete_container(created_collection.id)

    def test_query_change_feed_with_start_time(self):
        created_collection = self.created_db.create_container_if_not_exists("query_change_feed_start_time_test",
                                                                            PartitionKey(path="/pk"))
        batchSize = 50

        def round_time():
            utc_now = datetime.now(timezone.utc)
            return utc_now - timedelta(microseconds=utc_now.microsecond)
        def create_random_items(container, batch_size):
            for _ in range(batch_size):
                # Generate a Random partition key
                partition_key = 'pk' + str(uuid.uuid4())

                # Generate a random item
                item = {
                    'id': 'item' + str(uuid.uuid4()),
                    'partitionKey': partition_key,
                    'content': 'This is some random content',
                }

                try:
                    # Create the item in the container
                    container.upsert_item(item)
                except exceptions.CosmosHttpResponseError as e:
                    self.fail(e)

        # Create first batch of random items
        create_random_items(created_collection, batchSize)

        # wait for 1 second and record the time, then wait another second
        sleep(1)
        start_time = round_time()
        not_utc_time = datetime.now()
        sleep(1)

        # now create another batch of items
        create_random_items(created_collection, batchSize)

        # now query change feed based on start time
        change_feed_iter = list(created_collection.query_items_change_feed(start_time=start_time))
        totalCount = len(change_feed_iter)

        # now check if the number of items that were changed match the batch size
        self.assertEqual(totalCount, batchSize)

        # negative test: pass in a valid time in the future
        future_time = start_time + timedelta(hours=1)
        change_feed_iter = list(created_collection.query_items_change_feed(start_time=future_time))
        totalCount = len(change_feed_iter)
        # A future time should return 0
        self.assertEqual(totalCount, 0)

        # test a date that is not utc, will be converted to utc by sdk
        change_feed_iter = list(created_collection.query_items_change_feed(start_time=not_utc_time))
        totalCount = len(change_feed_iter)
        # Should equal batch size
        self.assertEqual(totalCount, batchSize)

        # test an invalid value, Attribute error will be raised for passing non datetime object
        invalid_time = "Invalid value"
        try:
            change_feed_iter = list(created_collection.query_items_change_feed(start_time=invalid_time))
            self.fail("Cannot format date on a non datetime object.")
        except AttributeError as e:
            self.assertTrue("'str' object has no attribute 'astimezone'" == e.args[0])

    def test_populate_query_metrics(self):
        created_collection = self.created_db.create_container("query_metrics_test",
                                                              PartitionKey(path="/pk"))
        doc_id = 'MyId' + str(uuid.uuid4())
        document_definition = {'pk': 'pk', 'id': doc_id}
        created_collection.create_item(body=document_definition)

        query = 'SELECT * from c'
        query_iterable = created_collection.query_items(
            query=query,
            partition_key='pk',
            populate_query_metrics=True
        )

        iter_list = list(query_iterable)
        self.assertEqual(iter_list[0]['id'], doc_id)

        METRICS_HEADER_NAME = 'x-ms-documentdb-query-metrics'
        self.assertTrue(METRICS_HEADER_NAME in created_collection.client_connection.last_response_headers)
        metrics_header = created_collection.client_connection.last_response_headers[METRICS_HEADER_NAME]
        # Validate header is well-formed: "key1=value1;key2=value2;etc"
        metrics = metrics_header.split(';')
        self.assertTrue(len(metrics) > 1)
        self.assertTrue(all(['=' in x for x in metrics]))
        self.created_db.delete_container(created_collection.id)

    def test_populate_index_metrics(self):
        created_collection = self.created_db.create_container("query_index_test",
                                                              PartitionKey(path="/pk"))

        doc_id = 'MyId' + str(uuid.uuid4())
        document_definition = {'pk': 'pk', 'id': doc_id}
        created_collection.create_item(body=document_definition)

        query = 'SELECT * from c'
        query_iterable = created_collection.query_items(
            query=query,
            partition_key='pk',
            populate_index_metrics=True
        )

        iter_list = list(query_iterable)
        self.assertEqual(iter_list[0]['id'], doc_id)

        INDEX_HEADER_NAME = http_constants.HttpHeaders.IndexUtilization
        self.assertTrue(INDEX_HEADER_NAME in created_collection.client_connection.last_response_headers)
        index_metrics = created_collection.client_connection.last_response_headers[INDEX_HEADER_NAME]
        self.assertIsNotNone(index_metrics)
        expected_index_metrics = {'UtilizedSingleIndexes': [{'FilterExpression': '', 'IndexSpec': '/pk/?',
                                                             'FilterPreciseSet': True, 'IndexPreciseSet': True,
                                                             'IndexImpactScore': 'High'}],
                                  'PotentialSingleIndexes': [], 'UtilizedCompositeIndexes': [],
                                  'PotentialCompositeIndexes': []}
        self.assertDictEqual(expected_index_metrics, index_metrics)
        self.created_db.delete_container(created_collection.id)

    # TODO: Need to validate the query request count logic
    @pytest.mark.skip
    def test_max_item_count_honored_in_order_by_query(self):
        created_collection = self.created_db.create_container("test-max-item-count" + str(uuid.uuid4()),
                                                              PartitionKey(path="/pk"))
        docs = []
        for i in range(10):
            document_definition = {'pk': 'pk', 'id': 'myId' + str(uuid.uuid4())}
            docs.append(created_collection.create_item(body=document_definition))

        query = 'SELECT * from c ORDER BY c._ts'
        query_iterable = created_collection.query_items(
            query=query,
            max_item_count=1,
            enable_cross_partition_query=True
        )
        self.validate_query_requests_count(query_iterable, 25)

        query_iterable = created_collection.query_items(
            query=query,
            max_item_count=100,
            enable_cross_partition_query=True
        )

        self.validate_query_requests_count(query_iterable, 5)
        self.created_db.delete_container(created_collection.id)

    def validate_query_requests_count(self, query_iterable, expected_count):
        self.count = 0
        self.OriginalExecuteFunction = retry_utility.ExecuteFunction
        retry_utility.ExecuteFunction = self._MockExecuteFunction
        for block in query_iterable.by_page():
            assert len(list(block)) != 0
        retry_utility.ExecuteFunction = self.OriginalExecuteFunction
        self.assertEqual(self.count, expected_count)
        self.count = 0

    def _MockExecuteFunction(self, function, *args, **kwargs):
        self.count += 1
        return self.OriginalExecuteFunction(function, *args, **kwargs)

    def test_get_query_plan_through_gateway(self):
        created_collection = self.created_db.get_container_client(self.config.TEST_MULTI_PARTITION_CONTAINER_ID)
        self._validate_query_plan(query="Select top 10 value count(c.id) from c",
                                  container_link=created_collection.container_link,
                                  top=10,
                                  order_by=[],
                                  aggregate=['Count'],
                                  select_value=True,
                                  offset=None,
                                  limit=None,
                                  distinct=_DistinctType.NoneType)

        self._validate_query_plan(query="Select * from c order by c._ts offset 5 limit 10",
                                  container_link=created_collection.container_link,
                                  top=None,
                                  order_by=['Ascending'],
                                  aggregate=[],
                                  select_value=False,
                                  offset=5,
                                  limit=10,
                                  distinct=_DistinctType.NoneType)

        self._validate_query_plan(query="Select distinct value c.id from c order by c.id",
                                  container_link=created_collection.container_link,
                                  top=None,
                                  order_by=['Ascending'],
                                  aggregate=[],
                                  select_value=True,
                                  offset=None,
                                  limit=None,
                                  distinct=_DistinctType.Ordered)

    def _validate_query_plan(self, query, container_link, top, order_by, aggregate, select_value, offset, limit,
                             distinct):
        query_plan_dict = self.client.client_connection._GetQueryPlanThroughGateway(query, container_link)
        query_execution_info = _PartitionedQueryExecutionInfo(query_plan_dict)
        self.assertTrue(query_execution_info.has_rewritten_query())
        self.assertEqual(query_execution_info.has_distinct_type(), distinct != "None")
        self.assertEqual(query_execution_info.get_distinct_type(), distinct)
        self.assertEqual(query_execution_info.has_top(), top is not None)
        self.assertEqual(query_execution_info.get_top(), top)
        self.assertEqual(query_execution_info.has_order_by(), len(order_by) > 0)
        self.assertListEqual(query_execution_info.get_order_by(), order_by)
        self.assertEqual(query_execution_info.has_aggregates(), len(aggregate) > 0)
        self.assertListEqual(query_execution_info.get_aggregates(), aggregate)
        self.assertEqual(query_execution_info.has_select_value(), select_value)
        self.assertEqual(query_execution_info.has_offset(), offset is not None)
        self.assertEqual(query_execution_info.get_offset(), offset)
        self.assertEqual(query_execution_info.has_limit(), limit is not None)
        self.assertEqual(query_execution_info.get_limit(), limit)

    def test_unsupported_queries(self):
        created_collection = self.created_db.get_container_client(self.config.TEST_MULTI_PARTITION_CONTAINER_ID)
        queries = ['SELECT COUNT(1) FROM c', 'SELECT COUNT(1) + 5 FROM c', 'SELECT COUNT(1) + SUM(c) FROM c']
        for query in queries:
            query_iterable = created_collection.query_items(query=query, enable_cross_partition_query=True)
            try:
                list(query_iterable)
                self.fail()
            except exceptions.CosmosHttpResponseError as e:
                self.assertEqual(e.status_code, 400)

    def test_query_with_non_overlapping_pk_ranges(self):
        created_collection = self.created_db.get_container_client(self.config.TEST_MULTI_PARTITION_CONTAINER_ID)
        query_iterable = created_collection.query_items("select * from c where c.pk='1' or c.pk='2'",
                                                        enable_cross_partition_query=True)
        self.assertListEqual(list(query_iterable), [])

    def test_offset_limit(self):
        created_collection = self.created_db.create_container("offset_limit_test_" + str(uuid.uuid4()),
                                                              PartitionKey(path="/pk"))
        values = []
        for i in range(10):
            document_definition = {'pk': i, 'id': 'myId' + str(uuid.uuid4()), 'value': i // 3}
            values.append(created_collection.create_item(body=document_definition)['pk'])

        self._validate_distinct_offset_limit(created_collection=created_collection,
                                             query='SELECT DISTINCT c["value"] from c ORDER BY c.pk OFFSET 0 LIMIT 2',
                                             results=[0, 1])

        self._validate_distinct_offset_limit(created_collection=created_collection,
                                             query='SELECT DISTINCT c["value"] from c ORDER BY c.pk OFFSET 2 LIMIT 2',
                                             results=[2, 3])

        self._validate_distinct_offset_limit(created_collection=created_collection,
                                             query='SELECT DISTINCT c["value"] from c ORDER BY c.pk OFFSET 4 LIMIT 3',
                                             results=[])

        self._validate_offset_limit(created_collection=created_collection,
                                    query='SELECT * from c ORDER BY c.pk OFFSET 0 LIMIT 5',
                                    results=values[:5])

        self._validate_offset_limit(created_collection=created_collection,
                                    query='SELECT * from c ORDER BY c.pk OFFSET 5 LIMIT 10',
                                    results=values[5:])

        self._validate_offset_limit(created_collection=created_collection,
                                    query='SELECT * from c ORDER BY c.pk OFFSET 10 LIMIT 5',
                                    results=[])

        self._validate_offset_limit(created_collection=created_collection,
                                    query='SELECT * from c ORDER BY c.pk OFFSET 100 LIMIT 1',
                                    results=[])
        self.created_db.delete_container(created_collection.id)

    def _validate_offset_limit(self, created_collection, query, results):
        query_iterable = created_collection.query_items(
            query=query,
            enable_cross_partition_query=True
        )
        self.assertListEqual(list(map(lambda doc: doc['pk'], list(query_iterable))), results)

    def _validate_distinct_offset_limit(self, created_collection, query, results):
        query_iterable = created_collection.query_items(
            query=query,
            enable_cross_partition_query=True
        )
        self.assertListEqual(list(map(lambda doc: doc["value"], list(query_iterable))), results)

    def test_distinct(self):
        distinct_field = 'distinct_field'
        pk_field = "pk"
        different_field = "different_field"

        created_collection = self.created_db.create_container(
            id='collection with composite index ' + str(uuid.uuid4()),
            partition_key=PartitionKey(path="/pk", kind="Hash"),
            indexing_policy={
                "compositeIndexes": [
                    [{"path": "/" + pk_field, "order": "ascending"},
                     {"path": "/" + distinct_field, "order": "ascending"}],
                    [{"path": "/" + distinct_field, "order": "ascending"},
                     {"path": "/" + pk_field, "order": "ascending"}]
                ]
            }
        )
        documents = []
        for i in range(5):
            j = i
            while j > i - 5:
                document_definition = {pk_field: i, 'id': str(uuid.uuid4()), distinct_field: j}
                documents.append(created_collection.create_item(body=document_definition))
                document_definition = {pk_field: i, 'id': str(uuid.uuid4()), distinct_field: j}
                documents.append(created_collection.create_item(body=document_definition))
                document_definition = {pk_field: i, 'id': str(uuid.uuid4())}
                documents.append(created_collection.create_item(body=document_definition))
                j -= 1

        padded_docs = self.config._pad_with_none(documents, distinct_field)

        self._validate_distinct(created_collection=created_collection,  # returns {} and is right number
                                query='SELECT distinct c.%s from c' % distinct_field,  # nosec
                                results=self.config._get_distinct_docs(padded_docs, distinct_field, None, False),
                                is_select=True,
                                fields=[distinct_field])

        self._validate_distinct(created_collection=created_collection,
                                query='SELECT distinct c.%s, c.%s from c' % (distinct_field, pk_field),  # nosec
                                results=self.config._get_distinct_docs(padded_docs, distinct_field, pk_field, False),
                                is_select=True,
                                fields=[distinct_field, pk_field])

        self._validate_distinct(created_collection=created_collection,
                                query='SELECT distinct value c.%s from c' % distinct_field,  # nosec
                                results=self.config._get_distinct_docs(padded_docs, distinct_field, None, True),
                                is_select=True,
                                fields=[distinct_field])

        self._validate_distinct(created_collection=created_collection,
                                query='SELECT distinct c.%s from c' % different_field,  # nosec
                                results=['None'],
                                is_select=True,
                                fields=[different_field])

        self.created_db.delete_container(created_collection.id)

    def _validate_distinct(self, created_collection, query, results, is_select, fields):
        query_iterable = created_collection.query_items(
            query=query,
            enable_cross_partition_query=True
        )
        query_results = list(query_iterable)

        self.assertEqual(len(results), len(query_results))
        query_results_strings = []
        result_strings = []
        for i in range(len(results)):
            query_results_strings.append(self.config._get_query_result_string(query_results[i], fields))
            result_strings.append(str(results[i]))
        if is_select:
            query_results_strings = sorted(query_results_strings)
            result_strings = sorted(result_strings)
        self.assertListEqual(result_strings, query_results_strings)

    def test_distinct_on_different_types_and_field_orders(self):
        created_collection = self.created_db.create_container(
            id="test-distinct-container-" + str(uuid.uuid4()),
            partition_key=PartitionKey("/pk"),
            offer_throughput=self.config.THROUGHPUT_FOR_5_PARTITIONS)
        self.payloads = [
            {'f1': 1, 'f2': 'value', 'f3': 100000000000000000, 'f4': [1, 2, '3'], 'f5': {'f6': {'f7': 2}}},
            {'f2': '\'value', 'f4': [1.0, 2, '3'], 'f5': {'f6': {'f7': 2.0}}, 'f1': 1.0, 'f3': 100000000000000000.00},
            {'f3': 100000000000000000.0, 'f5': {'f6': {'f7': 2}}, 'f2': '\'value', 'f1': 1, 'f4': [1, 2.0, '3']}
        ]
        self.OriginalExecuteFunction = _QueryExecutionContextBase.__next__
        _QueryExecutionContextBase.__next__ = self._MockNextFunction

        self._validate_distinct_on_different_types_and_field_orders(
            collection=created_collection,
            query="Select distinct value c.f1 from c",
            expected_results=[1],
            get_mock_result=lambda x, i: (None, x[i]["f1"])
        )

        self._validate_distinct_on_different_types_and_field_orders(
            collection=created_collection,
            query="Select distinct value c.f2 from c",
            expected_results=['value', '\'value'],
            get_mock_result=lambda x, i: (None, x[i]["f2"])
        )

        self._validate_distinct_on_different_types_and_field_orders(
            collection=created_collection,
            query="Select distinct value c.f2 from c order by c.f2",
            expected_results=['\'value', 'value'],
            get_mock_result=lambda x, i: (x[i]["f2"], x[i]["f2"])
        )

        self._validate_distinct_on_different_types_and_field_orders(
            collection=created_collection,
            query="Select distinct value c.f3 from c",
            expected_results=[100000000000000000],
            get_mock_result=lambda x, i: (None, x[i]["f3"])
        )

        self._validate_distinct_on_different_types_and_field_orders(
            collection=created_collection,
            query="Select distinct value c.f4 from c",
            expected_results=[[1, 2, '3']],
            get_mock_result=lambda x, i: (None, x[i]["f4"])
        )

        self._validate_distinct_on_different_types_and_field_orders(
            collection=created_collection,
            query="Select distinct value c.f5.f6 from c",
            expected_results=[{'f7': 2}],
            get_mock_result=lambda x, i: (None, x[i]["f5"]["f6"])
        )

        self._validate_distinct_on_different_types_and_field_orders(
            collection=created_collection,
            query="Select distinct c.f1, c.f2, c.f3 from c",
            expected_results=[self.payloads[0], self.payloads[1]],
            get_mock_result=lambda x, i: (None, x[i])
        )

        self._validate_distinct_on_different_types_and_field_orders(
            collection=created_collection,
            query="Select distinct c.f1, c.f2, c.f3 from c order by c.f1",
            expected_results=[self.payloads[0], self.payloads[1]],
            get_mock_result=lambda x, i: (i, x[i])
        )

        _QueryExecutionContextBase.__next__ = self.OriginalExecuteFunction
        _QueryExecutionContextBase.next = self.OriginalExecuteFunction

        self.created_db.delete_container(created_collection.id)

    def test_paging_with_continuation_token(self):
        created_collection = self.created_db.get_container_client(self.config.TEST_MULTI_PARTITION_CONTAINER_ID)

        document_definition = {'pk': 'pk', 'id': '1'}
        created_collection.create_item(body=document_definition)
        document_definition = {'pk': 'pk', 'id': '2'}
        created_collection.create_item(body=document_definition)

        query = 'SELECT * from c'
        query_iterable = created_collection.query_items(
            query=query,
            partition_key='pk',
            max_item_count=1
        )
        pager = query_iterable.by_page()
        pager.next()
        token = pager.continuation_token
        second_page = list(pager.next())[0]

        pager = query_iterable.by_page(token)
        second_page_fetched_with_continuation_token = list(pager.next())[0]

        self.assertEqual(second_page['id'], second_page_fetched_with_continuation_token['id'])

    def test_cross_partition_query_with_continuation_token(self):
        created_collection = self.created_db.get_container_client(self.config.TEST_MULTI_PARTITION_CONTAINER_ID)
        document_definition = {'pk': 'pk1', 'id': str(uuid.uuid4())}
        created_collection.create_item(body=document_definition)
        document_definition = {'pk': 'pk2', 'id': str(uuid.uuid4())}
        created_collection.create_item(body=document_definition)

        query = 'SELECT * from c'
        query_iterable = created_collection.query_items(
            query=query,
            enable_cross_partition_query=True,
            max_item_count=1,
        )
        pager = query_iterable.by_page()
        pager.next()
        token = pager.continuation_token
        second_page = list(pager.next())[0]

        pager = query_iterable.by_page(token)
        second_page_fetched_with_continuation_token = list(pager.next())[0]

        self.assertEqual(second_page['id'], second_page_fetched_with_continuation_token['id'])

    def _validate_distinct_on_different_types_and_field_orders(self, collection, query, expected_results,
                                                               get_mock_result):
        self.count = 0
        self.get_mock_result = get_mock_result
        query_iterable = collection.query_items(query, enable_cross_partition_query=True)
        results = list(query_iterable)
        for i in range(len(expected_results)):
            if isinstance(results[i], dict):
                self.assertDictEqual(results[i], expected_results[i])
            elif isinstance(results[i], list):
                self.assertListEqual(results[i], expected_results[i])
            else:
                self.assertEqual(results[i], expected_results[i])
        self.count = 0

    def test_value_max_query(self):
        container = self.created_db.get_container_client(self.config.TEST_MULTI_PARTITION_CONTAINER_ID)
        query = "Select value max(c.version) FROM c where c.isComplete = true and c.lookupVersion = @lookupVersion"
        query_results = container.query_items(query, parameters=[
            {"name": "@lookupVersion", "value": "console_csat"}  # cspell:disable-line
        ], enable_cross_partition_query=True)

        self.assertListEqual(list(query_results), [None])

    def test_continuation_token_size_limit_query(self):
        container = self.created_db.get_container_client(self.config.TEST_MULTI_PARTITION_CONTAINER_ID)
        for i in range(1, 1000):
            container.create_item(body=dict(pk='123', id=str(uuid.uuid4()), some_value=str(i % 3)))
        query = "Select * from c where c.some_value='2'"
        response_query = container.query_items(query, partition_key='123', max_item_count=100,
                                               continuation_token_limit=1)
        pager = response_query.by_page()
        pager.next()
        token = pager.continuation_token
        # Continuation token size should be below 1kb
        self.assertLessEqual(len(token.encode('utf-8')), 1024)
        pager.next()
        token = pager.continuation_token

        # verify a second time
        self.assertLessEqual(len(token.encode('utf-8')), 1024)

    @pytest.mark.cosmosLiveTest
    @pytest.mark.skip
    def test_computed_properties_query(self):
        computed_properties = [{'name': "cp_lower", 'query': "SELECT VALUE LOWER(c.db_group) FROM c"},
                               {'name': "cp_power",
                                'query': "SELECT VALUE POWER(c.val, 2) FROM c"},
                               {'name': "cp_str_len", 'query': "SELECT VALUE LENGTH(c.stringProperty) FROM c"}]
        items = [
            {'id': str(uuid.uuid4()), 'pk': 'test', 'val': 5, 'stringProperty': 'prefixOne', 'db_group': 'GroUp1'},
            {'id': str(uuid.uuid4()), 'pk': 'test', 'val': 5, 'stringProperty': 'prefixTwo', 'db_group': 'GrOUp1'},
            {'id': str(uuid.uuid4()), 'pk': 'test', 'val': 5, 'stringProperty': 'randomWord1', 'db_group': 'GroUp2'},
            {'id': str(uuid.uuid4()), 'pk': 'test', 'val': 5, 'stringProperty': 'randomWord2', 'db_group': 'groUp1'},
            {'id': str(uuid.uuid4()), 'pk': 'test', 'val': 5, 'stringProperty': 'randomWord3', 'db_group': 'GroUp3'},
            {'id': str(uuid.uuid4()), 'pk': 'test', 'val': 5, 'stringProperty': 'randomWord4', 'db_group': 'GrOUP1'},
            {'id': str(uuid.uuid4()), 'pk': 'test', 'val': 5, 'stringProperty': 'randomWord5', 'db_group': 'GroUp2'},
            {'id': str(uuid.uuid4()), 'pk': 'test', 'val': 0, 'stringProperty': 'randomWord6', 'db_group': 'group1'},
            {'id': str(uuid.uuid4()), 'pk': 'test', 'val': 3, 'stringProperty': 'randomWord7', 'db_group': 'group2'},
            {'id': str(uuid.uuid4()), 'pk': 'test', 'val': 2, 'stringProperty': 'randomWord8', 'db_group': 'GroUp3'}
        ]
        created_collection = self.created_db.create_container(
            "computed_properties_query_test_" + str(uuid.uuid4()), PartitionKey(path="/pk")
            , computed_properties=computed_properties)

        # Create Items
        for item in items:
            created_collection.create_item(body=item)
        # Check that computed properties were properly sent
        self.assertListEqual(computed_properties, created_collection._get_properties()["computedProperties"])

        # Test 0: Negative test, test if using non-existent computed property
        queried_items = list(
            created_collection.query_items(query='Select * from c Where c.cp_upper = "GROUP2"',
                                           partition_key="test"))
        self.assertEqual(len(queried_items), 0)

        # Test 1: Test first computed property
        queried_items = list(
            created_collection.query_items(query='Select * from c Where c.cp_lower = "group1"', partition_key="test"))
        self.assertEqual(len(queried_items), 5)

        # Test 1 Negative: Test if using non-existent string in group property returns nothing
        queried_items = list(
            created_collection.query_items(query='Select * from c Where c.cp_lower = "group4"', partition_key="test"))
        self.assertEqual(len(queried_items), 0)

        # Test 2: Test second computed property
        queried_items = list(
            created_collection.query_items(query='Select * from c Where c.cp_power = 25', partition_key="test"))
        self.assertEqual(len(queried_items), 7)

        # Test 2 Negative: Test Non-Existent POWER
        queried_items = list(
            created_collection.query_items(query='Select * from c Where c.cp_power = 16', partition_key="test"))
        self.assertEqual(len(queried_items), 0)

        # Test 3: Test Third Computed Property
        queried_items = list(
            created_collection.query_items(query='Select * from c Where c.cp_str_len = 9', partition_key="test"))
        self.assertEqual(len(queried_items), 2)

        # Test 3 Negative: Test Str length that isn't there
        queried_items = list(
            created_collection.query_items(query='Select * from c Where c.cp_str_len = 3', partition_key="test"))
        self.assertEqual(len(queried_items), 0)
        self.created_db.delete_container(created_collection.id)

    def _MockNextFunction(self):
        if self.count < len(self.payloads):
            item, result = self.get_mock_result(self.payloads, self.count)
            self.count += 1
            if item is not None:
                return {'orderByItems': [{'item': item}], '_rid': 'fake_rid', 'payload': result}
            else:
                return result
        else:
            raise StopIteration


if __name__ == "__main__":
    unittest.main()
