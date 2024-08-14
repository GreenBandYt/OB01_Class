# Home Work Part 1.

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()
        else:
            print("Недопустимый индекс задачи.")

    def list_pending_tasks(self):
        print("\nТекущие задачи:")
        for idx, task in enumerate(self.tasks):
            if not task.completed:
                print(f"{idx}. {task}")

    def list_all_tasks(self):
        print("\nВсе задачи:")
        for idx, task in enumerate(self.tasks):
            print(f"{idx}. {task}")


def main():
    manager = TaskManager()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить задачу")
        print("2. Отметить задачу как выполненную")
        print("3. Показать невыполненные задачи")
        print("4. Показать все задачи")
        print("5. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            description = input("Введите описание задачи: ")
            deadline = input("Введите срок выполнения задачи: ")
            manager.add_task(description, deadline)
        elif choice == "2":
            manager.list_all_tasks()
            try:
                task_index = int(input("Введите индекс задачи для отметки как выполненной: "))
                manager.mark_task_as_completed(task_index)
            except ValueError:
                print("Пожалуйста, введите правильный номер.")
        elif choice == "3":
            manager.list_pending_tasks()
        elif choice == "4":
            manager.list_all_tasks()
        elif choice == "5":
            break
        else:
            print("Недопустимый выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()