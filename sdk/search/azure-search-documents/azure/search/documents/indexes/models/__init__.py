# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

from ._index import (
    ComplexField,
    SearchField,
    SearchableField,
    SimpleField,
    SearchIndex,
)
from . import _edm
from ..._generated.models import SuggestOptions
from .._generated.models import (
    SearchAlias,
    AzureMachineLearningSkill,
    AnalyzeResult,
    AnalyzedTokenInfo,
    AsciiFoldingTokenFilter,
    BM25Similarity,
    CharFilter,
    CjkBigramTokenFilter,
    ClassicSimilarity,
    ClassicTokenizer,
    CommonGramTokenFilter,
    ConditionalSkill,
    CorsOptions,
    CustomEntityLookupSkill,
    CustomEntityLookupSkillLanguage,
    CustomNormalizer,
    DictionaryDecompounderTokenFilter,
    DistanceScoringFunction,
    DistanceScoringParameters,
    DocumentExtractionSkill,
    DocumentKeysOrIds,
    EdgeNGramTokenFilter,
    EdgeNGramTokenizer,
    EdgeNGramTokenFilterSide,
    ElisionTokenFilter,
    EntityCategory,
    EntityLinkingSkill,
    EntityRecognitionSkillLanguage,
    FieldMapping,
    FieldMappingFunction,
    FreshnessScoringFunction,
    FreshnessScoringParameters,
    GetIndexStatisticsResult,
    ImageAnalysisSkill,
    ImageAnalysisSkillLanguage,
    ImageDetail,
    IndexingSchedule,
    IndexingParameters,
    IndexerExecutionStatus,
    IndexerStatus,
    InputFieldMappingEntry,
    KeepTokenFilter,
    KeyPhraseExtractionSkill,
    KeyPhraseExtractionSkillLanguage,
    KeywordMarkerTokenFilter,
    KeywordTokenizerV2,
    LanguageDetectionSkill,
    LengthTokenFilter,
    LexicalAnalyzer,
    LexicalNormalizer,
    LexicalNormalizerName,
    LexicalTokenizer,
    LimitTokenFilter,
    LuceneStandardAnalyzer,
    LuceneStandardTokenizer,
    MagnitudeScoringFunction,
    MagnitudeScoringParameters,
    MappingCharFilter,
    MergeSkill,
    MicrosoftLanguageStemmingTokenizer,
    MicrosoftLanguageTokenizer,
    MicrosoftStemmingTokenizerLanguage,
    MicrosoftTokenizerLanguage,
    NGramTokenFilter,
    NGramTokenizer,
    OcrSkill,
    OcrSkillLanguage,
    OutputFieldMappingEntry,
    PathHierarchyTokenizerV2,
    PatternCaptureTokenFilter,
    PatternReplaceCharFilter,
    PatternReplaceTokenFilter,
    PIIDetectionSkill,
    PIIDetectionSkillMaskingMode,
    PhoneticEncoder,
    PhoneticTokenFilter,
    PrioritizedFields,
    RegexFlags,
    SearchIndexer,
    SearchIndexerCache,
    SearchIndexerDataContainer,
    SearchIndexerDataIdentity,
    SearchIndexerDataNoneIdentity,
    SearchIndexerDataUserAssignedIdentity,
    SearchIndexerDataSourceType,
    SearchIndexerError,
    SearchIndexerKnowledgeStore,
    SearchIndexerKnowledgeStoreFileProjectionSelector,
    SearchIndexerKnowledgeStoreObjectProjectionSelector,
    SearchIndexerKnowledgeStoreProjection,
    SearchIndexerKnowledgeStoreTableProjectionSelector,
    SearchIndexerLimits,
    SearchIndexerStatus,
    SemanticConfiguration,
    SemanticField,
    SemanticSettings,
    ScoringFunction,
    ScoringFunctionAggregation,
    ScoringFunctionInterpolation,
    ScoringProfile,
    SentimentSkillLanguage,
    ShaperSkill,
    ShingleTokenFilter,
    Similarity,
    SnowballTokenFilter,
    SnowballTokenFilterLanguage,
    SoftDeleteColumnDeletionDetectionPolicy,
    SplitSkill,
    SplitSkillLanguage,
    SqlIntegratedChangeTrackingPolicy,
    StemmerOverrideTokenFilter,
    StemmerTokenFilter,
    StemmerTokenFilterLanguage,
    StopAnalyzer,
    StopwordsList,
    StopwordsTokenFilter,
    Suggester,
    SynonymTokenFilter,
    TagScoringFunction,
    TagScoringParameters,
    TextSplitMode,
    TextTranslationSkill,
    TextTranslationSkillLanguage,
    TextWeights,
    TokenCharacterKind,
    TokenFilter,
    TokenFilterName,
    TruncateTokenFilter,
    UaxUrlEmailTokenizer,
    UniqueTokenFilter,
    WebApiSkill,
    VisualFeature,
    WordDelimiterTokenFilter,
)
from ._models import (
    AnalyzeTextOptions,
    CustomAnalyzer,
    EntityRecognitionSkill,
    EntityRecognitionSkillVersion,
    PatternAnalyzer,
    PatternTokenizer,
    SearchIndexerDataSourceConnection,
    SearchIndexerSkillset,
    SearchResourceEncryptionKey,
    SentimentSkill,
    SentimentSkillVersion,
    SynonymMap,
)

SearchFieldDataType = _edm

class BM25SimilarityAlgorithm(BM25Similarity):
    pass

class ClassicSimilarityAlgorithm(ClassicSimilarity):
    pass

class KeywordTokenizer(KeywordTokenizerV2):
    pass

class PathHierarchyTokenizer(PathHierarchyTokenizerV2):
    pass

