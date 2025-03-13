class Fitness:
    def __init__(self, gender: str, age: int):
        self.gender = gender
        self.age = age

    def type_of_load(self) -> str:
        return "Обычная тренировочная программа"

    def __str__(self) -> str:
        return f"{self.gender}, {self.age} возраст"


class Athlete(Fitness):
    def __init__(self, gender, age, sport_type: str):
        super().__init__(gender, age)
        self.sport_type = sport_type

    def type_of_load(self) -> str:
        return f"Профессиональная {self.sport_type} программа"


class Senior(Fitness):
    def __init__(self, gender, age, chronic_diseases: list):
        super().__init__(gender, age)
        self.chronic_diseases = chronic_diseases

    def type_of_load(self) -> str:
        return "Щадящая программа реабилитации"


class Teenager(Fitness):
    def __init__(self, gender, age, school_grade: int):
        super().__init__(gender, age)
        self.school_grade = school_grade

    def type_of_load(self) -> str:
        return "Молодежная фитнес-программа"


def show_workouts(clients: list[Fitness]):
    print("\nТренировочная программа:")
    for client in clients:
        print(f"{client}: {client.type_of_load()}")


class SportClub:
    def __init__(self, name: str):
        self.name = name
        self.members = []
        self.trainers = []

    def add_member(self, member: Fitness):
        self.members.append(member)

    def add_trainer(self, trainer):
        self.trainers.append(trainer)

    def show_info(self):
        print(f"\n{self.name} Club:")
        print(f"Посетители: {len(self.members)}")
        print(f"Тренеры: {len(self.trainers)}")


class GroupTraining:
    def __init__(self, trainer_name: str, max_participants: int):
        self.trainer_name = trainer_name
        self.max_participants = max_participants

    def conduct_session(self) -> str:
        return f"Групповое занятие с {self.trainer_name} (максимальным количеством {self.max_participants} человек)"


class PersonalTraining:
    def __init__(self, trainer_name: str, specialization: str):
        self.trainer_name = trainer_name
        self.specialization = specialization

    def conduct_session(self) -> str:
        return f"Персональная тренировка {self.specialization} с тренером {self.trainer_name}"


if __name__ == "__main__":

    boxer = Athlete("Мужчина", 25, "Бокс")
    grandma = Senior("Женщина", 68, ["Гипертоник"])
    student = Teenager("Мужчина", 15, 9)

    show_workouts([boxer, grandma, student])

    powerhouse = SportClub("Powerhouse Fitness")

    powerhouse.add_member(boxer)
    powerhouse.add_member(grandma)
    powerhouse.add_member(student)

    yoga_trainer = GroupTraining("Елена", 15)
    pro_coach = PersonalTraining("Дмитрий", "Пилатес")
    powerhouse.add_trainer(yoga_trainer)
    powerhouse.add_trainer(pro_coach)

    powerhouse.show_info()

    print("\nСегодняшнее расписание:")
    print(yoga_trainer.conduct_session())
    print(pro_coach.conduct_session())