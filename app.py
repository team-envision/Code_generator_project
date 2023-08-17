from flask import Flask, request
from flask_cors import CORS
from prototype1 import temp, prompt
from Get_Answer import get_answer
from pymongo import MongoClient
import os
import logging

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
    if "prompt" in entries and "code" in entries:
      entry = {
        "prompt": entries["prompt"],
        "code": entries["code"]
      }
      chat_history.insert_one(entry)
      return "Added to history"
    else:
      return ("error")
  except Exception as e:
    return (str(e))
  
@app.route("/get-history", methods=["GET"])
def get_chats():
  try:
    chat_list = list(chat_history.find({}, {"_id": 0}))
    return (chat_list)
  except Exception as e:
    return (str(e))

if __name__=="__main__":
  try:
    app.run(debug=True, host="0.0.0.0", port=5000)
  except KeyboardInterrupt:
    print("Keyboard interrupt: shutting down...")
  finally:
    client.close()
