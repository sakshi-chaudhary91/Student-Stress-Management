# Student Stress Management System 

A Python-based application designed to help students track their mental well-being and manage stress using AI. This project integrates Machine Learning for stress detection and the **Gemini AI API** for supportive chatbot conversations.

## 🚀 Features
- **Stress Level Detection:** Analyzes user input to predict stress levels using a pre-trained ML model.
- **AI Mental Health Chatbot:** Powered by Google Gemini to provide empathetic responses.
- **Interactive Interface:** Easy-to-use web interface using Streamlit.

## 🛠️ Tech Stack
- **Language:** Python
- **AI Engine:** Google Gemini Flash
- **Environment:** python-dotenv for security

## ⚙️ Setup & Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file and add: `API_KEY=your_key_here`
4. Run the app: `streamlit run app.py`

## 🔒 Security & Privacy
- API Keys are **not** stored in the repository.
- Sensitive files like `.env` and `__pycache__` are excluded via `.gitignore`.
- Users must use their own API key from Google AI Studio.

## 📂 Project Structure
- `app.py`: Main application UI and logic.
- `chatbot.py`: Handles communication with Gemini AI.
- `emotion.py`: Logic for emotion detection.
- `model.pkl`: The trained Machine Learning model.

---
**Developed with ❤️ by Sakshi**
