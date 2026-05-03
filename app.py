import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import pickle
import time
import plotly.express as px
from emotion import detect_emotion
from chatbot import get_response

# --- PAGE CONFIG ---
st.set_page_config(page_title="MindSync AI", layout="wide", initial_sidebar_state="collapsed")

# --- LOAD ML MODEL ---
try:
    model = pickle.load(open("model.pkl", "rb"))
except FileNotFoundError:
    st.error("Model file not found.")

# --- SESSION STATE FOR LOGIN & THEME ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# --- DYNAMIC THEME CSS ---
bg_color = "#0E1117" if "theme" not in st.session_state or st.session_state.theme == "Dark" else "#FFFFFF"
text_color = "white" if bg_color == "#0E1117" else "black"

st.markdown(f"""
    <style>
    .stApp {{ background-color: {bg_color}; color: {text_color}; }}
    .stButton>button {{ width: 100%; border-radius: 20px; height: 3em; background: linear-gradient(45deg, #4CAF50, #2E7D32); color: white; border:none; }}
    div[data-testid="stExpander"] {{ position: fixed; bottom: 20px; right: 20px; width: 350px; z-index: 1000; background-color: #1E1E1E; border-radius: 15px; }}
    </style>
    """, unsafe_allow_html=True)

# --- TOP NAVIGATION BAR ---
selected = option_menu(
    menu_title=None,
    options=["Home", "My Dashboard", "Stress Engine", "Focus & Vent", "Auth"],
    icons=["house", "person-badge", "cpu", "Interactivity", "shield-lock"],
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#1E1E1E"},
        "nav-link-selected": {"background-color": "#4CAF50"},
    }
)

# --- SIDEBAR (Settings & Theme) ---
with st.sidebar:
    st.title("Settings")
    theme_choice = st.radio("Choose Theme", ["Dark", "Light"])
    st.session_state.theme = theme_choice
    if st.session_state.logged_in:
        st.success(f"Welcome, {st.session_state.user_name}!")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

# ----------------- PAGE: AUTH (Login/Signup) -----------------
if selected == "Auth":
    st.title("🔐 Access Portal")
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    
    with tab1:
        u_email = st.text_input("Email", key="login_email")
        u_pass = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            st.session_state.logged_in = True
            st.session_state.user_name = u_email.split('@')[0]
            st.success("Welcome back!")
            st.rerun()

    with tab2:
        st.text_input("Full Name")
        st.text_input("New Email")
        st.text_input("Set Password", type="password")
        if st.button("Create Account"):
            st.balloons()
            st.info("Account created! Please login.")

# ----------------- PAGE: HOME -----------------
elif selected == "Home":
    st.title("🌍 MindSync Global Insights")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📊 Stressors in India")
        india_data = pd.DataFrame({"Source": ["Academic", "Career", "Social", "Family"], "Percentage": [45, 25, 15, 15]})
        st.plotly_chart(px.bar(india_data, x="Source", y="Percentage", color="Source", template="plotly_dark"), use_container_width=True)
    with c2:
        st.subheader("📈 Global Trend")
        world_data = pd.DataFrame({"Year": [2020, 2022, 2024, 2026], "Index": [72, 78, 85, 89]})
        st.plotly_chart(px.line(world_data, x="Year", y="Index", markers=True, template="plotly_dark"), use_container_width=True)

# ----------------- PAGE: MY DASHBOARD -----------------
elif selected == "My Dashboard":
    if not st.session_state.logged_in:
        st.warning("Please Login first to see your dashboard.")
    else:
        st.title(f"👋 Hello, {st.session_state.user_name}!")
        col1, col2, col3 = st.columns(3)
        col1.metric("Mental Health Score", "85/100", "+2%")
        col2.metric("Focus Streak", "12 Days", "🔥")
        col3.metric("Last Detection", "Medium Stress", "3 days ago")
        
        st.subheader("Your Progress")
        chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Stress', 'Happiness'])
        st.area_chart(chart_data)

# ----------------- PAGE: STRESS ENGINE (AI Logic) -----------------
elif selected == "Stress Engine":
    st.title("🧠 AI Stress Analysis Engine")
    
    if st.button("📸 Open Camera & Detect Emotion"):
        emotion = detect_emotion()
        st.info(f"AI Detected Emotion: **{emotion.upper()}**")

    st.divider()
    
    with st.container(border=True):
        c1, c2 = st.columns(2)
        with c1:
            anxiety = st.slider("Anxiety Level", 0, 10, 5)
            sleep = st.slider("Sleep Quality", 0, 10, 7)
            academic = st.slider("Academic Performance", 0, 10, 6)
            study_load = st.slider("Study Load", 0, 10, 5)
        with c2:
            social = st.slider("Social Support", 0, 10, 8)
            peer = st.slider("Peer Pressure", 0, 10, 4)
            future = st.slider("Future Career Concerns", 0, 10, 6)
            bullying = st.slider("Bullying Experience", 0, 10, 1)

        if st.button("🔍 Run Full Diagnostic"):
            dummy_input = np.array([[anxiety, 5, 5, 5, 5, 5, sleep, 5, 5, 5, 5, 5, academic, study_load, 5, future, social, peer, 5, bullying]])
            prediction = model.predict(dummy_input)[0]
            if prediction == 2: st.error("🔴 HIGH STRESS: Break zaroori hai!")
            elif prediction == 1: st.warning("🟡 MEDIUM STRESS: Relax karein.")
            else: st.success("🟢 LOW STRESS: Great job!")

# ----------------- PAGE: FOCUS & VENT -----------------
elif selected == "Focus & Vent":
    col_f, col_v = st.columns(2)
    with col_f:
        st.subheader("⏱ Pomodoro Focus")
        timer_min = st.number_input("Minutes", 1, 60, 25)
        if st.button("Start Timer"):
            ph = st.empty()
            for i in range(timer_min * 60, 0, -1):
                m, s = divmod(i, 60)
                ph.header(f"⏳ {m:02d}:{s:02d}")
                time.sleep(1)
            st.balloons()
            
    with col_v:
        st.subheader("🗑 Digital Vent Box")
        thought = st.text_area("Write what's bothering you...")
        if st.button("Destroy Thought"):
            with st.spinner("Deleting forever..."):
                time.sleep(1.5)
                st.toast("Thought deleted successfully!")

# --- FLOATING CHATBOT ---
with st.expander("💬 MindSync Assistant"):
    user_q = st.chat_input("Ask me something...")
    if user_q:
        st.chat_message("user").write(user_q)
        st.chat_message("assistant").write(get_response(user_q))