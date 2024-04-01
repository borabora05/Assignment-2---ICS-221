# Represents a single patient record + Appointment Booking + Doctor prescribtion + Prescribtion Dosage + Medical History
# Full Patient History and Appointment Booking
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
        self.current_condition = ""

    # Method to add a medical history entry
    def add_medical_history(self, entry):
        self.medical_history.append(entry)

    # Method to update the patient's current condition
    def update_condition(self, condition):
        self.current_condition = condition


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
        self.patients = {}  # Using a dictionary to store patient records
        self.doctors = {}  # Using a dictionary to store doctor records
        self.consultation_queue = []  # Using a list as a queue for patient consultations
        self.prescription_stack = []  # Using a list as a stack for prescriptions

    # Method to add a new patient record
    def add_patient(self, patient):
        self.patients[patient.patient_id] = patient

    # Method to update an existing patient record
    def update_patient(self, patient_id, **kwargs):
        patient = self.patients.get(patient_id)
        if patient:
            for key, value in kwargs.items():
                setattr(patient, key, value)

    # Method to remove a patient record
    def remove_patient(self, patient_id):
        if patient_id in self.patients:
            del self.patients[patient_id]

    # Method to schedule an appointment for a patient with a specific doctor
    def schedule_appointment(self, patient_id, doctor_id, appointment_time):
        patient = self.patients.get(patient_id)
        doctor = self.doctors.get(doctor_id)
        if patient and doctor:
            appointment = Appointment(patient, doctor, appointment_time)
            self.consultation_queue.append(appointment)

    # Method to manage the line of patients waiting for consultation (FIFO)
    def next_consultation(self):
        if self.consultation_queue:
            return self.consultation_queue.pop(0)
        else:
            return None

    # Method to issue a medical prescription to a patient during consultation
    # Method to issue a medical prescription to a patient during consultation
    def add_prescription(self, patient_id, prescription):
        patient = self.patients.get(patient_id)
        if patient:
            prescription.patient_id = patient_id
            self.prescription_stack.append(prescription)

    # Method to search for a patient and display a summary
    def search_patient(self, patient_id):
        patient = self.patients.get(patient_id)
        if patient:
            doctor = None
            appointment_time = None
            for appointment in self.consultation_queue:
                if appointment.patient == patient:
                    doctor = appointment.doctor
                    appointment_time = appointment.appointment_time
                    break
            medications = [prescription.medication for prescription in self.prescription_stack if
                           prescription.patient_id == patient_id]

            return {
                "Patient ID": patient.patient_id,
                "Name": patient.name,
                "Date of Birth": patient.dob,
                "Gender": patient.gender,
                "Address": patient.address,
                "Medical History": patient.medical_history,
                "Current Condition": patient.current_condition,
                "Doctor": doctor.name if doctor else "Not scheduled",
                "Appointment Time": appointment_time if appointment_time else "Not scheduled",
                "Medications": medications
            }
        else:
            return None


#Testing
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
hospital.doctors = {doctor1.doctor_id: doctor1, doctor2.doctor_id: doctor2}

# Updating patient information
hospital.update_patient(1, address="456 Updated St")
patient2.add_medical_history("Allergic to penicillin")
patient2.update_condition("Flu")

# Scheduling appointments
hospital.schedule_appointment(1, 101, "2024-04-01 10:00 am")
hospital.schedule_appointment(2, 102, "2024-04-02 11:00 am")

# Adding prescriptions during consultation
hospital.add_prescription(1, Prescription(1001, "Aspirin", "100mg"))
hospital.add_prescription(2, Prescription(1002, "Amoxicillin", "500mg"))

# Adding medical history for a patient
patient1.add_medical_history("Diagnosed with hypertension in 2010")
patient1.add_medical_history("Underwent appendectomy in 2015")

# Printing medical history for the patient
print("Medical History for Patient 1:")
for entry in patient1.medical_history:
    print("-", entry)


# Searching for a patient and displaying their summary
patient_summary = hospital.search_patient(1)
if patient_summary:
    print("Patient Summary:")
    for key, value in patient_summary.items():
        print(key + ":", value)
else:
    print("Patient not found.")
