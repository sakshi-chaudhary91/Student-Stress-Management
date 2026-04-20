import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))

def get_response(user_input):
    try:
       model = genai.GenerativeModel("gemini-1.0-pro")
       response = model.generate_content(user_input)
       return response.text
    except Exception as e:
        return f"Error: {e}"