

import tkinter as tk

tasks_read = open('tasks1.txt', 'r')

global user_tasks
global edit_data
global real_task_choice
user_tasks = tasks_read.readlines()



# Open a list to store usernames and dictionary for the respective passwords
user_names =[]
pass_words = {}

users = " "
# Read in the user text file to gain account data

with open('user1.txt', 'r+') as f:
    for users in f:

        # Split names by a comma and assign respective passwords
        name = users.split(',')
        user_password = name[1].strip()
        user_names.append(name[0])
        pass_words[name[0]] = user_password



def check_credentials(username, password, window):
    if username in user_names and password == pass_words[username]:
        print("Matched")
        window.destroy()

    else:
        print("Not Matched")


def login():
    # Create the main window
    window = tk.Tk()
    window.title("Login")

    # Create the username and password labels and entry fields
    tk.Label(window, text="Username:").grid(row=0, column=0)
    global username_entry
    username_entry = tk.Entry(window)
    username_entry.grid(row=0, column=1)

    tk.Label(window, text="Password:").grid(row=1, column=0)
    global password_entry
    password_entry = tk.Entry(window, show="*")
    password_entry.grid(row=1, column=1)

    # Create the submit button
    submit_button = tk.Button(window, text="Submit",
            command = lambda: check_credentials(username_entry.get(), password_entry.get(), window))
    submit_button.grid(row=2, column=0, columnspan=2)

    window.mainloop()

def edit_due_date():
   print("D")

def mark_my_task_completed(task_choice):
    real_task_choice = int(task_choice) - 1
    edit_data = user_tasks[real_task_choice]
    split_data = edit_data.split(", ")
    split_data[-1] = 'Yes\n'
    new_data = ", ".join(split_data)
    user_tasks[real_task_choice] = new_data


def my_task_menu():

    my_task_menu_window = tk.Tk()
    my_task_menu_window.title("Task Menu")
    tk.Label(my_task_menu_window, text="Task Menu").grid(row=0, column=0)

    tk.Label(my_task_menu_window, text="Select Task number: ").grid(row=1, column=0)
    global task_choice
    task_choice = tk.Entry(my_task_menu_window)
    task_choice.grid(row=1, column=1)

    number_submit_button = tk.Button(my_task_menu_window, text="Submit",
                              command=lambda: my_task_return(task_choice.get()))
    number_submit_button.grid(row=1, column=3)

    tk.Label(my_task_menu_window, text = "Edit due date:  ").grid(row=3, column=0)
    due_edit_button = tk.Button(my_task_menu_window, text = "d", command = lambda: edit_due_date()) #TODO - edit due date function
    due_edit_button.grid(row=3, column=1)

    tk.Label(my_task_menu_window, text="Mark as completed:  ").grid(row=4, column=0)
    due_edit_button = tk.Button(my_task_menu_window, text="m", command=lambda: mark_my_task_completed(task_choice.get()))  # TODO - task complete function
    due_edit_button.grid(row=4, column=1)

    my_task_menu_window.mainloop()

def my_task_return(task_choice):
    global real_task_choice
    real_task_choice = int(task_choice) - 1
    if real_task_choice < 0 or real_task_choice > len(user_tasks):
        print("This is an invalid option, try again.")

    else:

        edit_data = user_tasks[real_task_choice]
        my_task_return_window = tk.Tk()
        my_task_return_window.title("Selected Task")
        split_data = edit_data.split(", ")

        for pos, line in enumerate(user_tasks, real_task_choice):

            split_data = line.split(", ")
            output = f'---------[{pos+1}]---------\n'
            output += '\n'
            output += f"Assigned to: \t\t {split_data[0]}\n"
            output += f"Task:\t\t\t {split_data[1]}\n"
            output += f"Description:\t {split_data[2]}\n"
            output += f"Assigned date: \t{split_data[3]}\n"
            output += f"Due Date: \t\t{split_data[4]}\n"
            output += f"Is completed:\t\t {split_data[5]}\n"
            output += "\n"

            tk.Label(my_task_return_window, text=output).grid(row=1, column=0)

            tk.Label(my_task_return_window, text="Edit due date:  ").grid(row=3, column=0)
            due_edit_button = tk.Button(my_task_return_window, text="d",
                                        command=lambda: edit_due_date())  # TODO - edit due date function
            due_edit_button.grid(row=3, column=1)

            tk.Label(my_task_return_window, text="Mark as completed:  ").grid(row=4, column=0)
            due_edit_button = tk.Button(my_task_return_window, text="m", command=lambda: mark_my_task_completed(
                real_task_choice.get()))  # TODO - task complete function
            due_edit_button.grid(row=4, column=1)

            my_task_return_window.mainloop()






