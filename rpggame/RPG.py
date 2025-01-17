from random import randint


def dice_roll() -> int:
    roll = randint(1, 6)
    roll2 = randint(1, 6)
    roll3 = randint(1, 6)
    all_dice = roll + roll2 + roll3
    return all_dice


def rpg_game():
    print('~Welcome to Wizard Coast RPG.~')
    print('~You wake up in a dark and damp room.~')
    print('~You see a wooden door with metal bars for a window with a dim light coming in.~')

    main_location = 'Dungeon'
    current_location = 'Starting room'
    inventory = []
    equipped = []
    defeated_enemy = []
    player_alive = True
    gold = 0

    while player_alive:
        if current_location == 'Starting room':
            print(
                'What do you do:\n1.Look around the room.\n2.Look through the window.\n3.Open the door.\n4.Yell for '
                'help.\n5.Look in inventory')

            choice = input('What is your choice: ')
            while True:
                if choice == '1':
                    print(
                        'There are a few places you can look at.\n1.Table'
                        '\n2.Bed\n3.Toilet bowl\n4.Stop looking around.')
                    look_choice = input('Where do you want to look: ')

                    if look_choice == '1':
                        if 'Old Bread' in inventory:
                            print('There is nothing else on the table.')
                            continue
                        print('You look at the table. There is an old chunk of moldy bread.')
                        inventory.append('Old Bread')
                        print('Old bread added to your inventory')
                        continue
                    elif look_choice == '2':
                        if 'Unlit Torch' in inventory:
                            print('There is nothing else to find.')
                            continue
                        print(
                            'You take a look at the broken bed. At first glance there is nothing interesting on the '
                            'bed,\nbut after further inspection you find a wooden torch with old, oily cloth wrapped '
                            'around it.')
                        inventory.append('Unlit Torch')
                        print('Unlit torch added to your inventory')
                        continue
                    elif look_choice == '3':
                        if 'Shit Covered Mushroom' in inventory:
                            print("It's just shit.")
                            continue
                        print("You look at the toilet bowl, which is filled with shit and urine from the previous"
                              "visitors. You see a few stems of mushroom growing out of the pile of shit.")
                        mushroom = input('Do you pick the mushrooms?(y/n): ')
                        if mushroom == 'y':
                            inventory.append('Shit Covered Mushroom')
                            print('Shit Covered Mushroom added to your inventory')
                        else:
                            print('Might be for the best.')
                            continue
                        continue
                    else:
                        break

                elif choice == '2':
                    print('You see a dimly lit corridor with the shadow of an unknown figure in the distance.')
                    break
                elif choice == '4':
                    if 'Skeleton' in defeated_enemy:
                        print('There is no answer.')
                        break
                    print('You hear loud and metalic footsteps getting closer. All of a sudden the door slams '
                          'open\nand you see a sceleton in metal armor.')
                    print('What do you do?\n1.Punch\n2.Kick\n3.Run\n4.Look in inventory')
                    fight_choice = input('What is your choice?: ')

                    if fight_choice == '1':
                        roll_fight = dice_roll()
                        if 'A Nice High' in equipped:
                            roll_fight += 2
                        elif 'Poisoning' in equipped:
                            roll_fight -= 2
                            print(f'You rolled {roll_fight}')

                        if roll_fight >= 10:
                            print('You killed the enemy.')
                            inventory.append('Rusty Sword')
                            print('Rusty Sword added to inventory.')
                            defeated_enemy.append('Skeleton')
                            print('You found 5 Gold')
                            gold += 5
                            break
                        else:
                            print('You died.')
                            player_alive = False
                            break
                    if fight_choice == '2':
                        roll_fight = dice_roll()
                        if 'A Nice High' in equipped:
                            roll_fight += 2
                        elif 'Poisoning' in equipped:
                            roll_fight -= 2
                        print(f'You rolled {roll_fight}')

                        if roll_fight >= 8:
                            print('You killed the enemy.')
                            inventory.append('Rusty Sword')
                            print('Rusty sword added to inventory.')
                            defeated_enemy.append('Skeleton')
                            print('You found 5 Gold')
                            gold += 5
                            break
                        else:
                            print('You died.')
                            player_alive = False
                            break
                    if fight_choice == '3':
                        print("You're in a room, where are you running?")
                        print('You cornered yourself and the skeleton caught you.')
                        print('You died.')
                    if fight_choice == '4':
                        print(f'In your inventory you have {inventory}')

                elif choice == '5':
                    print(f'In your inventory you have {inventory} and {gold} Gold')
                    inv_choice = input('Would you like to use something?(Hint: Write an item or write "No"): ').lower()
                    if inv_choice == 'old bread':
                        print('You found a Rusty Key in the bread.')
                        inventory.remove('Old Bread')
                        inventory.append('Rusty Key')
                        print('Rusty Key added to inventory.')
                        print('Old Bread removed from inventory.')
                        break
                    elif inv_choice == 'unlit torch':
                        print('You need fire to light it')
                        torch = input('Would you like to equip it?(y/n): ')
                        if torch == 'y' and 'Rusty Sword' not in equipped:
                            inventory.remove('Unlit Torch')
                            equipped.append('Unlit Torch')
                        elif 'Rusty Sword' in equipped:
                            swap = input('Would you like to swap the Rusty Sword for an Unlit Torch?(y/n): ')
                            if swap == 'y':
                                print('You unequipped the Rusty Sword and equipped the Unlit Torch.')
                                equipped.remove('Rusty Sword')
                                inventory.append('Rusty Sword')
                                inventory.remove('Unlit Torch')
                                equipped.append('Unlit Torch')
                        else:
                            continue
                    elif inv_choice == 'shit covered mushroom':
                        inv_mush = input('Do you want to eat the Shit Covered Mushroom?(y/n): ')
                        if inv_mush == 'y':
                            print('Shit Covered Mushroom removed from inventory')
                            inventory.remove('Shit Covered Mushroom')
                            roll_mush = dice_roll()
                            if roll_mush == 18:
                                print('You feel an odd sensation.')
                                equipped.append('A Nice High')
                            else:
                                print("You don't feel so good.")
                                equipped.append('Poisoning')
                    elif inv_choice == 'rusty sword':
                        print('This sword has seen better days.')
                        sword = input('Would you like to equip it?(y/n): ')
                        if sword == 'y' and 'Unlit Torch' not in equipped:
                            inventory.remove('Rusty Sword')
                            equipped.append('Rusty Sword')
                        elif 'Unlit Torch' in equipped:
                            swap = input('Would you like to swap the Unlit Torch for a Rusty Sword?(y/n): ')
                            if swap == 'y':
                                print('You unequipped the Unlit Torch and equipped the Rusty Sword.')
                                equipped.remove('Unlit Torch')
                                inventory.append('Unlit Torch')
                                inventory.remove('Rusty Sword')
                                equipped.append('Rusty Sword')
                    break

                elif choice == '3':
                    if 'Rusty Key' in inventory or 'Skeleton' in defeated_enemy:
                        print('You have unlocked the door!\n1.Leave the room.\n2.Stay in the room.')
                        room_choice = input('What do you do?: ')
                        if room_choice == '2':
                            break
                        elif 'Skeleton' in defeated_enemy:
                            current_location = 'First corridor'
                            break
                        else:
                            print('As you leave the room the shadowy figure notices you and charges straight at you.')
                            print('What do you do?\n1.Punch\n2.Kick\n3.Run\n4.Look in inventory')
                            fight_choice = input('What is your choice?: ')

                            if fight_choice == '1':
                                roll_fight = dice_roll()
                                if 'A Nice High' in equipped:
                                    roll_fight += 2
                                elif 'Poisoning' in equipped:
                                    roll_fight -= 2
                                print(f'You rolled {roll_fight}')
                                if roll_fight >= 10:
                                    print('You killed the enemy.')
                                    inventory.append('Rusty sword')
                                    print('Rusty sword added to inventory.')
                                    defeated_enemy.append('Skeleton')
                                    current_location = 'First corridor'
                                    break
                                else:
                                    print('You died.')
                                    break
                            if fight_choice == '2':
                                roll_fight = dice_roll()
                                if 'A Nice High' in equipped:
                                    roll_fight += 2
                                elif 'Poisoning' in equipped:
                                    roll_fight -= 2
                                print(f'You rolled {roll_fight}')
                                if roll_fight >= 8:
                                    print('You killed the enemy.')
                                    inventory.append('Rusty sword')
                                    print('Rusty sword added to inventory.')
                                    defeated_enemy.append('Skeleton')
                                    current_location = 'First corridor'
                                    break
                                else:
                                    print('You died.')
                                    player_alive = False
                                    break
                    else:
                        print('The door requires a key to open.')
                        break
                else:
                    print('Pick an available choice')
                    break
        if current_location == 'First corridor':
            print('You escaped your prison. What now?\n1.Look around\n2.Continue down the corridor\n3.Go back to the'
                  ' first room\n4.Look in your inventory')
            choice1 = input('What do you do?: ')
            if choice1 == '1':
                print('You look around the long corridor. Outside of the door at the end of it and the lit torch on the'
                      'wall, there is nothing else.\n1.Look at the door\n2.Look at the lit torch\n3.Stop '
                      'looking around\n4.Look around again')
                look_choice1 = input('What do you do?: ')
                if look_choice1 == '1':
                    print('Just a steel reinforced wooden door.')
                if look_choice1 == '2':
                    if 'Unlit Torch' in inventory:
                        print("It's a lit torch, just like the one you have.")
                        torch_choice_inv = input('Would you like to light your torch?(Hint: Lighting your torch would '
                                                 'equip it.)(y/n): ')
                        if torch_choice_inv == 'y':
                            inventory.remove('Unlit Torch')
                            equipped.append('Lit Torch')
                            print('You now see better in the dark.')
                        else:
                            continue
                    elif 'Unlit Torch' in equipped:
                        print("It's a lit torch, just like the one you have.")
                        torch_choice_equip = input(
                            'Would you like to light your torch?(y/n): ')
                        if torch_choice_equip == 'y':
                            equipped.remove('Unlit Torch')
                            equipped.append('Lit Torch')
                            print('You now see better in the dark.')
                    else:
                        print("It's a lit torch.")
                        new_torch = input('Would you like to take it?(y/n): ')
                        if new_torch == 'y':
                            print('You have equipped the Lit Torch.')
                            equipped.append('Lit Torch')

rpg_game()
