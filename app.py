from flask import Flask, request
from flask_cors import CORS
from prototype1 import temp, prompt
from Get_Answer import get_answer

app = Flask(__name__)
CORS(app)

@app.route("/get-prompt", methods=["GET","POST"])
def userPrompt():
  user_prompt = request.get_json()
  print(user_prompt)
  refined_prompt = prompt(user_prompt.get("level"), user_prompt.get("prompt"), user_prompt.get("language"))
  print(refined_prompt)
  query = f"{refined_prompt}. provide only code, no explanation."
  response = get_answer(query, 0.7)
  return (response)

if __name__=="__main__":
  app.run(debug=True, host = "0.0.0.0", port = 5000)
