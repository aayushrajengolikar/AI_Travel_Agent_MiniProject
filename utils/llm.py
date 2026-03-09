import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(prompt):

    # list available models for this API key
    models = [m.name for m in genai.list_models() if "generateContent" in m.supported_generation_methods]

    model_name = models[0]  # pick first available model

    model = genai.GenerativeModel(model_name)

    response = model.generate_content(prompt)

    return response.text