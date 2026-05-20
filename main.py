import json

#defining required functions
def save_json():
    try:
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)
    except FileNotFoundError:
        return None


def load_json():
    try:
        with open("tasks.json") as f:
            return json.load(f)
    except:
        print('File named "tasks.json" doesn\'t exist')
        return []
    
tasks = load_json()

def show_tasks() :
    if not tasks:
        print("No tasks entered")
        return
    for index, task in enumerate(tasks):
        print(index + 1, task["task"] , "-", task["status"])

def add_task():
    new_task = input("Enter a task. ").strip()

    if new_task == "" :
        print("Enter a valid task")
		return
    else:
        tasks.append({"task": new_task, "status": "incomplete"})

    save_json()

def delete_task(index : int):
    tasks.pop(index)

    save_json()

def mark_taskcomplete(tasknum : int):
    if tasknum < 0 or tasknum >= len(tasks):
		print("Tasks doesn't exist")
    tasks[tasknum]["status"] = "completed"
    save_json()

#loop starts here
while True:
    print(
        """---Menu---
1.Add Task
2.Show Tasks
3.Delete a Task
4.Mark a Task Complete
5.End"""
    )
    choice = input("Choose an option: ")

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
        if not tasks:
            print("No Tasks yet")
            continue
        try:
            tasknum = int(input("Enter the number of task you want to mark as complete. "))
            mark_taskcomplete(tasknum - 1)
        except ValueError:
            print("Enter a valid number")
    elif choice == "5":
        break
    else:
        print("Enter a valid number")
