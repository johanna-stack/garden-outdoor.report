"""
CDON Marketplace — Garden & Outdoor: The Nordic Spring Opportunity
Streamlit Report Portal — Presentation-style multi-slide report
"""
 
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from fpdf import FPDF
import datetime, io, base64
 
# ── Page Config ─────────────────────────────────────────────────
st.set_page_config(
    page_title="Garden & Outdoor: The Nordic Spring Opportunity",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)
 
# ── Design Tokens ───────────────────────────────────────────────
# Matching the Apps Script reference: dark green gradient, gold accents
COLORS = {
    "bg_dark": "#1a2e1a",
    "bg_mid": "#1e3a1e",
    "bg_light": "#234a28",
    "bg_card": "rgba(255,255,255,0.07)",
    "bg_card_solid": "#1f3d22",
    "gold": "#c9a84c",
    "gold_light": "#d4b96a",
    "white": "#f0f0ec",
    "white_soft": "rgba(240,240,236,0.75)",
    "green_accent": "#4ade80",
    "red_accent": "#f87171",
    "amber_accent": "#fbbf24",
    "text_muted": "rgba(240,240,236,0.45)",
    "border": "rgba(255,255,255,0.08)",
}
 
# ── CSS ─────────────────────────────────────────────────────────
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
 
/* Hide Streamlit chrome */
#MainMenu {{visibility: hidden;}}
footer {{visibility: hidden;}}
header {{visibility: hidden;}}
.block-container {{ padding-top: 0 !important; max-width: 1400px; }}
 
