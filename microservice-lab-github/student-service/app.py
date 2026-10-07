from flask import Flask, jsonify

app = Flask(__name__)

STUDENTS = [
    {"id": 1, "name": "Preetam", "branch": "AIML"},
    {"id": 2, "name": "Sai", "branch": "AIML"},
    {"id": 3, "name": "Amit", "branch": "AIML"},
]

@app.get("/health")
def health():
    return jsonify({"service": "Student Service", "status": "Running"})

@app.get("/students")
def students():
    return jsonify({"service": "Student Service", "students": STUDENTS})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
