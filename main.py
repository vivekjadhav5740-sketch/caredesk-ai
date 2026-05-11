from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# This allows the frontend to talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# This defines what data the patient sends
class Patient(BaseModel):
    name: str
    age: int
    query: str

# This is the AI logic that assigns wards
def classify_ward(query: str) -> str:
    query = query.lower()
    emergency_keywords = ["chest pain", "accident", "bleeding", "unconscious", 
                          "heart attack", "stroke", "fracture", "injury", "faint"]
    mental_keywords = ["anxiety", "stress", "depression", "mental", 
                       "suicidal", "panic", "trauma", "psychiatric"]
    
    for word in emergency_keywords:
        if word in query:
            return "Emergency Ward"
    
    for word in mental_keywords:
        if word in query:
            return "Mental Health Ward"
    
    return "General Ward"

# Home route - just to check if server is running
@app.get("/")
def home():
    return {"message": "CareDesk AI is running!"}

# Main API route - processes patient info
@app.post("/process_patient")
def process_patient(patient: Patient):
    ward = classify_ward(patient.query)
    return {
        "patient_name": patient.name,
        "patient_age": patient.age,
        "patient_query": patient.query,
        "ward": ward,
        "timestamp": str(datetime.now())
    }