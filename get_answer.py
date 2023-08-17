import openai
from dotenv import dotenv_values

config = dotenv_values(".env")

API_KEY = config['OPENAI_API_KEY']

# def get_answer(text, temp):
#     openai.api_key = API_KEY
#     response = openai.ChatCompletion.create(
#         engine = "gpt-3.5-turbo",
#         prompt = text,
#         temperature = temp,
#         max_tokens = 150
#     )
#     return print(response.choices[0].text)
import os



def get_answer(text, temp):

    openai.api_key = API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=temp,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content