/* Dark green background */
.stApp {{
    background: linear-gradient(165deg, #1a2e1a 0%, #1a3520 30%, #1e3a1e 60%, #1a2e1a 100%);
    min-height: 100vh;
}}
 
/* Gold horizontal rule */
.gold-rule {{
    width: 60px; height: 4px;
    background: {COLORS['gold']};
    border: none; margin: 20px 0;
    border-radius: 2px;
}}
 
/* Slide container */
.slide {{
    min-height: 85vh;
    padding: 60px 0 40px;
    position: relative;
    border-bottom: 1px solid {COLORS['border']};
}}
 
/* Top bar */
.top-bar {{
    position: fixed;
    top: 0; left: 0; right: 0;
    background: rgba(26, 46, 26, 0.92);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid {COLORS['border']};
    padding: 10px 40px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    z-index: 9999;
    height: 48px;
    font-family: 'Inter', sans-serif;
}}
.top-bar-brand {{
    color: {COLORS['gold']};
    font-weight: 700;
    font-size: 14px;
    letter-spacing: 2px;
}}
.top-bar-nav {{
    display: flex;
    gap: 24px;
}}
.top-bar-nav a {{
    color: {COLORS['white_soft']};
    text-decoration: none;
    font-size: 12px;
    font-weight: 500;
    letter-spacing: 0.5px;
    transition: color 0.2s;
}}
.top-bar-nav a:hover {{ color: {COLORS['gold']}; }}
 
/* Section label */
.section-label {{
    color: {COLORS['gold']};
    font-family: 'Inter', sans-serif;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 8px;
}}
 
/* Title */
.slide-title {{
    color: {COLORS['white']};
    font-family: 'Inter', sans-serif;
    font-size: 44px;
    font-weight: 800;
    line-height: 1.15;
    margin-bottom: 0;
}}
.slide-title-sm {{
    color: {COLORS['white']};
    font-family: 'Inter', sans-serif;
    font-size: 30px;
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 12px;
}}
.slide-subtitle {{
    color: {COLORS['white_soft']};
    font-family: 'Inter', sans-serif;
    font-size: 17px;
    font-weight: 400;
    line-height: 1.6;
    max-width: 700px;
}}
 
/* KPI card */
.kpi-card {{
    background: {COLORS['bg_card']};
    border: 1px solid {COLORS['border']};
    border-radius: 12px;
    padding: 24px 20px;
    text-align: center;
    backdrop-filter: blur(4px);
}}
.kpi-label {{
    color: {COLORS['text_muted']};
    font-family: 'Inter', sans-serif;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 10px;
}}
.kpi-value {{
    color: {COLORS['white']};
    font-family: 'Inter', sans-serif;
    font-size: 32px;
    font-weight: 800;
}}
.kpi-value.gold {{ color: {COLORS['gold']}; }}
.kpi-value.green {{ color: {COLORS['green_accent']}; }}
.kpi-value.red {{ color: {COLORS['red_accent']}; }}
.kpi-sub {{
    color: {COLORS['text_muted']};
    font-family: 'Inter', sans-serif;
    font-size: 11px;
    margin-top: 6px;
}}
 
/* Info card */
.info-card {{
    background: {COLORS['bg_card']};
    border: 1px solid {COLORS['border']};
    border-radius: 12px;
    padding: 28px 24px;
    height: 100%;
}}
.info-card h4 {{
    color: {COLORS['gold']};
    font-family: 'Inter', sans-serif;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 16px;
}}
.info-card p, .info-card li {{
    color: {COLORS['white_soft']};
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    line-height: 1.7;
}}
.info-card ul {{
    padding-left: 0;
    list-style: none;
}}
.info-card li {{
    padding: 6px 0;
    border-bottom: 1px solid {COLORS['border']};
}}
.info-card li:before {{
    content: '';
    display: inline-block;
    width: 6px; height: 6px;
    background: {COLORS['gold']};
    border-radius: 50%;
    margin-right: 10px;
    vertical-align: middle;
}}
 
/* Table */
.data-table {{
    width: 100%;
    border-collapse: collapse;
    font-family: 'Inter', sans-serif;
}}
.data-table th {{
    color: {COLORS['text_muted']};
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    text-align: left;
    padding: 12px 16px;
    border-bottom: 1px solid {COLORS['border']};
}}
.data-table td {{
    color: {COLORS['white_soft']};
    font-size: 14px;
    padding: 14px 16px;
    border-bottom: 1px solid {COLORS['border']};
}}
.data-table tr:hover td {{
    background: rgba(255,255,255,0.03);
}}
 
/* Footer */
.slide-footer {{
    display: flex;
    justify-content: space-between;
    padding: 20px 0 0;
    font-family: 'Inter', sans-serif;
    font-size: 11px;
    color: {COLORS['text_muted']};
}}
 
/* Flags */
.flag-row {{
    display: flex;
    gap: 16px;
    align-items: center;
    margin-top: 40px;
}}
.flag-icon {{
    width: 42px;
    height: 30px;
    border-radius: 4px;
    overflow: hidden;
    box-shadow: 0 2px 6px rgba(0,0,0,0.3);
    display: inline-block;
}}
.flag-label {{
    color: {COLORS['text_muted']};
    font-family: 'Inter', sans-serif;
    font-size: 12px;
    font-weight: 500;
    letter-spacing: 2px;
    margin-left: 12px;
}}
 
/* Metric highlight */
.metric-highlight {{
    display: inline-block;
    background: rgba(201, 168, 76, 0.15);
    color: {COLORS['gold']};
    padding: 3px 10px;
    border-radius: 6px;
    font-weight: 700;
    font-size: 14px;
}}
 
/* Streamlit tab overrides */
.stTabs [data-baseweb="tab-list"] {{
    gap: 0;
    background: rgba(255,255,255,0.04);
    border-radius: 8px;
    padding: 4px;
}}
.stTabs [data-baseweb="tab"] {{
    color: {COLORS['white_soft']};
    font-family: 'Inter', sans-serif;
    font-size: 12px;
    font-weight: 500;
    letter-spacing: 0.5px;
    padding: 8px 20px;
    border-radius: 6px;
}}
.stTabs [aria-selected="true"] {{
    background: rgba(201, 168, 76, 0.15) !important;
    color: {COLORS['gold']} !important;
}}
.stTabs [data-baseweb="tab-panel"] {{
    padding-top: 24px;
}}
 
/* Download button override */
.stDownloadButton > button {{
    background: transparent !important;
    border: 1.5px solid {COLORS['gold']} !important;
    color: {COLORS['gold']} !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    letter-spacing: 0.5px !important;
    padding: 8px 24px !important;
    border-radius: 6px !important;
    transition: all 0.2s !important;
}}
.stDownloadButton > button:hover {{
    background: rgba(201, 168, 76, 0.12) !important;
}}
 
/* Plotly chart container */
[data-testid="stPlotlyChart"] {{
    background: {COLORS['bg_card']};
    border: 1px solid {COLORS['border']};
    border-radius: 12px;
    padding: 16px;
}}
 
/* Metric override */
[data-testid="stMetric"] {{
    background: {COLORS['bg_card']};
    border: 1px solid {COLORS['border']};
    border-radius: 12px;
    padding: 20px 16px;
    text-align: center;
}}
[data-testid="stMetricLabel"] {{
    color: {COLORS['text_muted']} !important;
    font-size: 10px !important;
    text-transform: uppercase;
    letter-spacing: 1px;
}}
[data-testid="stMetricValue"] {{
    color: {COLORS['white']} !important;
    font-size: 24px !important;
    font-weight: 800 !important;
}}
 
</style>
""", unsafe_allow_html=True)
 
 
# ══════════════════════════════════════════════════════════════════
# PUBLIC DATA — Garden & Outdoor Nordic Market (illustrative)
# ══════════════════════════════════════════════════════════════════
 
# Market-level estimates (public / illustrative)
market_data = {
    "total_nordic_ecom": 35.2,  # bn EUR
    "garden_outdoor_share": 4.8,  # %
    "garden_market_size": 1.69,  # bn EUR
    "yoy_growth": 12.3,
    "spring_peak_share": 62,  # % of annual sales in Mar-Jul
    "avg_order_value": 89,  # EUR
    "mobile_share": 58,  # %
    "repeat_rate": 34,  # %
}
 
# Country breakdown
countries = {
    "Sweden": {"flag_label": "SE", "population": 10.5, "ecom_penetration": 84, "garden_index": 112, "market_size": 620, "growth": 14.1, "aov": 95, "top_categories": ["Outdoor Furniture", "BBQ & Grills", "Garden Tools"]},
    "Denmark": {"flag_label": "DK", "population": 5.9, "ecom_penetration": 86, "garden_index": 108, "market_size": 380, "growth": 11.8, "aov": 92, "top_categories": ["Outdoor Lighting", "Planters & Pots", "Outdoor Furniture"]},
    "Norway": {"flag_label": "NO", "population": 5.5, "ecom_penetration": 82, "garden_index": 98, "market_size": 340, "growth": 10.5, "aov": 105, "top_categories": ["Heated Outdoor", "Garden Tools", "BBQ & Grills"]},
    "Finland": {"flag_label": "FI", "population": 5.6, "ecom_penetration": 79, "garden_index": 95, "market_size": 350, "growth": 13.2, "aov": 78, "top_categories": ["Sauna Accessories", "Garden Furniture", "Outdoor Decor"]},
}
 
# Monthly seasonality (% of annual sales)
seasonality = {
    "Jan": 2.8, "Feb": 3.5, "Mar": 8.2, "Apr": 14.5, "May": 18.3,
    "Jun": 15.8, "Jul": 12.4, "Aug": 8.5, "Sep": 5.8, "Oct": 4.2,
    "Nov": 3.5, "Dec": 2.5,
}
 
# Top subcategories on CDON
subcategories = [
    {"name": "Outdoor Furniture", "share": 22.4, "growth": 18.5, "aov": 142, "items": 12400},
    {"name": "BBQ & Grills", "share": 15.8, "growth": 14.2, "aov": 178, "items": 5600},
    {"name": "Garden Tools & Equipment", "share": 13.2, "growth": 9.8, "aov": 65, "items": 18200},
    {"name": "Outdoor Lighting", "share": 10.5, "growth": 22.1, "aov": 48, "items": 8900},
    {"name": "Planters, Pots & Soil", "share": 8.9, "growth": 11.3, "aov": 35, "items": 15100},
    {"name": "Garden Decor & Ornaments", "share": 7.4, "growth": 16.7, "aov": 42, "items": 9800},
    {"name": "Pools & Water Features", "share": 6.8, "growth": 25.4, "aov": 195, "items": 3200},
    {"name": "Greenhouses & Storage", "share": 5.2, "growth": 8.9, "aov": 320, "items": 2100},
    {"name": "Pest Control & Plant Care", "share": 4.9, "growth": 7.2, "aov": 28, "items": 6400},
    {"name": "Outdoor Textiles & Cushions", "share": 4.9, "growth": 19.8, "aov": 55, "items": 7200},
]
 
# Competitive landscape
competitors = [
    {"name": "Byggmax", "type": "Specialist", "strength": "Physical + online", "garden_focus": "High", "price_pos": "Mid"},
    {"name": "Plantagen", "type": "Specialist", "strength": "Plants & garden center", "garden_focus": "Very High", "price_pos": "Mid-High"},
    {"name": "Jula", "type": "General", "strength": "Tools & seasonal", "garden_focus": "Medium", "price_pos": "Value"},
    {"name": "Amazon.se", "type": "Marketplace", "strength": "Assortment breadth", "garden_focus": "Low-Med", "price_pos": "Competitive"},
    {"name": "XXL", "type": "Sports/Outdoor", "strength": "Outdoor lifestyle", "garden_focus": "Low", "price_pos": "Mid"},
]
 
# Weekly CDON search trends (index, 100 = avg)
search_trends = {
    "W1": 28, "W2": 25, "W3": 30, "W4": 32, "W5": 35, "W6": 38,
    "W7": 42, "W8": 48, "W9": 55, "W10": 68, "W11": 78, "W12": 92,
    "W13": 100, "W14": 115, "W15": 135, "W16": 152, "W17": 168,
    "W18": 185, "W19": 195, "W20": 188, "W21": 175, "W22": 162,
    "W23": 148, "W24": 135, "W25": 120, "W26": 108,
}
 
 
# ══════════════════════════════════════════════════════════════════
# PDF GENERATION
# ══════════════════════════════════════════════════════════════════
 
def generate_report_pdf():
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=15)
 
    bg = (26, 46, 26)
    panel = (31, 61, 34)
    gold = (201, 168, 76)
    white = (240, 240, 236)
    muted = (140, 145, 135)
 
    # --- Page 1: Title ---
    pdf.add_page()
    pdf.set_fill_color(*bg)
    pdf.rect(0, 0, 297, 210, "F")
 
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(*gold)
    pdf.set_xy(20, 30)
    pdf.cell(100, 8, "CDON MARKETPLACE")
 
    pdf.set_font("Helvetica", "B", 28)
    pdf.set_text_color(*white)
    pdf.set_xy(20, 48)
    pdf.cell(260, 16, "Garden & Outdoor:")
    pdf.set_xy(20, 68)
    pdf.cell(260, 16, "The Nordic Spring Opportunity")
 
    # Gold rule
    pdf.set_fill_color(*gold)
    pdf.rect(20, 92, 40, 3, "F")
 
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(*muted)
    pdf.set_xy(20, 104)
    pdf.multi_cell(200, 7, "A market overview for merchants looking to capture seasonal demand\nacross Sweden, Denmark, Norway and Finland.")
 
    pdf.set_xy(20, 130)
    pdf.cell(60, 6, "FOUR MARKETS - ONE PLATFORM")
 
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*muted)
    pdf.set_xy(20, 195)
    pdf.cell(120, 5, "CDON - Confidential")
    pdf.set_xy(200, 195)
    pdf.cell(80, 5, f"Spring/Summer 2026  |  Generated {datetime.date.today().strftime('%Y-%m-%d')}", align="R")
 
    # --- Page 2: Market Overview ---
    pdf.add_page()
    pdf.set_fill_color(*bg)
    pdf.rect(0, 0, 297, 210, "F")
 
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(*gold)
    pdf.set_xy(20, 15)
    pdf.cell(100, 8, "MARKET OVERVIEW")
 
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(*white)
    pdf.set_xy(20, 28)
    pdf.cell(260, 12, "The Nordic Garden Market at a Glance")
 
    kpis = [
        ("NORDIC E-COM", "EUR 35.2bn", "Total market"),
        ("GARDEN SHARE", "4.8%", "Of total e-com"),
        ("GARDEN MARKET", "EUR 1.69bn", "Online garden"),
        ("YOY GROWTH", "+12.3%", "vs. 2025"),
        ("SPRING PEAK", "62%", "Mar-Jul share"),
    ]
 
    for i, (label, value, sub) in enumerate(kpis):
        x = 20 + i * 54
        pdf.set_fill_color(*panel)
        pdf.set_draw_color(50, 70, 50)
        pdf.rect(x, 48, 50, 28, "DF")
        pdf.set_font("Helvetica", "", 6)
        pdf.set_text_color(*muted)
        pdf.set_xy(x, 50)
        pdf.cell(50, 5, label, align="C")
        pdf.set_font("Helvetica", "B", 14)
        pdf.set_text_color(*gold)
        pdf.set_xy(x, 57)
        pdf.cell(50, 8, value, align="C")
        pdf.set_font("Helvetica", "", 6)
        pdf.set_text_color(*muted)
        pdf.set_xy(x, 67)
        pdf.cell(50, 5, sub, align="C")
 
    # Country table
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(*white)
    pdf.set_xy(20, 86)
    pdf.cell(260, 8, "COUNTRY BREAKDOWN")
 
    headers = ["Country", "Pop (M)", "E-com %", "Market (M EUR)", "Growth %", "AOV (EUR)"]
    col_widths = [50, 30, 30, 45, 35, 35]
 
    pdf.set_font("Helvetica", "B", 7)
    pdf.set_text_color(*muted)
    y = 96
    for j, h in enumerate(headers):
        pdf.set_xy(20 + sum(col_widths[:j]), y)
        pdf.cell(col_widths[j], 6, h)
 
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*white)
    for name, d in countries.items():
        y += 8
        vals = [name, str(d["population"]), f"{d['ecom_penetration']}%", str(d["market_size"]), f"+{d['growth']}%", str(d["aov"])]
        for j, v in enumerate(vals):
            pdf.set_xy(20 + sum(col_widths[:j]), y)
            pdf.cell(col_widths[j], 6, v)
 
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*muted)
    pdf.set_xy(20, 195)
    pdf.cell(120, 5, "CDON - Confidential")
    pdf.set_xy(200, 195)
    pdf.cell(80, 5, "Spring/Summer 2026", align="R")
 
    # --- Page 3: Top Categories ---
    pdf.add_page()
    pdf.set_fill_color(*bg)
    pdf.rect(0, 0, 297, 210, "F")
 
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(*gold)
    pdf.set_xy(20, 15)
    pdf.cell(100, 8, "CATEGORY BREAKDOWN")
 
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(*white)
    pdf.set_xy(20, 28)
    pdf.cell(260, 12, "Top Subcategories on CDON")
 
    headers = ["Subcategory", "Share %", "Growth %", "AOV (EUR)", "Listed Items"]
    col_widths = [70, 35, 35, 40, 40]
 
    pdf.set_font("Helvetica", "B", 7)
    pdf.set_text_color(*muted)
    y = 48
    for j, h in enumerate(headers):
        pdf.set_xy(20 + sum(col_widths[:j]), y)
        pdf.cell(col_widths[j], 6, h)
 
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*white)
    for sc in subcategories:
        y += 7
        vals = [sc["name"], f"{sc['share']}%", f"+{sc['growth']}%", str(sc["aov"]), f"{sc['items']:,}"]
        for j, v in enumerate(vals):
            pdf.set_xy(20 + sum(col_widths[:j]), y)
            if j == 2:
                pdf.set_text_color(74, 222, 128)
            else:
                pdf.set_text_color(*white)
            pdf.cell(col_widths[j], 6, v)
 
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*muted)
    pdf.set_xy(20, 195)
    pdf.cell(120, 5, "CDON - Confidential")
    pdf.set_xy(200, 195)
    pdf.cell(80, 5, "Spring/Summer 2026", align="R")
 
    # --- Page 4: Opportunity ---
    pdf.add_page()
    pdf.set_fill_color(*bg)
    pdf.rect(0, 0, 297, 210, "F")
 
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(*gold)
    pdf.set_xy(20, 15)
    pdf.cell(100, 8, "THE OPPORTUNITY")
 
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(*white)
    pdf.set_xy(20, 28)
    pdf.cell(260, 12, "Why Garden & Outdoor on CDON?")
 
    reasons = [
        "Peak season (Mar-Jul) captures 62% of annual garden sales",
        "Nordic garden e-commerce growing 12.3% YoY - outpacing total e-com",
        "Average order value of EUR 89 with strong margin potential",
        "Four markets, one platform - reach 27.5M consumers",
        "Limited pure-play online competition in garden category",
        "Mobile commerce at 58% - CDON's app drives conversion",
        "34% repeat purchase rate - loyal customer base",
        "Cross-sell opportunity with home & living categories",
    ]
 
    pdf.set_font("Helvetica", "", 10)
    y = 50
    for r in reasons:
        pdf.set_fill_color(*gold)
        pdf.ellipse(24, y + 1.5, 4, 4, "F")
        pdf.set_text_color(*white)
        pdf.set_xy(32, y)
        pdf.cell(240, 7, r)
        y += 12
 
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*muted)
    pdf.set_xy(20, 195)
    pdf.cell(120, 5, "CDON - Confidential")
    pdf.set_xy(200, 195)
    pdf.cell(80, 5, "Spring/Summer 2026", align="R")
 
    return bytes(pdf.output())
 
 
# ══════════════════════════════════════════════════════════════════
# SLIDE 0: TOP BAR (fixed)
# ══════════════════════════════════════════════════════════════════
st.markdown("""
<div class="top-bar">
    <span class="top-bar-brand">CDON MARKETPLACE</span>
    <div class="top-bar-nav">
        <a href="#overview">Overview</a>
        <a href="#market">Market Data</a>
        <a href="#categories">Categories</a>
        <a href="#countries">Countries</a>
        <a href="#seasonality">Seasonality</a>
        <a href="#competition">Competition</a>
        <a href="#opportunity">Opportunity</a>
    </div>
</div>
<div style="height:56px"></div>
""", unsafe_allow_html=True)
 
 
# ══════════════════════════════════════════════════════════════════
# SLIDE 1: TITLE
# ══════════════════════════════════════════════════════════════════
# Download PDF button at top right
col_spacer, col_dl = st.columns([5, 1])
with col_dl:
    pdf_data = generate_report_pdf()
    st.download_button(
        label="Download PDF",
        data=pdf_data,
        file_name=f"CDON_Garden_Outdoor_Report_{datetime.date.today().strftime('%Y%m%d')}.pdf",
        mime="application/pdf",
    )
 
st.markdown(f"""
<div style="padding: 60px 0 40px;">
    <div class="section-label">CDON MARKETPLACE</div>
    <div class="slide-title">Garden & Outdoor:</div>
    <div class="slide-title">The Nordic Spring Opportunity</div>
    <div class="gold-rule"></div>
    <div class="slide-subtitle">
        A market overview for merchants looking to capture seasonal demand
        across Sweden, Denmark, Norway and Finland.
    </div>
    <div class="flag-row">
        <svg class="flag-icon" viewBox="0 0 42 30"><rect width="42" height="30" fill="#c8102e"/><rect x="12" width="6" height="30" fill="#fff"/><rect y="12" width="42" height="6" fill="#fff"/></svg>
        <svg class="flag-icon" viewBox="0 0 42 30"><rect width="42" height="30" fill="#004B87"/><rect x="12" width="6" height="30" fill="#FECC02"/><rect y="12" width="42" height="6" fill="#FECC02"/></svg>
        <svg class="flag-icon" viewBox="0 0 42 30"><rect width="42" height="30" fill="#ba0c2f"/><rect x="10" width="8" height="30" fill="#00205b"/><rect y="11" width="42" height="8" fill="#00205b"/><rect x="12" width="4" height="30" fill="#fff"/><rect y="13" width="42" height="4" fill="#fff"/></svg>
        <svg class="flag-icon" viewBox="0 0 42 30"><rect width="42" height="30" fill="#fff"/><rect x="12" width="6" height="30" fill="#002F6C"/><rect y="12" width="42" height="6" fill="#002F6C"/></svg>
        <span class="flag-label">FOUR MARKETS &middot; ONE PLATFORM</span>
    </div>
</div>
<div class="slide-footer">
    <span>CDON &mdash; Confidential</span>
    <span>Spring/Summer 2026</span>
</div>
""", unsafe_allow_html=True)
 
st.markdown("---")
 
 
# ══════════════════════════════════════════════════════════════════
# SLIDE 2: MARKET OVERVIEW KPIs
# ══════════════════════════════════════════════════════════════════
st.markdown('<div id="market"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div style="padding: 20px 0 12px;">
    <div class="section-label">MARKET OVERVIEW</div>
    <div class="slide-title-sm">The Nordic Garden Market at a Glance</div>
</div>
""", unsafe_allow_html=True)
 
