# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JobInnerError(Model):
    """
    The Data Lake Analytics job error details.

    :param diagnostic_code: Gets the diagnostic error code.
    :type diagnostic_code: int
    :param severity: Gets the severity level of the failure. Possible values
     include: 'Warning', 'Error', 'Info'
    :type severity: str
    :param details: Gets the details of the error message.
    :type details: str
    :param component: Gets the component that failed.
    :type component: str
    :param error_id: Gets the specific identifier for the type of error
     encountered in the job.
    :type error_id: str
    :param help_link: Gets the link to MSDN or Azure help for this type of
     error, if any.
    :type help_link: str
    :param internal_diagnostics: Gets the internal diagnostic stack trace if
     the user requesting the job error details has sufficient permissions it
     will be retrieved, otherwise it will be empty.
    :type internal_diagnostics: str
    :param message: Gets the user friendly error message for the failure.
    :type message: str
    :param resolution: Gets the recommended resolution for the failure, if
     any.
    :type resolution: str
    :param source: Gets the ultimate source of the failure (usually either
     SYSTEM or USER).
    :type source: str
    :param description: Gets the error message description
    :type description: str
    """ 

    _attribute_map = {
        'diagnostic_code': {'key': 'diagnosticCode', 'type': 'int'},
        'severity': {'key': 'severity', 'type': 'SeverityTypes'},
        'details': {'key': 'details', 'type': 'str'},
        'component': {'key': 'component', 'type': 'str'},
        'error_id': {'key': 'errorId', 'type': 'str'},
        'help_link': {'key': 'helpLink', 'type': 'str'},
        'internal_diagnostics': {'key': 'internalDiagnostics', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'resolution': {'key': 'resolution', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, diagnostic_code=None, severity=None, details=None, component=None, error_id=None, help_link=None, internal_diagnostics=None, message=None, resolution=None, source=None, description=None):
        self.diagnostic_code = diagnostic_code
        self.severity = severity
        self.details = details
        self.component = component
        self.error_id = error_id
        self.help_link = help_link
        self.internal_diagnostics = internal_diagnostics
        self.message = message
        self.resolution = resolution
        self.source = source
        self.description = description
