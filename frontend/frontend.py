from flask import Flask, request, jsonify

app = Flask(__name__)

tutors = {}  # Store tutors {address: rate_per_session}

@app.route('/register_tutor', methods=['POST'])
def register_tutor():
    data = request.json
    tutor_address = data.get("tutor_address")
    rate_per_session = data.get("rate_per_session")
    
    if not tutor_address or not rate_per_session:
        return jsonify({"error": "Missing tutor address or rate."}), 400
    
    tutors[tutor_address] = rate_per_session
    return jsonify({"message": "Tutor registered successfully", "rate_per_session": rate_per_session})

@app.route('/book_session', methods=['POST'])
def book_session():
    data = request.json
    student_address = data.get("student_address")
    tutor_address = data.get("tutor_address")
    
    if tutor_address not in tutors:
        return jsonify({"error": "Tutor not found."}), 404
    
    rate_per_session = tutors[tutor_address]
    return jsonify({"message": "Session booked successfully", "amount_paid": rate_per_session})

if __name__ == '__main__':
    app.run(debug=True)
