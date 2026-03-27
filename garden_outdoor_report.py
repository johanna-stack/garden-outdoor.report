import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from io import BytesIO
from datetime import datetime
import base64
 
# Configure page
st.set_page_config(page_title="CDON Garden & Outdoor Report", layout="wide", initial_sidebar_state="collapsed")
 
# Hide streamlit elements
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stAppViewContainer {margin-top: 0; padding-top: 0;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
 
# Color scheme
DARK_GREEN = "#1a472a"
LIGHT_GREEN = "#1e3a1e"
GOLD = "#c9a84c"
WHITE = "#ffffff"
LIGHT_BG = "#fafaf8"
GRAY_TEXT = "#555555"
ACCENT_GREEN = "#3d8b6e"
 
# SVG Flags
def get_flag_svg(country):
    flags = {
        "denmark": """<svg viewBox="0 0 60 40" width="40" height="27">
            <rect width="60" height="40" fill="#C8102E"/>
            <rect x="16" width="8" height="40" fill="white"/>
            <rect y="16" width="60" height="8" fill="white"/>
        </svg>""",
        "sweden": """<svg viewBox="0 0 60 40" width="40" height="27">
            <rect width="60" height="40" fill="#0066B2"/>
            <rect x="18" width="8" height="40" fill="#FFCC00"/>
            <rect y="16" width="60" height="8" fill="#FFCC00"/>
        </svg>""",
        "norway": """<svg viewBox="0 0 60 40" width="40" height="27">
            <rect width="60" height="40" fill="#BA0C2F"/>
            <rect x="16" width="8" height="40" fill="#FFFFFF"/>
            <rect y="16" width="60" height="8" fill="#FFFFFF"/>
            <rect x="18" width="4" height="40" fill="#00205B"/>
            <rect y="18" width="60" height="4" fill="#00205B"/>
        </svg>""",
        "finland": """<svg viewBox="0 0 60 40" width="40" height="27">
            <rect width="60" height="40" fill="white"/>
            <rect x="18" width="8" height="40" fill="#003580"/>
            <rect y="16" width="60" height="8" fill="#003580"/>
        </svg>"""
    }
    return flags.get(country.lower(), "")
 
# ==================== SLIDE 1: TITLE ====================
col1, col2, col3 = st.columns([1, 8, 1])
with col2:
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {DARK_GREEN} 0%, {LIGHT_GREEN} 100%);
                padding: 80px 60px; text-align: center; border-radius: 0; min-height: 100vh;
                display: flex; flex-direction: column; justify-content: center;">
        <div style="position: relative;">
            <div style="font-size: 14px; color: {GOLD}; letter-spacing: 2px; margin-bottom: 20px; font-weight: 600;">
                CDON MARKETPLACE
            </div>
            <h1 style="color: {WHITE}; font-size: 56px; font-weight: 700; margin: 30px 0; line-height: 1.3;">
                Garden & Outdoor: The Nordic Spring Opportunity
            </h1>
            <div style="height: 3px; background: {GOLD}; width: 120px; margin: 30px auto;"></div>
            <p style="color: {WHITE}; font-size: 18px; margin: 40px 0; font-weight: 300;">
                A market overview for merchants looking to capture seasonal demand across Sweden, Denmark, Norway and Finland.
            </p>
            <div style="display: flex; justify-content: center; gap: 30px; margin: 50px 0; align-items: center;">
                <div style="text-align: center;">{get_flag_svg('denmark')}</div>
                <div style="text-align: center;">{get_flag_svg('sweden')}</div>
                <div style="text-align: center;">{get_flag_svg('norway')}</div>
                <div style="text-align: center;">{get_flag_svg('finland')}</div>
            </div>
            <div style="color: {GOLD}; font-size: 16px; font-weight: 600; letter-spacing: 1px; margin: 40px 0;">
                FOUR MARKETS - ONE PLATFORM
            </div>
            <div style="display: flex; justify-content: space-between; margin-top: 60px; padding-top: 30px; border-top: 1px solid rgba(255,255,255,0.2);">
                <span style="color: {WHITE}; font-size: 12px;">CDON - Confidential</span>
                <span style="color: {WHITE}; font-size: 12px;">Spring/Summer 2026</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
 
st.markdown("""
<div style="height: 40px;"></div>
<div style="height: 1px; background: rgba(201, 168, 76, 0.3);"></div>
<div style="height: 40px;"></div>
""", unsafe_allow_html=True)
 
