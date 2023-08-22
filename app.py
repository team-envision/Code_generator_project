from flask import Flask, request, send_file
from flask_cors import CORS
from functions import temp, prompt, mermaid_chart, get_chats, clear_history, get_last_code
from Get_Answer import get_answer
from pymongo import MongoClient
import os
import logging
import subprocess
from functions import mermaid_chart

app = Flask(__name__)
CORS(app)

mongoHost = os.getenv("MONGO_HOST", "127.0.0.1")

client = MongoClient("mongodb://" + mongoHost + ":27017")  
db = client.mydb  
chat_history = db.history # 

logging.basicConfig(level=logging.ERROR)

@app.route("/")
def index():
  return "Welcome to the Code-Generator!"


@app.route("/get-prompt", methods=["POST"])
def userPrompt():
  try:
    user_prompt = request.get_json()
    if user_prompt is None:
      return ("error: empty request")
    level = user_prompt.get("level")
    prompt_text = user_prompt.get("prompt")
    language = user_prompt.get("language")
    if level is None or prompt_text is None or language is None:
      return ("error: Missing required parameters")
    refined_prompt = prompt(user_prompt.get("level"), user_prompt.get("prompt"), user_prompt.get("language"))
    query = f"{refined_prompt}. provide only code, no explanation."
    response = get_answer(query, 0.7)
    return (response)
  except Exception as e:
    return (str(e))

@app.route("/increment-to-history", methods=["POST"])
def add_to_history():
  try:
    entries = request.get_json()
    if "user_id" and "prompt" and "code" in entries:
      entry = {
        "user_id": entries["user_id"],
        "prompt": entries["prompt"],
        "code": entries["code"],
        "html_code": entries["html_code"]
      }
      chat_history.insert_one(entry)
      return "Added to history"
    else:
      return ("error")
  except Exception as e:
    return (str(e))

@app.route("/get-class-diagrams", methods=["GET"])
def get_class_diagrams():
  try:
    mermaid_input = get_last_code(chat_history)     
    mermaid_prompt = f"Generate a Mermaid.js mindmap only using the code given: \n {mermaid_input}"
    mermaid_code = get_answer(mermaid_prompt, 0.7)
    html_code = mermaid_chart(mermaid_code)
    # html_code = "move R in front of A. This is the code:" + html_code
    # changed_code = get_answer(html_code, 0.7)
    # return changed_code
    return html_code
  except Exception as e:
    return (str(e))
  
@app.route("/change-diagram", methods=["GET"])
def change_diagram():
  try:
    code_change_user_prompt = request.get_json()
    if code_change_user_prompt is None:
      return ("error: empty request")
    chatlist = get_chats(chat_history)
    chat_list = list(chatlist)
    html_code = len(chat_list)["html_code"]
    code_change_prompt = f"Make the following changes in the mermaid code: {code_change_user_prompt}. This is the mermaid code: {html_code}"
    changed_html_code = get_answer(code_change_prompt, 0.7)
    return changed_html_code
  except Exception as e:
    return (str(e))

if __name__=="__main__":
  try:
    app.run(debug=True, host="0.0.0.0", port=5000)
  except KeyboardInterrupt:
    print("Keyboard interrupt: shutting down...")
  finally:
    client.close()