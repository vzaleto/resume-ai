import os

import openai


openai.api_key = os.getenv("OPENAI_API_KEY")
def generate_resume(prompt: str) -> str:
    try:
        response = openai.Completion.create(
            model= "text-davinci-003",
            prompt= f"Создай профессиональное резюме на основе {prompt}",
            max_tokens=500,
            temperature=0.8,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"error: {str(e)}"