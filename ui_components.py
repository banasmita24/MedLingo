"""
Reusable UI components — clean light theme with proper alignments.
"""

import html as _html_mod


def render_navbar_brand() -> str:
    return """
    <div class="ml-navbar">
        <div class="ml-navbar-brand">
            <div class="ml-navbar-logo">ML</div>
            <div>
                <div class="ml-navbar-name">Med<span>Lingo</span></div>
                <div class="ml-navbar-tagline">Discharge Instruction Assistant</div>
            </div>
        </div>
        <div class="ml-navbar-right">
            <div class="ml-navbar-badge">
                <div class="ml-navbar-dot"></div>
                80+ Languages
            </div>
        </div>
    </div>
    """


def render_hero() -> str:
    return """
    <div class="ml-hero">
        <div class="ml-hero-pill">AI-Powered Medical Translation</div>
        <h1 class="ml-hero-title">
            Discharge instructions,<br>
            <span class="grad">understood by everyone.</span>
        </h1>
        <p class="ml-hero-sub">
            Paste any medical discharge instruction. MedLingo simplifies
            complex terminology and translates it into 80+ languages instantly.
        </p>
    </div>
    """


def render_landing_features() -> str:
    return """
    <div class="ml-features">
        <div class="ml-feature-card">
            <div class="ml-feature-icon accent">ML</div>
            <div class="ml-feature-title">ML Safety Analysis</div>
            <div class="ml-feature-desc">
                Validates medical instructions using a Restricted Boltzmann Machine reconstruction model, flagging unusual patterns instantly.
            </div>
        </div>
        <div class="ml-feature-card">
            <div class="ml-feature-icon teal">AI</div>
            <div class="ml-feature-title">LLM Simplification</div>
            <div class="ml-feature-desc">
                Rewrites complex clinical language into plain English any patient can understand, with clear step-by-step guidance.
            </div>
        </div>
        <div class="ml-feature-card">
            <div class="ml-feature-icon green">TX</div>
            <div class="ml-feature-title">80+ Languages</div>
            <div class="ml-feature-desc">
                Translates into Indian, European, Asian, Middle Eastern, and African languages — batch-processed for reliability.
            </div>
        </div>
    </div>
    """


def render_how_it_works() -> str:
    return """
    <div class="ml-how">
        <div class="ml-how-title">How It Works</div>
        <div class="ml-how-steps">
            <div class="ml-how-step">
                <div class="ml-how-num">1</div>
                <div class="ml-how-label">Paste Instruction</div>
                <div class="ml-how-sub">Enter any clinical discharge instruction</div>
            </div>
            <div class="ml-how-step">
                <div class="ml-how-num">2</div>
                <div class="ml-how-label">ML Validation</div>
                <div class="ml-how-sub">Model scores safety and medical relevance</div>
            </div>
            <div class="ml-how-step">
                <div class="ml-how-num">3</div>
                <div class="ml-how-label">LLM Simplification</div>
                <div class="ml-how-sub">Rewrites in plain English with clear steps</div>
            </div>
            <div class="ml-how-step">
                <div class="ml-how-num">4</div>
                <div class="ml-how-label">Translate and Download</div>
                <div class="ml-how-sub">Get a full report in 80+ languages</div>
            </div>
        </div>
    </div>
    """


def render_stats() -> str:
    return """
    <div class="ml-stats">
        <div class="ml-stat">
            <div class="ml-stat-num">80+</div>
            <div class="ml-stat-label">Languages</div>
        </div>
        <div class="ml-stat">
            <div class="ml-stat-num">ML</div>
            <div class="ml-stat-label">Safety Scoring</div>
        </div>
        <div class="ml-stat">
            <div class="ml-stat-num">LLM</div>
            <div class="ml-stat-label">Simplification</div>
        </div>
    </div>
    """


def render_page_header(eyebrow: str, title: str, subtitle: str) -> str:
    return f"""
    <div class="ml-page-header">
        <div class="ml-page-header-eyebrow">{_esc(eyebrow)}</div>
        <div class="ml-page-header-title">{_esc(title)}</div>
        <div class="ml-page-header-sub">{_esc(subtitle)}</div>
    </div>
    """


