from Get_Answer import get_answer


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
print("Temperature: ", temperature)
print("question: ", query)
question = query.choices[0].message.content
print("\n\n")
print(question)
query1 = f"{question}. provide only code, no explanation. language : {language}"
print(query1)
answer = get_answer(query1, 0)
print(answer.choices[0].message.content)

