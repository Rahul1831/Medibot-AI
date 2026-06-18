from app.models.doctor_model import Doctor

doctors = [
    Doctor("Dr. Sharma", "Cardiologist", 12),
    Doctor("Dr. Priya", "Dermatologist", 8),
    Doctor("Dr. Reddy", "Neurologist", 15)
]


def get_all_doctors():
    return [doctor.to_dict() for doctor in doctors]


def get_doctor_by_id(doctor_id):
    if 1 <= doctor_id <= len(doctors):
        return doctors[doctor_id - 1].to_dict()

    return None


def create_doctor(name, specialization, experience):

    new_doctor = Doctor(
        name=name,
        specialization=specialization,
        experience=experience
    )

    doctors.append(new_doctor)

    return new_doctor.to_dict()


def get_doctor_count():
    return len(doctors)


def delete_doctor(doctor_id):

    if 1 <= doctor_id <= len(doctors):
        deleted_doctor = doctors.pop(doctor_id - 1)
        return deleted_doctor.to_dict()

    return None