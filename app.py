from flask import Flask, request

app = Flask(__name__)

tests = [
    {
        "test_id": 1,
        "name": "2019_ga_en",
        "year": 2019,
        "subject": "English",
        "program": "Undergraduate",
        "instructions": [
            {
                "id": "I",
                "text": "Choose the word or phrase that best completes each sentence."
            }
        ],
        "questions": [
            {
                "id": "question_1",
                "instruction_id": "I",
                "number": 1,
                "text": "A judge should be (      ) in a case.",
                "options": {
                    "A": "disengaged",
                    "B": "disgruntled",
                    "C": "disinterested",
                    "D": "disposed"
                },
                "correct_answer": "C"
            }
        ]
    }
]

@app.get("/tests")
def get_tests():
    return {"tests": tests}

@app.post("/tests")
def create_store():
    request_data = request.get_json()
    new_test = {
        "test_id": request_data["test_id"],
        "name": request_data["name"],
        "year": request_data["year"]}
    tests.append(new_test)
    return new_test, 201