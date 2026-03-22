# tools/ollama_tool.py

import os
import streamlit as st
from groq import Groq

def get_api_key():
    try:
        return st.secrets["GROQ_API_KEY"]
    except Exception:
        return os.getenv("GROQ_API_KEY")

client = Groq(api_key=get_api_key())

def generate_travel_plan(prompt: str) -> str:

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are an expert AI travel planner."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating response: {str(e)}"