k1, k2, k3, k4, k5 = st.columns(5)
with k1:
    st.markdown(f"""<div class="kpi-card">
        <div class="kpi-label">NORDIC E-COMMERCE</div>
        <div class="kpi-value gold">EUR 35.2bn</div>
        <div class="kpi-sub">Total addressable market</div>
    </div>""", unsafe_allow_html=True)
with k2:
    st.markdown(f"""<div class="kpi-card">
        <div class="kpi-label">GARDEN & OUTDOOR</div>
        <div class="kpi-value gold">4.8%</div>
        <div class="kpi-sub">Share of total e-commerce</div>
    </div>""", unsafe_allow_html=True)
with k3:
    st.markdown(f"""<div class="kpi-card">
        <div class="kpi-label">ONLINE GARDEN MARKET</div>
        <div class="kpi-value gold">EUR 1.69bn</div>
        <div class="kpi-sub">Nordic online garden 2026E</div>
    </div>""", unsafe_allow_html=True)
with k4:
    st.markdown(f"""<div class="kpi-card">
        <div class="kpi-label">YEAR-OVER-YEAR GROWTH</div>
        <div class="kpi-value green">+12.3%</div>
        <div class="kpi-sub">vs. 2025 (outpacing total e-com)</div>
    </div>""", unsafe_allow_html=True)
