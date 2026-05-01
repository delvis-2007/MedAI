from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

# 🔑 Gemini setup
genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel("gemini-1.5-flash")

# 🏠 Home route
@app.route("/")
def home():
    return render_template("index.html")

# 🤖 AI route
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    question = data.get("question", "")

    try:
        response = model.generate_content(question)
        answer = response.text
    except Exception as e:
        answer = str(e)

    return jsonify({"answer": answer})

# 🚀 Run locally (Render ignores this)
if __name__ == "__main__":
    app.run()
  
