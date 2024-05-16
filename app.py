from flask import Flask

app = Flask(__name__)

tests = [
    {
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