from groq import Groq
import os

def generate_travel_plan(prompt):

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )

    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content