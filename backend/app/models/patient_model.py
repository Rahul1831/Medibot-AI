class Patient:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender
        }