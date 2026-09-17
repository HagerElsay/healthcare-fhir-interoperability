# Hospital A - Source System

import json


patients = [
    {
        "patient_id": "101",
        "full_name": "Ahmed Ali",
        "dob": "1995-06-12",
        "gender": "male",
        "diagnosis": "Diabetes",
        "blood_pressure": "140/90",
        "medication": "Metformin"
    },
    {
        "patient_id": "102",
        "full_name": "Nour Mohamed",
        "dob": "2002-03-25",
        "gender": "female",
        "diagnosis": "Asthma",
        "blood_pressure": "120/80",
        "medication": "Salbutamol"
    },
    {
        "patient_id": "102",
        "full_name": "Omar Hassan",
        "dob": "1990-08-15",
        "gender": "male",
        "diagnosis": "Hypertension",
        "blood_pressure": "150/95",
        "medication": "Amlodipine"
    }
]


def export_data():

    with open("hospital_a_data.json", "w") as file:
        json.dump(patients, file, indent=4)

    print("Patient data exported to hospital_a_data.json")
