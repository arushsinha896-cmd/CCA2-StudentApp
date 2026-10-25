from flask import Flask, render_template, jsonify

app = Flask(__name__)

ASSIGNMENTS = [
    {"id": 1, "title": "Cloud Computing Lab", "course": "Cloud & DevOps",
     "deadline": "2026-10-29", "status": "Completed"},
    {"id": 2, "title": "Computer Networks Project", "course": "Networks",
     "deadline": "2026-10-31", "status": "In Progress"},
    {"id": 3, "title": "IoT Practical Assignment", "course": "Internet of Things",
     "deadline": "2026-11-02", "status": "Pending"},
    {"id": 4, "title": "Kubernetes Deployment Lab", "course": "Cloud & DevOps",
     "deadline": "2026-11-05", "status": "Pending"}
]

@app.route("/")
def home():
    completed = sum(a["status"] == "Completed" for a in ASSIGNMENTS)
    return render_template(
        "index.html",
        assignments=ASSIGNMENTS,
        completed=completed,
        total=len(ASSIGNMENTS)
    )

@app.route("/health")
def health():
    return jsonify(status="healthy", version="2")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
