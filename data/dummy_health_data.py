# data/dummy_health_data.py

from datetime import datetime, timedelta
import random

def generate_time_series(days=90):
    base = datetime.today()
    return [(base - timedelta(days=x)).strftime("%Y-%m-%d") for x in range(days)][::-1]

def get_dashboard_data():
    dates = generate_time_series()

    heart_rate = [(d, random.randint(65, 90)) for d in dates]
    systolic = [(d, random.randint(110, 130)) for d in dates]
    diastolic = [(d, random.randint(70, 85)) for d in dates]
    glucose = [(d, random.randint(80, 140)) for d in dates]

    symptoms = {
        "None": random.randint(15, 30),
        "Chest Pain": random.randint(10, 20),
        "Headache": random.randint(10, 20),
        "Nausea": random.randint(5, 15),
        "Dizziness": random.randint(5, 15),
        "Fatigue": random.randint(5, 15)
    }

    return {
        "heart_rate": heart_rate,
        "blood_pressure": {
            "systolic": systolic,
            "diastolic": diastolic
        },
        "glucose": glucose,
        "symptoms": symptoms
    }
