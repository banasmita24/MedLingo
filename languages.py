"""
Language definitions and presets.
"""

LANGUAGE_GROUPS = {
    "Indian": [
        "Hindi", "Kannada", "Tamil", "Telugu", "Bengali",
        "Marathi", "Gujarati", "Malayalam", "Punjabi", "Odia",
        "Assamese", "Urdu", "Konkani", "Manipuri", "Dogri",
        "Bodo", "Santali", "Kashmiri", "Maithili", "Sindhi",
        "Sanskrit", "Nepali", "Tulu",
    ],
    "European": [
        "French", "Spanish", "German", "Italian", "Portuguese",
        "Dutch", "Polish", "Romanian", "Greek", "Czech",
        "Swedish", "Norwegian", "Danish", "Finnish", "Hungarian",
        "Ukrainian", "Serbian", "Croatian", "Bulgarian", "Slovak",
    ],
    "Asian": [
        "Chinese (Simplified)", "Chinese (Traditional)", "Japanese",
        "Korean", "Thai", "Vietnamese", "Indonesian", "Malay",
        "Filipino (Tagalog)", "Burmese", "Khmer", "Lao",
        "Mongolian", "Sinhala", "Tibetan",
    ],
    "Middle Eastern and African": [
        "Arabic", "Persian (Farsi)", "Turkish", "Hebrew",
        "Swahili", "Amharic", "Hausa", "Yoruba", "Zulu",
        "Somali", "Pashto", "Kurdish",
    ],
    "Other": [
        "Russian", "Georgian", "Armenian", "Azerbaijani",
        "Kazakh", "Uzbek", "Tajik", "Esperanto",
    ],
}

PRESETS = {
    "Top Indian (6)": ["Hindi", "Bengali", "Telugu", "Marathi", "Tamil", "Gujarati"],
    "South Indian (4)": ["Tamil", "Telugu", "Kannada", "Malayalam"],
    "European (5)": ["French", "Spanish", "German", "Italian", "Portuguese"],
    "East Asian (4)": ["Chinese (Simplified)", "Japanese", "Korean", "Vietnamese"],
    "Middle Eastern (3)": ["Arabic", "Persian (Farsi)", "Turkish"],
    "All Indian (23)": LANGUAGE_GROUPS["Indian"],
}


def get_all_languages() -> list[str]:
    languages = []
    for group in LANGUAGE_GROUPS.values():
        languages.extend(group)
    return languages