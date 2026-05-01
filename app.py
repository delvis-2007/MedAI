import os
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

# This looks for the key in Render's environment settings
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash-lite")

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

        response = model.generate_content(question)
        return jsonify({"answer": response.text})

    except Exception as e:
        # If the key is missing or invalid, this will tell you
        return jsonify({"answer": f"System Error: {str(e)}"})

if __name__ == "__main__":
    # Required for Render deployment
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

  
