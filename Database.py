# ==========================================
# DATABASE INITIALIZE  
# ==========================================

# DATA INITIALIZE ADMIN

admin = [
    {"userid": "admin_paw1", "password": "Adminpaw@123", "name": "Rosa", "role": "Clinic Administrator"},
    {"userid": "admin_paw2", "password": "Adminpaw@456", "name": "Alex", "role": "Clinic Administrator"}
]
# DATA INITIALIZE SERVICES

services = {
    "Health Care": ["Consultation", "Vaccination", "Sterilization", "Inpatient Care"],
    "Grooming": ["Healthy Bath", "Flea/Mite Bath", "Haircut"],
    "Pet Hotel": ["Stay Only", "Stay + Playdate"]
}

services_data = [
    # ===== HEALTH CARE =====
    {"category": "Health Care", "service": "Consultation", "price": 200_000},
    {"category": "Health Care", "service": "Vaccination", "price": 150_000},
    {"category": "Health Care", "service": "Sterilization", "price": 1_000_000},
    {"category": "Health Care", "service": "Inpatient Care", "price": 500_000},

    # ===== GROOMING =====
    {"category": "Grooming", "service": "Healthy Bath", "price": 100_000},
    {"category": "Grooming", "service": "Flea/Mite Bath", "price": 120_000},
    {"category": "Grooming", "service": "Haircut", "price": 150_000},

    # ===== PET HOTEL =====
    {"category": "Pet Hotel", "service": "Stay Only", "price": 250_000},
    {"category": "Pet Hotel", "service": "Stay + Playdate", "price": 350_000}
]

# DATA INITIALIZE PATIENT RECORDS 
patient_records = [
    {
        "no": 1,
        "date": "2026-02-20",
        "owner_name": "Rosa",
        "pet_name": "Bobby",
        "category": "Health Care",
        "service": "Consultation",
        "staff": "Dr. John",
        "status": "Check-In"
    },
    {
        "no": 2,
        "date": "2026-02-19",
        "owner_name": "Alex",
        "pet_name": "Milo",
        "category": "Grooming",
        "service": "Haircut",
        "staff": "Alex (Groomer)",
        "status": "Check-In"
    },
    {
        "no": 3,
        "date": "2026-02-18",
        "owner_name": "Lina",
        "pet_name": "Kitty",
        "category": "Pet Hotel",
        "service": "Stay + Playdate",
        "staff": "Maria (Staff)",
        "status": "Check-In"
    },
    {
        "no": 4,
        "date": "2026-02-20",
        "owner_name": "Diana",
        "pet_name": "Rocky",
        "category": "Pet Hotel",
        "service": "Vaccination",
        "staff": "Dr. Sarah",
        "status": "Completed"
    }
]

# DATA INITIALIZE STAFF DATA 
staff_data = [
    # ===== HEALTH CARE =====
    {"name": "Dr. John", "category": "Health Care", "service": "Consultation", "status": "Available"},
    {"name": "Dr. Sarah", "category": "Health Care", "service": "Consultation", "status": "Available"},
    {"name": "Dr. Kevin", "category": "Health Care", "service": "Vaccination", "status": "Available"},
    {"name": "Dr. Laura", "category": "Health Care", "service": "Vaccination", "status": "Available"},
    {"name": "Dr. Adam", "category": "Health Care", "service": "Sterilization", "status": "Available"},
    {"name": "Dr. Zoe", "category": "Health Care", "service": "Sterilization", "status": "Available"},
    {"name": "Dr. Mike", "category": "Health Care", "service": "Inpatient Care", "status": "Available"},
    {"name": "Dr. Anna", "category": "Health Care", "service": "Inpatient Care", "status": "Available"},

    # ===== GROOMING =====
    {"name": "Alex", "category": "Grooming", "service": "Healthy Bath", "status": "Available"},
    {"name": "Lina", "category": "Grooming", "service": "Healthy Bath", "status": "Available"},
    {"name": "Mark", "category": "Grooming", "service": "Haircut", "status": "Available"},
    {"name": "Maya", "category": "Grooming", "service": "Haircut", "status": "Available"},
    {"name": "Jack", "category": "Grooming", "service": "Flea/Mite Bath", "status": "Available"},
    {"name": "Mili", "category": "Grooming", "service": "Flea/Mite Bath", "status": "Available"},

    # ===== PET HOTEL =====
    {"name": "Maria", "category": "Pet Hotel", "service": "Stay Only", "status": "Available"},
    {"name": "Olivia", "category": "Pet Hotel", "service": "Stay Only", "status": "Available"},
    {"name": "James", "category": "Pet Hotel", "service": "Stay + Playdate", "status": "Available"},
    {"name": "Ricki", "category": "Pet Hotel", "service": "Stay + Playdate", "status": "Available"},
]