with k5:
    st.markdown(f"""<div class="kpi-card">
        <div class="kpi-label">SPRING PEAK SHARE</div>
        <div class="kpi-value gold">62%</div>
        <div class="kpi-sub">Of annual sales in Mar-Jul</div>
    </div>""", unsafe_allow_html=True)
 
st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
 
# Secondary KPIs
s1, s2, s3, s4 = st.columns(4)
with s1:
    st.markdown(f"""<div class="kpi-card">
        <div class="kpi-label">AVG ORDER VALUE</div>
        <div class="kpi-value">EUR 89</div>
        <div class="kpi-sub">Cross-market average</div>
    </div>""", unsafe_allow_html=True)
with s2:
    st.markdown(f"""<div class="kpi-card">
        <div class="kpi-label">MOBILE COMMERCE</div>
        <div class="kpi-value">58%</div>
        <div class="kpi-sub">Of garden purchases on mobile</div>
    </div>""", unsafe_allow_html=True)
with s3:
    st.markdown(f"""<div class="kpi-card">
        <div class="kpi-label">REPEAT PURCHASE RATE</div>
        <div class="kpi-value">34%</div>
        <div class="kpi-sub">Returning garden shoppers</div>
    </div>""", unsafe_allow_html=True)
with s4:
    st.markdown(f"""<div class="kpi-card">
        <div class="kpi-label">TOTAL CONSUMERS</div>
        <div class="kpi-value">27.5M</div>
        <div class="kpi-sub">Across 4 Nordic markets</div>
    </div>""", unsafe_allow_html=True)
 
