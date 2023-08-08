import openai
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()

def get_answer(text, temp):
    openai.api_key = "OPENAI_API_KEY"
    response = openai.ChatCompletion.create(
        engine = "gpt-3.5-turbo",
        prompt = text,
        temperature = temp,
        max_tokens = 150
    )
    return print(response.choices[0].text)