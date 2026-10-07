from flask import Flask, jsonify

app = Flask(__name__)

COURSES = [
    {"id": 101, "name": "Machine Learning", "credits": 4},
    {"id": 102, "name": "Computer Networks", "credits": 3},
    {"id": 103, "name": "Database Management Systems", "credits": 4},
]

@app.get("/health")
def health():
    return jsonify({"service": "Course Service", "status": "Running"})

@app.get("/courses")
def courses():
    return jsonify({"courses": COURSES, "service": "Course Service"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
