import json 

FILE_NAME = "to_do_list.json"

# methos
def get_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def write_to_file(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4) 
        
def add_task(task_name):
    task = {"name": task_name, "status": "pending"}
    tasks = get_tasks()
    print('tasks', tasks)
    tasks.append(task)
    write_to_file(tasks)
    print("Task added successfully.")
   

def complete_task(task_index):
    tasks = get_tasks()
    tasks[task_index]["status"] = 'done'
    write_to_file(tasks)
    print("Task updated successfully.")

def display_tasks(tasks):
    if len(tasks) == 0:
        print("No task has been added yet.")
    else:
        for i, v in enumerate(tasks):
            print(f"[{i}] {v["name"]} - {v["status"]}")

def delete_task(task_index):
    tasks = get_tasks()
    tasks.pop(task_index)
    write_to_file(tasks)
    print("Task deleted successfully.")



# main function
    
try:
    with open(FILE_NAME, "x") as f:
        f.write("[]")
except FileExistsError:
    pass
    

while True:    

    operation = input("""=== To-do List ===
                  1. View Tasks
                  2. Add Task
                  3. Mark Task as Done
                  4. Delete Task
                  5. Exit \n""")
    
    match operation:
        case "1":
            display_tasks(get_tasks())
        case "2":
            task = input("Enter task: ")
            add_task(task)
        case "3":
            display_tasks(get_tasks())
            task_index = int(input("Enter task index: "))
            complete_task(task_index)
        case "4":
            display_tasks(get_tasks())
            task_index = int(input("Enter task index: "))
            delete_task(task_index)
        case "5":
            break
        case "_":
            print("Please select correct input.")

            


