"""
MedLingo UI styles — Clean light theme with proper alignments.
"""


def get_css() -> str:
    return """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* ── CSS Variables — Light theme ── */
    :root {
        --bg-base:        #F8F9FC;
        --bg-surface:     #FFFFFF;
        --bg-elevated:    #F1F3F8;
        --bg-card:        #FFFFFF;
        --bg-card-hover:  #F7F8FC;
        --border:         #E4E7EF;
        --border-strong:  #CDD2E1;
        --text-primary:   #111827;
        --text-secondary: #374151;
        --text-muted:     #6B7280;
        --text-light:     #9CA3AF;
        --accent:         #4F46E5;
        --accent-hover:   #4338CA;
        --accent-light:   #EEF2FF;
        --accent-border:  #C7D2FE;
        --teal:           #0D9488;
        --teal-light:     #F0FDFA;
        --teal-border:    #99F6E4;
        --green:          #16A34A;
        --green-light:    #F0FDF4;
        --green-border:   #BBF7D0;
        --orange:         #D97706;
        --orange-light:   #FFFBEB;
        --orange-border:  #FDE68A;
        --red:            #DC2626;
        --red-light:      #FFF1F2;
        --red-border:     #FECDD3;
        --radius-sm:  6px;
        --radius-md:  10px;
        --radius-lg:  14px;
        --radius-xl:  20px;
        --shadow-xs:  0 1px 2px rgba(0,0,0,0.05);
        --shadow-sm:  0 1px 6px rgba(0,0,0,0.07), 0 1px 2px rgba(0,0,0,0.04);
        --shadow-md:  0 4px 16px rgba(0,0,0,0.08), 0 2px 6px rgba(0,0,0,0.05);
    }

    /* ── Base ── */
    .stApp {
        background: var(--bg-base) !important;
        font-family: 'Inter', sans-serif !important;
    }

    #MainMenu, footer, header { visibility: hidden; }
    * { box-sizing: border-box; }

    .block-container {
        max-width: 880px !important;
        padding: 0 1.5rem 3rem !important;
        margin: 0 auto !important;
    }

    /* ── Navbar ── */
    .ml-navbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 20px 0 16px 0;
        border-bottom: 1px solid var(--border);
        margin-bottom: 8px;
    }

    .ml-navbar-brand {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .ml-navbar-logo {
        width: 36px;
        height: 36px;
        background: linear-gradient(135deg, var(--accent) 0%, var(--teal) 100%);
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.75rem;
        font-weight: 800;
        color: white;
        letter-spacing: 0.5px;
        flex-shrink: 0;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25);
    }

    .ml-navbar-name {
        font-size: 1.1rem;
        font-weight: 700;
        color: var(--text-primary);
        letter-spacing: -0.4px;
        line-height: 1.3;
    }

    .ml-navbar-name span {
        background: linear-gradient(135deg, var(--accent), var(--teal));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .ml-navbar-tagline {
        font-size: 0.7rem;
        color: var(--text-muted);
        font-weight: 400;
        margin-top: 2px;
    }

    .ml-navbar-right {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .ml-navbar-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: var(--accent-light);
        border: 1px solid var(--accent-border);
        border-radius: 24px;
        padding: 6px 14px;
        font-size: 0.7rem;
        font-weight: 600;
        color: var(--accent);
        letter-spacing: 0.2px;
    }

    .ml-navbar-dot {
        width: 6px;
        height: 6px;
        background: var(--teal);
        border-radius: 50%;
        animation: pulse-dot 2.5s infinite;
        flex-shrink: 0;
    }

    @keyframes pulse-dot {
        0%, 100% { opacity: 1; transform: scale(1); }
        50%       { opacity: 0.4; transform: scale(0.75); }
    }

    /* ── Page Navigation ── */
    .ml-page-nav {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 8px;
        margin: 24px 0 36px 0;
    }

    .ml-page-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 18px;
        border-radius: 30px;
        font-size: 0.75rem;
        font-weight: 600;
        border: 1.5px solid var(--border);
        background: var(--bg-card);
        color: var(--text-muted);
        letter-spacing: 0.2px;
        box-shadow: var(--shadow-xs);
        transition: all 0.15s ease;
    }

    .ml-page-pill.active {
        background: var(--accent-light);
        border-color: var(--accent);
        color: var(--accent);
        box-shadow: 0 2px 8px rgba(79, 70, 229, 0.12);
    }

    .ml-page-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: currentColor;
        opacity: 0.8;
    }

    /* ── Hero Section ── */
    .ml-hero {
        text-align: center;
        padding: 48px 24px 40px;
    }

    .ml-hero-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: var(--teal-light);
        border: 1px solid var(--teal-border);
        border-radius: 30px;
        padding: 6px 16px;
        font-size: 0.7rem;
        font-weight: 700;
        color: var(--teal);
        letter-spacing: 0.8px;
        text-transform: uppercase;
        margin-bottom: 24px;
    }

    .ml-hero-title {
        font-size: clamp(2rem, 5vw, 2.8rem);
        font-weight: 800;
        color: var(--text-primary);
        letter-spacing: -1.2px;
        line-height: 1.15;
        margin: 0 0 20px 0;
    }

    .ml-hero-title .grad {
        background: linear-gradient(135deg, var(--accent) 0%, var(--teal) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .ml-hero-sub {
        font-size: clamp(0.9rem, 2vw, 1.05rem);
        color: var(--text-muted);
        font-weight: 400;
        max-width: 480px;
        margin: 0 auto;
        line-height: 1.7;
    }

    /* ── Feature Cards ── */
    .ml-features {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
        margin: 40px 0;
    }

    .ml-feature-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 24px 20px;
        transition: all 0.2s ease;
        box-shadow: var(--shadow-sm);
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        height: 100%;
    }

    .ml-feature-card:hover {
        border-color: var(--accent-border);
        box-shadow: var(--shadow-md);
        transform: translateY(-3px);
    }

    .ml-feature-icon {
        width: 40px;
        height: 40px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.7rem;
        font-weight: 800;
        letter-spacing: 0.5px;
        margin-bottom: 16px;
        flex-shrink: 0;
    }

    .ml-feature-icon.accent {
        background: var(--accent-light);
        color: var(--accent);
        border: 1.5px solid var(--accent-border);
    }

    .ml-feature-icon.teal {
        background: var(--teal-light);
        color: var(--teal);
        border: 1.5px solid var(--teal-border);
    }

    .ml-feature-icon.green {
        background: var(--green-light);
        color: var(--green);
        border: 1.5px solid var(--green-border);
    }

    .ml-feature-title {
        font-size: 0.95rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 8px;
        letter-spacing: -0.2px;
    }

    .ml-feature-desc {
        font-size: 0.8rem;
        color: var(--text-muted);
        line-height: 1.65;
        flex: 1;
    }

    .ml-feature-card::after {
        content: '';
        display: block;
        height: 3px;
        border-radius: 0 0 var(--radius-lg) var(--radius-lg);
        margin: 18px -20px -24px;
    }

    .ml-feature-card:nth-child(1)::after { background: var(--accent); opacity: 0.5; }
    .ml-feature-card:nth-child(2)::after { background: var(--teal); opacity: 0.5; }
    .ml-feature-card:nth-child(3)::after { background: var(--green); opacity: 0.5; }

    /* ── How It Works ── */
    .ml-how {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius-xl);
        padding: 32px 28px;
        margin: 8px 0 28px 0;
        box-shadow: var(--shadow-sm);
    }

    .ml-how-title {
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: var(--text-muted);
        margin-bottom: 28px;
        text-align: center;
    }

    .ml-how-steps {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
    }

    .ml-how-step {
        text-align: center;
        padding: 0 8px;
    }

    .ml-how-num {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        background: var(--accent-light);
        border: 2px solid var(--accent-border);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.9rem;
        font-weight: 800;
        color: var(--accent);
        margin: 0 auto 12px auto;
    }

    .ml-how-label {
        font-size: 0.82rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 6px;
    }

    .ml-how-sub {
        font-size: 0.72rem;
        color: var(--text-muted);
        line-height: 1.55;
    }

    /* ── Stats ── */
    .ml-stats {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
        margin-bottom: 40px;
    }

    .ml-stat {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 22px 16px;
        text-align: center;
        box-shadow: var(--shadow-sm);
    }

    .ml-stat-num {
        font-size: 1.6rem;
        font-weight: 800;
        letter-spacing: -0.8px;
        background: linear-gradient(135deg, var(--accent), var(--teal));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.2;
    }

    .ml-stat-label {
        font-size: 0.72rem;
        color: var(--text-muted);
        font-weight: 500;
        margin-top: 6px;
    }

    .ml-cta-note {
        font-size: 0.75rem;
        color: var(--text-light);
        margin-top: 14px;
        text-align: center;
    }

    /* ── Page Header ── */
    .ml-page-header {
        text-align: center;
        padding: 20px 0 16px 0;
        margin-bottom: 12px;
    }

    .ml-page-header-eyebrow {
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: var(--text-muted);
        margin-bottom: 12px;
    }

    .ml-page-header-title {
        font-size: 1.8rem;
        font-weight: 800;
        color: var(--text-primary);
        letter-spacing: -0.8px;
        margin-bottom: 10px;
        line-height: 1.2;
    }

    .ml-page-header-sub {
        font-size: 0.9rem;
        color: var(--text-muted);
        max-width: 460px;
        margin: 0 auto;
        line-height: 1.6;
    }

    /* ── Results Header ── */
    .ml-results-header {
        display: flex;
        align-items: center;
        gap: 16px;
        margin: 8px 0 24px 0;
    }

    .ml-results-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: var(--text-primary);
        letter-spacing: -0.3px;
        white-space: nowrap;
    }

    .ml-results-divider {
        flex: 1;
        height: 1px;
        background: linear-gradient(90deg, var(--border), transparent);
    }

    /* ── Metrics Cards ── */
    .ml-metrics {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 14px;
        margin-bottom: 20px;
    }

    .ml-metric-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 18px 18px 16px;
        box-shadow: var(--shadow-sm);
        transition: box-shadow 0.2s;
        display: flex;
        flex-direction: column;
    }

    .ml-metric-card:hover {
        box-shadow: var(--shadow-md);
    }

    .ml-metric-card.green  { border-left: 4px solid var(--green); }
    .ml-metric-card.orange { border-left: 4px solid var(--orange); }
    .ml-metric-card.red    { border-left: 4px solid var(--red); }
    .ml-metric-card.teal   { border-left: 4px solid var(--teal); }

    .ml-metric-eyebrow {
        font-size: 0.62rem;
        font-weight: 700;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        color: var(--text-muted);
        margin-bottom: 10px;
    }

    .ml-metric-value {
        font-size: 2rem;
        font-weight: 800;
        letter-spacing: -0.8px;
        line-height: 1;
        margin-bottom: 6px;
    }

    .ml-metric-desc {
        font-size: 0.7rem;
        color: var(--text-muted);
    }

    .ml-metric-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .ml-metric-badge-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        flex-shrink: 0;
    }

    /* ── Safety Bar ── */
    .ml-safety-bar-wrap {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 16px 20px 18px;
        margin-bottom: 22px;
        box-shadow: var(--shadow-sm);
    }

    .ml-safety-bar-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
    }

    .ml-safety-bar-label {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        color: var(--text-muted);
    }

    .ml-safety-bar-pct {
        font-size: 0.8rem;
        font-weight: 700;
        color: var(--text-secondary);
    }

    .ml-safety-track {
        height: 8px;
        background: var(--bg-elevated);
        border-radius: 10px;
        overflow: hidden;
    }

    .ml-safety-fill {
        height: 100%;
        border-radius: 10px;
        transition: width 0.9s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .ml-safety-endpoints {
        display: flex;
        justify-content: space-between;
        margin-top: 8px;
        font-size: 0.65rem;
        color: var(--text-light);
        font-weight: 500;
    }

    /* ── Content Panels ── */
    .ml-panel {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        margin-bottom: 16px;
        overflow: hidden;
        box-shadow: var(--shadow-sm);
    }

    .ml-panel-head {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 14px 20px;
        border-bottom: 1px solid var(--border);
        background: var(--bg-base);
    }

    .ml-panel-icon {
        width: 30px;
        height: 30px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.72rem;
        font-weight: 800;
        flex-shrink: 0;
    }

    .ml-panel-icon.accent {
        background: var(--accent-light);
        color: var(--accent);
        border: 1.5px solid var(--accent-border);
    }

    .ml-panel-icon.teal {
        background: var(--teal-light);
        color: var(--teal);
        border: 1.5px solid var(--teal-border);
    }

    .ml-panel-title {
        font-size: 0.88rem;
        font-weight: 700;
        color: var(--text-primary);
        letter-spacing: -0.2px;
    }

    .ml-panel-subtitle {
        font-size: 0.68rem;
        color: var(--text-muted);
        font-weight: 400;
        margin-top: 2px;
    }

    .ml-panel-body {
        padding: 18px 22px;
        color: var(--text-secondary);
        font-size: 0.9rem;
        line-height: 1.8;
    }

    /* ── Tip ── */
    .ml-tip {
        background: var(--accent-light);
        border: 1px solid var(--accent-border);
        border-left: 4px solid var(--accent);
        border-radius: 0 var(--radius-md) var(--radius-md) 0;
        padding: 12px 16px;
        font-size: 0.8rem;
        color: var(--text-secondary);
        line-height: 1.6;
        margin: 14px 0 22px 0;
    }

    /* ── Section Label ── */
    .ml-section-label {
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: var(--text-muted);
        margin-bottom: 14px;
    }

    /* ── Divider ── */
    .ml-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, var(--border), transparent);
        margin: 28px 0;
    }

    /* ── Translation Box ── */
    .ml-translation-box {
        background: var(--bg-elevated);
        border: 1px solid var(--border);
        border-radius: var(--radius-md);
        padding: 18px 22px;
        color: var(--text-secondary);
        font-size: 0.88rem;
        line-height: 1.8;
    }

    .ml-translation-empty {
        background: var(--bg-elevated);
        border: 1.5px dashed var(--border-strong);
        border-radius: var(--radius-md);
        padding: 32px 24px;
        text-align: center;
        color: var(--text-muted);
        font-size: 0.85rem;
    }

    /* ── Footer ── */
    .ml-footer {
        text-align: center;
        padding: 32px 0 20px 0;
        border-top: 1px solid var(--border);
        margin-top: 48px;
    }

    .ml-footer-brand {
        font-size: 0.88rem;
        font-weight: 700;
        color: var(--text-muted);
        margin-bottom: 8px;
    }

    .ml-footer-brand span {
        background: linear-gradient(135deg, var(--accent), var(--teal));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .ml-footer-text {
        font-size: 0.72rem;
        color: var(--text-light);
        font-weight: 400;
    }

    /* ── Streamlit Widget Overrides ── */
    .stTextArea textarea {
        background: var(--bg-card) !important;
        border: 1.5px solid var(--border-strong) !important;
        border-radius: var(--radius-md) !important;
        color: var(--text-primary) !important;
        font-size: 0.9rem !important;
        font-family: 'Inter', sans-serif !important;
        padding: 14px 16px !important;
        line-height: 1.7 !important;
        caret-color: var(--accent) !important;
        box-shadow: var(--shadow-xs) !important;
    }

    .stTextArea textarea:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1) !important;
        outline: none !important;
    }

    .stTextArea textarea::placeholder {
        color: var(--text-light) !important;
    }

    .stTextArea label,
    .stMultiSelect label,
    .stSelectbox label {
        color: var(--text-secondary) !important;
        font-weight: 600 !important;
        font-size: 0.8rem !important;
        font-family: 'Inter', sans-serif !important;
        margin-bottom: 4px !important;
    }

    .stMultiSelect > div > div,
    .stSelectbox > div > div {
        background: var(--bg-card) !important;
        border: 1.5px solid var(--border-strong) !important;
        border-radius: var(--radius-md) !important;
        color: var(--text-primary) !important;
        box-shadow: var(--shadow-xs) !important;
    }

    .stMultiSelect [data-baseweb="tag"] {
        background: var(--accent-light) !important;
        border: 1px solid var(--accent-border) !important;
        border-radius: 6px !important;
        color: var(--accent) !important;
        font-weight: 600 !important;
        font-size: 0.75rem !important;
    }

    [data-baseweb="popover"],
    [data-baseweb="menu"],
    [data-baseweb="select"] ul {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
        box-shadow: var(--shadow-md) !important;
    }

    [data-baseweb="option"]:hover {
        background: var(--accent-light) !important;
    }

    /* ── Tabs ── */
    .stTabs [data-baseweb="tab-list"] {
        background: var(--bg-elevated) !important;
        border-radius: var(--radius-md) !important;
        padding: 4px !important;
        gap: 2px !important;
        border: 1px solid var(--border) !important;
        flex-wrap: wrap !important;
        box-shadow: var(--shadow-xs) !important;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: var(--radius-sm) !important;
        color: var(--text-muted) !important;
        font-weight: 600 !important;
        font-size: 0.76rem !important;
        padding: 6px 14px !important;
        font-family: 'Inter', sans-serif !important;
    }

    .stTabs [aria-selected="true"] {
        background: var(--bg-card) !important;
        color: var(--accent) !important;
        font-weight: 700 !important;
        box-shadow: var(--shadow-sm) !important;
    }

    .stTabs [data-baseweb="tab-panel"] {
        padding-top: 16px !important;
    }

    /* ── Buttons ── */
    .stButton > button {
        background: var(--accent) !important;
        color: white !important;
        border: none !important;
        border-radius: var(--radius-md) !important;
        padding: 12px 24px !important;
        font-size: 0.9rem !important;
        font-weight: 600 !important;
        font-family: 'Inter', sans-serif !important;
        width: 100% !important;
        letter-spacing: 0.2px !important;
        box-shadow: 0 2px 12px rgba(79, 70, 229, 0.25) !important;
        transition: all 0.15s ease !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    .stButton > button:hover {
        background: var(--accent-hover) !important;
        box-shadow: 0 4px 20px rgba(79, 70, 229, 0.35) !important;
        transform: translateY(-1px) !important;
    }

    .ml-secondary-btn .stButton > button {
        background: var(--bg-card) !important;
        color: var(--text-secondary) !important;
        border: 1.5px solid var(--border-strong) !important;
        box-shadow: var(--shadow-xs) !important;
    }

    .ml-secondary-btn .stButton > button:hover {
        background: var(--bg-elevated) !important;
        border-color: var(--text-muted) !important;
        box-shadow: var(--shadow-sm) !important;
        transform: none !important;
    }

    /* ── Download Button ── */
    .stDownloadButton > button {
        background: var(--bg-card) !important;
        border: 1.5px solid var(--border-strong) !important;
        color: var(--text-secondary) !important;
        border-radius: var(--radius-md) !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        transition: all 0.15s !important;
        width: 100% !important;
        padding: 12px 24px !important;
        box-shadow: var(--shadow-xs) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    .stDownloadButton > button:hover {
        background: var(--accent-light) !important;
        border-color: var(--accent-border) !important;
        color: var(--accent) !important;
    }

    /* ── Alerts ── */
    .stAlert {
        background: var(--bg-card) !important;
        border-radius: var(--radius-md) !important;
        border: 1px solid var(--border) !important;
        font-family: 'Inter', sans-serif !important;
        color: var(--text-secondary) !important;
        box-shadow: var(--shadow-sm) !important;
    }

    hr {
        border-color: var(--border) !important;
        margin: 24px 0 !important;
    }

    /* ── Expander ── */
    .stExpander {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
        box-shadow: var(--shadow-xs) !important;
        margin-top: 16px !important;
    }

    .stExpander summary {
        color: var(--text-secondary) !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.8rem !important;
        font-weight: 600 !important;
        padding: 10px 16px !important;
    }

    .stSpinner > div {
        border-top-color: var(--accent) !important;
    }

    /* ── Column Layout Fixes ── */
    [data-testid="column"] {
        padding: 0 6px !important;
    }

    [data-testid="column"]:first-child {
        padding-left: 0 !important;
    }

    [data-testid="column"]:last-child {
        padding-right: 0 !important;
    }

    /* ── Button Row Alignment ── */
    .stHorizontalBlock {
        align-items: center !important;
    }

    div[data-testid="stHorizontalBlock"] > div {
        display: flex !important;
        align-items: stretch !important;
    }

    div[data-testid="stHorizontalBlock"] > div > div {
        display: flex !important;
        align-items: stretch !important;
    }

    div[data-testid="stHorizontalBlock"] .stButton,
    div[data-testid="stHorizontalBlock"] .stDownloadButton {
        height: 100% !important;
        display: flex !important;
        align-items: stretch !important;
    }

    div[data-testid="stHorizontalBlock"] .stButton > button,
    div[data-testid="stHorizontalBlock"] .stDownloadButton > button {
        height: 100% !important;
        min-height: 48px !important;
    }

    /* ── Caption Text ── */
    .stCaption {
        font-size: 0.75rem !important;
        color: var(--text-muted) !important;
    }

    /* ════════════════════════════════════════
       RESPONSIVE
    ════════════════════════════════════════ */
    @media (max-width: 768px) {
        .block-container {
            padding: 0 1rem 2.5rem !important;
        }

        .ml-hero {
            padding: 36px 12px 28px;
        }

        .ml-features {
            grid-template-columns: 1fr;
            gap: 14px;
        }

        .ml-how-steps {
            grid-template-columns: repeat(2, 1fr);
            gap: 24px 16px;
        }

        .ml-metrics {
            grid-template-columns: 1fr 1fr;
        }

        .ml-navbar-badge {
            display: none;
        }

        .ml-panel-body {
            padding: 14px 18px;
            font-size: 0.86rem;
        }

        .ml-translation-box {
            padding: 14px 16px;
            font-size: 0.86rem;
        }
    }

    @media (max-width: 480px) {
        .block-container {
            padding: 0 0.75rem 2rem !important;
        }

        .ml-metrics {
            grid-template-columns: 1fr;
        }

        .ml-stats {
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
        }

        .ml-how-steps {
            grid-template-columns: 1fr;
            gap: 18px;
        }

        .ml-metric-value {
            font-size: 1.6rem;
        }

        .ml-navbar-tagline {
            display: none;
        }

        .ml-page-pill {
            font-size: 0.7rem;
            padding: 6px 14px;
        }

        .ml-hero-title {
            letter-spacing: -0.5px;
        }

        .ml-page-header-title {
            font-size: 1.5rem;
        }
    }

    @media (min-width: 1100px) {
        .block-container {
            max-width: 880px !important;
        }
    }
</style>
"""