st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
st.markdown(f"""<div class="slide-footer">
    <span>CDON &mdash; Confidential</span>
    <span>Spring/Summer 2026</span>
</div>""", unsafe_allow_html=True)
 
st.markdown("---")
 
 
# ══════════════════════════════════════════════════════════════════
# SLIDE 3: TOP CATEGORIES
# ══════════════════════════════════════════════════════════════════
st.markdown('<div id="categories"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div style="padding: 20px 0 12px;">
    <div class="section-label">CATEGORY BREAKDOWN</div>
    <div class="slide-title-sm">Top Subcategories on CDON</div>
</div>
""", unsafe_allow_html=True)
 
col_chart, col_table = st.columns([1, 1])
 
with col_chart:
    fig_cat = go.Figure()
    fig_cat.add_trace(go.Bar(
        y=[sc["name"] for sc in reversed(subcategories)],
        x=[sc["share"] for sc in reversed(subcategories)],
        orientation="h",
        marker_color=[COLORS["gold"] if sc["share"] > 10 else "rgba(201,168,76,0.4)" for sc in reversed(subcategories)],
        text=[f'{sc["share"]}%' for sc in reversed(subcategories)],
        textposition="outside",
        textfont=dict(color=COLORS["white_soft"], size=11),
    ))
    fig_cat.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=COLORS["white_soft"], family="Inter"),
        xaxis=dict(visible=False, range=[0, 30]),
        yaxis=dict(tickfont=dict(size=11, color=COLORS["white_soft"])),
        margin=dict(l=10, r=40, t=10, b=10),
        height=420,
        showlegend=False,
    )
    st.plotly_chart(fig_cat, use_container_width=True, key="cat_chart")
 
with col_table:
    rows_html = ""
    for sc in subcategories:
        growth_color = COLORS["green_accent"] if sc["growth"] > 15 else COLORS["gold_light"]
        rows_html += f"""<tr>
            <td>{sc['name']}</td>
            <td><span class="metric-highlight">{sc['share']}%</span></td>
            <td style="color:{growth_color}">+{sc['growth']}%</td>
            <td>EUR {sc['aov']}</td>
            <td>{sc['items']:,}</td>
        </tr>"""
 
    st.markdown(f"""
    <table class="data-table">
        <thead><tr>
            <th>Subcategory</th><th>Share</th><th>Growth</th><th>AOV</th><th>Items</th>
        </tr></thead>
        <tbody>{rows_html}</tbody>
    </table>
    """, unsafe_allow_html=True)
 
st.markdown(f"""<div class="slide-footer">
    <span>CDON &mdash; Confidential</span>
    <span>Spring/Summer 2026</span>
</div>""", unsafe_allow_html=True)
 
st.markdown("---")
 
 
# ══════════════════════════════════════════════════════════════════
# SLIDE 4: COUNTRY DEEP DIVE
# ══════════════════════════════════════════════════════════════════
st.markdown('<div id="countries"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div style="padding: 20px 0 12px;">
    <div class="section-label">COUNTRY DEEP DIVE</div>
    <div class="slide-title-sm">Market by Market</div>
</div>
""", unsafe_allow_html=True)
 
