# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.7, generator: @autorest/python@6.7.1)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class Answers(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Answers."""

    NONE = "none"
    """Do not return answers for the query."""
    EXTRACTIVE = "extractive"
    """Extracts answer candidates from the contents of the documents returned in response to a query
    #: expressed as a question in natural language."""


class AutocompleteMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the mode for Autocomplete. The default is 'oneTerm'. Use 'twoTerms' to get shingles
    and 'oneTermWithContext' to use the current context in producing autocomplete terms.
    """

    ONE_TERM = "oneTerm"
    """Only one term is suggested. If the query has two terms, only the last term is completed. For
    #: example, if the input is 'washington medic', the suggested terms could include 'medicaid',
    #: 'medicare', and 'medicine'."""
    TWO_TERMS = "twoTerms"
    """Matching two-term phrases in the index will be suggested. For example, if the input is 'medic',
    #: the suggested terms could include 'medicare coverage' and 'medical assistant'."""
    ONE_TERM_WITH_CONTEXT = "oneTermWithContext"
    """Completes the last term in a query with two or more terms, where the last two terms are a
    #: phrase that exists in the index. For example, if the input is 'washington medic', the suggested
    #: terms could include 'washington medicaid' and 'washington medical'."""


class Captions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Captions."""

    NONE = "none"
    """Do not return captions for the query."""
    EXTRACTIVE = "extractive"
    """Extracts captions from the matching documents that contain passages relevant to the search
    #: query."""


class IndexActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The operation to perform on a document in an indexing batch."""

    UPLOAD = "upload"
    """Inserts the document into the index if it is new and updates it if it exists. All fields are
    #: replaced in the update case."""
    MERGE = "merge"
    """Merges the specified field values with an existing document. If the document does not exist,
    #: the merge will fail. Any field you specify in a merge will replace the existing field in the
    #: document. This also applies to collections of primitive and complex types."""
    MERGE_OR_UPLOAD = "mergeOrUpload"
    """Behaves like merge if a document with the given key already exists in the index. If the
    #: document does not exist, it behaves like upload with a new document."""
    DELETE = "delete"
    """Removes the specified document from the index. Any field you specify in a delete operation
    #: other than the key field will be ignored. If you want to remove an individual field from a
    #: document, use merge instead and set the field explicitly to null."""


