class Doctor:

    def __init__(
        self,
        name,
        specialization,
        experience
    ):
        self.name = name
        self.specialization = specialization
        self.experience = experience

    def to_dict(self):
        return {
            "name": self.name,
            "specialization": self.specialization,
            "experience": self.experience
        }