tabs = st.tabs([f'{d["flag_label"]}  {name}' for name, d in countries.items()])
 
for i, (country, data) in enumerate(countries.items()):
    with tabs[i]:
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f"""<div class="kpi-card">
                <div class="kpi-label">MARKET SIZE</div>
                <div class="kpi-value gold">EUR {data['market_size']}M</div>
                <div class="kpi-sub">Online garden & outdoor</div>
            </div>""", unsafe_allow_html=True)
        with c2:
            st.markdown(f"""<div class="kpi-card">
                <div class="kpi-label">GROWTH</div>
                <div class="kpi-value green">+{data['growth']}%</div>
                <div class="kpi-sub">Year-over-year</div>
            </div>""", unsafe_allow_html=True)
        with c3:
            st.markdown(f"""<div class="kpi-card">
                <div class="kpi-label">E-COM PENETRATION</div>
                <div class="kpi-value">{data['ecom_penetration']}%</div>
                <div class="kpi-sub">Of population shops online</div>
            </div>""", unsafe_allow_html=True)
        with c4:
            st.markdown(f"""<div class="kpi-card">
                <div class="kpi-label">AVG ORDER VALUE</div>
                <div class="kpi-value">EUR {data['aov']}</div>
                <div class="kpi-sub">Garden category average</div>
            </div>""", unsafe_allow_html=True)
 
        st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
 
        ic1, ic2 = st.columns(2)
        with ic1:
            cats_html = "".join(f"<li>{c}</li>" for c in data["top_categories"])
            st.markdown(f"""<div class="info-card">
                <h4>TOP CATEGORIES</h4>
                <ul>{cats_html}</ul>
            </div>""", unsafe_allow_html=True)
        with ic2:
            st.markdown(f"""<div class="info-card">
                <h4>MARKET PROFILE</h4>
                <p>Population: <strong>{data['population']}M</strong></p>
                <p>Garden interest index: <strong>{data['garden_index']}</strong> (100 = Nordic avg)</p>
                <p>{country} represents a {('mature' if data['ecom_penetration'] > 83 else 'growing')} e-commerce market
                with {('above' if data['garden_index'] > 100 else 'near')}-average garden interest.</p>
            </div>""", unsafe_allow_html=True)
 
