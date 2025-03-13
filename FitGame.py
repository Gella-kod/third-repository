from abc import ABC, abstractmethod
import re


class FitnessExercises(ABC):
    @abstractmethod
    def sport(self):
        pass


class Pushups(FitnessExercises):
    def sport(self):
        return "Отжимания: -100 калорий за подход"


class Squats(FitnessExercises):
    def sport(self):
        return "Приседания: -150 калорий за подход"


class Fat:
    def __init__(self, initial_weight: int):
        self.weight = initial_weight

    def burn_fat(self, coach):
        exercise = coach.perform_exercise()
        if "калорий" in exercise:

            calories = int(re.search(r'-(\d+)\s', exercise).group(1))
            self.weight -= calories // 50
        return f"Текущий вес: {self.weight} кг"


class Coach:
    def __init__(self):
        self.current_exercise = None

    def change_exercise(self, new_exercise: FitnessExercises):
        self.current_exercise = new_exercise

    def perform_exercise(self):
        if self.current_exercise:
            return self.current_exercise.sport()
        return "Выберите упражнение сначала!"


if __name__ == "__main__":
    trainer = Coach()
    client = Fat(100)

    trainer.change_exercise(Pushups())
    print("1-я тренировка:", trainer.perform_exercise())
    print(client.burn_fat(trainer))  # Вес: 100 - (100//50) = 98 кг

    trainer.change_exercise(Squats())
    print("\n2-я тренировка:", trainer.perform_exercise())
    print(client.burn_fat(trainer))  # Вес: 98 - (150//50) = 95 кг