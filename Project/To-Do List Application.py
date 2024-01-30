class Task:
    def __init__(self,description):
        self.description=description
        self.completed= False

    def __str__(self):
        return f"{'[✓]' if self.completed else '[ ]'} {self.description}"
    
class ToDoList:
    def __init__(self):
        self.tasks=[]

    def add_task(self,description):
        self.tasks.append(Task(description))

    def complete_task(self,index):
        if 0<=index<len(self.tasks):
            self.tasks[index].completed=True
    
    def remove_task(self,index):
        if 0 <=index <len(self.tasks):
            del self.tasks[index]

    def __str__(self):
        return "\n".join(str(task) for task in self.tasks)
    
def main():
    # Create a to-do list
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Complete Task")
        print("3. Remove Task")
        print("4. View Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_description = input("Enter task description: ")
            todo_list.add_task(task_description)
        elif choice == '2':
            index = int(input("Enter index of task to complete: "))
            todo_list.complete_task(index)
        elif choice == '3':
            index = int(input("Enter index of task to remove: "))
            todo_list.remove_task(index)
        elif choice == '4':
            print("\nCurrent To-Do List:")
            print(todo_list)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()