class QueryAnswerType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This parameter is only valid if the query type is 'semantic'. If set, the query returns answers
    extracted from key passages in the highest ranked documents. The number of answers returned can
    be configured by appending the pipe character '|' followed by the 'count-:code:`<number of
    answers>`' option after the answers parameter value, such as 'extractive|count-3'. Default
    count is 1. The confidence threshold can be configured by appending the pipe character '|'
    followed by the 'threshold-:code:`<confidence threshold>`' option after the answers parameter
    value, such as 'extractive|threshold-0.9'. Default threshold is 0.7.
    """

    NONE = "none"
    """Do not return answers for the query."""
    EXTRACTIVE = "extractive"
    """Extracts answer candidates from the contents of the documents returned in response to a query
    #: expressed as a question in natural language."""


class QueryCaptionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This parameter is only valid if the query type is 'semantic'. If set, the query returns
    captions extracted from key passages in the highest ranked documents. When Captions is set to
    'extractive', highlighting is enabled by default, and can be configured by appending the pipe
    character '|' followed by the 'highlight-<true/false>' option, such as
    'extractive|highlight-true'. Defaults to 'None'.
    """

    NONE = "none"
    """Do not return captions for the query."""
    EXTRACTIVE = "extractive"
    """Extracts captions from the matching documents that contain passages relevant to the search
    #: query."""


class QueryDebugMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enables a debugging tool that can be used to further explore your search results."""

    DISABLED = "disabled"
    """No query debugging information will be returned."""
    SEMANTIC = "semantic"
    """Allows the user to further explore their Semantic search results."""


class QueryLanguage(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The language of the query."""

    NONE = "none"
    """Query language not specified."""
    EN_US = "en-us"
    """Query language value for English (United States)."""
    EN_GB = "en-gb"
    """Query language value for English (Great Britain)."""
    EN_IN = "en-in"
    """Query language value for English (India)."""
    EN_CA = "en-ca"
    """Query language value for English (Canada)."""
    EN_AU = "en-au"
    """Query language value for English (Australia)."""
    FR_FR = "fr-fr"
    """Query language value for French (France)."""
    FR_CA = "fr-ca"
    """Query language value for French (Canada)."""
    DE_DE = "de-de"
    """Query language value for German (Germany)."""
    ES_ES = "es-es"
    """Query language value for Spanish (Spain)."""
    ES_MX = "es-mx"
    """Query language value for Spanish (Mexico)."""
    ZH_CN = "zh-cn"
    """Query language value for Chinese (China)."""
    ZH_TW = "zh-tw"
    """Query language value for Chinese (Taiwan)."""
    PT_BR = "pt-br"
    """Query language value for Portuguese (Brazil)."""
    PT_PT = "pt-pt"
    """Query language value for Portuguese (Portugal)."""
    IT_IT = "it-it"
    """Query language value for Italian (Italy)."""
    JA_JP = "ja-jp"
    """Query language value for Japanese (Japan)."""
    KO_KR = "ko-kr"
    """Query language value for Korean (Korea)."""
    RU_RU = "ru-ru"
    """Query language value for Russian (Russia)."""
    CS_CZ = "cs-cz"
    """Query language value for Czech (Czech Republic)."""
    NL_BE = "nl-be"
    """Query language value for Dutch (Belgium)."""
    NL_NL = "nl-nl"
    """Query language value for Dutch (Netherlands)."""
    HU_HU = "hu-hu"
    """Query language value for Hungarian (Hungary)."""
    PL_PL = "pl-pl"
    """Query language value for Polish (Poland)."""
    SV_SE = "sv-se"
    """Query language value for Swedish (Sweden)."""
    TR_TR = "tr-tr"
    """Query language value for Turkish (Turkey)."""
    HI_IN = "hi-in"
    """Query language value for Hindi (India)."""
    AR_SA = "ar-sa"
    """Query language value for Arabic (Saudi Arabia)."""
    AR_EG = "ar-eg"
    """Query language value for Arabic (Egypt)."""
    AR_MA = "ar-ma"
    """Query language value for Arabic (Morocco)."""
    AR_KW = "ar-kw"
    """Query language value for Arabic (Kuwait)."""
    AR_JO = "ar-jo"
    """Query language value for Arabic (Jordan)."""
    DA_DK = "da-dk"
    """Query language value for Danish (Denmark)."""
    NO_NO = "no-no"
    """Query language value for Norwegian (Norway)."""
    BG_BG = "bg-bg"
    """Query language value for Bulgarian (Bulgaria)."""
    HR_HR = "hr-hr"
    """Query language value for Croatian (Croatia)."""
    HR_BA = "hr-ba"
    """Query language value for Croatian (Bosnia and Herzegovina)."""
    MS_MY = "ms-my"
    """Query language value for Malay (Malaysia)."""
    MS_BN = "ms-bn"
    """Query language value for Malay (Brunei Darussalam)."""
    SL_SL = "sl-sl"
    """Query language value for Slovenian (Slovenia)."""
    TA_IN = "ta-in"
    """Query language value for Tamil (India)."""
    VI_VN = "vi-vn"
    """Query language value for Vietnamese (Viet Nam)."""
    EL_GR = "el-gr"
    """Query language value for Greek (Greece)."""
    RO_RO = "ro-ro"
    """Query language value for Romanian (Romania)."""
    IS_IS = "is-is"
    """Query language value for Icelandic (Iceland)."""
    ID_ID = "id-id"
    """Query language value for Indonesian (Indonesia)."""
    TH_TH = "th-th"
    """Query language value for Thai (Thailand)."""
    LT_LT = "lt-lt"
    """Query language value for Lithuanian (Lithuania)."""
    UK_UA = "uk-ua"
    """Query language value for Ukrainian (Ukraine)."""
    LV_LV = "lv-lv"
    """Query language value for Latvian (Latvia)."""
    ET_EE = "et-ee"
    """Query language value for Estonian (Estonia)."""
    CA_ES = "ca-es"
    """Query language value for Catalan (Spain)."""
    FI_FI = "fi-fi"
    """Query language value for Finnish (Finland)."""
    SR_BA = "sr-ba"
    """Query language value for Serbian (Bosnia and Herzegovina)."""
    SR_ME = "sr-me"
    """Query language value for Serbian (Montenegro)."""
    SR_RS = "sr-rs"
    """Query language value for Serbian (Serbia)."""
    SK_SK = "sk-sk"
    """Query language value for Slovak (Slovakia)."""
    NB_NO = "nb-no"
    """Query language value for Norwegian (Norway)."""
    HY_AM = "hy-am"
    """Query language value for Armenian (Armenia)."""
    BN_IN = "bn-in"
    """Query language value for Bengali (India)."""
    EU_ES = "eu-es"
    """Query language value for Basque (Spain)."""
    GL_ES = "gl-es"
    """Query language value for Galician (Spain)."""
    GU_IN = "gu-in"
    """Query language value for Gujarati (India)."""
    HE_IL = "he-il"
    """Query language value for Hebrew (Israel)."""
    GA_IE = "ga-ie"
    """Query language value for Irish (Ireland)."""
    KN_IN = "kn-in"
    """Query language value for Kannada (India)."""
    ML_IN = "ml-in"
    """Query language value for Malayalam (India)."""
    MR_IN = "mr-in"
    """Query language value for Marathi (India)."""
    FA_AE = "fa-ae"
    """Query language value for Persian (U.A.E.)."""
    PA_IN = "pa-in"
    """Query language value for Punjabi (India)."""
    TE_IN = "te-in"
    """Query language value for Telugu (India)."""
    UR_PK = "ur-pk"
    """Query language value for Urdu (Pakistan)."""


class QueryResultDocumentSemanticFieldState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The way the field was used for the semantic enrichment process."""

    USED = "used"
    """The field was fully used for semantic enrichment."""
    UNUSED = "unused"
    """The field was not used for semantic enrichment."""
    PARTIAL = "partial"
    """The field was partially used for semantic enrichment."""


class QuerySpellerType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Improve search recall by spell-correcting individual search query terms."""

    NONE = "none"
    """Speller not enabled."""
    LEXICON = "lexicon"
    """Speller corrects individual query terms using a static lexicon for the language specified by
    #: the queryLanguage parameter."""


class QueryType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the syntax of the search query. The default is 'simple'. Use 'full' if your query
    uses the Lucene query syntax and 'semantic' if query syntax is not needed.
    """

    SIMPLE = "simple"
    """Uses the simple query syntax for searches. Search text is interpreted using a simple query
    #: language that allows for symbols such as +, * and "". Queries are evaluated across all
    #: searchable fields by default, unless the searchFields parameter is specified."""
    FULL = "full"
    """Uses the full Lucene query syntax for searches. Search text is interpreted using the Lucene
    #: query language which allows field-specific and weighted searches, as well as other advanced
    #: features."""
    SEMANTIC = "semantic"
    """Best suited for queries expressed in natural language as opposed to keywords. Improves
    #: precision of search results by re-ranking the top search results using a ranking model trained
    #: on the Web corpus."""


class ScoringStatistics(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """A value that specifies whether we want to calculate scoring statistics (such as document
    frequency) globally for more consistent scoring, or locally, for lower latency. The default is
    'local'. Use 'global' to aggregate scoring statistics globally before scoring. Using global
    scoring statistics can increase latency of search queries.
    """

    LOCAL = "local"
    """The scoring statistics will be calculated locally for lower latency."""
    GLOBAL = "global"
    """The scoring statistics will be calculated globally for more consistent scoring."""
    GLOBAL_ENUM = "global"
    """The scoring statistics will be calculated globally for more consistent scoring."""


class SearchMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies whether any or all of the search terms must be matched in order to count the document
    as a match.
    """

    ANY = "any"
    """Any of the search terms must be matched in order to count the document as a match."""
    ALL = "all"
    """All of the search terms must be matched in order to count the document as a match."""


class SemanticErrorHandling(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Allows the user to choose whether a semantic call should fail completely, or to return partial
    results.
    """

    PARTIAL = "partial"
    """If the semantic processing fails, partial results still return. The definition of partial
    #: results depends on what semantic step failed and what was the reason for failure."""
    FAIL = "fail"
    """If there is an exception during the semantic processing step, the query will fail and return
    #: the appropriate HTTP code depending on the error."""


class SemanticPartialResponseReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Reason that a partial response was returned for a semantic search request."""

    MAX_WAIT_EXCEEDED = "maxWaitExceeded"
    """If 'semanticMaxWaitInMilliseconds' was set and the semantic processing duration exceeded that
    #: value. Only the base results were returned."""
    CAPACITY_OVERLOADED = "capacityOverloaded"
    """The request was throttled. Only the base results were returned."""
    TRANSIENT = "transient"
    """At least one step of the semantic process failed."""


class SemanticPartialResponseType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of partial response that was returned for a semantic search request."""

    BASE_RESULTS = "baseResults"
    """Results without any semantic enrichment or reranking."""
    RERANKED_RESULTS = "rerankedResults"
    """Results have been reranked with the reranker model and will include semantic captions. They
    #: will not include any answers, answers highlights or caption highlights."""


class Speller(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Speller."""

    NONE = "none"
    """Speller not enabled."""
    LEXICON = "lexicon"
    """Speller corrects individual query terms using a static lexicon for the language specified by
    #: the queryLanguage parameter."""