def menu():
    menu_window = tk.Tk()
    menu_window.title("Menu")
    tk.Label(menu_window, text = "Menu").grid(row = 0, column = 0)
    tk.Label(menu_window, text = "Registering a user  ").grid(row = 1, column =0)
    register_button = tk.Button(menu_window, text = "r", command = lambda: register_user())
    register_button.grid(row = 1, column = 1)

    tk.Label(menu_window, text = "Adding a task  ").grid(row=2, column=0)
    add_task_button = tk.Button(menu_window, text="a", command=lambda: add_task())
    add_task_button.grid(row=2, column=1)

    tk.Label(menu_window, text="View all tasks  ").grid(row=3, column=0)
    view_all_tasks_button = tk.Button(menu_window, text="va", command=lambda: view_all_tasks())
    view_all_tasks_button.grid(row=3, column=1)

    tk.Label(menu_window, text="View my task  ").grid(row=4, column=0)
    view_my_tasks_button = tk.Button(menu_window, text="vm", command=lambda: my_task_menu())
    view_my_tasks_button.grid(row=4, column=1)

    tk.Label(menu_window, text="Generate Reports  ").grid(row=5, column=0)
    view_my_tasks_button = tk.Button(menu_window, text="gr", command=lambda: generate_reports())
    view_my_tasks_button.grid(row=5, column=1)

    tk.Label(menu_window, text="Display Statistics  ").grid(row=6, column=0)
    view_my_tasks_button = tk.Button(menu_window, text="ds", command=lambda: display_statistics())
    view_my_tasks_button.grid(row=6, column=1)

    menu_window.mainloop()

def generate_reports():

    with open("tasks1.txt", 'r') as file:
        number_of_tasks = sum(1 for line in file)
        print(f"There is a total of {number_of_tasks} tasks.")

    with open("tasks1.txt", 'r') as file:


        for line in file:
            i = 0
            if line.strip().endswith("yes"):
                i += 1
    print(f"There is {i} tasks that are completed.")









def register_user():

    register_user_window = tk.Tk()
    register_user_window.title("New user")

    tk.Label(register_user_window, text = "New Username:").grid(row = 0, column = 0)
    new_username_entry = tk.Entry(register_user_window)
    new_username_entry.grid(row = 0, column = 1)

    tk.Label(register_user_window, text = "New Password:").grid(row = 1, column = 0)
    new_password_entry = tk.Entry(register_user_window)
    new_password_entry.grid(row = 1, column = 1)

    tk.Label(register_user_window,text= "Password Confirmation:").grid(row = 2, column = 0)
    password_conf_entry = tk.Entry(register_user_window)
    password_conf_entry.grid(row = 2, column =1 )

    register_user_button = tk.Button(register_user_window, text = "Register", command = lambda:
    register_user_to_file(new_username_entry.get(), new_password_entry.get(), password_conf_entry.get()))
    register_user_button.grid(row=3, column=0, columnspan=2)

    register_user_window.mainloop()


def register_user_to_file(username, password, password_conf):
    if password == password_conf:
        with open('user1.txt', 'a') as user_file:
            if username in user_names:
                register_user_to_file_window = tk.Tk()
                register_user_to_file_window.title("New user")
                tk.Label(register_user_to_file_window, text="Username already taken, please choose another:").grid(row=4, column=0)

            else:
                user_file.write(username + ',' + password + '\n')
                print("User successfully registered.")

    else:
        print("Passwords do not match.")
    menu()


    #else:
        #tk.Label(register_user, text="Please ensure password and confirmation are the same.").grid(row=1, column=0)

    register_user_to_file.mainloop()




