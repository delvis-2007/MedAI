
import os
from flask import Flask, request, jsonify, render_template
from google import genai
from google.genai import types #THIS LINE FIXES THE ERROR

app = Flask(__name__)
 
#Initialize the 2026 Free-Tier Client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json(silent=True) or {}
        question = data.get("question", "")

        if not question:
            return jsonify({"answer": "Please ask a question!"})

        # Using 2.5-flash-lite ensures it stays free and bypasses the "Limit: 0" error
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite", 
            contents=question,
            config=types.GenerateContentConfig(
              system_instruction="Your name is MedAI.You were created by Delvis Ogenche.You are a medical and biology assistant."
            )
          )
          

        return jsonify({"answer": response.text})

    except Exception as e:
        return jsonify({"answer": f"System Error: {str(e)}"})

if __name__ == "__main__":
    # This port configuration is required for Render to work
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
  
