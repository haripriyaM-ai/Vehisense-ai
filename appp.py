import streamlit as st
import time as time_module

st.set_page_config(
    page_title="VehiSense AI",
    page_icon=None,
    layout="wide"
)

# ============================================================
# THEME — Navy / White / Light Grey enterprise diagnostic UI
# ============================================================
st.markdown("""
<style>
:root {
    --navy: #0B1E3D;
    --navy-light: #14294D;
    --steel: #2C3E5C;
    --grey-bg: #F4F6F9;
    --grey-border: #D8DEE6;
    --text-dark: #101828;
    --text-muted: #5A6472;
    --critical: #B3261E;
    --warning: #B5750B;
    --ok: #1B6B3C;
    --root: #0B1E3D;
}

/* Remove Streamlit default chrome feel */
#MainMenu, footer {visibility: hidden;}
.block-container {padding-top: 1.5rem; max-width: 1100px;}
body, .stApp {background-color: var(--grey-bg);}

/* ---------- Header ---------- */
.vs-header {
    background-color: var(--navy);
    border-radius: 6px;
    padding: 22px 28px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 22px;
}
.vs-header-title {
    color: #FFFFFF;
    font-size: 26px;
    font-weight: 700;
    letter-spacing: 0.5px;
    margin: 0;
}
.vs-header-sub {
    color: #AEB9CC;
    font-size: 13px;
    font-weight: 400;
    margin-top: 2px;
}
.badge-row { display: flex; gap: 8px; flex-wrap: wrap; }
.badge {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.4px;
    padding: 5px 10px;
    border-radius: 3px;
    border: 1px solid;
    text-transform: uppercase;
}
.badge-blue { color: #9FC5FF; border-color: #3A5A8C; background-color: rgba(58,90,140,0.25); }
.badge-green { color: #8FE3B0; border-color: #2E6B47; background-color: rgba(46,107,71,0.25); }
.badge-grey { color: #D8DEE6; border-color: #4A5670; background-color: rgba(74,86,112,0.25); }

/* ---------- Section headers ---------- */
.section-label {
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    color: var(--text-muted);
    text-transform: uppercase;
    border-bottom: 2px solid var(--navy);
    padding-bottom: 6px;
    margin: 26px 0 14px 0;
}

/* ---------- Generic card ---------- */
.vs-card {
    background-color: #FFFFFF;
    border: 1px solid var(--grey-border);
    border-radius: 6px;
    padding: 16px 18px;
}
.field-label {
    font-size: 11px;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-weight: 600;
    margin-bottom: 3px;
}
.field-value {
    font-size: 15px;
    color: var(--text-dark);
    font-weight: 600;
}
.status-pill {
    display: inline-block;
    font-size: 11px;
    font-weight: 700;
    padding: 3px 9px;
    border-radius: 3px;
    text-transform: uppercase;
}
.status-ok { background-color: #E4F3EA; color: var(--ok); }
.status-warn { background-color: #FBEFDD; color: var(--warning); }

/* ---------- Event log (Failure Progression) ---------- */
.log-row {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    padding: 10px 14px;
    background-color: #FFFFFF;
    border-radius: 4px;
    margin-bottom: 6px;
    border: 1px solid var(--grey-border);
    border-left-width: 4px;
}
.log-row.warning { border-left-color: var(--warning); }
.log-row.critical { border-left-color: var(--critical); }
.log-row.root { border-left-color: var(--navy); background-color: #EEF1F8; }
.log-time {
    font-family: 'Courier New', monospace;
    font-size: 13px;
    color: var(--text-muted);
    min-width: 70px;
    padding-top: 2px;
}
.log-dot {
    width: 9px; height: 9px; border-radius: 50%;
    margin-top: 6px;
    flex-shrink: 0;
}
.dot-warning { background-color: var(--warning); }
.dot-critical { background-color: var(--critical); }
.dot-root { background-color: var(--navy); }
.log-body { flex-grow: 1; }
.log-title { font-size: 14px; font-weight: 600; color: var(--text-dark); }
.log-tag {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.5px;
    padding: 2px 7px;
    border-radius: 3px;
    text-transform: uppercase;
    margin-left: 8px;
}
.tag-warning { background-color: #FBEFDD; color: var(--warning); }
.tag-critical { background-color: #FBE6E4; color: var(--critical); }
.tag-root { background-color: #DCE3F2; color: var(--navy); }
.log-arrow { text-align: center; color: var(--grey-border); font-size: 13px; margin: -3px 0; }

/* ---------- KPI cards ---------- */
.kpi-card {
    background-color: #FFFFFF;
    border: 1px solid var(--grey-border);
    border-radius: 6px;
    padding: 14px 16px;
    text-align: left;
}
.kpi-label {
    font-size: 11px;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-weight: 600;
}
.kpi-value {
    font-size: 22px;
    font-weight: 700;
    color: var(--navy);
    margin-top: 4px;
}

/* ---------- Footer ---------- */
.vs-footer {
    margin-top: 34px;
    padding: 16px 20px;
    background-color: var(--navy);
    border-radius: 6px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 8px;
    color: #AEB9CC;
    font-size: 12px;
}
.vs-footer b { color: #FFFFFF; }

/* Buttons */
div.stButton > button {
    border-radius: 4px;
    font-weight: 600;
    border: 1px solid var(--grey-border);
}
div.stButton > button[kind="primary"] {
    background-color: var(--navy);
    border: none;
}
div.stButton > button[kind="primary"]:hover {
    background-color: var(--navy-light);
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# SESSION STATE
# ============================================================
if "analyzed" not in st.session_state:
    st.session_state.analyzed = False
if "vehicle_source" not in st.session_state:
    st.session_state.vehicle_source = None

# ============================================================
# HEADER
# ============================================================
st.markdown("""
<div class="vs-header">
    <div>
        <p class="vs-header-title">VEHISENSE AI</p>
        <p class="vs-header-sub">Edge AI Diagnostic Assistant for Mechanics</p>
    </div>
    <div class="badge-row">
        <span class="badge badge-blue">Edge Processing</span>
        <span class="badge badge-green">Offline Ready</span>
        <span class="badge badge-grey">Vehicle Connected</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# VEHICLE DIAGNOSTIC INFORMATION
# ============================================================
st.markdown('<div class="section-label">Vehicle Diagnostic Information</div>', unsafe_allow_html=True)

info_fields_row1 = [
    ("Vehicle ID", "TATA-NEXON-001"),
    ("VIN", "MAT625432ABC1234"),
    ("Vehicle Model", "Tata Nexon EV"),
    ("Mileage", "48,210 km"),
]
info_fields_row2 = [
    ("Firmware Version", "v3.2.1-EDGE"),
    ("Current Health Status", "STATUS::WARN"),
    ("Last Service Date", "12 Mar 2026"),
    ("Connection Status", "STATUS::OK"),
]

cols = st.columns(4)
for col, (label, value) in zip(cols, info_fields_row1):
    with col:
        st.markdown(f"""
        <div class="vs-card">
            <div class="field-label">{label}</div>
            <div class="field-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

cols2 = st.columns(4)
for col, (label, value) in zip(cols2, info_fields_row2):
    with col:
        if "STATUS::WARN" in value:
            pill = '<span class="status-pill status-warn">Inspection Due</span>'
        elif "STATUS::OK" in value:
            pill = '<span class="status-pill status-ok">Connected</span>'
        else:
            pill = f'<div class="field-value">{value}</div>'
        st.markdown(f"""
        <div class="vs-card">
            <div class="field-label">{label}</div>
            {pill}
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# DATA INPUT / ANALYZE
# ============================================================
st.markdown('<div class="section-label">Data Input</div>', unsafe_allow_html=True)

input_col1, input_col2 = st.columns([2, 1])
with input_col1:
    st.markdown('<div class="vs-card">', unsafe_allow_html=True)
    st.markdown('<div class="field-label">Upload Telemetry CSV</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(" ", type=["csv"], label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)
with input_col2:
    st.markdown('<div class="vs-card">', unsafe_allow_html=True)
    st.markdown('<div class="field-label">Reference Dataset</div>', unsafe_allow_html=True)
    use_demo = st.button("Use Demo Vehicle", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

if use_demo:
    st.session_state.vehicle_source = "demo"
    st.session_state.analyzed = False
if uploaded_file is not None:
    st.session_state.vehicle_source = "upload"
    st.session_state.analyzed = False

if st.session_state.vehicle_source:
    src_name = "Demo Vehicle (TATA-NEXON-001)" if st.session_state.vehicle_source == "demo" else uploaded_file.name
    st.markdown(f"""
    <div style="margin-top:10px; font-size:13px; color:#1B6B3C;">
        ● Dataset loaded — {src_name}
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)
analyze_clicked = st.button(
    "ANALYZE VEHICLE",
    type="primary",
    use_container_width=True,
    disabled=st.session_state.vehicle_source is None
)

# ============================================================
# LOADING SEQUENCE (unchanged logic)
# ============================================================
if analyze_clicked:
    steps = [
        "Reading telemetry...",
        "Behaviour profiling...",
        "Detecting anomalies...",
        "Reconstructing failure progression...",
        "Generating recommendations..."
    ]
    progress_bar = st.progress(0)
    status_text = st.empty()
    for i, step_label in enumerate(steps):
        status_text.markdown(f"<span style='color:#5A6472; font-size:13px;'>{step_label}</span>", unsafe_allow_html=True)
        time_module.sleep(0.5)
        progress_bar.progress((i + 1) / len(steps))
    status_text.empty()
    progress_bar.empty()
    st.session_state.analyzed = True

# ============================================================
# FAILURE PROGRESSION — DIAGNOSTIC EVENT LOG
# ============================================================
if st.session_state.analyzed:

    st.markdown('<div class="section-label">Failure Progression — Diagnostic Event Log</div>', unsafe_allow_html=True)

    events = [
        ("08:42:11", "warning", "WARNING", "Repeated Hard Braking Detected"),
        ("08:42:36", "warning", "WARNING", "Brake Temperature Increased"),
        ("08:43:04", "critical", "CRITICAL", "Abnormal Vibration Pattern"),
        ("08:43:40", "critical", "CRITICAL", "Uneven Front-Left Pad Wear Detected"),
        ("08:44:02", "root", "ROOT CAUSE", "Root Cause Identified — Front-Left Brake Pad Wear"),
    ]

    for idx, (ts, level, tag, title) in enumerate(events):
        st.markdown(f"""
        <div class="log-row {level}">
            <div class="log-time">{ts}</div>
            <div class="log-dot dot-{level}"></div>
            <div class="log-body">
                <span class="log-title">{title}</span>
                <span class="log-tag tag-{level}">{tag}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if idx < len(events) - 1:
            st.markdown('<div class="log-arrow">│</div>', unsafe_allow_html=True)

    # ============================================================
    # MECHANIC RECOMMENDATION — STRUCTURED INSPECTION CARD
    # ============================================================
    st.markdown('<div class="section-label">Inspection Recommendation</div>', unsafe_allow_html=True)

    r1, r2, r3, r4 = st.columns(4)
    with r1:
        st.markdown("""<div class="vs-card"><div class="field-label">Estimated Severity</div>
        <span class="status-pill status-warn">High</span></div>""", unsafe_allow_html=True)
    with r2:
        st.markdown("""<div class="vs-card"><div class="field-label">Affected Component</div>
        <div class="field-value">Front-Left Brake Assembly</div></div>""", unsafe_allow_html=True)
    with r3:
        st.markdown("""<div class="vs-card"><div class="field-label">Est. Inspection Time</div>
        <div class="field-value">25–35 min</div></div>""", unsafe_allow_html=True)
    with r4:
        st.markdown("""<div class="vs-card"><div class="field-label">Priority</div>
        <span class="status-pill status-warn">Priority 2</span></div>""", unsafe_allow_html=True)

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    tools_col, checklist_col = st.columns(2)
    with tools_col:
        st.markdown('<div class="vs-card">', unsafe_allow_html=True)
        st.markdown('<div class="field-label">Recommended Tools</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="font-size:14px; color:#101828; line-height:1.9;">
        Brake caliper wrench set<br>
        Disc thickness micrometer<br>
        Pad wear gauge<br>
        Torque wrench (calibrated)
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with checklist_col:
        st.markdown('<div class="vs-card">', unsafe_allow_html=True)
        st.markdown('<div class="field-label">Inspection Checklist</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="font-size:14px; color:#101828; line-height:1.9;">
        ☐ Inspect front brake pads<br>
        ☐ Check brake disc thickness<br>
        ☐ Verify caliper alignment<br>
        ☐ Conduct road test after replacement
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ============================================================
    # CONFIDENCE ANALYSIS
    # ============================================================
    st.markdown('<div class="section-label">Confidence Analysis</div>', unsafe_allow_html=True)

    conf_col1, conf_col2 = st.columns([1, 2])
    with conf_col1:
        st.markdown('<div class="vs-card">', unsafe_allow_html=True)
        st.markdown('<div class="field-label">Overall Confidence Score</div>', unsafe_allow_html=True)
        st.markdown('<div class="kpi-value" style="font-size:34px;">92%</div>', unsafe_allow_html=True)
        st.progress(92)
        st.markdown('</div>', unsafe_allow_html=True)

    with conf_col2:
        sub_metrics = [
            ("Reasoning Confidence", 94),
            ("Data Quality", 90),
            ("Telemetry Completeness", 96),
            ("Model Confidence", 88),
        ]
        m_cols = st.columns(2)
        for i, (label, val) in enumerate(sub_metrics):
            with m_cols[i % 2]:
                st.markdown(f"""
                <div class="vs-card" style="margin-bottom:8px;">
                    <div class="field-label">{label}</div>
                    <div class="field-value">{val}%</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("""
    <div class="vs-card" style="margin-top:8px;">
        <div class="field-label">Why 92%</div>
        <div style="font-size:14px; color:#101828; line-height:1.8; margin-top:4px;">
        • Multiple correlated anomalies detected across braking and vibration channels<br>
        • Stable telemetry with no sensor dropout during event window<br>
        • Pattern matched against historical brake-wear failure signatures
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ============================================================
    # ENGINEERING DASHBOARD — KPI CARDS
    # ============================================================
    st.markdown('<div class="section-label">Engineering Dashboard</div>', unsafe_allow_html=True)

    kpis_row1 = [
        ("Vehicle Health", "Warning"),
        ("Critical Alerts", "2"),
        ("Detected Anomalies", "4"),
        ("Inspection Status", "Required"),
    ]
    kpis_row2 = [
        ("Telemetry Samples", "1,240"),
        ("Edge Processing Time", "0.84s"),
        ("Prediction Latency", "120ms"),
        ("Last Sync Time", "08:44:02"),
    ]

    kc1 = st.columns(4)
    for col, (label, val) in zip(kc1, kpis_row1):
        with col:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-label">{label}</div>
                <div class="kpi-value">{val}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    kc2 = st.columns(4)
    for col, (label, val) in zip(kc2, kpis_row2):
        with col:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-label">{label}</div>
                <div class="kpi-value">{val}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="vs-card" style="margin-top:10px; text-align:center;">
        <span class="field-label">Processing Mode</span>
        <span class="status-pill status-ok" style="margin-left:8px;">On-Device Edge Inference</span>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================
st.markdown("""
<div class="vs-footer">
    <div><b>VehiSense AI</b> · Edge Processing Active</div>
    <div>Version 0.1.0 · Local Processing · Prototype</div>
</div>
""", unsafe_allow_html=True)
