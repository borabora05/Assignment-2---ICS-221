# Represents a single patient record
class Patient:
    '''class to represent patients'''
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

    # Method to remove a prescription
    def remove_prescription(self, prescription):
        self.prescriptions.remove(prescription)


# Represents the hospital record management system
class HospitalRecordSystem:
    '''class to represent the functions of the hospital record system'''
    # Constructor to initialize the system
    def __init__(self):
        self.patients = {}

    # Method to add a patient to the system
    def add_patient(self, patient):
        self.patients[patient.patient_id] = patient

    # Method to get a patient's record
    def get_patient(self, patient_id):
        return self.patients.get(patient_id)

    # Method to remove a patient from the system
    def remove_patient(self, patient_id):
        if patient_id in self.patients:
            del self.patients[patient_id]
            return True
        return False

    # Method to update a patient's record
    def update_patient(self, patient_id, **kwargs):
        patient = self.get_patient(patient_id)
        if patient:
            for key, value in kwargs.items():
                setattr(patient, key, value)
            return True
        return False


# Example usage:

# Creating patients
patient1 = Patient(1, " Aysha Al marri", "1990-05-15", "Female", "123 Main St")
patient2 = Patient(2, "Mohammed Alblooshi", "1985-10-20", "Male", "456 Dubai St")

# Creating hospital record system
hospital_system = HospitalRecordSystem()

# Adding patients to the system
hospital_system.add_patient(patient1)
hospital_system.add_patient(patient2)

# Retrieving a patient's record
print('Patient Name: ', hospital_system.get_patient(1).name)  # Output: John Doe

# Updating a patient's record
hospital_system.update_patient(1, address="1a Dubai St")
print('Patient Address: ', hospital_system.get_patient(1).address)  # Output: 789 Oak St

# Removing a patient's record
hospital_system.remove_patient(2)
print('Patient Record: ', hospital_system.get_patient(2))  # Output: None
