class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)
        print(f"Задача добавлена: {task}")

    def complete_task(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_completed()
                print(f"Задача отмечена как выполненная: {task}")
                return
        print(f"Задача с описанием '{description}' не найдена.")

    def show_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        if current_tasks:
            print("Текущие задачи:")
            for task in current_tasks:
                print(task)
        else:
            print("Нет текущих задач.")


task_manager = TaskManager()

task_manager.add_task("Пройти два урока", "2023-10-05")
task_manager.add_task("Погулять с собакой", "2023-10-06")
task_manager.add_task("Помыть сапоги", "2023-10-07")

task_manager.show_current_tasks()

task_manager.complete_task("Погулять с собакой")

task_manager.show_current_tasks()