def add_task():
    # Create a new window for adding a task
    add_task_window = tk.Tk()
    add_task_window.title("Add Task")

    # Create entry fields for task details
    tk.Label(add_task_window, text="Assign To:").grid(row=0, column=0)
    global task_assign_entry
    task_assign_entry = tk.Entry(add_task_window)
    task_assign_entry.grid(row=0, column=1)

    tk.Label(add_task_window, text="Task:").grid(row=1, column=0)
    global task_entry
    task_entry = tk.Entry(add_task_window)
    task_entry.grid(row=1, column=1)

    tk.Label(add_task_window, text="Task Description:").grid(row=2, column=0)
    global task_desc_entry
    task_desc_entry = tk.Entry(add_task_window)
    task_desc_entry.grid(row=2, column=1)

    tk.Label(add_task_window, text="Assigned Date (MM/DD/YYYY):").grid(row=3, column=0)
    global assigned_date_entry
    assigned_date_entry = tk.Entry(add_task_window)
    assigned_date_entry.grid(row=3, column=1)

    tk.Label(add_task_window, text="Due Date (MM/DD/YYYY):").grid(row=4, column=0)
    global due_date_entry
    due_date_entry= tk.Entry(add_task_window)
    due_date_entry.grid(row=4, column=1)

    tk.Label(add_task_window, text="Is Completed:").grid(row=5, column=0)
    global is_completed_entry
    is_completed_entry = tk.Entry(add_task_window)
    is_completed_entry.grid(row=5, column=1)

    # Create submit button
    submit_button = tk.Button(add_task_window, text="Submit",
                                  command=lambda: validate_and_save_task(add_task_window))
    submit_button.grid(row=6, column=0, columnspan=2)

    add_task_window.mainloop()

def view_all_tasks():

    view_all_tasks_window = tk.Tk()
    view_all_tasks_window.title("Task Viewer")
    tk.Label(view_all_tasks_window, text = "Here are the Tasks:").grid(row=0, column=0)


    user_tasks = tasks_read.readlines()
    for pos, line in enumerate(user_tasks, 1):
        split_data = line.split(", ")
        output = f'---------[{pos}]---------\n'
        output += '\n'
        output += f"Assigned to: \t\t {split_data[0]}\n"
        output += f"Task:\t\t\t {split_data[1]}\n"
        output += f"Description:\t {split_data[2]}\n"
        output += f"Assigned date: \t{split_data[3]}\n"
        output += f"Due Date: \t\t{split_data[4]}\n"
        output += f"Is completed:\t\t {split_data[5]}\n"
        output += "\n"

        tk.Label(view_all_tasks_window, text=output).grid(row=1, column=0)

        view_all_tasks_window.mainloop()


def view_my_tasks():

    view_my_tasks_window = tk.Tk()
    view_my_tasks_window.title("Your Tasks")
    tk.Label(view_my_tasks_window, text = "Here are the tasks assigned to you personally:").grid(row=0, column=0)

    global user_tasks
    user_tasks = tasks_read.readlines()
    for pos, line in enumerate(user_tasks, 1):
        split_data = line.split(", ")
        output = f'---------[{pos}]---------\n'
        output += '\n'
        output += f"Assigned to: \t\t {split_data[0]}\n"
        output += f"Task:\t\t\t {split_data[1]}\n"
        output += f"Description:\t {split_data[2]}\n"
        output += f"Assigned date: \t\t{split_data[3]}\n"
        output += f"Due Date: \t\t\t{split_data[4]}\n"
        output += f"Is completed:\t\t {split_data[5]}\n"
        output += "\n"

        if split_data[0] == username_entry:
            my_task_menu()
            #tk.Label(view_my_tasks_window, text=output).grid(row=1, column=0)
        else:
            tk.Label(view_my_tasks_window, text="There are no tasks assigned to you.").grid(row=1, column=0)

        view_my_tasks_window.mainloop()





def validate_and_save_task(window):
    # Retrieve task details from entry fields

    assigned_user = task_assign_entry.get()
    task = task_entry.get()
    assign_date = assigned_date_entry.get()
    is_completed = is_completed_entry.get()
    task_desc = task_desc_entry.get()
    due_date = due_date_entry.get()

        # Validate task details
    if assigned_user not in user_names:
        tk.Label(window, text="Error: Assigned user does not exist").grid(row=4, column=0)
        return
    #try:
        #datetime.strptime(due_date, '%m/%d/%Y')
    #except ValueError:
        #tk.Label(window, text="Error: Invalid date format").grid(row=4, column=0)
        #return

        # Save task to file
    with open('tasks1.txt', 'a') as tasks_file:
        tasks_file.write('\n' + assigned_user + ', ' + task + ', ' + task_desc + ', ' + due_date + ', ' + assign_date + ', ' + is_completed + "\n")
    window.destroy()



while True:
    login()
    menu()
    break