st.markdown(f"""<div class="slide-footer">
    <span>CDON &mdash; Confidential</span>
    <span>Spring/Summer 2026</span>
</div>""", unsafe_allow_html=True)
 
st.markdown("---")
 
 
# ══════════════════════════════════════════════════════════════════
# SLIDE 5: SEASONALITY
# ══════════════════════════════════════════════════════════════════
st.markdown('<div id="seasonality"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div style="padding: 20px 0 12px;">
    <div class="section-label">SEASONALITY & TIMING</div>
    <div class="slide-title-sm">When Demand Peaks</div>
</div>
""", unsafe_allow_html=True)
 
col_season, col_search = st.columns(2)
 
with col_season:
    months = list(seasonality.keys())
    values = list(seasonality.values())
    colors_bar = [COLORS["gold"] if v > 10 else "rgba(201,168,76,0.35)" for v in values]
 
    fig_season = go.Figure()
    fig_season.add_trace(go.Bar(
        x=months, y=values,
        marker_color=colors_bar,
        text=[f"{v}%" for v in values],
        textposition="outside",
        textfont=dict(color=COLORS["white_soft"], size=10),
    ))
    fig_season.update_layout(
        title=dict(text="Monthly Sales Distribution", font=dict(color=COLORS["gold"], size=13)),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=COLORS["white_soft"], family="Inter"),
        xaxis=dict(gridcolor="rgba(255,255,255,0.05)", tickfont=dict(size=10)),
        yaxis=dict(visible=False, range=[0, 24]),
        margin=dict(l=10, r=10, t=40, b=30),
        height=350,
        showlegend=False,
    )
    # Add peak season annotation
    fig_season.add_vrect(x0="Mar", x1="Jul", fillcolor="rgba(201,168,76,0.08)", line_width=0)
    fig_season.add_annotation(
        x="May", y=22, text="PEAK SEASON (62%)",
        font=dict(color=COLORS["gold"], size=10, family="Inter"),
        showarrow=False,
    )
    st.plotly_chart(fig_season, use_container_width=True, key="season_chart")
 
with col_search:
    weeks = list(search_trends.keys())
    trend_vals = list(search_trends.values())
 
    fig_search = go.Figure()
    fig_search.add_trace(go.Scatter(
        x=weeks, y=trend_vals,
        mode="lines+markers",
        line=dict(color=COLORS["gold"], width=2.5),
        marker=dict(size=4, color=COLORS["gold"]),
        fill="tozeroy",
        fillcolor="rgba(201,168,76,0.08)",
    ))
    # Add "NOW" marker
    fig_search.add_vline(x="W13", line_dash="dash", line_color=COLORS["green_accent"], line_width=1.5)
    fig_search.add_annotation(
        x="W13", y=max(trend_vals) + 10, text="NOW (W13)",
        font=dict(color=COLORS["green_accent"], size=10),
        showarrow=False,
    )
    fig_search.update_layout(
        title=dict(text="CDON Search Trend Index (H1)", font=dict(color=COLORS["gold"], size=13)),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=COLORS["white_soft"], family="Inter"),
        xaxis=dict(gridcolor="rgba(255,255,255,0.05)", tickfont=dict(size=9), dtick=2),
        yaxis=dict(gridcolor="rgba(255,255,255,0.05)", tickfont=dict(size=10)),
        margin=dict(l=40, r=10, t=40, b=30),
        height=350,
        showlegend=False,
    )
    st.plotly_chart(fig_search, use_container_width=True, key="search_chart")
 
st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
 
t1, t2, t3 = st.columns(3)
with t1:
    st.markdown(f"""<div class="info-card">
        <h4>PRE-SEASON (W10-W14)</h4>
        <p>Search interest surges 3-4x. Merchants should have full assortment live and campaigns ready by W10.</p>
    </div>""", unsafe_allow_html=True)
with t2:
    st.markdown(f"""<div class="info-card">
        <h4>PEAK SEASON (W15-W22)</h4>
        <p>Highest conversion rates and traffic. Focus on inventory depth, competitive pricing, and promoted listings.</p>
    </div>""", unsafe_allow_html=True)
with t3:
    st.markdown(f"""<div class="info-card">
        <h4>LATE SEASON (W23-W26)</h4>
        <p>Clearance opportunity. End-of-season deals drive volume. Good time for pool/water accessories push.</p>
    </div>""", unsafe_allow_html=True)
 
st.markdown(f"""<div class="slide-footer">
    <span>CDON &mdash; Confidential</span>
    <span>Spring/Summer 2026</span>
</div>""", unsafe_allow_html=True)
 
st.markdown("---")
 
 
# ══════════════════════════════════════════════════════════════════
# SLIDE 6: COMPETITIVE LANDSCAPE
# ══════════════════════════════════════════════════════════════════
st.markdown('<div id="competition"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div style="padding: 20px 0 12px;">
    <div class="section-label">COMPETITIVE LANDSCAPE</div>
    <div class="slide-title-sm">Who Else is Playing?</div>
</div>
""", unsafe_allow_html=True)
 
