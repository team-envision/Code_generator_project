import os
from Code_generator_project.get_answer import get_answer
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()

# require('dotenv').config()
# console.log(process.env) # remove this after you've confirmed it is working

def temp(userlevel):
    if user_level.lower() in ['beginner','']:
        temperature = 0.7
        return temperature 
    
    if user_level.lower() in ['intermediate']:
        temperature = 0.35
        return temperature 
    
    if user_level.lower() in ['advanced']:
        temperature = 0
        return temperature 
    
#input user language
language = input("\nEnter the language you want to work in: ")

#input user level 
user_level = input("\nEnter your level (beginner, intermediate, advanced): ")

#input user prompt
user_prompt = input("\nEnter your prompt: \n")

temperature = temp(user_level)
if (temperature > 0):
    question = "Refine this query in a more technical way, keep it short: " + user_prompt
    query = get_answer(question, temperature)

else:
    query = user_prompt
# print("question: ", query)
# query = query ," language : ", language
# answer = get_answer(query, 0)
