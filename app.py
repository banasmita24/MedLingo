"""
MedLingo — 3-Page Multi-Step Application
Page 1: Landing / Home
Page 2: Analyze & Translate
Page 3: Results
"""

import streamlit as st

from config import (
    PAGE_CONFIG,
    MEDICAL_CONFIDENCE_THRESHOLD,
)
from styles import get_css
from ui_components import (
    render_navbar_brand,
    render_hero,
    render_landing_features,
    render_how_it_works,
    render_stats,
    render_page_header,
    render_metrics,
    render_safety_bar,
    render_results_header,
    render_panel,
    render_translation_content,
    render_footer,
    render_tip,
)
from models import load_models, compute_medical_confidence, compute_safety_score, get_safety_status
from llm import process_instruction
from parser import parse_output
from languages import get_all_languages, PRESETS


# Page config
st.set_page_config(**PAGE_CONFIG)

# Session state bootstrap
if "page" not in st.session_state:
    st.session_state.page = 1
if "results" not in st.session_state:
    st.session_state.results = None
if "input_text" not in st.session_state:
    st.session_state.input_text = ""
if "selected_languages" not in st.session_state:
    st.session_state.selected_languages = ["Hindi", "Kannada", "Tamil"]
if "confidence" not in st.session_state:
    st.session_state.confidence = None
if "safety_score" not in st.session_state:
    st.session_state.safety_score = None
if "safety_status" not in st.session_state:
    st.session_state.safety_status = None

# Apply CSS
st.markdown(get_css(), unsafe_allow_html=True)

# Load models once
models = load_models()
all_languages = get_all_languages()


# Navigation helpers
def go_to(page: int):
    st.session_state.page = page


def render_page_indicator(current: int):
    pages = [("Home", 1), ("Analyze", 2), ("Results", 3)]
    pills_html = '<div class="ml-page-nav">'
    for label, num in pages:
        active_cls = "active" if current == num else ""
        pills_html += (
            f'<div class="ml-page-pill {active_cls}">'
            f'<span class="ml-page-dot"></span>{label}</div>'
        )
    pills_html += "</div>"
    st.markdown(pills_html, unsafe_allow_html=True)


# PAGE 1 — Landing
def page_landing():
    st.markdown(render_navbar_brand(), unsafe_allow_html=True)
    render_page_indicator(1)
    st.markdown(render_hero(), unsafe_allow_html=True)
    st.markdown(render_landing_features(), unsafe_allow_html=True)
    st.markdown(render_how_it_works(), unsafe_allow_html=True)
    st.markdown(render_stats(), unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Get Started — Analyze an Instruction", use_container_width=True, key="get_started_btn"):
            go_to(2)
            st.rerun()

    st.markdown(
        '<div class="ml-cta-note">No account required · Free to use · Results in seconds</div>',
        unsafe_allow_html=True,
    )
    st.markdown(render_footer(), unsafe_allow_html=True)


# PAGE 2 — Analyze & Translate
def page_analyze():
    st.markdown(render_navbar_brand(), unsafe_allow_html=True)
    render_page_indicator(2)

    st.markdown(
        render_page_header(
            eyebrow="Step 2 — Input and Configure",
            title="Paste Your Discharge Instruction",
            subtitle="Our ML model will validate it, then simplify and translate into your chosen languages.",
        ),
        unsafe_allow_html=True,
    )

    user_input = st.text_area(
        "Medical discharge instruction",
        value=st.session_state.input_text,
        placeholder=(
            "e.g. Administer 500mg Amoxicillin PO q8h for 7 days. "
            "Monitor for signs of allergic reaction including urticaria, "
            "angioedema, or anaphylaxis. Maintain adequate hydration."
        ),
        height=160,
        label_visibility="visible",
    )
    st.session_state.input_text = user_input

    st.markdown(
        render_tip(
            "Paste the full discharge instruction for best results. "
            "The system will validate medical content, simplify terminology, "
            "break it into steps, and translate into your selected languages."
        ),
        unsafe_allow_html=True,
    )

    col_lang, col_preset = st.columns([3, 1])

    with col_lang:
        selected_languages = st.multiselect(
            "Target languages",
            options=all_languages,
            default=st.session_state.selected_languages,
            help="Select one or more languages for translation.",
        )

    with col_preset:
        preset_options = ["Custom"] + list(PRESETS.keys())
        preset_choice = st.selectbox("Quick preset", options=preset_options, index=0)

    if preset_choice != "Custom" and preset_choice in PRESETS:
        selected_languages = PRESETS[preset_choice]
        st.caption(f"Preset applied: {preset_choice} — {len(selected_languages)} languages")

    st.session_state.selected_languages = selected_languages

    if selected_languages:
        st.caption(
            f"{len(selected_languages)} language{'s' if len(selected_languages) != 1 else ''} selected"
        )

    st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

    # Primary action button - full width
    analyze = st.button("Analyze and Translate", use_container_width=True, key="analyze_btn")

    st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)

    # Secondary action button - full width
    st.markdown('<div class="ml-secondary-btn">', unsafe_allow_html=True)
    back_clicked = st.button("Back to Home", use_container_width=True, key="back_btn")
    st.markdown('</div>', unsafe_allow_html=True)

    if back_clicked:
        go_to(1)
        st.rerun()

    if analyze:
        if not user_input.strip():
            st.warning("Please enter a medical discharge instruction.")
        elif not selected_languages:
            st.warning("Please select at least one target language.")
        else:
            # Check for API key
            if "GROQ_API_KEY" not in st.secrets:
                st.error("GROQ_API_KEY not found. Please add it to .streamlit/secrets.toml")
                st.info("Get a free API key from https://console.groq.com/")
                return
            
            # Process medical confidence
            with st.spinner("Evaluating medical content..."):
                confidence = compute_medical_confidence(user_input, models)

            if confidence < MEDICAL_CONFIDENCE_THRESHOLD:
                st.error(
                    "This does not appear to be a valid medical discharge instruction. "
                    "Please verify your input and try again."
                )
            else:
                safety_score = compute_safety_score(user_input, models)
                safety_status = get_safety_status(safety_score)

                # Process instruction with translations
                raw_output = process_instruction(user_input, selected_languages)
                sections = parse_output(raw_output, selected_languages)

                st.session_state.confidence = confidence
                st.session_state.safety_score = safety_score
                st.session_state.safety_status = safety_status
                st.session_state.results = sections
                go_to(3)
                st.rerun()

    st.markdown(render_footer(), unsafe_allow_html=True)


