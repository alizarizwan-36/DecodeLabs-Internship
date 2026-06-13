# To-Do List Application

tasks = []
# adding infinite loops
while True:
    print("\n===== TO-DO LIST MENU =====\n")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")


# add your tasks
    if choice == "1":
        task = input("Enter a new task: ")

        task_data = {
            "id": len(tasks) + 1,
            "task": task
        }

        tasks.append(task_data)

        print("Task added successfully!")


# view your tasks 
    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\n----- YOUR TASKS -----")

            for item in tasks:
                print(f"{item['id']}. {item['task']}")


# quiting the app or the program 
    elif choice == "3":
        print("Exiting program...")
        break

    
# request for valid input
    else:
        print("Invalid choice! Please enter 1, 2 or 3.")

