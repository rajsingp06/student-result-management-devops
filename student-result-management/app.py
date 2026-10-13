from flask import Flask, jsonify

app = Flask(__name__)

STUDENTS = {
    101: {"name": "Aarav Sharma", "marks": {"Python": 78, "DevOps": 82, "DBMS": 74}},
    102: {"name": "Diya Patel", "marks": {"Python": 91, "DevOps": 88, "DBMS": 95}},
    103: {"name": "Kabir Singh", "marks": {"Python": 32, "DevOps": 28, "DBMS": 41}},
}
PASS_MARKS = 35


def calculate_result(student):
    marks = student["marks"]
    total = sum(marks.values())
    maximum = len(marks) * 100
    percentage = round(total / maximum * 100, 2)
    status = "PASS" if all(mark >= PASS_MARKS for mark in marks.values()) else "FAIL"
    return {"name": student["name"], "marks": marks, "total": total,
            "maximum_marks": maximum, "percentage": percentage, "status": status}


@app.get("/")
def home():
    return jsonify({"message": "Student Result Management System",
                    "endpoints": ["/results/101", "/results/102", "/results/103", "/health"]})


@app.get("/results/<int:roll_number>")
def result(roll_number):
    student = STUDENTS.get(roll_number)
    if student is None:
        return jsonify({"error": "Student not found", "roll_number": roll_number}), 404
    return jsonify({"roll_number": roll_number, **calculate_result(student)})


@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