comp_rows = ""
for c in competitors:
    comp_rows += f"""<tr>
        <td style="font-weight:600;color:{COLORS['white']}">{c['name']}</td>
        <td>{c['type']}</td>
        <td>{c['strength']}</td>
        <td><span class="metric-highlight">{c['garden_focus']}</span></td>
        <td>{c['price_pos']}</td>
    </tr>"""
 
st.markdown(f"""
<table class="data-table">
    <thead><tr>
        <th>Competitor</th><th>Type</th><th>Key Strength</th><th>Garden Focus</th><th>Price Position</th>
    </tr></thead>
    <tbody>{comp_rows}</tbody>
</table>
""", unsafe_allow_html=True)
 
st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
 
a1, a2 = st.columns(2)
with a1:
    st.markdown(f"""<div class="info-card">
        <h4>CDON ADVANTAGE</h4>
        <ul>
            <li>Pure marketplace model - no own-stock competition with merchants</li>
            <li>Four Nordic markets from a single integration</li>
            <li>Strong brand awareness in electronics cross-selling to home/garden</li>
            <li>Mobile-first platform with high app engagement</li>
        </ul>
    </div>""", unsafe_allow_html=True)
with a2:
    st.markdown(f"""<div class="info-card">
        <h4>GAP OPPORTUNITY</h4>
        <ul>
            <li>No dominant pure-play online garden retailer in Nordics</li>
            <li>Specialists (Plantagen, Byggmax) weak in e-commerce</li>
            <li>Amazon.se still building garden assortment</li>
            <li>Cross-border merchants can unlock all four markets instantly</li>
        </ul>
    </div>""", unsafe_allow_html=True)
 
st.markdown(f"""<div class="slide-footer">
    <span>CDON &mdash; Confidential</span>
    <span>Spring/Summer 2026</span>
</div>""", unsafe_allow_html=True)
 
st.markdown("---")
 
 
# ══════════════════════════════════════════════════════════════════
# SLIDE 7: THE OPPORTUNITY / CTA
# ══════════════════════════════════════════════════════════════════
st.markdown('<div id="opportunity"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div style="padding: 40px 0 20px;">
    <div class="section-label">THE OPPORTUNITY</div>
    <div class="slide-title-sm">Why Garden & Outdoor on CDON?</div>
    <div class="gold-rule"></div>
</div>
""", unsafe_allow_html=True)
 
reasons = [
    ("62%", "of annual garden sales happen Mar-Jul - the peak is NOW"),
    ("+12.3%", "YoY market growth - outpacing total Nordic e-commerce"),
    ("EUR 89", "average order value with strong margin potential"),
    ("27.5M", "consumers across four Nordic markets, one integration"),
    ("58%", "mobile commerce share - CDON's app drives conversion"),
    ("34%", "repeat purchase rate - build a loyal customer base"),
]
 
for val, desc in reasons:
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:20px;padding:14px 0;border-bottom:1px solid {COLORS['border']};">
        <div style="min-width:100px;text-align:right;">
            <span style="color:{COLORS['gold']};font-family:'Inter',sans-serif;font-size:24px;font-weight:800;">{val}</span>
        </div>
        <div style="color:{COLORS['white_soft']};font-family:'Inter',sans-serif;font-size:15px;">{desc}</div>
    </div>
    """, unsafe_allow_html=True)
 
st.markdown("<div style='height:30px'></div>", unsafe_allow_html=True)
 
st.markdown(f"""
<div style="text-align:center;padding:40px;background:{COLORS['bg_card']};border:1px solid {COLORS['border']};border-radius:16px;">
    <div style="color:{COLORS['gold']};font-family:'Inter',sans-serif;font-size:11px;font-weight:600;letter-spacing:3px;margin-bottom:12px;">READY TO GROW?</div>
    <div style="color:{COLORS['white']};font-family:'Inter',sans-serif;font-size:22px;font-weight:700;margin-bottom:8px;">Start selling Garden & Outdoor on CDON today</div>
    <div style="color:{COLORS['white_soft']};font-family:'Inter',sans-serif;font-size:14px;">Contact your Category Manager or visit merchant.cdon.com</div>
</div>
""", unsafe_allow_html=True)
 
st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
 
# Final download button
col_a, col_b, col_c = st.columns([2, 1, 2])
with col_b:
    st.download_button(
        label="Download PDF",
        data=pdf_data,
        file_name=f"CDON_Garden_Outdoor_Report_{datetime.date.today().strftime('%Y%m%d')}.pdf",
        mime="application/pdf",
        key="pdf_bottom",
    )
 
st.markdown(f"""
<div style="text-align:center;padding:40px 0 20px;">
    <div style="color:{COLORS['text_muted']};font-family:'Inter',sans-serif;font-size:11px;">
        CDON &mdash; Confidential &middot; Category Success &middot; Spring/Summer 2026
    </div>
</div>
""", unsafe_allow_html=True)
