"""
Parser for structured output.
"""


def parse_output(processed: dict, languages: list[str]) -> dict:
    """Parse the processed output into the expected format."""
    
    simplified = processed.get("simplified", "")
    steps = processed.get("steps", "")
    translations = processed.get("translations", {})
    
    # Ensure all selected languages have a translation
    formatted_translations = {}
    for lang in languages:
        content = translations.get(lang, "")
        if not content:
            content = f"[Translation for {lang} was not generated. Please try again.]"
        formatted_translations[lang] = content
    
    return {
        "simplified": simplified or "Not available.",
        "steps": steps or "Not available.",
        "translations": formatted_translations,
        "raw": processed.get("raw_simplification", ""),
    }