# PAGE 3 — Results
def page_results():
    st.markdown(render_navbar_brand(), unsafe_allow_html=True)
    render_page_indicator(3)

    if not st.session_state.results:
        st.warning("No results found. Please go back and analyze an instruction first.")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("Go to Analyze", use_container_width=True):
                go_to(2)
                st.rerun()
        return

    sections = st.session_state.results
    confidence = st.session_state.confidence
    safety_score = st.session_state.safety_score
    safety_status = st.session_state.safety_status
    selected_languages = st.session_state.selected_languages

    simplified = sections["simplified"] or "Not available. Please try again."
    steps = sections["steps"] or "Not available. Please try again."

    st.markdown(
        render_page_header(
            eyebrow="Step 3 — Analysis Results",
            title="Your Report Is Ready",
            subtitle="Review the simplified instruction, step-by-step guide, and translations below.",
        ),
        unsafe_allow_html=True,
    )

    st.markdown(render_results_header(), unsafe_allow_html=True)
    st.markdown(render_metrics(confidence, safety_score, safety_status), unsafe_allow_html=True)
    st.markdown(render_safety_bar(safety_score, safety_status["color"]), unsafe_allow_html=True)

    st.markdown(
        render_panel(
            title="Simplified Version",
            subtitle="Plain-English rewrite for patient comprehension",
            content=simplified,
            icon="S",
            icon_type="accent",
        ),
        unsafe_allow_html=True,
    )

    st.markdown(
        render_panel(
            title="Step-by-Step Guide",
            subtitle="Actionable steps the patient needs to follow",
            content=steps,
            icon="G",
            icon_type="teal",
        ),
        unsafe_allow_html=True,
    )

    if selected_languages:
        st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
        st.markdown(
            '<div class="ml-section-label">Translations</div>',
            unsafe_allow_html=True,
        )
        tabs = st.tabs(selected_languages)
        for i, lang in enumerate(selected_languages):
            with tabs[i]:
                content = sections["translations"].get(lang, "")
                st.markdown(render_translation_content(content, lang), unsafe_allow_html=True)

    st.markdown('<div class="ml-divider"></div>', unsafe_allow_html=True)

    # Download section
    st.markdown(
        '<div class="ml-section-label" style="margin-bottom:14px;">Download Report</div>',
        unsafe_allow_html=True,
    )

    report_lines = [
        "MEDLINGO REPORT",
        "=" * 50,
        "",
        "SIMPLIFIED VERSION",
        "-" * 30,
        simplified,
        "",
        "STEP-BY-STEP GUIDE",
        "-" * 30,
        steps,
        "",
    ]
    for lang in selected_languages:
        content = sections["translations"].get(lang, "").strip()
        report_lines.extend([
            f"TRANSLATION: {lang.upper()}",
            "-" * 30,
            content if content else "(Not available)",
            "",
        ])
    full_report = "\n".join(report_lines)

    # Download button - full width
    st.download_button(
        label="Download Text Report",
        data=full_report,
        file_name="medlingo_report.txt",
        mime="text/plain",
        use_container_width=True,
    )

    st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)

    # New Analysis button - full width
    st.markdown('<div class="ml-secondary-btn">', unsafe_allow_html=True)
    if st.button("New Analysis", use_container_width=True):
        st.session_state.results = None
        st.session_state.input_text = ""
        go_to(2)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("View raw model output"):
        st.code(sections.get("raw", ""), language=None)

    st.markdown(render_footer(), unsafe_allow_html=True)


# Router
page = st.session_state.page

if page == 1:
    page_landing()
elif page == 2:
    page_analyze()
elif page == 3:
    page_results()