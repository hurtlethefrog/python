def car():
    switcher = {
        'help':'''
        start - to start the car
        stop - to stop the car
        exit - exit program
        ''',
        'start': "Car started, let's go G2\n",
        'stop': "You stopped the car\n",
        'exit': False
    }
    action = input("you're sitting in a car, what do you do?\n")
    while action != 'exit':
        if action == 'start' or action == 'stop' or action == 'help':
            action = input(switcher[action]).lower()
        else:
            action = input("You can't do that, try \'help\' to see your options!\n").lower()
car()
