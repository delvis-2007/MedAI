from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json(silent=True) or {}
        question = data.get("question", "")

        if not question:
            return jsonify({"answer": "No question received."})

        response = model.generate_content(question)

        return jsonify({"answer": response.text})

    except Exception as e:
        return jsonify({"answer": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run()

  
