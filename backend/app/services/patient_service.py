from app.models.patient_model import Patient

patients = [
    Patient("Rahul", 25, "Male"),
    Patient("John", 30, "Male"),
    Patient("Sarah", 28, "Female")
]


def get_all_patients():
    return [patient.to_dict() for patient in patients]


def get_patient_by_id(patient_id):
    if 1 <= patient_id <= len(patients):
        return patients[patient_id - 1].to_dict()

    return None


def create_patient(name, age, gender):

    new_patient = Patient(
        name=name,
        age=age,
        gender=gender
    )

    patients.append(new_patient)

    return new_patient.to_dict()


def get_patient_count():
    return len(patients)


def delete_patient(patient_id):

    if 1 <= patient_id <= len(patients):
        deleted_patient = patients.pop(patient_id - 1)
        return deleted_patient.to_dict()

    return None