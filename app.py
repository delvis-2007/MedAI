from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
import google.generativeai as genai
@app.route("/")
def home():
    return render_template("index.html")
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

genai.configure(api_key="AIzaSyB31b4KFNIkGVILELKfCEkgstCmCNFT-X4")

model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    question = data.get("question", "")

    try:
        response = model.generate_content(question)
        answer = response.text
    except Exception as e:
        answer = "AI error: " + str(e)

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
