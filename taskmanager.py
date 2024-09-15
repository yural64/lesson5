class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        self.tasks.append({"description": description, "deadline": deadline,
                          "status": "Не выполнено"})

    def complete_tasks(self, description):
        for task in self.tasks:
            if task["description"] == description:
                task["status"] = "Выполнено"
                print(f"Задача {description} выполнена")
            else:
                print(f"Задача {description} не найдена в списке текущих задач.")

    def show_tasks(self):
        print()
        print("Список задач - срок:")
        print("--------------------")
        for task in self.tasks:
            if task["status"] == "Не выполнено":
                print(f"{task["description"]} - {task["deadline"]}")

# Выполнение задачи
t = Task()
t.add_task("Выполнить ДЗ", "14.09.2024")
t.add_task("Прочитать книгу", "30.09.2024")
t.add_task("Починить холодильник", "19.09.2024")

t.show_tasks()

t.complete_tasks("Выполнить ДЗ")

t.show_tasks()