# ==================== SLIDE 2: THE MARKET ====================
col1, col2, col3 = st.columns([1, 8, 1])
with col2:
    st.markdown(f"""
    <div style="padding: 60px 60px; background: {LIGHT_BG}; border-radius: 0;">
        <div style="font-size: 14px; color: {GOLD}; letter-spacing: 2px; font-weight: 600; margin-bottom: 10px;">
            THE MARKET
        </div>
        <h2 style="color: {DARK_GREEN}; font-size: 48px; font-weight: 700; margin: 20px 0;">
            Nordics: A Region That Lives Outdoors
        </h2>
        <div style="height: 3px; background: {GOLD}; width: 80px; margin: 20px 0;"></div>
        <p style="color: {GRAY_TEXT}; font-size: 16px; line-height: 1.8; margin: 30px 0; max-width: 800px;">
            The Nordic garden and outdoor market is one of Europe's most dynamic. Long winters create concentrated,
            high-intensity seasonal demand and consumers are ready to spend when spring arrives.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 20px; margin: 50px 0;">
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 25px; text-align: center;">
                <div style="color: {DARK_GREEN}; font-size: 32px; font-weight: 700; margin-bottom: 10px;">2.5B+</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px; font-weight: 600;">NORDIC GARDEN MARKET</div>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 25px; text-align: center;">
                <div style="color: {DARK_GREEN}; font-size: 32px; font-weight: 700; margin-bottom: 10px;">320M</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px; font-weight: 600;">OUTDOOR EQUIPMENT</div>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 25px; text-align: center;">
                <div style="color: {DARK_GREEN}; font-size: 32px; font-weight: 700; margin-bottom: 10px;">25M+</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px; font-weight: 600;">CONSUMERS</div>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 25px; text-align: center;">
                <div style="color: {DARK_GREEN}; font-size: 32px; font-weight: 700; margin-bottom: 10px;">6mo</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px; font-weight: 600;">PEAK SEASON</div>
            </div>
        </div>
        <div style="color: #999; font-size: 12px; margin-top: 40px;">
            Sources: Statista, Euromonitor, Nordic industry reports
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: 50px; padding-top: 20px; border-top: 1px solid #ddd;">
            <span style="color: {GRAY_TEXT}; font-size: 12px;">CDON - Garden & Outdoor Opportunity</span>
            <span style="color: {GRAY_TEXT}; font-size: 12px;">02</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
 
st.markdown("""
<div style="height: 40px;"></div>
<div style="height: 1px; background: rgba(201, 168, 76, 0.3);"></div>
<div style="height: 40px;"></div>
""", unsafe_allow_html=True)
 
# ==================== SLIDE 3: SEASONALITY ====================
col1, col2, col3 = st.columns([1, 8, 1])
with col2:
    st.markdown(f"""
    <div style="padding: 60px 60px; background: {LIGHT_BG}; border-radius: 0;">
        <div style="font-size: 14px; color: {GOLD}; letter-spacing: 2px; font-weight: 600; margin-bottom: 10px;">
            SEASONALITY
        </div>
        <h2 style="color: {DARK_GREEN}; font-size: 48px; font-weight: 700; margin: 20px 0;">
            The Spring Spike Is Real
        </h2>
        <div style="height: 3px; background: {GOLD}; width: 80px; margin: 20px 0;"></div>
        <p style="color: {GRAY_TEXT}; font-size: 16px; line-height: 1.8; margin: 30px 0; max-width: 800px;">
            Consumer search interest surges 3-5x from winter to peak season. Those who are listed early capture the full wave.
        </p>
    </div>
    """, unsafe_allow_html=True)
 
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    values = [10, 12, 25, 45, 95, 100, 70, 55, 35, 20, 15, 10]
    colors = ['#2d6a47' if v < 50 else '#3d8b6e' if v < 80 else '#52c76a' for v in values]
 
    fig = go.Figure(data=[
        go.Bar(x=months, y=values, marker=dict(color=colors), hovertemplate='%{x}: %{y}<extra></extra>')
    ])
    fig.update_layout(
        showlegend=False, height=300, margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(showgrid=False, zeroline=False), yaxis=dict(showgrid=False, zeroline=False),
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
 
    st.markdown(f"""
    <div style="padding: 0 60px;">
        <div style="color: {GRAY_TEXT}; font-size: 13px; margin-bottom: 30px;">
            Garden & Outdoor Search Interest (Google Trends, Nordics)
        </div>
        <div style="background: #f0f8f4; border-left: 4px solid {ACCENT_GREEN}; padding: 20px; border-radius: 6px; margin: 30px 0;">
            <div style="color: {DARK_GREEN}; font-weight: 600; font-size: 15px; margin-bottom: 10px;">
                Merchants who list by March capture 40% more of the spring demand curve
            </div>
            <div style="color: {GRAY_TEXT}; font-size: 13px;">
                Early listing = better search ranking = more visibility during peak
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: 50px; padding-top: 20px; border-top: 1px solid #ddd;">
            <span style="color: {GRAY_TEXT}; font-size: 12px;">CDON - Garden & Outdoor Opportunity</span>
            <span style="color: {GRAY_TEXT}; font-size: 12px;">03</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
 
st.markdown("""
<div style="height: 40px;"></div>
<div style="height: 1px; background: rgba(201, 168, 76, 0.3);"></div>
<div style="height: 40px;"></div>
""", unsafe_allow_html=True)
 
# ==================== SLIDE 4: THE SPRING WAVE ====================
col1, col2, col3 = st.columns([1, 8, 1])
with col2:
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {DARK_GREEN} 0%, {LIGHT_GREEN} 100%);
                padding: 60px 60px; border-radius: 0;">
        <div style="font-size: 14px; color: {GOLD}; letter-spacing: 2px; font-weight: 600; margin-bottom: 10px;">
            THE SPRING WAVE
        </div>
        <h2 style="color: {WHITE}; font-size: 48px; font-weight: 700; margin: 20px 0;">
            One Season. Four Markets. Four Launch Windows.
        </h2>
        <div style="height: 3px; background: {GOLD}; width: 80px; margin: 20px 0;"></div>
        <p style="color: {WHITE}; font-size: 16px; line-height: 1.8; margin: 30px 0; max-width: 900px;">
            Spring doesn't arrive everywhere at once. Denmark leads by weeks, followed by Sweden, Norway, and finally Finland.
            Smart merchants align their listings with each market's timing.
        </p>
        <div style="margin: 50px 0; padding: 30px; background: rgba(255,255,255,0.05); border-radius: 8px;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 20px; position: relative; height: 80px;">
                <div style="position: absolute; top: 20px; width: 100%; height: 2px; background: {GOLD};"></div>
                <div style="text-align: center; z-index: 10;">
                    <div style="display: inline-block; background: {DARK_GREEN}; padding: 8px; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; margin-bottom: 10px;">
                        {get_flag_svg('denmark')}
                    </div>
                    <div style="color: {GOLD}; font-weight: 700; font-size: 14px;">Denmark</div>
                    <div style="color: {WHITE}; font-size: 12px; margin-top: 5px;">March-April</div>
                    <div style="color: #ccc; font-size: 11px;">First movers</div>
                </div>
                <div style="text-align: center; z-index: 10;">
                    <div style="display: inline-block; background: {DARK_GREEN}; padding: 8px; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; margin-bottom: 10px;">
                        {get_flag_svg('sweden')}
                    </div>
                    <div style="color: {GOLD}; font-weight: 700; font-size: 14px;">Sweden</div>
                    <div style="color: {WHITE}; font-size: 12px; margin-top: 5px;">April-May</div>
                    <div style="color: #ccc; font-size: 11px;">Main wave</div>
                </div>
                <div style="text-align: center; z-index: 10;">
                    <div style="display: inline-block; background: {DARK_GREEN}; padding: 8px; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; margin-bottom: 10px;">
                        {get_flag_svg('norway')}
                    </div>
                    <div style="color: {GOLD}; font-weight: 700; font-size: 14px;">Norway</div>
                    <div style="color: {WHITE}; font-size: 12px; margin-top: 5px;">April-June</div>
                    <div style="color: #ccc; font-size: 11px;">Outdoor season</div>
                </div>
                <div style="text-align: center; z-index: 10;">
                    <div style="display: inline-block; background: {DARK_GREEN}; padding: 8px; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; margin-bottom: 10px;">
                        {get_flag_svg('finland')}
                    </div>
                    <div style="color: {GOLD}; font-weight: 700; font-size: 14px;">Finland</div>
                    <div style="color: {WHITE}; font-size: 12px; margin-top: 5px;">May-July</div>
                    <div style="color: #ccc; font-size: 11px;">Mokki season</div>
                </div>
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: 60px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.2);">
            <span style="color: {WHITE}; font-size: 12px;">CDON - Garden & Outdoor Opportunity</span>
            <span style="color: {WHITE}; font-size: 12px;">04</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
 
