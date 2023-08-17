from Get_Answer import get_answer


def temp(user_level):
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


def prompt(user_level, user_prompt, lang):

    temperature = temp(user_level)
    if (temperature > 0):
        question = "Refine this query in a more technical way, keep it short: " + user_prompt + f"using {lang}. Do not give me code in your response."
        query = get_answer(question, temperature)
        # return query.choices[0].message.content

    else:
        query = user_prompt
        # return query
    return query

answer = prompt("beginner", "how to print hello world", "python")
print(answer)