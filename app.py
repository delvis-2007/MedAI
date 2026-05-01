from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "").lower()

    # SIMPLE MEDICAL LOGIC
    if "malaria" in question:
        answer = "Malaria is a mosquito-borne disease caused by parasites."
    elif "fever" in question:
        answer = "Fever is usually a sign your body is fighting an infection."
    elif "headache" in question:
        answer = "Headaches can be caused by stress, dehydration, or illness."
    elif "nursing" in question:
        answer = "Nursing is a healthcare profession focused on patient care."
    else:
        answer = "I am still learning. Try asking about malaria, fever, headache, or nursing."

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