st.markdown("""
<div style="height: 40px;"></div>
<div style="height: 1px; background: rgba(201, 168, 76, 0.3);"></div>
<div style="height: 40px;"></div>
""", unsafe_allow_html=True)
 
# ==================== MARKET SLIDES (5-8) ====================
# DENMARK SLIDE
col1, col2, col3 = st.columns([1, 8, 1])
with col2:
    st.markdown(f"""
    <div style="padding: 60px 60px; background: {LIGHT_BG}; border-radius: 0;">
        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
            <div style="width: 50px;">{get_flag_svg('denmark')}</div>
            <div style="font-size: 14px; color: {GOLD}; letter-spacing: 2px; font-weight: 600;">DENMARK</div>
        </div>
        <h2 style="color: {DARK_GREEN}; font-size: 48px; font-weight: 700; margin: 20px 0;">The First Movers</h2>
        <div style="height: 3px; background: {GOLD}; width: 80px; margin: 20px 0;"></div>
        <p style="color: {GRAY_TEXT}; font-size: 16px; line-height: 1.8; margin: 30px 0; max-width: 800px;">
            Denmark enjoys the earliest spring across the Nordics, typically 3-4 weeks ahead of Sweden.
        </p>
        <div style="background: #f5f5f5; padding: 20px; border-radius: 6px; margin: 30px 0; border-left: 4px solid {ACCENT_GREEN};">
            <div style="color: {DARK_GREEN}; font-style: italic; font-size: 15px;">
                "Danes kick off the Nordic buying wave. If you're listed by March, you're ahead of the curve."
            </div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 15px; margin: 30px 0;">
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center;">
                <div style="color: {DARK_GREEN}; font-size: 14px; font-weight: 700;">Mar-Apr</div>
                <div style="color: {GRAY_TEXT}; font-size: 12px; margin-top: 8px;">PEAK GARDEN SEASON</div>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center;">
                <div style="color: {DARK_GREEN}; font-size: 14px; font-weight: 700;">3-4 wks</div>
                <div style="color: {GRAY_TEXT}; font-size: 12px; margin-top: 8px;">AHEAD OF SWEDEN</div>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center;">
                <div style="color: {DARK_GREEN}; font-size: 14px; font-weight: 700;">High</div>
                <div style="color: {GRAY_TEXT}; font-size: 12px; margin-top: 8px;">E-COMMERCE MATURITY</div>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center;">
                <div style="color: {DARK_GREEN}; font-size: 14px; font-weight: 700;">Strong</div>
                <div style="color: {GRAY_TEXT}; font-size: 12px; margin-top: 8px;">OUTDOOR COOKING</div>
            </div>
        </div>
        <div style="margin: 40px 0;">
            <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 14px; margin-bottom: 15px;">Trending Categories</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Garden furniture & outdoor living</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Outdoor cooking & BBQ</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Greenhouses & raised beds</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Balcony & small-space gardening</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Pool & spa products</div>
            </div>
        </div>
        <div style="margin: 40px 0;">
            <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 14px; margin-bottom: 20px;">TOP 10 PRODUCTS</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 25px; font-size: 13px;">
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">1</span>Cane-line Moments Sofa</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">2</span>Weber Spirit E-325</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">3</span>Juliana Grand Oase</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">4</span>Ooni Karu 16 Pizza Oven</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">5</span>Gardena SILENO City 600</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">6</span>Houe Click Dining Set</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">7</span>Kamado Joe Classic III</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">8</span>SACKit Cobana Lounge</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">9</span>Palram Hybrid Greenhouse</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">10</span>Skagerak Riviera Sun Lounger</div>
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: 50px; padding-top: 20px; border-top: 1px solid #ddd;">
            <span style="color: {GRAY_TEXT}; font-size: 12px;">CDON - Garden & Outdoor Opportunity</span>
            <span style="color: {GRAY_TEXT}; font-size: 12px;">05</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
 
st.markdown("""<div style="height: 40px;"></div><div style="height: 1px; background: rgba(201, 168, 76, 0.3);"></div><div style="height: 40px;"></div>""", unsafe_allow_html=True)
 
# SWEDEN SLIDE
col1, col2, col3 = st.columns([1, 8, 1])
with col2:
    st.markdown(f"""
    <div style="padding: 60px 60px; background: {LIGHT_BG}; border-radius: 0;">
        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
            <div style="width: 50px;">{get_flag_svg('sweden')}</div>
            <div style="font-size: 14px; color: {GOLD}; letter-spacing: 2px; font-weight: 600;">SWEDEN</div>
        </div>
        <h2 style="color: {DARK_GREEN}; font-size: 48px; font-weight: 700; margin: 20px 0;">The Main Wave</h2>
        <div style="height: 3px; background: {GOLD}; width: 80px; margin: 20px 0;"></div>
        <p style="color: {GRAY_TEXT}; font-size: 16px; line-height: 1.8; margin: 30px 0; max-width: 800px;">
            Sweden is the largest Nordic garden market by volume. Peak demand stretches from April through May.
        </p>
        <div style="background: #f5f5f5; padding: 20px; border-radius: 6px; margin: 30px 0; border-left: 4px solid {ACCENT_GREEN};">
            <div style="color: {DARK_GREEN}; font-style: italic; font-size: 15px;">
                "Sweden's garden market is the Nordic powerhouse. Robot mowers alone are growing over 20% annually."
            </div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 15px; margin: 30px 0;">
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center;">
                <div style="color: {DARK_GREEN}; font-size: 14px; font-weight: 700;">Apr-May</div>
                <div style="color: {GRAY_TEXT}; font-size: 12px; margin-top: 8px;">PEAK SEASON</div>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center;">
                <div style="color: {DARK_GREEN}; font-size: 14px; font-weight: 700;">22.5%</div>
                <div style="color: {GRAY_TEXT}; font-size: 12px; margin-top: 8px;">ROBOT MOWER CAGR</div>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center;">
                <div style="color: {DARK_GREEN}; font-size: 14px; font-weight: 700;">14.1%</div>
                <div style="color: {GRAY_TEXT}; font-size: 12px; margin-top: 8px;">ELECTRIC TOOLS CAGR</div>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center;">
                <div style="color: {DARK_GREEN}; font-size: 14px; font-weight: 700;">#1</div>
                <div style="color: {GRAY_TEXT}; font-size: 12px; margin-top: 8px;">NORDIC MARKET</div>
            </div>
        </div>
        <div style="margin: 40px 0;">
            <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 14px; margin-bottom: 15px;">Trending Categories</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Robot mowers & smart garden tech</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Electric garden tools</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Outdoor furniture & lounge sets</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Cultivation/growing/greenhouse</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Garden lighting & irrigation</div>
            </div>
        </div>
        <div style="margin: 40px 0;">
            <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 14px; margin-bottom: 20px;">TOP 10 PRODUCTS</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 25px; font-size: 13px;">
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">1</span>Husqvarna Automower 450X</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">2</span>Gardena SILENO Life 1500</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">3</span>STIHL HSA 60 Trimmer</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">4</span>Sweden Greenhouse Classic</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">5</span>Brafab Sottenville Lounge</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">6</span>Einhell GE-CM 36 Li Mower</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">7</span>Halsing Outdoor Kitchen</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">8</span>Gardena Smart Water Control</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">9</span>Inflatable SUP Boards</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">10</span>Skargards Wood-Fired Tub</div>
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: 50px; padding-top: 20px; border-top: 1px solid #ddd;">
            <span style="color: {GRAY_TEXT}; font-size: 12px;">CDON - Garden & Outdoor Opportunity</span>
            <span style="color: {GRAY_TEXT}; font-size: 12px;">06</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
 
st.markdown("""<div style="height: 40px;"></div><div style="height: 1px; background: rgba(201, 168, 76, 0.3);"></div><div style="height: 40px;"></div>""", unsafe_allow_html=True)
 
# NORWAY SLIDE
col1, col2, col3 = st.columns([1, 8, 1])
with col2:
    st.markdown(f"""
    <div style="padding: 60px 60px; background: {LIGHT_BG}; border-radius: 0;">
        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
            <div style="width: 50px;">{get_flag_svg('norway')}</div>
            <div style="font-size: 14px; color: {GOLD}; letter-spacing: 2px; font-weight: 600;">NORWAY</div>
        </div>
        <h2 style="color: {DARK_GREEN}; font-size: 48px; font-weight: 700; margin: 20px 0;">The Outdoor Nation</h2>
        <div style="height: 3px; background: {GOLD}; width: 80px; margin: 20px 0;"></div>
        <p style="color: {GRAY_TEXT}; font-size: 16px; line-height: 1.8; margin: 30px 0; max-width: 800px;">
            77% of Norwegians engage in weekly outdoor activities. The market is premium-oriented with the highest average order values.
        </p>
        <div style="background: #f5f5f5; padding: 20px; border-radius: 6px; margin: 30px 0; border-left: 4px solid {ACCENT_GREEN};">
            <div style="color: {DARK_GREEN}; font-style: italic; font-size: 15px;">
                "2025 was declared Norway's Year of Outdoor. The momentum hasn't slowed."
            </div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 15px; margin: 30px 0;">
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center;">
                <div style="color: {DARK_GREEN}; font-size: 14px; font-weight: 700;">77%</div>
                <div style="color: {GRAY_TEXT}; font-size: 12px; margin-top: 8px;">OUTDOOR ACTIVITY</div>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center;">
                <div style="color: {DARK_GREEN}; font-size: 14px; font-weight: 700;">Highest</div>
                <div style="color: {GRAY_TEXT}; font-size: 12px; margin-top: 8px;">AVERAGE ORDER VALUE</div>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center;">
                <div style="color: {DARK_GREEN}; font-size: 14px; font-weight: 700;">Apr-Jun</div>
                <div style="color: {GRAY_TEXT}; font-size: 12px; margin-top: 8px;">PEAK SEASON</div>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center;">
                <div style="color: {DARK_GREEN}; font-size: 14px; font-weight: 700;">Premium</div>
                <div style="color: {GRAY_TEXT}; font-size: 12px; margin-top: 8px;">ORIENTATION</div>
            </div>
        </div>
        <div style="margin: 40px 0;">
            <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 14px; margin-bottom: 15px;">Trending Categories</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Hiking & camping</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Outdoor furniture for cabins</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Fishing gear</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">SUP boards & water sports</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Premium outdoor cooking</div>
            </div>
        </div>
        <div style="margin: 40px 0;">
            <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 14px; margin-bottom: 20px;">TOP 10 PRODUCTS</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 25px; font-size: 13px;">
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">1</span>Hilleberg Anjan 2 Tent</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">2</span>Norrona Trollveggen Shell</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">3</span>Red Paddle Co Sport 11'3</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">4</span>Weber Genesis E-435</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">5</span>Husqvarna Automower 320</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">6</span>Fiskars X27 Splitting Axe</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">7</span>Helinox Chair One</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">8</span>Abu Garcia Revo Beast X</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">9</span>Ooni Volt 12 Electric Oven</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">10</span>Garmin inReach Mini 2</div>
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: 50px; padding-top: 20px; border-top: 1px solid #ddd;">
            <span style="color: {GRAY_TEXT}; font-size: 12px;">CDON - Garden & Outdoor Opportunity</span>
            <span style="color: {GRAY_TEXT}; font-size: 12px;">07</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
 
st.markdown("""<div style="height: 40px;"></div><div style="height: 1px; background: rgba(201, 168, 76, 0.3);"></div><div style="height: 40px;"></div>""", unsafe_allow_html=True)
 
# FINLAND SLIDE
col1, col2, col3 = st.columns([1, 8, 1])
with col2:
    st.markdown(f"""
    <div style="padding: 60px 60px; background: {LIGHT_BG}; border-radius: 0;">
        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
            <div style="width: 50px;">{get_flag_svg('finland')}</div>
            <div style="font-size: 14px; color: {GOLD}; letter-spacing: 2px; font-weight: 600;">FINLAND</div>
        </div>
        <h2 style="color: {DARK_GREEN}; font-size: 48px; font-weight: 700; margin: 20px 0;">Mokki & Nature</h2>
        <div style="height: 3px; background: {GOLD}; width: 80px; margin: 20px 0;"></div>
        <p style="color: {GRAY_TEXT}; font-size: 16px; line-height: 1.8; margin: 30px 0; max-width: 800px;">
            Finland's mokki (cabin) culture is central to the nation's identity. With 1.5 million active fishers, outdoor gear demand peaks May-July.
        </p>
        <div style="background: #f5f5f5; padding: 20px; border-radius: 6px; margin: 30px 0; border-left: 4px solid {ACCENT_GREEN};">
            <div style="color: {DARK_GREEN}; font-style: italic; font-size: 15px;">
                "Finland's mokki culture means every family needs garden and outdoor gear - twice."
            </div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 15px; margin: 30px 0;">
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center;">
                <div style="color: {DARK_GREEN}; font-size: 14px; font-weight: 700;">1.5M</div>
                <div style="color: {GRAY_TEXT}; font-size: 12px; margin-top: 8px;">ACTIVE FISHERS</div>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center;">
                <div style="color: {DARK_GREEN}; font-size: 14px; font-weight: 700;">27%</div>
                <div style="color: {GRAY_TEXT}; font-size: 12px; margin-top: 8px;">POPULATION FISHING</div>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center;">
                <div style="color: {DARK_GREEN}; font-size: 14px; font-weight: 700;">May-Jul</div>
                <div style="color: {GRAY_TEXT}; font-size: 12px; margin-top: 8px;">PEAK SEASON</div>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center;">
                <div style="color: {DARK_GREEN}; font-size: 14px; font-weight: 700;">Top</div>
                <div style="color: {GRAY_TEXT}; font-size: 12px; margin-top: 8px;">CAMPING SPEND</div>
            </div>
        </div>
        <div style="margin: 40px 0;">
            <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 14px; margin-bottom: 15px;">Trending Categories</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Fishing gear & tackle</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Sauna & outdoor wellness</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Camping equipment</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Garden tools & mokki maintenance</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Outdoor furniture & decor</div>
            </div>
        </div>
        <div style="margin: 40px 0;">
            <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 14px; margin-bottom: 20px;">TOP 10 PRODUCTS</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 25px; font-size: 13px;">
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">1</span>Kirami FinVision Sauna</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">2</span>Muurikka Electric Smoker</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">3</span>Fiskars Norden N12 Axe</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">4</span>Rapala X-Rap Lures</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">5</span>Husqvarna Automower 405X</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">6</span>Savotta Hiisi 20 Backpack</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">7</span>HAY Palissade Table</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">8</span>Kirami Wood-Fired Hot Tub</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">9</span>Shimano Stradic FL Reel</div>
                <div><span style="background: {ACCENT_GREEN}; color: white; padding: 2px 8px; border-radius: 50%; font-weight: 700; margin-right: 8px;">10</span>MSR Hubba Hubba NX Tent</div>
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: 50px; padding-top: 20px; border-top: 1px solid #ddd;">
            <span style="color: {GRAY_TEXT}; font-size: 12px;">CDON - Garden & Outdoor Opportunity</span>
            <span style="color: {GRAY_TEXT}; font-size: 12px;">08</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
 
st.markdown("""<div style="height: 40px;"></div><div style="height: 1px; background: rgba(201, 168, 76, 0.3);"></div><div style="height: 40px;"></div>""", unsafe_allow_html=True)
 
# ==================== SLIDE 9: CONSUMER TRENDS ====================
col1, col2, col3 = st.columns([1, 8, 1])
with col2:
    st.markdown(f"""
    <div style="padding: 60px 60px; background: #fffbf5; border-radius: 0;">
        <div style="font-size: 14px; color: {GOLD}; letter-spacing: 2px; font-weight: 600; margin-bottom: 10px;">
            CONSUMER TRENDS
        </div>
        <h2 style="color: {DARK_GREEN}; font-size: 48px; font-weight: 700; margin: 20px 0;">
            What Nordic Consumers Are Searching For
        </h2>
        <div style="height: 3px; background: {GOLD}; width: 80px; margin: 20px 0;"></div>
        <p style="color: {GRAY_TEXT}; font-size: 16px; line-height: 1.8; margin: 30px 0; max-width: 900px;">
            Google Trends data reveals the product categories driving growth across all four markets.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 25px; margin: 40px 0;">
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 25px; background: white;">
                <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 15px; margin-bottom: 8px;">Robot Mowers</div>
                <div style="color: {ACCENT_GREEN}; font-weight: 700; font-size: 13px; margin-bottom: 12px;">22.5% CAGR</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Premium segment. Peak: April-May</div>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 25px; background: white;">
                <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 15px; margin-bottom: 8px;">Garden Furniture</div>
                <div style="color: {ACCENT_GREEN}; font-weight: 700; font-size: 13px; margin-bottom: 12px;">Consistent</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Largest subcategory. Peak: March-June</div>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 25px; background: white;">
                <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 15px; margin-bottom: 8px;">SUP / Paddleboards</div>
                <div style="color: {ACCENT_GREEN}; font-weight: 700; font-size: 13px; margin-bottom: 12px;">7-10% CAGR</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Fastest growing. Peak: May-July</div>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 25px; background: white;">
                <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 15px; margin-bottom: 8px;">Camping Equipment</div>
                <div style="color: {ACCENT_GREEN}; font-weight: 700; font-size: 13px; margin-bottom: 12px;">4-6% CAGR</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Post-COVID demand. Peak: June-July</div>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 25px; background: white;">
                <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 15px; margin-bottom: 8px;">Outdoor Cooking</div>
                <div style="color: {ACCENT_GREEN}; font-weight: 700; font-size: 13px; margin-bottom: 12px;">5-7% CAGR</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Social trend. Peak: April-August</div>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 25px; background: white;">
                <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 15px; margin-bottom: 8px;">Electric Garden Tools</div>
                <div style="color: {ACCENT_GREEN}; font-weight: 700; font-size: 13px; margin-bottom: 12px;">14.1% CAGR</div>
                <div style="color: {GRAY_TEXT}; font-size: 13px;">Replacing gas. Peak: April-May</div>
            </div>
        </div>
        <div style="color: #999; font-size: 12px; margin-top: 40px;">
            Growth rates based on Google Trends analysis 2023-2025, Statista, and industry reports
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: 50px; padding-top: 20px; border-top: 1px solid #ddd;">
            <span style="color: {GRAY_TEXT}; font-size: 12px;">CDON - Garden & Outdoor Opportunity</span>
            <span style="color: {GRAY_TEXT}; font-size: 12px;">09</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
 
st.markdown("""<div style="height: 40px;"></div><div style="height: 1px; background: rgba(201, 168, 76, 0.3);"></div><div style="height: 40px;"></div>""", unsafe_allow_html=True)
 
# ==================== SLIDE 10: CATEGORY SPOTLIGHT GARDEN ====================
col1, col2, col3 = st.columns([1, 8, 1])
with col2:
    st.markdown(f"""
    <div style="padding: 60px 60px; background: {LIGHT_BG}; border-radius: 0;">
        <div style="font-size: 14px; color: {GOLD}; letter-spacing: 2px; font-weight: 600; margin-bottom: 10px;">
            CATEGORY SPOTLIGHT
        </div>
        <h2 style="color: {DARK_GREEN}; font-size: 56px; font-weight: 700; margin: 20px 0;">Garden</h2>
        <div style="height: 3px; background: {GOLD}; width: 80px; margin: 20px 0;"></div>
        <p style="color: {GRAY_TEXT}; font-size: 16px; line-height: 1.8; margin: 30px 0; max-width: 800px;">
            The garden category spans everything from furniture to irrigation systems, representing the "outdoor living room" trend.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin: 50px 0;">
            <div>
                <div style="display: flex; gap: 20px; margin-bottom: 30px; align-items: flex-start;">
                    <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 24px; min-width: 40px;">01</div>
                    <div style="flex: 1;">
                        <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 14px; margin-bottom: 5px;">Outdoor Furniture</div>
                        <div style="color: {GRAY_TEXT}; font-size: 13px; margin-bottom: 10px;">Lounge sets, dining tables, parasols</div>
                        <div style="background: #e8f0e8; height: 6px; border-radius: 3px;"></div>
                    </div>
                </div>
                <div style="display: flex; gap: 20px; margin-bottom: 30px; align-items: flex-start;">
                    <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 24px; min-width: 40px;">02</div>
                    <div style="flex: 1;">
                        <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 14px; margin-bottom: 5px;">Garden Tools & Machines</div>
                        <div style="color: {GRAY_TEXT}; font-size: 13px; margin-bottom: 10px;">Robot mowers, trimmers, electric saws</div>
                        <div style="background: linear-gradient(to right, #3d8b6e 75%, #e8f0e8 25%); height: 6px; border-radius: 3px;"></div>
                    </div>
                </div>
                <div style="display: flex; gap: 20px; margin-bottom: 30px; align-items: flex-start;">
                    <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 24px; min-width: 40px;">03</div>
                    <div style="flex: 1;">
                        <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 14px; margin-bottom: 5px;">Cultivation & Growing</div>
                        <div style="color: {GRAY_TEXT}; font-size: 13px; margin-bottom: 10px;">Greenhouses, raised beds, pots, seeds</div>
                        <div style="background: linear-gradient(to right, #3d8b6e 60%, #e8f0e8 40%); height: 6px; border-radius: 3px;"></div>
                    </div>
                </div>
                <div style="display: flex; gap: 20px; margin-bottom: 30px; align-items: flex-start;">
                    <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 24px; min-width: 40px;">04</div>
                    <div style="flex: 1;">
                        <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 14px; margin-bottom: 5px;">Pool & Spa</div>
                        <div style="color: {GRAY_TEXT}; font-size: 13px; margin-bottom: 10px;">Above-ground pools, hot tubs</div>
                        <div style="background: linear-gradient(to right, #3d8b6e 85%, #e8f0e8 15%); height: 6px; border-radius: 3px;"></div>
                    </div>
                </div>
                <div style="display: flex; gap: 20px; margin-bottom: 30px; align-items: flex-start;">
                    <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 24px; min-width: 40px;">05</div>
                    <div style="flex: 1;">
                        <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 14px; margin-bottom: 5px;">Outdoor Cooking</div>
                        <div style="color: {GRAY_TEXT}; font-size: 13px; margin-bottom: 10px;">Grills, smokers, pizza ovens, fire pits</div>
                        <div style="background: linear-gradient(to right, #3d8b6e 90%, #e8f0e8 10%); height: 6px; border-radius: 3px;"></div>
                    </div>
                </div>
            </div>
            <div>
                <div style="background: {DARK_GREEN}; color: white; padding: 30px; border-radius: 8px;">
                    <div style="color: {GOLD}; font-weight: 700; font-size: 14px; margin-bottom: 15px; text-transform: uppercase; letter-spacing: 1px;">
                        Key Insight
                    </div>
                    <p style="color: white; font-size: 15px; line-height: 1.7; margin-bottom: 25px;">
                        The "outdoor living room" trend is transforming Nordic gardens. Consumers now invest in complete outdoor setups.
                    </p>
                    <div style="border-top: 1px solid rgba(255,255,255,0.2); padding-top: 20px;">
                        <div style="color: {GOLD}; font-weight: 600; font-size: 13px; margin-bottom: 8px;">PEAK SEASON</div>
                        <div style="color: white; font-size: 13px; margin-bottom: 20px;">March - June</div>
                        <div style="color: {GOLD}; font-weight: 600; font-size: 13px; margin-bottom: 8px;">CONSUMER MINDSET</div>
                        <div style="color: white; font-size: 13px; font-style: italic;">
                            "Invest in quality for the summer"
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: 50px; padding-top: 20px; border-top: 1px solid #ddd;">
            <span style="color: {GRAY_TEXT}; font-size: 12px;">CDON - Garden & Outdoor Opportunity</span>
            <span style="color: {GRAY_TEXT}; font-size: 12px;">10</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
 
st.markdown("""<div style="height: 40px;"></div><div style="height: 1px; background: rgba(201, 168, 76, 0.3);"></div><div style="height: 40px;"></div>""", unsafe_allow_html=True)
 
# ==================== SLIDE 11: CATEGORY SPOTLIGHT OUTDOOR & ADVENTURE ====================
col1, col2, col3 = st.columns([1, 8, 1])
with col2:
    st.markdown(f"""
    <div style="padding: 60px 60px; background: {LIGHT_BG}; border-radius: 0;">
        <div style="font-size: 14px; color: {GOLD}; letter-spacing: 2px; font-weight: 600; margin-bottom: 10px;">
            CATEGORY SPOTLIGHT
        </div>
        <h2 style="color: {DARK_GREEN}; font-size: 56px; font-weight: 700; margin: 20px 0;">Outdoor & Adventure</h2>
        <div style="height: 3px; background: {GOLD}; width: 80px; margin: 20px 0;"></div>
        <p style="color: {GRAY_TEXT}; font-size: 16px; line-height: 1.8; margin: 30px 0; max-width: 800px;">
            The outdoor and adventure market is valued at 310-320 million euros. For Nordic consumers, outdoor recreation is a way of life.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin: 50px 0;">
            <div>
                <div style="display: flex; gap: 20px; margin-bottom: 30px; align-items: flex-start;">
                    <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 24px; min-width: 40px;">01</div>
                    <div style="flex: 1;">
                        <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 14px; margin-bottom: 5px;">Camping & Hiking</div>
                        <div style="color: {GRAY_TEXT}; font-size: 13px; margin-bottom: 10px;">Tents, sleeping bags, backpacks</div>
                        <div style="background: linear-gradient(to right, #3d8b6e 80%, #e8f0e8 20%); height: 6px; border-radius: 3px;"></div>
                    </div>
                </div>
                <div style="display: flex; gap: 20px; margin-bottom: 30px; align-items: flex-start;">
                    <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 24px; min-width: 40px;">02</div>
                    <div style="flex: 1;">
                        <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 14px; margin-bottom: 5px;">Fishing</div>
                        <div style="color: {GRAY_TEXT}; font-size: 13px; margin-bottom: 10px;">Rods, reels, tackle, waders, boats</div>
                        <div style="background: linear-gradient(to right, #3d8b6e 70%, #e8f0e8 30%); height: 6px; border-radius: 3px;"></div>
                    </div>
                </div>
                <div style="display: flex; gap: 20px; margin-bottom: 30px; align-items: flex-start;">
                    <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 24px; min-width: 40px;">03</div>
                    <div style="flex: 1;">
                        <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 14px; margin-bottom: 5px;">Water Sports</div>
                        <div style="color: {GRAY_TEXT}; font-size: 13px; margin-bottom: 10px;">SUP boards, kayaks, wetsuits</div>
                        <div style="background: linear-gradient(to right, #3d8b6e 65%, #e8f0e8 35%); height: 6px; border-radius: 3px;"></div>
                    </div>
                </div>
                <div style="display: flex; gap: 20px; margin-bottom: 30px; align-items: flex-start;">
                    <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 24px; min-width: 40px;">04</div>
                    <div style="flex: 1;">
                        <div style="color: {DARK_GREEN}; font-weight: 700; font-size: 14px; margin-bottom: 5px;">Hunting & Optics</div>
                        <div style="color: {GRAY_TEXT}; font-size: 13px; margin-bottom: 10px;">Hunting gear, binoculars, knives</div>
                        <div style="background: linear-gradient(to right, #3d8b6e 55%, #e8f0e8 45%); height: 6px; border-radius: 3px;"></div>
                    </div>
                </div>
            </div>
            <div>
                <div style="background: #2a4a6f; color: white; padding: 30px; border-radius: 8px;">
                    <div style="color: {GOLD}; font-weight: 700; font-size: 14px; margin-bottom: 15px; text-transform: uppercase; letter-spacing: 1px;">
                        Market Context
                    </div>
                    <div style="color: {GOLD}; font-weight: 700; font-size: 32px; margin-bottom: 10px;">310-320M</div>
                    <div style="color: white; font-size: 13px; margin-bottom: 30px;">Nordic outdoor equipment market</div>
                    <div style="border-top: 1px solid rgba(255,255,255,0.2); padding-top: 20px;">
                        <div style="display: flex; gap: 15px; align-items: flex-start; margin-bottom: 15px;">
                            <div style="width: 35px; flex-shrink: 0;">{get_flag_svg('norway')}</div>
                            <div>
                                <div style="color: {GOLD}; font-weight: 600; font-size: 12px;">Norway</div>
                                <div style="color: white; font-size: 12px;">77% weekly nature participation</div>
                            </div>
                        </div>
                        <div style="display: flex; gap: 15px; align-items: flex-start; margin-bottom: 15px;">
                            <div style="width: 35px; flex-shrink: 0;">{get_flag_svg('finland')}</div>
                            <div>
                                <div style="color: {GOLD}; font-weight: 600; font-size: 12px;">Finland</div>
                                <div style="color: white; font-size: 12px;">1.5M fishers, 27% of population</div>
                            </div>
                        </div>
                        <div style="display: flex; gap: 15px; align-items: flex-start; margin-bottom: 15px;">
                            <div style="width: 35px; flex-shrink: 0;">{get_flag_svg('sweden')}</div>
                            <div>
                                <div style="color: {GOLD}; font-weight: 600; font-size: 12px;">Sweden</div>
                                <div style="color: white; font-size: 12px;">Largest camping market</div>
                            </div>
                        </div>
                        <div style="display: flex; gap: 15px; align-items: flex-start;">
                            <div style="width: 35px; flex-shrink: 0;">{get_flag_svg('denmark')}</div>
                            <div>
                                <div style="color: {GOLD}; font-weight: 600; font-size: 12px;">Denmark</div>
                                <div style="color: white; font-size: 12px;">Strong watersports adoption</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: 50px; padding-top: 20px; border-top: 1px solid #ddd;">
            <span style="color: {GRAY_TEXT}; font-size: 12px;">CDON - Garden & Outdoor Opportunity</span>
            <span style="color: {GRAY_TEXT}; font-size: 12px;">11</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
 
st.markdown("""<div style="height: 40px;"></div><div style="height: 1px; background: rgba(201, 168, 76, 0.3);"></div><div style="height: 40px;"></div>""", unsafe_allow_html=True)
 
# ==================== SLIDE 12: YOUR OPPORTUNITY ====================
col1, col2, col3 = st.columns([1, 8, 1])
with col2:
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {DARK_GREEN} 0%, {LIGHT_GREEN} 100%);
                padding: 60px 60px; border-radius: 0;">
        <div style="font-size: 14px; color: {GOLD}; letter-spacing: 2px; font-weight: 600; margin-bottom: 10px;">
            YOUR OPPORTUNITY
        </div>
        <h2 style="color: {WHITE}; font-size: 48px; font-weight: 700; margin: 20px 0;">
            4 Markets. 25M+ Consumers. One Platform.
        </h2>
        <div style="height: 3px; background: {GOLD}; width: 80px; margin: 20px 0;"></div>
        <div style="background: rgba(201, 168, 76, 0.15); border: 2px solid {GOLD}; padding: 20px 30px;
                   border-radius: 6px; margin: 40px 0; text-align: center;">
            <div style="color: {GOLD}; font-size: 28px; font-weight: 700; letter-spacing: 3px;">
                DK - SE - NO - FI
            </div>
        </div>
        <div style="color: {GOLD}; font-size: 18px; font-weight: 600; margin: 30px 0; text-align: center;">
            The spring wave - March through July
        </div>
        <div style="margin: 50px 0; padding: 30px 0;">
            <div style="display: flex; gap: 20px; align-items: flex-start; margin-bottom: 25px;">
                <div style="color: {GOLD}; font-size: 20px; font-weight: 700;">+</div>
                <div style="color: {WHITE}; font-size: 16px; line-height: 1.6;">
                    List your products before March to capture Denmark's early wave
                </div>
            </div>
            <div style="display: flex; gap: 20px; align-items: flex-start; margin-bottom: 25px;">
                <div style="color: {GOLD}; font-size: 20px; font-weight: 700;">+</div>
                <div style="color: {WHITE}; font-size: 16px; line-height: 1.6;">
                    Reach all four Nordic markets from a single platform
                </div>
            </div>
            <div style="display: flex; gap: 20px; align-items: flex-start; margin-bottom: 25px;">
                <div style="color: {GOLD}; font-size: 20px; font-weight: 700;">+</div>
                <div style="color: {WHITE}; font-size: 16px; line-height: 1.6;">
                    Tap into consumers actively searching for your products
                </div>
            </div>
            <div style="display: flex; gap: 20px; align-items: flex-start;">
                <div style="color: {GOLD}; font-size: 20px; font-weight: 700;">+</div>
                <div style="color: {WHITE}; font-size: 16px; line-height: 1.6;">
                    Benefit from growing categories: robot mowers, SUP, outdoor cooking & more
                </div>
            </div>
        </div>
        <div style="margin: 60px 0; padding: 40px 0; border-top: 1px solid rgba(255,255,255,0.2); border-bottom: 1px solid rgba(255,255,255,0.2); text-align: center;">
            <div style="color: {WHITE}; font-size: 22px; font-weight: 600; margin-bottom: 15px;">
                Ready to grow with us?
            </div>
            <div style="color: {GOLD}; font-size: 14px; letter-spacing: 1px;">
                Contact your CDON Merchant Success Manager to get started
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: 60px; padding-top: 20px; align-items: flex-end;">
            <span style="color: {WHITE}; font-size: 12px;">CDON - Garden & Outdoor Opportunity</span>
            <div style="font-size: 20px; font-weight: 700; color: {GOLD};">CDON</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
 
st.markdown("""<div style="height: 40px;"></div>""", unsafe_allow_html=True)
 
# ==================== PDF GENERATION ====================
def generate_pdf():
    from fpdf import FPDF
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=False)
    slides_content = [
        ("CDON MARKETPLACE", "Garden & Outdoor: The Nordic Spring Opportunity", "A market overview for merchants looking to capture seasonal demand across Sweden, Denmark, Norway and Finland.", "title"),
        ("THE MARKET", "Nordics: A Region That Lives Outdoors", "The Nordic garden and outdoor market is one of Europe's most dynamic. Long winters create concentrated, high-intensity seasonal demand.\n\nMarket: 2.5B+ | Equipment: 320M | Consumers: 25M+ | Peak: 6 months", "content"),
        ("SEASONALITY", "The Spring Spike Is Real", "Consumer search interest surges 3-5x from winter to peak season. Merchants who list by March capture 40% more of the spring demand curve.", "content"),
        ("THE SPRING WAVE", "One Season. Four Markets. Four Launch Windows.", "Spring doesn't arrive everywhere at once.\n- Denmark: March-April (First movers)\n- Sweden: April-May (Main wave)\n- Norway: April-June (Outdoor season)\n- Finland: May-July (Mokki season)", "content"),
        ("DENMARK", "The First Movers", "Peak Season: March-April | 3-4 weeks ahead of Sweden | High e-commerce maturity | Strong outdoor cooking trend", "content"),
        ("SWEDEN", "The Main Wave", "Peak Season: April-May | Robot Mower CAGR: 22.5% | Electric Tools CAGR: 14.1% | #1 Nordic Garden Market", "content"),
        ("NORWAY", "The Outdoor Nation", "77% weekly outdoor activity | Highest average order value | Peak Season: April-June | Premium consumer orientation", "content"),
        ("FINLAND", "Mokki & Nature", "1.5M active fishers | 27% population fishing | Peak Season: May-July | Top camping spend per capita", "content"),
        ("CONSUMER TRENDS", "What Nordic Consumers Are Searching For", "Robot Mowers: 22.5% CAGR | Garden Furniture: Consistent | SUP Boards: 7-10% CAGR | Camping: 4-6% CAGR | Outdoor Cooking: 5-7% CAGR | Electric Tools: 14.1% CAGR", "content"),
        ("CATEGORY SPOTLIGHT", "Garden", "The garden category represents the outdoor living room trend. Outdoor furniture, tools & machines, cultivation & growing, pool & spa, outdoor cooking. Peak: March-June", "content"),
        ("CATEGORY SPOTLIGHT", "Outdoor & Adventure", "Market: 310-320M euros. Camping & hiking, fishing, water sports, hunting & optics. Norway: 77% participation | Finland: 1.5M fishers | Sweden: Largest camping | Denmark: Strong watersports", "content"),
        ("YOUR OPPORTUNITY", "4 Markets. 25M+ Consumers. One Platform.", "DK - SE - NO - FI. List before March for Denmark wave. Reach all four markets. Tap active consumers. Benefit from growing categories.", "content"),
    ]
 
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)
    w = 180  # usable width = 210 - 15 - 15
 
    # Replace smart quotes and special chars for Helvetica compatibility
    def safe(txt):
        return txt.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"').replace('\u2013', '-').replace('\u2014', '-').replace('\u2022', '-').replace('\u00e9', 'e')
 
    for i, (label, title, content, slide_type) in enumerate(slides_content, 1):
        pdf.add_page()
        if slide_type == "title":
            pdf.set_fill_color(26, 71, 42)
            pdf.rect(0, 0, 210, 297, 'F')
            pdf.set_xy(15, 60)
            pdf.set_font('helvetica', 'B', 28)
            pdf.set_text_color(201, 168, 76)
            pdf.multi_cell(w, 15, safe(label))
            pdf.set_x(15)
            pdf.set_font('helvetica', 'B', 22)
            pdf.set_text_color(255, 255, 255)
            pdf.multi_cell(w, 12, safe(title))
            pdf.ln(20)
            pdf.set_x(15)
            pdf.set_font('helvetica', '', 12)
            pdf.set_text_color(255, 255, 255)
            pdf.multi_cell(w, 6, safe(content))
        else:
            pdf.set_fill_color(250, 250, 248)
            pdf.rect(0, 0, 210, 297, 'F')
            pdf.set_xy(15, 20)
            pdf.set_font('helvetica', 'B', 16)
            pdf.set_text_color(26, 71, 42)
            pdf.cell(w, 15, safe(label), new_x="LMARGIN", new_y="NEXT")
            pdf.set_fill_color(201, 168, 76)
            pdf.rect(15, pdf.get_y(), 40, 1, 'F')
            pdf.ln(8)
            pdf.set_x(15)
            pdf.set_font('helvetica', 'B', 20)
            pdf.set_text_color(26, 71, 42)
            pdf.multi_cell(w, 12, safe(title))
            pdf.ln(10)
            pdf.set_x(15)
            pdf.set_font('helvetica', '', 11)
            pdf.set_text_color(85, 85, 85)
            pdf.multi_cell(w, 6, safe(content))
 
        pdf.set_xy(15, 280)
        pdf.set_font('helvetica', '', 9)
        pdf.set_text_color(85, 85, 85)
        pdf.cell(w / 2, 10, 'CDON - Garden & Outdoor Opportunity')
        pdf.cell(w / 2, 10, f'{i:02d}', align='R')
 
    return bytes(pdf.output())
 
st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)
col_left, col_center, col_right = st.columns([1, 2, 1])
with col_center:
    pdf_bytes = generate_pdf()
    if pdf_bytes:
        st.download_button(
            label="Download Full Report as PDF",
            data=pdf_bytes,
            file_name="CDON_Garden_Outdoor_Report.pdf",
            mime="application/pdf",
            key="pdf_download",
            use_container_width=True
        )
st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)
 
