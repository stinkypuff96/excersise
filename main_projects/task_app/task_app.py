import json
import os


tasks = []
done_tasks = []

file_name = input('Enter the name of the file: ').strip()

if not file_name.endswith('.json'):
    file_name += '.json'

if os.path.exists(file_name):
    print(f"Loading tasks from '{file_name}'...")
    with open(file_name, 'r') as file:
        data = json.load(file)
        tasks = data.get('tasks', [])
        done_tasks = data.get('done_tasks', [])
else:
    print(f"Creating new task file '{file_name}'")

def save_tasks():
    with open(file_name, 'w') as file:
        json.dump({'tasks': tasks, 'done_tasks': done_tasks}, file)

while True:
    u_inp = input(str('What do you want to do(1. Add task/2. Did task/3. Remove task/4. Read task list'
                      '/5. Quit/6. Delete file): '))

    if u_inp == '1':
        task_inp = input('Add a new task: ')
        tasks.append(task_inp)
        save_tasks()
    elif u_inp == '2':
        print('Which task did you complete?')
        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task}')
        done_inp = input('Enter number: ')
        if done_inp.isdigit() and 1 <= int(done_inp) <= len(tasks):
            done_task = tasks.pop(int(done_inp) - 1)
            done_tasks.append(done_task)
            print(f'{done_task} is done!')
            save_tasks()
        else:
            print('Task not found. Please enter a valid task.')
    elif u_inp == '3':
        print('Which task do you want to remove: ')
        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task}')
        remove_inp = input('Enter number: ')
        if remove_inp.isdigit() and 1 <= int(remove_inp) <= len(tasks):
            remove_task = tasks.pop(int(remove_inp) - 1)
            print(f'{remove_task} is removed!')
            save_tasks()
        else:
            print('Task not found. Please enter a valid task.')
    elif u_inp == '4':
        print('Tasks:')
        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task}')
        if len(done_tasks) > 0:
            print('Done Tasks:')
            for i, done_task in enumerate(done_tasks, 1):
                print(f'{i}. {done_task}')

    elif u_inp == '5':
        break
    elif u_inp == '6':
        confirm = input(f"Are you sure you want to delete '{file_name}'? This cannot be undone. (y/n):  ").lower()
        if confirm == 'y':
            try:
                os.remove(file_name)
                print(f"'{file_name}' has been deleted.")
                break
            except FileNotFoundError:
                print('File not found.')
            except Exception as e:
                print(f'Something went wrong: {e}')
        else:
            print('File deletion cancelled.')
    else:
        print('Invalid number. Try again!')