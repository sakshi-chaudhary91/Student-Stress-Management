import streamlit as st
import numpy as np
import pickle
import os

from emotion import detect_emotion
from chatbot import get_response

# Load model
model = pickle.load(open("model.pkl", "rb"))

# 🌙 Dark Theme Styling
st.set_page_config(page_title="AI Stress Analyzer", layout="wide")

st.markdown("""
<style>
body {
    background-color: #0E1117;
    color: white;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# 🎯 Header
st.markdown("<h1 style='text-align: center;'>🧠 AI Student Stress Analyzer</h1>", unsafe_allow_html=True)
st.markdown("---")

# 📷 Emotion Detection
st.subheader("📷 Emotion Detection")

if st.button("Detect Emotion"):
    emotion = detect_emotion()
    st.info(f"Detected Emotion: {emotion}")

# 🎯 Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Psychological Factors")
    anxiety = st.slider("Anxiety", 0, 10)
    self_esteem = st.slider("Self Esteem", 0, 10)
    mental_health = st.slider("Mental Health History", 0, 10)
    depression = st.slider("Depression", 0, 10)
    headache = st.slider("Headache", 0, 10)
    bp = st.slider("Blood Pressure", 0, 10)
    sleep = st.slider("Sleep Quality", 0, 10)
    breathing = st.slider("Breathing Problem", 0, 10)

with col2:
    st.subheader("Environment & Academic")
    noise = st.slider("Noise Level", 0, 10)
    living = st.slider("Living Conditions", 0, 10)
    safety = st.slider("Safety", 0, 10)
    basic = st.slider("Basic Needs", 0, 10)
    academic = st.slider("Academic Performance", 0, 10)
    study_load = st.slider("Study Load", 0, 10)
    teacher = st.slider("Teacher-Student Relationship", 0, 10)
    future = st.slider("Future Career Concerns", 0, 10)
    social = st.slider("Social Support", 0, 10)
    peer = st.slider("Peer Pressure", 0, 10)
    extra = st.slider("Extracurricular Activities", 0, 10)
    bullying = st.slider("Bullying", 0, 10)

# 🎯 Input Array (IMPORTANT ORDER)
input_data = np.array([[anxiety, self_esteem, mental_health, depression,
                        headache, bp, sleep, breathing,
                        noise, living, safety, basic,
                        academic, study_load, teacher, future,
                        social, peer, extra, bullying]])

st.markdown("---")

# 🔍 Prediction
if st.button("Analyze Stress"):
    result = model.predict(input_data)[0]

    if result == 2:
        st.error("🔴 High Stress")
    elif result == 1:
        st.warning("🟡 Medium Stress")
    else:
        st.success("🟢 Low Stress")

# 💬 AI Chatbot
st.markdown("---")
st.subheader("💬 AI Mental Health Assistant")

user_input = st.text_input("Ask anything about stress...")

if user_input:
    response = get_response(user_input)
    st.write(response)
    print(os.getenv("API_KEY"))