def render_metrics(confidence: float, safety_score: float, safety_status: dict) -> str:
    conf_pct = f"{confidence:.0%}"
    conf_color = "#16A34A" if confidence > 0.8 else "#D97706" if confidence > 0.6 else "#DC2626"
    conf_cls = "green" if confidence > 0.8 else "orange" if confidence > 0.6 else "red"
    safety_color = safety_status["color"]
    safety_cls = "green" if safety_score > 0.8 else "orange" if safety_score > 0.6 else "red"
    badge_bg = safety_status.get("bg", "rgba(0,0,0,0.05)")
    badge_border = safety_status.get("border", "rgba(0,0,0,0.1)")

    return f"""
    <div class="ml-metrics">
        <div class="ml-metric-card {conf_cls}">
            <div class="ml-metric-eyebrow">Medical Confidence</div>
            <div class="ml-metric-value" style="color: {conf_color};">{conf_pct}</div>
            <div class="ml-metric-desc">Classification probability</div>
        </div>
        <div class="ml-metric-card {safety_cls}">
            <div class="ml-metric-eyebrow">Safety Score</div>
            <div class="ml-metric-value" style="color: {safety_color};">{safety_score:.2f}</div>
            <div class="ml-metric-desc">Reconstruction analysis</div>
        </div>
        <div class="ml-metric-card teal">
            <div class="ml-metric-eyebrow">Status</div>
            <div class="ml-metric-badge" style="background:{badge_bg}; border: 1px solid {badge_border}; color:{safety_color};">
                <div class="ml-metric-badge-dot" style="background:{safety_color};"></div>
                {_esc(safety_status['label'])}
            </div>
            <div class="ml-metric-desc">{_esc(safety_status['description'])}</div>
        </div>
    </div>
    """


def render_safety_bar(score: float, color: str) -> str:
    pct = max(0, min(100, score * 100))
    return f"""
    <div class="ml-safety-bar-wrap">
        <div class="ml-safety-bar-row">
            <div class="ml-safety-bar-label">Safety Analysis</div>
            <div class="ml-safety-bar-pct">{pct:.0f}%</div>
        </div>
        <div class="ml-safety-track">
            <div class="ml-safety-fill" style="width:{pct:.0f}%; background: linear-gradient(90deg, {color}99, {color});"></div>
        </div>
        <div class="ml-safety-endpoints">
            <span>Caution</span>
            <span>Safe</span>
        </div>
    </div>
    """


def render_results_header() -> str:
    return """
    <div class="ml-results-header">
        <div class="ml-results-title">Analysis Results</div>
        <div class="ml-results-divider"></div>
    </div>
    """


def render_panel(title: str, subtitle: str, content: str, icon: str = "S", icon_type: str = "accent") -> str:
    safe_content = _esc(content).replace("\n", "<br>")
    return f"""
    <div class="ml-panel">
        <div class="ml-panel-head">
            <div class="ml-panel-icon {icon_type}">{_esc(icon)}</div>
            <div>
                <div class="ml-panel-title">{_esc(title)}</div>
                <div class="ml-panel-subtitle">{_esc(subtitle)}</div>
            </div>
        </div>
        <div class="ml-panel-body">{safe_content}</div>
    </div>
    """


def render_translation_content(content: str, language: str) -> str:
    if not content:
        return f"""
        <div class="ml-translation-empty">
            Translation for <strong>{_esc(language)}</strong> was not returned by the model.
            Try re-running or reducing the number of selected languages.
        </div>
        """
    safe_content = _esc(content).replace("\n", "<br>")
    return f'<div class="ml-translation-box">{safe_content}</div>'


def render_tip(text: str) -> str:
    return f'<div class="ml-tip">{_esc(text)}</div>'


def render_footer() -> str:
    return """
    <div class="ml-footer">
        <div class="ml-footer-brand"><span>MedLingo</span></div>
        <div class="ml-footer-text">
            AI-Powered Medical Discharge Instruction Assistant — 80+ languages supported
        </div>
    </div>
    """


def _esc(text: str) -> str:
    return _html_mod.escape(str(text))