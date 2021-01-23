import os
import torch
from backend.functional import read_config

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# DIR&PATH
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

CORE_DIR = os.path.join(ROOT_DIR, '../core')
NLU_DIR = os.path.join(CORE_DIR, 'nlu')
TAGGER_DIR = os.path.join(NLU_DIR, 'semantic_tagger')
CLASSIFIER_DIR = os.path.join(NLU_DIR, 'intent_classifier')
IMAP_PATH = os.path.join(NLU_DIR, 'tag_intent_manager/taggers_map.json')
CONFIG_DIR = os.path.join(ROOT_DIR, 'config.py')
CONFIG = read_config()

CUDA = CONFIG['global_config']['cuda']

FS_PATH = os.path.join(ROOT_DIR, '../filesystem')
DATA_PATH = os.path.join(FS_PATH, 'datasets')
SKILLS_PATH = os.path.join(FS_PATH, 'skills')

PACKAGE_NAME = "delOS"

NLU_ENCODER_CONFIG = CONFIG['encoder_core_module']
NLU_INTENTS_CONFIG = CONFIG['intent_classifier_core_module']

NLU_ENGINE_CONFIG = CONFIG['nlu_engine']
NER_CONFIG = CONFIG['ner_engine']

# MODELLING
MODELS_FIT_PARAMS = os.path.join(ROOT_DIR, 'models_fit_params.json')




























# miscellaneous
BUILTIN_ENTITY_TAGGER = "builtin_entity_tagger"
INTENT = "intent"
INTENTS = "intents"
ENTITIES = "entities"
ENTITY = "entity"
ENTITY_KIND = "entity_kind"


AUTOMATICALLY_EXTENSIBLE = "automatically_extensible"
USE_SYNONYMS = "use_synonyms"
SYNONYMS = "synonyms"
DATA = "data"
RESOLVED_VALUE = "resolved_value"
SLOT_NAME = "slot_name"
TEXT = "text"
UTTERANCES = "utterances"
LANGUAGE = "language"
VALUE = "value"
NGRAM = "ngram"
TOKEN_INDEXES = "token_indexes"
CAPITALIZE = "capitalize"
UNKNOWNWORD = "unknownword"
VALIDATED = "validated"
START = "start"
END = "end"
CUSTOM_ENTITY_PARSER = "custom_entity_parser"
MATCHING_STRICTNESS = "matching_strictness"
RANDOM_STATE = "random_state"

# resources
RESOURCES = "resources"
METADATA = "metadata"
STOP_WORDS = "stop_words"
NOISE = "noise"
GAZETTEERS = "gazetteers"
STEMS = "stems"
CUSTOM_ENTITY_PARSER_USAGE = "custom_entity_parser_usage"
WORD_CLUSTERS = "word_clusters"
GAZETTEER_ENTITIES = "gazetteer_entities"

# builtin entities TODO: REDO
SNIPS_AMOUNT_OF_MONEY = "snips/amountOfMoney"
SNIPS_DATETIME = "snips/datetime"
SNIPS_DURATION = "snips/duration"
SNIPS_NUMBER = "snips/number"
SNIPS_ORDINAL = "snips/ordinal"
SNIPS_PERCENTAGE = "snips/percentage"
SNIPS_TEMPERATURE = "snips/temperature"