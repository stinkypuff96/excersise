tasks = []
done_tasks = []

while True:
    u_inp = input(str('What do you want to do(1. Add task/2. Did task/3. Remove task/4. Read task list): '))

    if u_inp == '1':
        task_inp = input('Add a new task: ')
        tasks.append(task_inp)

    elif u_inp == '2':
        done_inp = input('Which task did you do?')
        if done_inp in tasks:
            print(f'{done_inp} is done!')
            tasks.remove(done_inp)
            done_tasks.append(done_inp)
    elif u_inp == '4':
        print(tasks)
        print(done_tasks)