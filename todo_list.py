# To-Do list
import snoop
tasks=[]

def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully!")
    else:
        print("Task not found in the list.")    

def display_tasks():
    if tasks:
        print("\nTasks:")
        for task in tasks:
            print("-> " + task)
    else:
        print("No tasks in the list.")
def add_task(todo_list, task):
    todo_list.append(task)
    print("Task added:", task)

def remove_task(todo_list, task):

    if task in todo_list:
        todo_list.remove(task)
        print("Task removed:", task)
    else:
        print("Task not found in the list.")

def modify_task(todo_list, old_task, new_task):
    if old_task in todo_list:
        old_task_index = todo_list.index(old_task)
        todo_list[old_task_index] = new_task
        print("Task modified:", old_task, "->", new_task)
    else:
        print("Task not found in the list.")

def view_tasks(todo_list):
    print("Tasks:")
    if len(todo_list) == 0:
        print("There are no tasks.")
    else:
        for task in todo_list:
            print("- " + task)

todo_list = []

@snoop

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Modify Tasks")
    print("4. View Tasks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(todo_list, task)
    elif choice == "2":
        task = input("Enter the task to remove: ")
        remove_task(todo_list, task)
    elif choice == "3":
        old_task = input("Enter the task to modify: ")
        new_task = input("Enter the new task: ")
        modify_task(todo_list, old_task, new_task)
    elif choice == "4":
        view_tasks(todo_list)
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Try again.")



#Simple interest calculator
def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

def user_input():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest: "))
    time = float(input("Enter the time in years: "))
    return principal, rate, time

principal, rate, time = user_input()
interest = simple_interest(principal, rate, time)
print("Simple Interest:", interest)



# 
eval(input("Enter list1 : "))