class SimilarityAlgorithm(Similarity):
    pass

class SearchSuggester(Suggester):
    pass




__all__ = (
    "SearchAlias",
    "AzureMachineLearningSkill",
    "AnalyzeTextOptions",
    "AnalyzeResult",
    "AnalyzedTokenInfo",
    "AsciiFoldingTokenFilter",
    "BM25SimilarityAlgorithm",
    "CharFilter",
    "CjkBigramTokenFilter",
    "ClassicSimilarityAlgorithm",
    "ClassicTokenizer",
    "CommonGramTokenFilter",
    "ComplexField",
    "ConditionalSkill",
    "CorsOptions",
    "CustomAnalyzer",
    "CustomEntityLookupSkill",
    "CustomEntityLookupSkillLanguage",
    "CustomNormalizer",
    "DictionaryDecompounderTokenFilter",
    "DistanceScoringFunction",
    "DistanceScoringParameters",
    "DocumentExtractionSkill",
    "DocumentKeysOrIds",
    "EdgeNGramTokenFilter",
    "EdgeNGramTokenizer",
    "ElisionTokenFilter",
    "EdgeNGramTokenFilterSide",
    "EntityCategory",
    "EntityLinkingSkill",
    "EntityRecognitionSkill",
    "EntityRecognitionSkillLanguage",
    "EntityRecognitionSkillVersion",
    "FieldMapping",
    "FieldMappingFunction",
    "FreshnessScoringFunction",
    "FreshnessScoringParameters",
    "GetIndexStatisticsResult",
    "ImageAnalysisSkill",
    "ImageAnalysisSkillLanguage",
    "ImageDetail",
    "IndexingSchedule",
    "IndexingParameters",
    "IndexerExecutionStatus",
    "IndexerStatus",
    "InputFieldMappingEntry",
    "KeepTokenFilter",
    "KeyPhraseExtractionSkill",
    "KeyPhraseExtractionSkillLanguage",
    "KeywordMarkerTokenFilter",
    "KeywordTokenizer",
    "LanguageDetectionSkill",
    "LengthTokenFilter",
    "LexicalAnalyzer",
    "LexicalNormalizer",
    "LexicalNormalizerName",
    "LexicalTokenizer",
    "LimitTokenFilter",
    "LuceneStandardAnalyzer",
    "LuceneStandardTokenizer",
    "MagnitudeScoringFunction",
    "MagnitudeScoringParameters",
    "MappingCharFilter",
    "MergeSkill",
    "MicrosoftLanguageStemmingTokenizer",
    "MicrosoftLanguageTokenizer",
    "MicrosoftStemmingTokenizerLanguage",
    "MicrosoftTokenizerLanguage",
    "NGramTokenFilter",
    "NGramTokenizer",
    "OcrSkill",
    "OcrSkillLanguage",
    "OutputFieldMappingEntry",
    "PathHierarchyTokenizer",
    "PatternAnalyzer",
    "PatternCaptureTokenFilter",
    "PatternReplaceCharFilter",
    "PatternReplaceTokenFilter",
    "PatternTokenizer",
    "PIIDetectionSkill",
    "PIIDetectionSkillMaskingMode",
    "PhoneticEncoder",
    "PhoneticTokenFilter",
    "PrioritizedFields",
    "RegexFlags",
    "ScoringFunction",
    "ScoringFunctionAggregation",
    "ScoringFunctionInterpolation",
    "ScoringProfile",
    "SearchField",
    "SearchIndex",
    "SearchIndexer",
    "SearchIndexerCache",
    "SearchIndexerDataContainer",
    "SearchIndexerDataIdentity",
    "SearchIndexerDataNoneIdentity",
    "SearchIndexerDataUserAssignedIdentity",
    "SearchIndexerDataSourceConnection",
    "SearchIndexerDataSourceType",
    "SearchIndexerError",
    "SearchIndexerKnowledgeStore",
    "SearchIndexerKnowledgeStoreFileProjectionSelector",
    "SearchIndexerKnowledgeStoreObjectProjectionSelector",
    "SearchIndexerKnowledgeStoreProjection",
    "SearchIndexerKnowledgeStoreTableProjectionSelector",
    "SearchIndexerLimits",
    "SearchIndexerSkillset",
    "SearchIndexerStatus",
    "SearchResourceEncryptionKey",
    "SearchableField",
    "SemanticConfiguration",
    "SemanticField",
    "SemanticSettings",
    "SentimentSkill",
    "SentimentSkillLanguage",
    "SentimentSkillVersion",
    "ShaperSkill",
    "ShingleTokenFilter",
    "SimpleField",
    "SimilarityAlgorithm",
    "SnowballTokenFilter",
    "SnowballTokenFilterLanguage",
    "SoftDeleteColumnDeletionDetectionPolicy",
    "SplitSkill",
    "SplitSkillLanguage",
    "SqlIntegratedChangeTrackingPolicy",
    "StemmerOverrideTokenFilter",
    "StemmerTokenFilter",
    "StemmerTokenFilterLanguage",
    "StopAnalyzer",
    "StopwordsList",
    "StopwordsTokenFilter",
    "SearchSuggester",
    "SuggestOptions",
    "SynonymMap",
    "SynonymTokenFilter",
    "TagScoringFunction",
    "TagScoringParameters",
    "TextSplitMode",
    "TextTranslationSkill",
    "TextTranslationSkillLanguage",
    "TextWeights",
    "TokenCharacterKind",
    "TokenFilter",
    "TokenFilterName",
    "TruncateTokenFilter",
    "UaxUrlEmailTokenizer",
    "UniqueTokenFilter",
    "VisualFeature",
    "WebApiSkill",
    "WordDelimiterTokenFilter",
    "SearchFieldDataType",
)
