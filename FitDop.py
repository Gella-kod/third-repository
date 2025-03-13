import json
from typing import Dict, Any


class Fitness:
    def __init__(self, gender: str, age: int):
        self.gender = gender
        self.age = age

    def type_of_load(self) -> str:
        return "Обычная тренировочная программа"

    def __str__(self) -> str:
        return f"{self.gender}, {self.age} лет"

    def to_dict(self) -> Dict[str, Any]:
        return {
            '__class__': self.__class__.__name__,
            'gender': self.gender,
            'age': self.age
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(data['gender'], data['age'])


class Athlete(Fitness):
    def __init__(self, gender, age, sport_type: str):
        super().__init__(gender, age)
        self.sport_type = sport_type

    def type_of_load(self) -> str:
        return f"Профессиональная {self.sport_type} программа"

    def to_dict(self):
        data = super().to_dict()
        data['sport_type'] = self.sport_type
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data['gender'], data['age'], data['sport_type'])


class Senior(Fitness):
    def __init__(self, gender, age, chronic_diseases: list):
        super().__init__(gender, age)
        self.chronic_diseases = chronic_diseases

    def type_of_load(self) -> str:
        return "Щадящая программа реабилитации"

    def to_dict(self):
        data = super().to_dict()
        data['chronic_diseases'] = self.chronic_diseases
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data['gender'], data['age'], data['chronic_diseases'])


class Teenager(Fitness):
    def __init__(self, gender, age, school_grade: int):
        super().__init__(gender, age)
        self.school_grade = school_grade

    def type_of_load(self) -> str:
        return "Молодежная фитнес-программа"

    def to_dict(self):
        data = super().to_dict()
        data['school_grade'] = self.school_grade
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data['gender'], data['age'], data['school_grade'])


class SportClub:
    def __init__(self, name: str):
        self.name = name
        self.members = []
        self.trainers = []

    def add_member(self, member: Fitness):
        self.members.append(member)

    def add_trainer(self, trainer):
        self.trainers.append(trainer)

    def to_dict(self):
        return {
            'name': self.name,
            'members': [m.to_dict() for m in self.members],
            'trainers': [t.to_dict() for t in self.trainers]
        }

    @classmethod
    def from_dict(cls, data):
        club = cls(data['name'])
        class_map = {
            'Athlete': Athlete,
            'Senior': Senior,
            'Teenager': Teenager,
            'GroupTraining': GroupTraining,
            'PersonalTraining': PersonalTraining
        }

        for member_data in data['members']:
            cls_name = member_data.pop('__class__')
            club.add_member(class_map[cls_name].from_dict(member_data))

        for trainer_data in data['trainers']:
            cls_name = trainer_data.pop('__class__')
            club.add_trainer(class_map[cls_name].from_dict(trainer_data))

        return club

    def save_to_file(self, filename: str = 'fitness_club.json'):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)

    @classmethod
    def load_from_file(cls, filename: str = 'fitness_club.json'):
        try:
            with open(filename, encoding='utf-8') as f:
                data = json.load(f)
            return cls.from_dict(data)
        except FileNotFoundError:
            return cls("Новый фитнес клуб")

    def show_info(self):
        print(f"\n{self.name}:")
        print(f"Посетители: {len(self.members)}")
        print(f"Тренеры: {len(self.trainers)}")


class GroupTraining:
    def __init__(self, trainer_name: str, max_participants: int):
        self.trainer_name = trainer_name
        self.max_participants = max_participants

    def conduct_session(self) -> str:
        return f"Групповое занятие с {self.trainer_name}"

    def to_dict(self):
        return {
            '__class__': self.__class__.__name__,
            'trainer_name': self.trainer_name,
            'max_participants': self.max_participants
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['trainer_name'], data['max_participants'])


class PersonalTraining:
    def __init__(self, trainer_name: str, specialization: str):
        self.trainer_name = trainer_name
        self.specialization = specialization

    def conduct_session(self) -> str:
        return f"Персональная тренировка {self.specialization}"

    def to_dict(self):
        return {
            '__class__': self.__class__.__name__,
            'trainer_name': self.trainer_name,
            'specialization': self.specialization
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['trainer_name'], data['specialization'])


if __name__ == "__main__":

    club = SportClub.load_from_file()

    if not club.members:

        club = SportClub("Powerhouse Fitness")
        club.add_member(Athlete("Мужчина", 25, "Бокс"))
        club.add_member(Senior("Женщина", 68, ["Гипертония"]))
        club.add_trainer(GroupTraining("Елена", 15))
        club.save_to_file()


    if len(club.members) < 5:
        club.add_member(Teenager("Мужчина", 15, 9))
        club.save_to_file()


    club.show_info()
    print("\nПрограммы тренировок:")
    for member in club.members:
        print(f"- {member}: {member.type_of_load()}")

    print("\nРасписание занятий:")
    for trainer in club.trainers:
        print(f"- {trainer.conduct_session()}")