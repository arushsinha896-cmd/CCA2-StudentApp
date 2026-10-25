from flask import Flask, render_template, jsonify

app = Flask(__name__)

STUDENTS = [
    {"id": 1, "name": "Aarav Sharma", "course": "Computer Science"},
    {"id": 2, "name": "Priya Patel", "course": "Information Technology"},
    {"id": 3, "name": "Rohan Verma", "course": "Computer Science"}
]

@app.route("/")
def home():
    return render_template("index.html", students=STUDENTS)

@app.route("/health")
def health():
    return jsonify(status="healthy", version="1")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
