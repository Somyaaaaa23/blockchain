from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database (Replace with MySQL/PostgreSQL later)
tutors = {}

@app.route("/register_tutor", methods=["POST"])
def register_tutor():
    data = request.json
    tutor_id = data.get("tutor_id")
    rate_per_session = data.get("rate_per_session")

    if not tutor_id or not rate_per_session:
        return jsonify({"error": "Tutor ID and rate_per_session are required"}), 400

    tutors[tutor_id] = {"rate_per_session": rate_per_session}
    return jsonify({"message": "Tutor registered successfully", "tutor": tutors[tutor_id]})

@app.route("/book_session", methods=["POST"])
def book_session():
    data = request.json
    student_id = data.get("student_id")
    tutor_id = data.get("tutor_id")

    if not student_id or not tutor_id:
        return jsonify({"error": "Student ID and Tutor ID are required"}), 400

    tutor = tutors.get(tutor_id)
    if not tutor:
        return jsonify({"error": "Tutor not found"}), 404

    return jsonify({
        "message": "Session booked successfully",
        "tutor_id": tutor_id,
        "rate_per_session": tutor["rate_per_session"]
    })

# WSGI entry point
if __name__ == "__main__":
    app.run()

