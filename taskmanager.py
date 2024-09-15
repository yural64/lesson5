class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        self.task.append({"description": description, "deadline": deadline,
                          "status": "Не выполнено"})

    def complete_tasks(self, description):
        for task in self.tasks:
            if task["description"] == description:
                task["status"] = "Выполнено"
                print(f"Задача {description} выполнена")
            else:
                print(f"Задача {description} не найдена")