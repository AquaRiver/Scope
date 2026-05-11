import json

def save_json():
    with open("todo.txt", "w") as f:
        json.dump(tasks, f)


def load_json():
    try:
        with open("todo.txt") as f:
            return json.load(f)
    except:
        print('File named "todo.txt" doesn\'t exist')
        return []
    
tasks = load_json()

def show_tasks() :
    for index, task in enumerate(tasks):
        print(index + 1, task , "-", task["status"])

def add_task():
    new_task = input("Enter a task. ").strip()

    if new_task == "" :
        print("Enter a valid task")
    else:
        tasks.append({"task": new_task, "status": "incomplete"})

    save_json()

def delete_task(index : int):
    tasks.pop(index)

    save_json()

def mark_taskcomplete(tasknum : int):
    tasks[tasknum]["status"] = "completed"
    save_json()



while True:
    print(
        """Choose an option:(Enter only the number)
        1.Add Task
        2.Show Tasks
        3.Delete a Task
        4.Mark a Tak Complete
        5.End"""
    )
    choice = input("")
    print(" Enter a valid number")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        try:
            index = int(input("Enter the number of task you want to delete. "))
            if index < 1 or index > len(tasks):
                print("Task with the entered number doesn't exist")
        except:
            print("Invalid number")
            continue
        delete_task(index - 1)
    elif choice == "4":
        try:
            tasknum = int(input("Enter the number of task you want to mark as complete. "))
            mark_taskcomplete(tasknum)
        except:
            print("Enter a valid number")



