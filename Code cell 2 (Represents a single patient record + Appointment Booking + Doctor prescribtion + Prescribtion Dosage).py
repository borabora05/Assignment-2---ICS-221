# Represents a single patient record + Appointment Booking + Doctor prescribtion + Prescribtion Dosage
class Patient:
    '''A class to represent the patient'''
    # Constructor to initialize patient attributes
    def __init__(self, patient_id, name, dob, gender, address):
        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.gender = gender
        self.address = address
        self.medical_history = []
        self.prescriptions = []

    # Method to add a medical history entry
    def add_medical_history(self, entry):
        self.medical_history.append(entry)

    # Method to add a prescription
    def add_prescription(self, prescription):
        self.prescriptions.append(prescription)


# Represents a single doctor record
class Doctor:
    '''A class to represent the doctor working in the hospital'''
    # Constructor to initialize doctor attributes
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty


# Represents a single prescription record
class Prescription:
    '''a class to represent the Doctor prescribtion'''
    # Constructor to initialize prescription attributes
    def __init__(self, prescription_id, medication, dosage):
        self.prescription_id = prescription_id
        self.medication = medication
        self.dosage = dosage


# Represents a single appointment record
class Appointment:
    ''' A class to represent the Patient Appointment Booking information'''
    # Constructor to initialize appointment attributes
    def __init__(self, patient, doctor, appointment_time):
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time


# Represents the hospital record management system
class Hospital:
    '''A class to represent the Hospital that the patient will be treated in'''
    # Constructor to initialize the system
    def __init__(self):
        self.patients = []  # Using a simple list to store patient records
        self.doctors = {}   # Using a dictionary to store doctor records
        self.consultation_queue = []  # Using a list as a queue for patient consultations
        self.prescription_stack = []  # Using a list as a stack for prescriptions

    # Method to add a patient to the system
    def add_patient(self, patient):
        self.patients.append(patient)

    # Method to add a doctor to the system
    def add_doctor(self, doctor):
        self.doctors[doctor.doctor_id] = doctor

    # Method to schedule an appointment between a patient and a doctor
    def schedule_appointment(self, patient_id, doctor_id, appointment_time):
        patient = next((p for p in self.patients if p.patient_id == patient_id), None)
        doctor = self.doctors.get(doctor_id)
        if patient and doctor:
            appointment = Appointment(patient, doctor, appointment_time)
            self.consultation_queue.append(appointment)

    # Method to retrieve the next consultation from the queue
    def next_consultation(self):
        if self.consultation_queue:
            return self.consultation_queue.pop(0)
        else:
            return None

    # Method to add a prescription to the stack
    def add_prescription(self, prescription):
        self.prescription_stack.append(prescription)


# Example Usage:

# Creating patients
patient1 = Patient(1, "Aysha Al marri", "1990-05-15", "Female", "123 Main St")
patient2 = Patient(2, "Mohammed Alblooshi", "1985-10-20", "Male", "456 Dubai St")

# Creating doctors
doctor1 = Doctor(101, "Dr. Smith", "Cardiologist")
doctor2 = Doctor(102, "Dr. Johnson", "Pediatrician")

# Creating prescriptions
prescription1 = Prescription(1001, "Aspirin", "100mg")
prescription2 = Prescription(1002, "Amoxicillin", "500mg")

# Creating hospital
hospital = Hospital()

# Adding patients to the hospital
hospital.add_patient(patient1)
hospital.add_patient(patient2)

# Adding doctors to the hospital
hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)

# Scheduling appointments
hospital.schedule_appointment(1, 101, "2024-04-01 10:00 am")
hospital.schedule_appointment(2, 102, "2024-04-02 11:00 am")


# Retrieving next consultation
next_appointment = hospital.next_consultation()
if next_appointment:
    print("Next Consultation:", next_appointment.patient.name, "with", next_appointment.doctor.name)

# Adding prescriptions during consultation
hospital.add_prescription(prescription1)
hospital.add_prescription(prescription2)

# Printing the patient's appointment date and time
print("Patient Appointment Date and Time:", next_appointment.appointment_time)
# Printing the prescription stack
print("Prescription Stack:", [p.medication for p in hospital.prescription_stack])
# Printing prescription dosages
print('Prescribtion dosage: ', [prescription1.dosage], [prescription2.dosage])
