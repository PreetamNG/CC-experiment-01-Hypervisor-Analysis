from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)

STUDENT_SERVICE_URL = os.getenv("STUDENT_SERVICE_URL", "http://localhost:5001")
COURSE_SERVICE_URL = os.getenv("COURSE_SERVICE_URL", "http://localhost:5002")

def get_json(url):
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()

@app.get("/health")
def health():
    return jsonify({"service": "API Gateway", "status": "Running"})

@app.get("/students")
def students():
    return jsonify(get_json(f"{STUDENT_SERVICE_URL}/students"))

@app.get("/courses")
def courses():
    return jsonify(get_json(f"{COURSE_SERVICE_URL}/courses"))

@app.get("/dashboard")
def dashboard():
    students_data = get_json(f"{STUDENT_SERVICE_URL}/students")
    courses_data = get_json(f"{COURSE_SERVICE_URL}/courses")
    return jsonify({
        "courses": courses_data,
        "message": "API Gateway successfully communicated with Student and Course Services",
        "students": students_data,
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
