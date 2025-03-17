tasks = []
done_tasks = []

while True:
    u_inp = input(str('What do you want to do(1. Add task/2. Did task/3. Remove task/4. Read task list'
                      '/5. Quit): '))

    if u_inp == '1':
        task_inp = input('Add a new task: ')
        tasks.append(task_inp)

    elif u_inp == '2':
        print('Which task did you complete?')
        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task}')
        done_inp = input('Enter number: ')
        if done_inp.isdigit() and 1 <= int(done_inp) <= len(tasks):
            done_task = tasks.pop(int(done_inp) - 1)
            done_tasks.append(done_task)
            print(f'{done_task} is done!')
        else:
            print('Task not found. Please enter a valid task.')
    elif u_inp == '3':
        remove_inp = input('Which task do you want to remove: ')
        if remove_inp in tasks:
            tasks.remove(remove_inp)
            print(f'{remove_inp} has been removed from tasks.')
    elif u_inp == '4':
        print(tasks)
        print(done_tasks)
    elif u_inp == '5':
        break
    else:
        print('Invalid number. Try again!')