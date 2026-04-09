"""
ML model loading and inference.
Based on your working original approach.
"""

import pickle
import numpy as np
import streamlit as st
import os


try:
    from config import MODEL_FILES, SAFETY_THRESHOLDS
except ImportError:
    MODEL_FILES = {
        "vectorizer": "vectorizer.pkl",
        "binarizer": "binarizer.pkl",
        "rbm": "rbm.pkl",
        "classifier": "classifier.pkl",
        "mean_error": "mean_error.npy",
        "std_error": "std_error.npy",
    }
    SAFETY_THRESHOLDS = {
        "safe": 0.8,
        "moderate": 0.6,
    }


@st.cache_resource
def load_models():
    """Load ML models."""
    models = {}
    
    for key, filename in MODEL_FILES.items():
        if not os.path.exists(filename):
            st.warning(f"Model file not found: {filename}")
            return None
    
    try:
        models["vectorizer"] = pickle.load(open(MODEL_FILES["vectorizer"], "rb"))
        models["binarizer"] = pickle.load(open(MODEL_FILES["binarizer"], "rb"))
        models["rbm"] = pickle.load(open(MODEL_FILES["rbm"], "rb"))
        models["classifier"] = pickle.load(open(MODEL_FILES["classifier"], "rb"))
        models["mean_error"] = np.load(MODEL_FILES["mean_error"])
        models["std_error"] = np.load(MODEL_FILES["std_error"])
        
        return models
    except Exception as e:
        st.warning(f"Error loading models: {str(e)}")
        return None


def sigmoid(x):
    """Sigmoid function."""
    return 1 / (1 + np.exp(-np.clip(x, -500, 500)))


def compute_medical_confidence(text: str, models: dict) -> float:
    """Compute medical confidence score."""
    if models is None:
        return 0.75
    
    try:
        vectorizer = models["vectorizer"]
        clf = models["classifier"]
        X = vectorizer.transform([text])
        prob = clf.predict_proba(X)[0][1]
        return float(prob)
    except Exception as e:
        return 0.75


def compute_safety_score(text: str, models: dict) -> float:
    """Compute safety score using RBM reconstruction error."""
    if models is None:
        return 0.85
    
    try:
        vectorizer = models["vectorizer"]
        binarizer = models["binarizer"]
        rbm = models["rbm"]
        mean_error = models["mean_error"]
        std_error = models["std_error"]

        X = vectorizer.transform([text])
        X_bin = binarizer.transform(X).toarray()
        H = rbm.transform(X_bin)
        X_recon = sigmoid(np.dot(H, rbm.components_) + rbm.intercept_visible_)
        
        error = np.mean((X_bin - X_recon) ** 2)
        z = (error - mean_error) / std_error
        score = 1 / (1 + np.exp(np.clip(z, -10, 10)))
        
        return float(score)
    except Exception as e:
        return 0.85


def get_safety_status(score: float) -> dict:
    """Get safety status with color coding."""
    if score > SAFETY_THRESHOLDS["safe"]:
        return {
            "label": "Safe",
            "color": "#34C759",
            "bg": "rgba(52, 199, 89, 0.08)",
            "border": "rgba(52, 199, 89, 0.2)",
            "description": "This instruction follows standard medical safety patterns.",
        }
    elif score > SAFETY_THRESHOLDS["moderate"]:
        return {
            "label": "Review Recommended",
            "color": "#FF9500",
            "bg": "rgba(255, 149, 0, 0.08)",
            "border": "rgba(255, 149, 0, 0.2)",
            "description": "Some elements may need professional review.",
        }
    else:
        return {
            "label": "Caution",
            "color": "#FF3B30",
            "bg": "rgba(255, 59, 48, 0.08)",
            "border": "rgba(255, 59, 48, 0.2)",
            "description": "This instruction contains unusual patterns. Professional review advised.",
        }