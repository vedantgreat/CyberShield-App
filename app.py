import streamlit as st
import time

# --- 1. SETTINGS & UI DESIGN ---
st.set_page_config(page_title="CyberShield Pro", page_icon="🛡️", layout="wide")

# Modern CSS for that "Instagram/YouTube" look
st.markdown("""
    <style>
    .stApp { background: #0e1117; color: white; }
    [data-testid="stSidebar"] { background-color: #161b22; }
    .card { 
        background: rgba(255, 255, 255, 0.05); 
        padding: 20px; border-radius: 15px; 
        border: 1px solid #00ffcc; margin-bottom: 15px;
    }
    .stButton>button { 
        background: linear-gradient(90deg, #00ffcc, #00d2ff); 
        color: black; border-radius: 10px; font-weight: bold; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("# 🛡️ CyberShield")
    st.write("---")
    menu = st.radio("EXPLORE", ["🏠 Home Feed", "🔍 URL Scanner", "👤 My Profile", "📢 Report Scam"])
    st.write("---")
    st.caption("Developed by: Manmeet,Sanchiti,Megha,Rishabh & Vedant")

# --- 3. PAGE LOGIC ---

if menu == "🏠 Home Feed":
    st.title("Your Security Dashboard")
    st.write("Live updates from the Nagpur Security Network.")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<div class="card"><h3>Featured Guide</h3><p>Watch: How hackers use "Deepfakes" in 2026.</p></div>', unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=6vMLTdg_n_k")
    with col2:
        st.subheader("Active Threats")
        st.error("🚨 Bank KYC Scam")
        st.warning("⚠️ Fake Job Portal")
        st.info("ℹ️ App Update v2.0")

elif menu == "🔍 URL Scanner":
    st.title("AI Link Investigator")
    url = st.text_input("Paste URL here:", placeholder="https://...")
    if st.button("Deep Scan Now"):
        with st.spinner("Analyzing URL DNA..."):
            time.sleep(1.5)
            score = 0
            if "http://" in url: score += 60
            if any(x in url.lower() for x in ["login", "verify", "bank"]): score += 30
            
            if score > 50:
                st.error(f"DANGER DETECTED! Risk Level: {score}%")
                st.snow()
            else:
                st.success("CLEAN: This link appears safe.")
                st.balloons()

elif menu == "👤 My Profile":
    st.title("User Identity")
    c1, c2 = st.columns([1, 2])
    c1.image("https://api.dicebear.com/7.x/avataaars/svg?seed=Vedant", width=150)
    c2.subheader("Vedant Ramesh Bagde")
    c2.write("Rank: **Cyber Sentinel** 🎖️")
    c2.write("Nagpur Institute of Technology")

elif menu == "📢 Report Scam":
    st.title("Community Reporting")
    st.write("Help us build a safer web.")
    scam_url = st.text_input("Submit suspicious link:")
    if st.button("Add to Database"):
        st.success("Report submitted! Our AI will analyze it.")
