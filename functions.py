from Get_Answer import get_answer
import base64
from IPython.display import Image, display
import matplotlib.pyplot as plt


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



def mermaid_chart(mindmap_code):
    html_code = f"""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
    <div class="mermaid">{mindmap_code}</div>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>mermaid.initialize({{startOnLoad:true}});</script>
    """
    return html_code


def prompt(user_level, user_prompt, lang):

    temperature = temp(user_level)
    if (temperature > 0):
        question = """Refine this query in a more technical way, keep it short: " """ + user_prompt + f""" using {lang}." Do not give me code in your response."""
        query = get_answer(question, temperature)
        # return query.choices[0].message.content

    else:
        query = user_prompt
        # return query
    return query

answer = prompt("beginner", "how to print hello world", "python")
print(answer)

def clear_history(collection_name):
  try:
    collection_name.delete_many({})
    return "History cleared"
  except Exception as e:
    return (str(e))
  
def get_chats(collection_name):
  try:
    chat_list = list(collection_name.find({}, {"_id": 0}))
    return (chat_list)
  except Exception as e:
    return (str(e))
  
def get_last_code(collection_name):
  try:
    chatlist = get_chats(collection_name)
    chat_list = list(chatlist)
    last_code = ""
    i = len(chat_list)
    last_code = last_code + "\n" + i["code"]
    return (last_code)
  except Exception as e:
    return (str(e))