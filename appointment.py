patients=[]
doctors=[
    "dr.smith(cardiologist)",
    "dr.johnson(dermatologist)",
    "dr.williams(orthopedic)"
]
def register_patient():
    name=input("enter patient name:")
    age=input("enter age:")
    patient ={"name":name,"age":age}
    patients.append(patient)
    print("patientregistered successfully!\n")
def view_patients():
    print("---registered patients ---")
    if not patients:
        print("no patients registered.\n")
        return
    for p in patients:
        print(p)
    
def book_appoinment(patient_name,doctor_name,date):
    print(f"appointmemnt booked for{patient_name}with {doctor_name} on {date}")
print("hospital appointment booking system")
def view_appointments():
    print("Viewing appointments")