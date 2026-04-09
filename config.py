"""
Application configuration and constants.
"""

APP_TITLE = "MedLingo"
APP_SUBTITLE = "Medical Discharge Instruction Assistant"
APP_DESCRIPTION = "Simplify and translate discharge instructions for patient comprehension."

PAGE_CONFIG = {
    "page_title": "MedLingo — Discharge Assistant",
    "page_icon": "💊",
    "layout": "centered",
    "initial_sidebar_state": "collapsed",
}

MODEL_FILES = {
    "vectorizer": "vectorizer.pkl",
    "binarizer": "binarizer.pkl",
    "rbm": "rbm.pkl",
    "classifier": "classifier.pkl",
    "mean_error": "mean_error.npy",
    "std_error": "std_error.npy",
}

# Using the same model that worked in your original code
LLM_MODEL = "openai/gpt-oss-120b"
LLM_TEMPERATURE = 0.3

SAFETY_THRESHOLDS = {
    "safe": 0.8,
    "moderate": 0.6,
}

MEDICAL_CONFIDENCE_THRESHOLD = 0.5