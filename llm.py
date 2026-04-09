"""
LLM interaction for simplification and translation.
Based on the working 3-language approach.
"""

import streamlit as st
from groq import Groq
import time
import re


LLM_MODEL = "openai/gpt-oss-120b"
LLM_TEMPERATURE = 0.3


@st.cache_resource
def get_client():
    """Get Groq client."""
    try:
        if "GROQ_API_KEY" not in st.secrets:
            st.error("GROQ_API_KEY not found in secrets.")
            return None
        
        api_key = st.secrets["GROQ_API_KEY"]
        if not api_key:
            st.error("GROQ_API_KEY is empty.")
            return None
            
        return Groq(api_key=api_key)
    except Exception as e:
        st.error(f"Failed to initialize Groq client: {str(e)}")
        return None


def process_instruction(text: str, languages: list[str]) -> dict:
    """Process simplification and translations in a single API call."""
    
    client = get_client()
    if not client:
        return {
            "simplified": "",
            "steps": "",
            "translations": {},
            "raw_simplification": "",
        }
    
    # Build the language list for the prompt
    lang_list = ", ".join(languages)
    
    prompt = f"""
Simplify this medical instruction into plain English, convert into clear numbered steps, and translate into {lang_list}.

Medical Instruction:
{text}

Format your response exactly like this:

SIMPLIFIED:
[Write the simplified version here in plain English]

STEPS:
1. [First step]
2. [Second step]
3. [Third step]
... continue with all steps

HINDI:
[Translation in Hindi]

KANNADA:
[Translation in Kannada]

TAMIL:
[Translation in Tamil]

... continue for all requested languages: {lang_list}
"""
    
    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=LLM_TEMPERATURE,
            max_tokens=4096,
        )
        raw_output = response.choices[0].message.content
        
        # Parse the response
        sections = parse_output(raw_output, languages)
        
        return {
            "simplified": sections.get("simplified", ""),
            "steps": sections.get("steps", ""),
            "translations": sections.get("translations", {}),
            "raw_simplification": raw_output,
        }
        
    except Exception as e:
        st.error(f"API call failed: {str(e)}")
        return {
            "simplified": "",
            "steps": "",
            "translations": {},
            "raw_simplification": "",
        }


def parse_output(text: str, languages: list[str]) -> dict:
    """Parse the LLM output into sections."""
    
    sections = {
        "simplified": "",
        "steps": "",
        "translations": {}
    }
    
    current = None
    current_content = []
    
    # Normalize language names for matching
    lang_lower_map = {lang.lower(): lang for lang in languages}
    
    lines = text.split("\n")
    
    for line in lines:
        line_lower = line.lower().strip()
        line_stripped = line.strip()
        
        # Check for section headers
        if "simplified" in line_lower and len(line_stripped) < 30:
            if current and current_content:
                _save_section(sections, current, current_content, lang_lower_map)
            current = "simplified"
            current_content = []
        elif "step" in line_lower and len(line_stripped) < 30:
            if current and current_content:
                _save_section(sections, current, current_content, lang_lower_map)
            current = "steps"
            current_content = []
        else:
            # Check if this line is a language header
            found_lang = False
            for lang_lower, lang_original in lang_lower_map.items():
                if lang_lower in line_lower and len(line_stripped) < 30:
                    if current and current_content:
                        _save_section(sections, current, current_content, lang_lower_map)
                    current = lang_original
                    current_content = []
                    found_lang = True
                    break
            
            # If not a header, add to current section
            if not found_lang and current:
                current_content.append(line)
    
    # Save the last section
    if current and current_content:
        _save_section(sections, current, current_content, lang_lower_map)
    
    return sections


def _save_section(sections: dict, current: str, content: list, lang_lower_map: dict):
    """Save content to the appropriate section."""
    text = "\n".join(content).strip()
    
    if current == "simplified":
        sections["simplified"] = text
    elif current == "steps":
        sections["steps"] = text
    elif current in lang_lower_map.values():
        sections["translations"][current] = text