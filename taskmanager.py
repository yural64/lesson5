#Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач
# и вывода списка текущих (не выполненных) задач.

class Task:
    tasks = [] # пустой список для добавления задач
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.is_complected = False #значение статуса по умолчанию "не выполнено" или False
        Task.tasks.append(self)

    def mark_completed(self): #пометить задачу выполненной
        self.is_complected = True

    @classmethod #метод класса для управления задачами
    def get_pending_tasks(cls):
        return [task for task in cls.tasks if not task.is_complected]

    @classmethod #метод класса для отображения задачами
    def display_pending_tasks(cls):
        print()
        print("Текущие задачи (не выполненные):")
        for i, task in enumerate(cls.get_pending_tasks(), start = 1): #перебираем список задач
            status = "Выполнено" if task.is_complected else "Не выполнено"
            print(f"{i}. Описание: {task.description}, Срок: {task.deadline}, Статус: {status}")

# Выполнение
task1 = Task("Купить продукты", "2024-09-14")
task2 = Task("Закончить ДЗ к уроку", "2024-09-15")

# Вывод списка текущих задач
Task.display_pending_tasks()

# Отметим задачу 1 как выполненную
task1.mark_completed()

# Еще раз выведем список текущих задач
Task.display_pending_tasks()