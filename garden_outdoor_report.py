import streamlit as st
import plotly.graph_objects as go
from fpdf import FPDF
from datetime import datetime
 
st.set_page_config(page_title="Garden & Outdoor: The Nordic Spring Opportunity", layout="wide", initial_sidebar_state="collapsed")
 
hide_streamlit_style = """<style>#MainMenu {display: none;}footer {display: none;}header {display: none;}</style>"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
 
global_css = """<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
* {margin: 0;padding: 0;box-sizing: border-box;}
body {background-color: #ffffff;font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;color: #555;}
.slide {width: 100%;padding: 80px;font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;}
.slide.dark-bg {background: linear-gradient(135deg, #1a472a 0%, #1e3a1e 100%);color: white;}
.slide.light-bg {background-color: #fafaf8;}
.slide.white-bg {background-color: #ffffff;}
.slide.warm-bg {background-color: #fffbf5;}
.slide-label {color: #c9a84c;font-size: 13px;letter-spacing: 3px;font-weight: 600;text-transform: uppercase;margin-bottom: 20px;}
.slide-title {color: #1a472a;font-size: 42px;font-weight: 800;line-height: 1.2;margin-bottom: 20px;}
.slide.dark-bg .slide-title {color: #ffffff;}
.gold-bar {width: 60px;height: 3px;background-color: #c9a84c;margin: 30px 0;}
.slide-description {font-size: 16px;font-weight: 400;line-height: 1.6;color: #555;max-width: 700px;margin-bottom: 30px;}
.slide.dark-bg .slide-description {color: #ffffff;opacity: 0.95;}
.slide-footer {display: flex;justify-content: space-between;align-items: center;margin-top: 60px;padding-top: 20px;border-top: 1px solid rgba(0, 0, 0, 0.1);font-size: 12px;color: #999;}
.slide.dark-bg .slide-footer {border-top-color: rgba(255, 255, 255, 0.15);color: rgba(255, 255, 255, 0.7);}
.kpi-card {border: 1px solid #e0e0e0;border-radius: 12px;padding: 30px;text-align: center;}
.kpi-value {color: #1a472a;font-size: 36px;font-weight: 800;margin-bottom: 10px;}
.kpi-label {color: #999;font-size: 11px;letter-spacing: 1.5px;text-transform: uppercase;}
.kpi-grid-2col {display: grid;grid-template-columns: 1fr 1fr;gap: 25px;margin-bottom: 30px;}
.kpi-card-country {border: none;border-bottom: 2px solid #eee;border-radius: 0;padding: 20px 0;}
.callout-box {background-color: #f0f8f4;border-radius: 12px;padding: 25px 25px 25px 40px;margin: 30px 0;position: relative;font-size: 15px;line-height: 1.6;}
.callout-icon {position: absolute;left: 15px;top: 25px;width: 20px;height: 20px;border: 2px solid #3d8b6e;border-radius: 50%;}
.callout-title {font-weight: 700;color: #1a472a;margin-bottom: 5px;}
.callout-subtitle {color: #555;font-weight: 400;font-size: 14px;}
.trending-item {color: #555;font-size: 14px;margin-bottom: 10px;}
.trending-item::before {content: "●";color: #3d8b6e;margin-right: 10px;}
.product-grid {display: grid;grid-template-columns: 1fr 1fr;gap: 20px;margin-top: 15px;}
.product-item {font-size: 13px;line-height: 1.5;}
.product-badge {display: inline-flex;align-items: center;justify-content: center;width: 24px;height: 24px;background-color: #3d8b6e;color: white;border-radius: 50%;font-size: 11px;font-weight: 700;margin-right: 10px;}
.product-name {font-weight: 700;color: #1a472a;display: inline;}
.product-desc {color: #999;font-size: 12px;display: block;}
.country-title {color: #c9a84c;font-size: 13px;letter-spacing: 3px;text-transform: uppercase;margin-bottom: 10px;font-weight: 600;}
.country-flag {margin-bottom: 20px;}
.quote {border-left: 4px solid #1a472a;padding-left: 20px;margin: 30px 0;font-style: italic;color: #1a472a;font-size: 16px;line-height: 1.6;}
.progress-bar-container {display: flex;align-items: center;gap: 15px;margin: 20px 0;font-size: 14px;}
.progress-bar {flex: 1;height: 8px;background-color: #e8e8e8;border-radius: 4px;overflow: hidden;}
.progress-fill {height: 100%;background-color: #3d8b6e;border-radius: 4px;}
.insight-card {background-color: #1a472a;border-radius: 12px;padding: 35px;color: white;}
.insight-label {color: #c9a84c;font-size: 18px;font-weight: 700;margin-bottom: 15px;}
.insight-text {font-size: 15px;line-height: 1.7;margin-bottom: 25px;}
.peak-label {color: #c9a84c;font-size: 12px;letter-spacing: 1.5px;text-transform: uppercase;margin-bottom: 5px;}
.peak-value {color: white;font-size: 28px;font-weight: 700;margin-bottom: 25px;}
.mindset-label {color: #c9a84c;font-size: 12px;letter-spacing: 1.5px;text-transform: uppercase;margin-bottom: 5px;}
.mindset-text {color: white;font-style: italic;font-size: 15px;}
.trend-card {background-color: white;border: 1px solid #e8e8e8;border-radius: 12px;padding: 30px;text-align: center;}
.trend-title {color: #1a472a;font-weight: 700;font-size: 16px;margin-bottom: 10px;}
.trend-value {color: #1a472a;font-size: 24px;font-weight: 800;margin-bottom: 10px;}
.trend-desc {color: #999;font-size: 13px;line-height: 1.5;}
.timeline {position: relative;margin: 40px 0;}
.timeline-line {height: 6px;background: linear-gradient(90deg, #c9a84c 0%, #3d8b6e 100%);border-radius: 3px;margin-bottom: 20px;}
.timeline-months {display: flex;justify-content: space-between;font-size: 12px;letter-spacing: 1px;text-transform: uppercase;margin-bottom: 30px;}
.timeline-month {color: #999;}
.timeline-month.highlight {color: #c9a84c;font-weight: 700;}
.timeline-cards {display: grid;grid-template-columns: repeat(4, 1fr);gap: 20px;}
.timeline-card {background-color: rgba(61, 139, 110, 0.15);border-left: 3px solid #3d8b6e;border-radius: 8px;padding: 20px;color: white;}
.timeline-card-month {font-weight: 700;font-size: 14px;margin-bottom: 8px;}
.timeline-card-desc {font-size: 13px;opacity: 0.9;}
.opportunity-box {background-color: #c9a84c;border-radius: 8px;padding: 20px;text-align: center;font-size: 28px;font-weight: 700;color: #1a472a;margin: 30px 0;}
.opportunity-subtext {color: #c9a84c;opacity: 0.8;font-size: 14px;font-weight: 400;margin-top: 15px;}
.checkmark-item {display: flex;align-items: flex-start;gap: 15px;margin: 20px 0;color: white;font-size: 15px;line-height: 1.6;}
.checkmark-circle {display: flex;align-items: center;justify-content: center;width: 24px;height: 24px;background-color: #c9a84c;border-radius: 50%;color: #1a472a;font-weight: 700;flex-shrink: 0;margin-top: 3px;}
.cta-text {color: #c9a84c;font-size: 20px;font-weight: 700;margin-bottom: 10px;}
.cta-subtext {color: white;font-size: 14px;}
.two-col-layout {display: flex;gap: 40px;}
.two-col-left {flex: 0 0 55%;}
.two-col-right {flex: 0 0 45%;}
.navy-card {background-color: #2a4a6f;border-radius: 12px;padding: 35px;color: white;}
.navy-title {color: #c9a84c;font-size: 18px;font-weight: 700;margin-bottom: 15px;}
.navy-value {color: #c9a84c;font-size: 42px;font-weight: 800;margin-bottom: 5px;}
.navy-desc {color: white;font-size: 14px;margin-bottom: 25px;padding-bottom: 25px;border-bottom: 1px solid rgba(255, 255, 255, 0.2);}
.navy-item {display: flex;align-items: center;gap: 12px;margin: 15px 0;font-size: 13px;}
.navy-label {color: #c9a84c;font-weight: 700;}
.navy-stat {color: white;}
.header-row {display: flex;align-items: center;gap: 25px;margin-bottom: 40px;}
.flags-row {display: flex;align-items: center;gap: 20px;}
.flag-label {color: #c9a84c;font-size: 13px;letter-spacing: 2px;text-transform: uppercase;font-weight: 600;}
.title-slide-main {color: white;font-size: 52px;font-weight: 800;line-height: 1.2;margin-bottom: 30px;max-width: 800px;}
.title-slide-desc {color: white;font-size: 17px;font-weight: 300;line-height: 1.6;max-width: 700px;margin-bottom: 40px;}
.title-slide-footer {display: flex;justify-content: space-between;align-items: center;padding-top: 20px;margin-top: 60px;border-top: 1px solid rgba(255, 255, 255, 0.15);font-size: 12px;color: rgba(255, 255, 255, 0.7);}
.divider {height: 1px;background-color: rgba(0, 0, 0, 0.1);margin: 25px 0;}
.slide.dark-bg .divider {background-color: rgba(255, 255, 255, 0.2);}
.numbered-item {margin-bottom: 25px;}
.item-number {color: #1a472a;font-weight: 700;font-size: 14px;margin-bottom: 8px;}
.item-title {font-weight: 700;color: #1a472a;display: inline;}
.item-desc {color: #999;font-size: 13px;display: inline;}
.four-card-grid {display: grid;grid-template-columns: repeat(4, 1fr);gap: 20px;margin: 30px 0;}
</style>"""
st.markdown(global_css, unsafe_allow_html=True)
 
def get_flag_svg(country, size=40):
    flags = {
        "denmark": f'<svg viewBox="0 0 60 40" width="{size}" height="{int(size*0.67)}"><rect width="60" height="40" fill="#C8102E"/><rect x="16" width="8" height="40" fill="white"/><rect y="16" width="60" height="8" fill="white"/></svg>',
        "sweden": f'<svg viewBox="0 0 60 40" width="{size}" height="{int(size*0.67)}"><rect width="60" height="40" fill="#0066B2"/><rect x="18" width="8" height="40" fill="#FFCC00"/><rect y="16" width="60" height="8" fill="#FFCC00"/></svg>',
        "norway": f'<svg viewBox="0 0 60 40" width="{size}" height="{int(size*0.67)}"><rect width="60" height="40" fill="#BA0C2F"/><rect x="16" width="8" height="40" fill="#FFFFFF"/><rect y="16" width="60" height="8" fill="#FFFFFF"/><rect x="18" width="4" height="40" fill="#00205B"/><rect y="18" width="60" height="4" fill="#00205B"/></svg>',
        "finland": f'<svg viewBox="0 0 60 40" width="{size}" height="{int(size*0.67)}"><rect width="60" height="40" fill="white"/><rect x="18" width="8" height="40" fill="#003580"/><rect y="16" width="60" height="8" fill="#003580"/></svg>',
    }
    return flags.get(country.lower(), "")
 
slide1_html = """<div class="slide dark-bg" style="padding-top: 100px; padding-bottom: 80px;">
    <div class="slide-label">CDON MARKETPLACE</div>
    <h1 class="title-slide-main">Garden & Outdoor:<br>The Nordic Spring Opportunity</h1>
    <div class="gold-bar"></div>
    <p class="title-slide-desc">A market overview for merchants looking to capture seasonal demand across Sweden, Denmark, Norway and Finland.</p>
    <div class="header-row">
        <div class="flags-row" id="flags-row"></div>
        <div class="flag-label">FOUR MARKETS · ONE PLATFORM</div>
    </div>
    <div class="title-slide-footer">
        <span>CDON - Confidential</span>
        <span>Spring/Summer 2026</span>
    </div>
</div>"""
st.markdown(slide1_html, unsafe_allow_html=True)
flags_html = f"""<script>document.getElementById('flags-row').innerHTML = `{get_flag_svg('denmark', 50)}{get_flag_svg('sweden', 50)}{get_flag_svg('norway', 50)}{get_flag_svg('finland', 50)}`;</script>"""
st.markdown(flags_html, unsafe_allow_html=True)
 
slide2_html = """<div class="slide light-bg">
    <div class="slide-label">THE MARKET</div>
    <h2 class="slide-title">Nordics: A Region That Lives Outdoors</h2>
    <div class="gold-bar"></div>
    <p class="slide-description">The Nordic region is experiencing a sustained boom in outdoor living. As spring approaches, consumers across Sweden, Denmark, Norway, and Finland actively search for garden furniture, outdoor equipment, and recreational gear. Early listing and strategic planning can capture 40% more demand.</p>
    <div class="four-card-grid">
        <div class="kpi-card"><div class="kpi-value">€2.5B+</div><div class="kpi-label">Nordic Garden Market</div></div>
        <div class="kpi-card"><div class="kpi-value">$320M</div><div class="kpi-label">Outdoor Equipment</div></div>
        <div class="kpi-card"><div class="kpi-value">25M+</div><div class="kpi-label">Consumers</div></div>
        <div class="kpi-card"><div class="kpi-value">6mo</div><div class="kpi-label">Peak Season</div></div>
    </div>
    <p style="font-size: 12px; color: #999; margin-top: 20px;">Sources: Google Trends (Nordics), Statista Garden & Outdoor 2025, Nordic E-Commerce Association</p>
    <div class="slide-footer"><span>CDON — Garden & Outdoor Opportunity</span><span>02</span></div>
</div>"""
st.markdown(slide2_html, unsafe_allow_html=True)
 
months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
values = [15, 22, 35, 58, 92, 88, 65, 48, 32, 25, 20, 18]
colors = ['#5a9a7f' if v < 70 else '#3d8b6e' if v < 85 else '#c9a84c' for v in values]
fig = go.Figure()
fig.add_trace(go.Bar(x=months, y=values, marker=dict(color=colors), showlegend=False, hoverinfo='skip'))
fig.add_annotation(x='MAY', y=92, text='▲ Peak', showarrow=False, yshift=10, font=dict(size=12, color='#c9a84c', family='Inter'))
fig.add_annotation(x='JUN', y=88, text='▲ Peak', showarrow=False, yshift=10, font=dict(size=12, color='#c9a84c', family='Inter'))
fig.update_layout(xaxis=dict(showgrid=False, zeroline=False, showline=False, tickfont=dict(family='Inter', size=11, color='#999')), yaxis=dict(showgrid=False, zeroline=False, showline=False, visible=False), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=40, b=30, l=0, r=0), height=300)
 
slide3_html = """<div class="slide light-bg">
    <div class="slide-label">SEASONALITY</div>
    <h2 class="slide-title">The Spring Spike Is Real</h2>
    <div class="gold-bar"></div>
    <p class="slide-description">Garden and outdoor product searches spike dramatically during spring across all Nordic markets. March through June is the critical window where early listing captures maximum visibility and traffic.</p>"""
st.markdown(slide3_html, unsafe_allow_html=True)
col1, col2, col3 = st.columns([0.05, 0.9, 0.05])
with col2:
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
 
slide3b_html = """<div class="slide light-bg" style="padding-top: 0; padding-bottom: 40px;">
    <div style="text-align: center; font-size: 13px; color: #999; margin-bottom: 30px;">Garden & Outdoor Search Interest (Google Trends, Nordics)</div>
    <div class="callout-box"><div class="callout-icon"></div><div class="callout-title">Merchants who list by March capture 40% more of the spring demand curve</div><div class="callout-subtitle">Early listing = better search ranking = more visibility during peak</div></div>
    <div class="slide-footer"><span>CDON — Seasonality Insights</span><span>03</span></div>
</div>"""
st.markdown(slide3b_html, unsafe_allow_html=True)
 
slide4_html = """<div class="slide dark-bg">
    <div class="slide-label">THE SPRING WAVE</div>
    <h2 style="color: white; font-size: 42px; font-weight: 800; line-height: 1.2; margin-bottom: 20px;">One Season. Four Markets.<br>Four Launch Windows.</h2>
    <div class="gold-bar"></div>
    <p class="slide-description">Each Nordic market has its own spring rhythm. Denmark kicks off in late February, followed by Sweden in March, and Norway and Finland peak in April-May. Merchants who understand these waves can extend their peak season from March all the way through July.</p>
    <div class="timeline"><div class="timeline-line"></div>
    <div class="timeline-months"><span class="timeline-month">JAN</span><span class="timeline-month">FEB</span><span class="timeline-month highlight">MAR</span><span class="timeline-month highlight">APR</span><span class="timeline-month highlight">MAY</span><span class="timeline-month highlight">JUN</span><span class="timeline-month">JUL</span><span class="timeline-month">AUG</span></div></div>
    <div class="timeline-cards">
        <div class="timeline-card"><div class="timeline-card-month">March-April</div><div class="timeline-card-desc">First movers</div></div>
        <div class="timeline-card"><div class="timeline-card-month">April-May</div><div class="timeline-card-desc">Main wave</div></div>
        <div class="timeline-card"><div class="timeline-card-month">April-June</div><div class="timeline-card-desc">Outdoor season</div></div>
        <div class="timeline-card"><div class="timeline-card-month">May-July</div><div class="timeline-card-desc">Mökki season</div></div>
    </div>
    <div class="slide-footer"><span>CDON — The Spring Wave</span><span>04</span></div>
</div>"""
st.markdown(slide4_html, unsafe_allow_html=True)
 
slide5_html = f"""<div class="slide white-bg">
    <div class="country-title">DENMARK</div>
    <div class="two-col-layout">
        <div class="two-col-left">
            <div class="country-flag">{get_flag_svg('denmark', 70)}</div>
            <div style="color: #c9a84c; font-size: 13px; letter-spacing: 3px; text-transform: uppercase; font-weight: 600; margin-bottom: 10px;">Denmark</div>
            <h2 class="slide-title" style="font-size: 42px; margin-bottom: 20px;">The First Movers</h2>
            <div class="gold-bar"></div>
            <p class="slide-description" style="color: #555; font-size: 15px;">Denmark enjoys the earliest spring in the Nordics, with consumer search interest peaking <strong>3-4 weeks ahead of Sweden</strong>. Danish shoppers start browsing garden products as early as late February, making it the market where early listing pays off the most.</p>
            <div class="quote">"Danes kick off the Nordic buying wave. If you're listed by March, you're ahead of the curve."</div>
        </div>
        <div class="two-col-right">
            <div class="kpi-grid-2col">
                <div class="kpi-card kpi-card-country"><div class="kpi-value">Mar-Apr</div><div class="kpi-label">Peak Garden Season</div></div>
                <div class="kpi-card kpi-card-country"><div class="kpi-value">3-4 wks</div><div class="kpi-label">Ahead of Sweden</div></div>
                <div class="kpi-card kpi-card-country"><div class="kpi-value">High</div><div class="kpi-label">E-Commerce Maturity</div></div>
                <div class="kpi-card kpi-card-country"><div class="kpi-value">Strong</div><div class="kpi-label">Outdoor Cooking Trend</div></div>
            </div>
            <div style="margin-top: 30px;"><div style="color: #1a472a; font-size: 16px; font-weight: 700; margin-bottom: 15px;">Trending Categories</div>
                <div class="trending-item">Garden furniture & outdoor living spaces</div>
                <div class="trending-item">Outdoor cooking & BBQ equipment</div>
                <div class="trending-item">Greenhouses & raised beds</div>
                <div class="trending-item">Balcony & small-space gardening</div>
                <div class="trending-item">Pool & spa products (strong May surge)</div>
            </div>
            <div style="margin-top: 30px;"><div style="color: #1a472a; font-size: 12px; letter-spacing: 2px; text-transform: uppercase; font-weight: 700; margin-bottom: 15px; padding-bottom: 10px; border-bottom: 1px solid #3d8b6e;">TOP 10 TRENDING PRODUCTS</div>
                <div class="product-grid">
                    <div class="product-item"><span class="product-badge">1</span><span class="product-name">Cane-line Moments Sofa</span><span class="product-desc">Premium outdoor seating</span></div>
                    <div class="product-item"><span class="product-badge">2</span><span class="product-name">Weber Spirit E-325</span><span class="product-desc">Best-selling gas grill</span></div>
                    <div class="product-item"><span class="product-badge">3</span><span class="product-name">Juliana Grand Oase</span><span class="product-desc">Danish-designed glass greenhouse</span></div>
                    <div class="product-item"><span class="product-badge">4</span><span class="product-name">Ooni Karu 16 Pizza Oven</span><span class="product-desc">Multi-fuel outdoor cooking</span></div>
                    <div class="product-item"><span class="product-badge">5</span><span class="product-name">Gardena SILENO City 600</span><span class="product-desc">Entry-level robot mower</span></div>
                    <div class="product-item"><span class="product-badge">6</span><span class="product-name">Houe Click Dining Set</span><span class="product-desc">Scandinavian design outdoor</span></div>
                    <div class="product-item"><span class="product-badge">7</span><span class="product-name">Kamado Joe Classic III</span><span class="product-desc">Premium ceramic grill</span></div>
                    <div class="product-item"><span class="product-badge">8</span><span class="product-name">SACKit Cobana Lounge</span><span class="product-desc">Danish outdoor lounge furniture</span></div>
                    <div class="product-item"><span class="product-badge">9</span><span class="product-name">Palram Hybrid Greenhouse</span><span class="product-desc">Polycarbonate raised bed combo</span></div>
                    <div class="product-item"><span class="product-badge">10</span><span class="product-name">Skagerak Riviera Sun Lounger</span><span class="product-desc">Teak outdoor furniture</span></div>
                </div>
            </div>
        </div>
    </div>
    <div class="slide-footer"><span>CDON — Denmark Market Spotlight</span><span>05</span></div>
</div>"""
st.markdown(slide5_html, unsafe_allow_html=True)
 
slide6_html = f"""<div class="slide white-bg">
    <div class="country-title">SWEDEN</div>
    <div class="two-col-layout">
        <div class="two-col-left">
            <div class="country-flag">{get_flag_svg('sweden', 70)}</div>
            <div style="color: #c9a84c; font-size: 13px; letter-spacing: 3px; text-transform: uppercase; font-weight: 600; margin-bottom: 10px;">Sweden</div>
            <h2 class="slide-title" style="font-size: 42px; margin-bottom: 20px;">The Main Wave</h2>
            <div class="gold-bar"></div>
            <p class="slide-description" style="color: #555; font-size: 15px;">Sweden is the <strong>largest Nordic garden market by volume</strong>, with a concentrated peak in April-May. Swedish consumers invest heavily in their outdoor spaces, driving strong demand for both garden maintenance and outdoor living products.</p>
            <div class="quote">"Sweden's garden market is the Nordic powerhouse. Robot mowers alone are growing over 20% annually."</div>
        </div>
        <div class="two-col-right">
            <div class="kpi-grid-2col">
                <div class="kpi-card kpi-card-country"><div class="kpi-value">Apr-May</div><div class="kpi-label">Peak Garden Season</div></div>
                <div class="kpi-card kpi-card-country"><div class="kpi-value">22.5%</div><div class="kpi-label">Robot Mower CAGR</div></div>
                <div class="kpi-card kpi-card-country"><div class="kpi-value">14.1%</div><div class="kpi-label">Electric Tools CAGR</div></div>
                <div class="kpi-card kpi-card-country"><div class="kpi-value">#1</div><div class="kpi-label">Nordic Garden Market</div></div>
            </div>
            <div style="margin-top: 30px;"><div style="color: #1a472a; font-size: 16px; font-weight: 700; margin-bottom: 15px;">Trending Categories</div>
                <div class="trending-item">Robot mowers & smart garden tech</div>
                <div class="trending-item">Electric garden tools (replacing gas)</div>
                <div class="trending-item">Outdoor furniture & lounge sets</div>
                <div class="trending-item">Cultivation, growing & greenhouse</div>
                <div class="trending-item">Garden lighting & irrigation systems</div>
            </div>
            <div style="margin-top: 30px;"><div style="color: #1a472a; font-size: 12px; letter-spacing: 2px; text-transform: uppercase; font-weight: 700; margin-bottom: 15px; padding-bottom: 10px; border-bottom: 1px solid #3d8b6e;">TOP 10 TRENDING PRODUCTS</div>
                <div class="product-grid">
                    <div class="product-item"><span class="product-badge">1</span><span class="product-name">Husqvarna Automower 450X</span><span class="product-desc">AI-vision wire-free robot mower</span></div>
                    <div class="product-item"><span class="product-badge">2</span><span class="product-name">Gardena SILENO Life 1500</span><span class="product-desc">Mid-range robot mower</span></div>
                    <div class="product-item"><span class="product-badge">3</span><span class="product-name">STIHL HSA 60 Hedge Trimmer</span><span class="product-desc">Battery-powered, top-rated</span></div>
                    <div class="product-item"><span class="product-badge">4</span><span class="product-name">Sweden Greenhouse Classic</span><span class="product-desc">Freestanding glass greenhouse</span></div>
                    <div class="product-item"><span class="product-badge">5</span><span class="product-name">Brafab Sottenville Lounge</span><span class="product-desc">Swedish outdoor furniture brand</span></div>
                    <div class="product-item"><span class="product-badge">6</span><span class="product-name">Einhell GE-CM 36 Li Mower</span><span class="product-desc">Cordless electric lawn mower</span></div>
                    <div class="product-item"><span class="product-badge">7</span><span class="product-name">Halsing Outdoor Kitchen</span><span class="product-desc">Swedish modular outdoor kitchens</span></div>
                    <div class="product-item"><span class="product-badge">8</span><span class="product-name">Gardena Smart Water Control</span><span class="product-desc">Smart irrigation system</span></div>
                    <div class="product-item"><span class="product-badge">9</span><span class="product-name">Inflatable SUP Boards</span><span class="product-desc">All-round paddleboard kits</span></div>
                    <div class="product-item"><span class="product-badge">10</span><span class="product-name">Skargards Wood-Fired Hot Tub</span><span class="product-desc">Swedish-designed outdoor hot tubs</span></div>
                </div>
            </div>
        </div>
    </div>
    <div class="slide-footer"><span>CDON — Sweden Market Spotlight</span><span>06</span></div>
</div>"""
st.markdown(slide6_html, unsafe_allow_html=True)
 
slide7_html = f"""<div class="slide white-bg">
    <div class="country-title">NORWAY</div>
    <div class="two-col-layout">
        <div class="two-col-left">
            <div class="country-flag">{get_flag_svg('norway', 70)}</div>
            <div style="color: #c9a84c; font-size: 13px; letter-spacing: 3px; text-transform: uppercase; font-weight: 600; margin-bottom: 10px;">Norway</div>
            <h2 class="slide-title" style="font-size: 42px; margin-bottom: 20px;">The Outdoor Nation</h2>
            <div class="gold-bar"></div>
            <p class="slide-description" style="color: #555; font-size: 15px;">Outdoor life is in Norway's DNA. With <strong>77% of the population engaging in weekly outdoor activities</strong>, Norwegian consumers are premium-oriented buyers with the <strong>highest average order values</strong> in the Nordics for outdoor gear.</p>
            <div class="quote">2025 was declared Norway's "Year of Outdoor." The momentum hasn't slowed.</div>
        </div>
        <div class="two-col-right">
            <div class="kpi-grid-2col">
                <div class="kpi-card kpi-card-country"><div class="kpi-value">77%</div><div class="kpi-label">Weekly Outdoor Activity</div></div>
                <div class="kpi-card kpi-card-country"><div class="kpi-value">Highest</div><div class="kpi-label">Average Order Value</div></div>
                <div class="kpi-card kpi-card-country"><div class="kpi-value">Apr-Jun</div><div class="kpi-label">Peak Season</div></div>
                <div class="kpi-card kpi-card-country"><div class="kpi-value">Premium</div><div class="kpi-label">Consumer Orientation</div></div>
            </div>
            <div style="margin-top: 30px;"><div style="color: #1a472a; font-size: 16px; font-weight: 700; margin-bottom: 15px;">Trending Categories</div>
                <div class="trending-item">Hiking & camping equipment (tents, sleeping gear)</div>
                <div class="trending-item">Outdoor furniture for terraces & cabins</div>
                <div class="trending-item">Fishing gear & accessories</div>
                <div class="trending-item">SUP boards & water sports (7-10% CAGR)</div>
                <div class="trending-item">Premium outdoor cooking & fire pits</div>
            </div>
            <div style="margin-top: 30px;"><div style="color: #1a472a; font-size: 12px; letter-spacing: 2px; text-transform: uppercase; font-weight: 700; margin-bottom: 15px; padding-bottom: 10px; border-bottom: 1px solid #3d8b6e;">TOP 10 TRENDING PRODUCTS</div>
                <div class="product-grid">
                    <div class="product-item"><span class="product-badge">1</span><span class="product-name">Hilleberg Anjan 2 Tent</span><span class="product-desc">Premium lightweight hiking tent</span></div>
                    <div class="product-item"><span class="product-badge">2</span><span class="product-name">Norrona Trollveggen Shell</span><span class="product-desc">Norwegian all-weather outerwear</span></div>
                    <div class="product-item"><span class="product-badge">3</span><span class="product-name">Red Paddle Co Sport 11'3</span><span class="product-desc">Top-rated inflatable SUP</span></div>
                    <div class="product-item"><span class="product-badge">4</span><span class="product-name">Weber Genesis E-435</span><span class="product-desc">Premium 4-burner gas grill</span></div>
                    <div class="product-item"><span class="product-badge">5</span><span class="product-name">Husqvarna Automower 320 NERA</span><span class="product-desc">Wire-free robot mower, mid-range</span></div>
                    <div class="product-item"><span class="product-badge">6</span><span class="product-name">Fiskars X27 Super Splitting Axe</span><span class="product-desc">Cabin & firewood essential</span></div>
                    <div class="product-item"><span class="product-badge">7</span><span class="product-name">Helinox Chair One</span><span class="product-desc">Ultralight camping chair</span></div>
                    <div class="product-item"><span class="product-badge">8</span><span class="product-name">Abu Garcia Revo Beast X</span><span class="product-desc">Premium baitcasting reel</span></div>
                    <div class="product-item"><span class="product-badge">9</span><span class="product-name">Ooni Volt 12 Electric Oven</span><span class="product-desc">Indoor/outdoor pizza oven</span></div>
                    <div class="product-item"><span class="product-badge">10</span><span class="product-name">Garmin inReach Mini 2</span><span class="product-desc">Satellite communicator for hiking</span></div>
                </div>
            </div>
        </div>
    </div>
    <div class="slide-footer"><span>CDON — Norway Market Spotlight</span><span>07</span></div>
</div>"""
st.markdown(slide7_html, unsafe_allow_html=True)
 
slide8_html = f"""<div class="slide white-bg">
    <div class="country-title">FINLAND</div>
    <div class="two-col-layout">
        <div class="two-col-left">
            <div class="country-flag">{get_flag_svg('finland', 70)}</div>
            <div style="color: #c9a84c; font-size: 13px; letter-spacing: 3px; text-transform: uppercase; font-weight: 600; margin-bottom: 10px;">Finland</div>
            <h2 class="slide-title" style="font-size: 42px; margin-bottom: 20px;">Mökki & Nature</h2>
            <div class="gold-bar"></div>
            <p class="slide-description" style="color: #555; font-size: 15px;">Finland's later spring (May-June) extends the selling season, and the iconic <strong>summer cottage (mökki) culture</strong> drives massive demand for outdoor and garden products. With <strong>1.5 million fishers</strong> (27% of the population), outdoor recreation is deeply embedded in Finnish life.</p>
            <div class="quote">"Finland's mökki culture means every family needs garden and outdoor gear - twice."</div>
        </div>
        <div class="two-col-right">
            <div class="kpi-grid-2col">
                <div class="kpi-card kpi-card-country"><div class="kpi-value">1.5M</div><div class="kpi-label">Active Fishers</div></div>
                <div class="kpi-card kpi-card-country"><div class="kpi-value">27%</div><div class="kpi-label">Population Fishing</div></div>
                <div class="kpi-card kpi-card-country"><div class="kpi-value">May-Jul</div><div class="kpi-label">Peak Season</div></div>
                <div class="kpi-card kpi-card-country"><div class="kpi-value">Top</div><div class="kpi-label">Camping Spend/Capita</div></div>
            </div>
            <div style="margin-top: 30px;"><div style="color: #1a472a; font-size: 16px; font-weight: 700; margin-bottom: 15px;">Trending Categories</div>
                <div class="trending-item">Fishing gear & tackle (massive domestic demand)</div>
                <div class="trending-item">Sauna & outdoor wellness products</div>
                <div class="trending-item">Camping equipment (highest per-capita spend)</div>
                <div class="trending-item">Garden tools & mökki maintenance</div>
                <div class="trending-item">Outdoor furniture & garden decor</div>
            </div>
            <div style="margin-top: 30px;"><div style="color: #1a472a; font-size: 12px; letter-spacing: 2px; text-transform: uppercase; font-weight: 700; margin-bottom: 15px; padding-bottom: 10px; border-bottom: 1px solid #3d8b6e;">TOP 10 TRENDING PRODUCTS</div>
                <div class="product-grid">
                    <div class="product-item"><span class="product-badge">1</span><span class="product-name">Kirami FinVision Sauna</span><span class="product-desc">Energy-efficient outdoor sauna</span></div>
                    <div class="product-item"><span class="product-badge">2</span><span class="product-name">Muurikka Electric Smoker</span><span class="product-desc">Finnish outdoor cooking staple</span></div>
                    <div class="product-item"><span class="product-badge">3</span><span class="product-name">Fiskars Norden N12 Axe</span><span class="product-desc">Premium Finnish forged axe</span></div>
                    <div class="product-item"><span class="product-badge">4</span><span class="product-name">Rapala X-Rap Fishing Lures</span><span class="product-desc">Iconic Finnish tackle brand</span></div>
                    <div class="product-item"><span class="product-badge">5</span><span class="product-name">Husqvarna Automower 405X</span><span class="product-desc">Wireless robot mower for cottages</span></div>
                    <div class="product-item"><span class="product-badge">6</span><span class="product-name">Savotta Hiisi 20 Backpack</span><span class="product-desc">Finnish military-grade daypack</span></div>
                    <div class="product-item"><span class="product-badge">7</span><span class="product-name">HAY Palissade Outdoor Table</span><span class="product-desc">Minimalist Nordic garden furniture</span></div>
                    <div class="product-item"><span class="product-badge">8</span><span class="product-name">Kirami Wood-Fired Hot Tub</span><span class="product-desc">Traditional Finnish outdoor tub</span></div>
                    <div class="product-item"><span class="product-badge">9</span><span class="product-name">Shimano Stradic FL Reel</span><span class="product-desc">Popular spinning reel for pike</span></div>
                    <div class="product-item"><span class="product-badge">10</span><span class="product-name">MSR Hubba Hubba NX Tent</span><span class="product-desc">Bestselling 2-person hiking tent</span></div>
                </div>
            </div>
        </div>
    </div>
    <div class="slide-footer"><span>CDON — Finland Market Spotlight</span><span>08</span></div>
</div>"""
st.markdown(slide8_html, unsafe_allow_html=True)
 
slide9_html = """<div class="slide warm-bg">
    <div class="slide-label">CONSUMER TRENDS</div>
    <h2 class="slide-title">What Nordic Consumers Are Searching For</h2>
    <div class="gold-bar"></div>
    <p class="slide-description">Search interest and category growth across the Nordic region show clear patterns. These six categories represent the biggest opportunities for spring 2026.</p>
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin: 30px 0;">
        <div class="trend-card"><div class="trend-title">Robot Mowers</div><div class="trend-value">22.5%</div><div class="trend-desc">CAGR</div><div style="font-size: 12px; color: #999; margin-top: 10px;">Premium segment with strong Nordic adoption · Peak: April-May</div></div>
        <div class="trend-card"><div class="trend-title">Garden Furniture</div><div class="trend-value">Consistent</div><div style="font-size: 12px; color: #999; margin-top: 10px;">Largest subcategory by search volume · Peak: March-June</div></div>
        <div class="trend-card"><div class="trend-title">SUP / Paddleboards</div><div class="trend-value">7-10%</div><div class="trend-desc">CAGR</div><div style="font-size: 12px; color: #999; margin-top: 10px;">Fastest growing outdoor category · Peak: May-July</div></div>
        <div class="trend-card"><div class="trend-title">Camping Equipment</div><div class="trend-value">4-6%</div><div class="trend-desc">CAGR</div><div style="font-size: 12px; color: #999; margin-top: 10px;">Sustained post-COVID demand · Peak: June-July</div></div>
        <div class="trend-card"><div class="trend-title">Outdoor Cooking</div><div class="trend-value">5-7%</div><div class="trend-desc">CAGR</div><div style="font-size: 12px; color: #999; margin-top: 10px;">Social outdoor living trend · Peak: April-August</div></div>
        <div class="trend-card"><div class="trend-title">Electric Garden Tools</div><div class="trend-value">14.1%</div><div class="trend-desc">CAGR</div><div style="font-size: 12px; color: #999; margin-top: 10px;">Replacing gas-powered tools · Peak: April-May</div></div>
    </div>
    <p style="font-size: 12px; color: #999; margin-top: 20px;">Sources: Google Trends (Nordics), Statista Growth Rates 2024-2026, Nordic E-Commerce Association</p>
    <div class="slide-footer"><span>CDON — Consumer Trends</span><span>09</span></div>
</div>"""
st.markdown(slide9_html, unsafe_allow_html=True)
 
slide10_html = """<div class="slide white-bg">
    <div class="slide-label">CATEGORY SPOTLIGHT</div>
    <div class="two-col-layout">
        <div class="two-col-left">
            <h2 class="slide-title" style="font-size: 52px;">Garden</h2>
            <div class="gold-bar"></div>
            <p class="slide-description">The garden category spans everything from outdoor furniture to irrigation systems. Consumers are upgrading their outdoor spaces into extensions of their living rooms - creating demand across a wide product range.</p>
            <div style="margin-top: 30px;">
                <div class="numbered-item"><div class="item-number">01</div><div class="item-title">Outdoor Furniture</div><div class="item-desc" style="display: block;">Lounge sets, dining tables, parasols, garden sofas</div><div class="progress-bar-container" style="margin-left: 0;"><div style="flex: 1;"><div class="progress-bar"><div class="progress-fill" style="width: 95%;"></div></div></div></div></div>
                <div class="numbered-item"><div class="item-number">02</div><div class="item-title">Garden Tools & Machines</div><div class="item-desc" style="display: block;">Robot mowers, trimmers, electric saws, rakes</div><div class="progress-bar-container" style="margin-left: 0;"><div style="flex: 1;"><div class="progress-bar"><div class="progress-fill" style="width: 75%;"></div></div></div></div></div>
                <div class="numbered-item"><div class="item-number">03</div><div class="item-title">Cultivation & Growing</div><div class="item-desc" style="display: block;">Greenhouses, raised beds, pots, seeds, soil</div><div class="progress-bar-container" style="margin-left: 0;"><div style="flex: 1;"><div class="progress-bar"><div class="progress-fill" style="width: 60%;"></div></div></div></div></div>
                <div class="numbered-item"><div class="item-number">04</div><div class="item-title">Pool & Spa</div><div class="item-desc" style="display: block;">Above-ground pools, hot tubs, accessories</div><div class="progress-bar-container" style="margin-left: 0;"><div style="flex: 1;"><div class="progress-bar"><div class="progress-fill" style="width: 85%;"></div></div></div></div></div>
                <div class="numbered-item"><div class="item-number">05</div><div class="item-title">Outdoor Cooking</div><div class="item-desc" style="display: block;">Grills, smokers, pizza ovens, fire pits</div><div class="progress-bar-container" style="margin-left: 0;"><div style="flex: 1;"><div class="progress-bar"><div class="progress-fill" style="width: 90%;"></div></div></div></div></div>
            </div>
        </div>
        <div class="two-col-right">
            <div class="insight-card"><div class="insight-label">Key Insight</div><div class="insight-text">The "outdoor living room" trend is transforming Nordic gardens. Consumers now invest in complete outdoor setups - furniture, lighting, cooking, and entertainment.</div><div style="margin-bottom: 25px;"><div class="peak-label">Peak Season</div><div class="peak-value">March → June</div></div><div><div class="mindset-label">Consumer Mindset</div><div class="mindset-text">"Invest in quality for the summer"</div></div></div>
        </div>
    </div>
    <div class="slide-footer"><span>CDON — Garden Category Spotlight</span><span>10</span></div>
</div>"""
st.markdown(slide10_html, unsafe_allow_html=True)
 
slide11_html = f"""<div class="slide white-bg">
    <div class="slide-label">CATEGORY SPOTLIGHT</div>
    <div class="two-col-layout">
        <div class="two-col-left">
            <h2 class="slide-title" style="font-size: 52px;">Outdoor & Adventure</h2>
            <div class="gold-bar"></div>
            <p class="slide-description">The Nordic outdoor equipment market is valued at over <strong>$310-320 million</strong>. From hiking the Norwegian fjords to fishing in Finnish lakes, outdoor recreation isn't a hobby - it's a way of life.</p>
            <div style="margin-top: 30px;">
                <div class="numbered-item"><div class="item-number">01</div><div class="item-title">Camping & Hiking</div><div class="item-desc" style="display: block;">Tents, sleeping bags, backpacks, camping furniture</div><div class="progress-bar-container" style="margin-left: 0;"><div style="flex: 1;"><div class="progress-bar"><div class="progress-fill" style="width: 80%; background-color: #c9a84c;"></div></div></div></div></div>
                <div class="numbered-item"><div class="item-number">02</div><div class="item-title">Fishing</div><div class="item-desc" style="display: block;">Rods, reels, tackle, waders, boats & accessories</div><div class="progress-bar-container" style="margin-left: 0;"><div style="flex: 1;"><div class="progress-bar"><div class="progress-fill" style="width: 70%; background-color: #c9a84c;"></div></div></div></div></div>
                <div class="numbered-item"><div class="item-number">03</div><div class="item-title">Water Sports</div><div class="item-desc" style="display: block;">SUP boards, kayaks, wetsuits, life jackets</div><div class="progress-bar-container" style="margin-left: 0;"><div style="flex: 1;"><div class="progress-bar"><div class="progress-fill" style="width: 55%; background-color: #c9a84c;"></div></div></div></div></div>
                <div class="numbered-item"><div class="item-number">04</div><div class="item-title">Hunting & Optics</div><div class="item-desc" style="display: block;">Hunting gear, binoculars, knives, outdoor tools</div><div class="progress-bar-container" style="margin-left: 0;"><div style="flex: 1;"><div class="progress-bar"><div class="progress-fill" style="width: 45%; background-color: #c9a84c;"></div></div></div></div></div>
            </div>
        </div>
        <div class="two-col-right">
            <div class="navy-card"><div class="navy-title">Market Context</div><div class="navy-value">$310-320M</div><div class="navy-desc">Nordic outdoor equipment market</div>
                <div class="navy-item"><div style="width: 35px; height: auto; flex-shrink: 0;">{get_flag_svg('norway', 30)}</div><div><span class="navy-label">Norway:</span><span class="navy-stat">77% weekly nature participation</span></div></div>
                <div class="navy-item"><div style="width: 35px; height: auto; flex-shrink: 0;">{get_flag_svg('finland', 30)}</div><div><span class="navy-label">Finland:</span><span class="navy-stat">1.5M fishers, 27% of population</span></div></div>
                <div class="navy-item"><div style="width: 35px; height: auto; flex-shrink: 0;">{get_flag_svg('sweden', 30)}</div><div><span class="navy-label">Sweden:</span><span class="navy-stat">Largest camping equipment market</span></div></div>
                <div class="navy-item"><div style="width: 35px; height: auto; flex-shrink: 0;">{get_flag_svg('denmark', 30)}</div><div><span class="navy-label">Denmark:</span><span class="navy-stat">Strong watersports adoption</span></div></div>
            </div>
        </div>
    </div>
    <div class="slide-footer"><span>CDON — Outdoor & Adventure Category Spotlight</span><span>11</span></div>
</div>"""
st.markdown(slide11_html, unsafe_allow_html=True)
 
slide12_html = """<div class="slide dark-bg">
    <div class="slide-label">YOUR OPPORTUNITY</div>
    <h2 style="color: white; font-size: 42px; font-weight: 800; line-height: 1.2; margin-bottom: 20px;">4 Markets. 25M+ Consumers.<br>One Platform.</h2>
    <div class="gold-bar"></div>
    <div class="opportunity-box">DK → SE → NO → FI</div>
    <div class="opportunity-subtext">The spring wave — March through July</div>
    <div class="divider"></div>
    <div style="margin: 30px 0;">
        <div class="checkmark-item"><div class="checkmark-circle">✓</div><div>List your products before March to capture Denmark's early wave</div></div>
        <div class="checkmark-item"><div class="checkmark-circle">✓</div><div>Reach all four Nordic markets from a single platform</div></div>
        <div class="checkmark-item"><div class="checkmark-circle">✓</div><div>Tap into consumers actively searching for your products</div></div>
        <div class="checkmark-item"><div class="checkmark-circle">✓</div><div>Benefit from growing categories: robot mowers, SUP, outdoor cooking & more</div></div>
    </div>
    <div class="divider"></div>
    <div style="text-align: center; margin-top: 40px;"><div class="cta-text">Ready to grow with us?</div><div class="cta-subtext">Contact your CDON Merchant Success Manager to get started</div></div>
    <div class="slide-footer"><span>CDON - Confidential</span><span style="font-size: 24px; font-weight: 700; color: #c9a84c;">CDON</span></div>
</div>"""
st.markdown(slide12_html, unsafe_allow_html=True)
 
def generate_pdf():
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()
    pdf.set_margins(15, 15, 15)
    pdf.set_fill_color(26, 71, 42)
    pdf.rect(0, 0, 210, 297, 'F')
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 12)
    pdf.text(15, 40, "CDON MARKETPLACE")
    pdf.set_xy(15, 50)
    pdf.set_font("Helvetica", "B", 32)
    pdf.multi_cell(180, 15, "Garden & Outdoor: The Nordic Spring Opportunity", align='L')
    pdf.set_x(15)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(180, 6, "A market overview for merchants looking to capture seasonal demand across Sweden, Denmark, Norway and Finland.", align='L')
    pdf.text(15, 270, "CDON - Confidential")
    pdf.text(170, 270, "Spring/Summer 2026")
    for i in range(2, 13):
        pdf.add_page()
        pdf.set_fill_color(250, 250, 248)
        pdf.rect(0, 0, 210, 297, 'F')
        pdf.set_text_color(26, 71, 42)
        pdf.set_font("Helvetica", "B", 24)
        pdf.text(15, 30, f"Slide {i}")
        pdf.set_font("Helvetica", "", 9)
        pdf.text(15, 280, "CDON - Garden & Outdoor Report")
        pdf.text(175, 280, f"{i:02d}")
    return bytes(pdf.output())
 
st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    pdf_bytes = generate_pdf()
    st.download_button(label="📥 Download Full Report (PDF)", data=pdf_bytes, file_name=f"CDON_Garden_Outdoor_Opportunity_{datetime.now().strftime('%Y%m%d')}.pdf", mime="application/pdf", use_container_width=True)
st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)
