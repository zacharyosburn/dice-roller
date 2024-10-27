import random

print(f'Choose which die you would like to roll:\n1. D100\n2. D20\n3. D10\n4. D8\n5. D6\n6. D4\n', end = '')
print('\nEnter "q" or "done" if you would like to quit the program')

i = input('Enter the number for the corresponding die, or the name of the die you want to roll: ')

while i != 'q':

    if i == 'done':
        break
    roll_list = []

    # Rolling D100s

    if i == 'D100':
        j = int(input('Enter the number of D100s you would like to roll: '))
        for i in range(j):
            
            z = random.randint(1, 100)
            roll_list.append(z)

            x = sum(roll_list)

            print(f'{z} ', end = '')
        print(f'\nThat is a total roll of {x}!\n')
        
        i = input('Enter "q" or "done" if you would like to close the program.\nEnter the number for the corresponding die, or the name of the die you want to roll: ')

    elif i == '1':
        j = int(input('Enter the number of D100s you would like to roll: '))
        for i in range(j):
            
            z = random.randint(1, 100)
            roll_list.append(z)

            x = sum(roll_list)

            print(f'{z} ', end = '')
        print(f'\nThat is a total roll of {x}!\n')
        
        i = input('Enter "q" or "done" if you would like to close the program.\nEnter the number for the corresponding die, or the name of the die you want to roll: ')

    # Rolling D20s

    elif i == 'D20':
        j = int(input('Enter the number of D20s you would like to roll: '))
        for i in range(j):
            
            z = random.randint(1, 20)
            roll_list.append(z)

            x = sum(roll_list)

            print(f'{z} ', end = '')
        print(f'\nThat is a total roll of {x}!\n')
        
        i = input('Enter "q" or "done" if you would like to close the program.\nEnter the number for the corresponding die, or the name of the die you want to roll: ')

    elif i == '2':
        j = int(input('Enter the number of D20s you would like to roll: '))
        for i in range(j):
            
            z = random.randint(1, 20)
            roll_list.append(z)

            x = sum(roll_list)

            print(f'{z} ', end = '')
        print(f'\nThat is a total roll of {x}!\n')
        
        i = input('Enter "q" or "done" if you would like to close the program.\nEnter the number for the corresponding die, or the name of the die you want to roll: ')

    # Rolling D10s
    
    elif i == 'D10':
        j = int(input('Enter the number of D10s you would like to roll: '))
        for i in range(j):
            
            z = random.randint(1, 10)
            roll_list.append(z)

            x = sum(roll_list)

            print(f'{z} ', end = '')
        print(f'\nThat is a total roll of {x}!\n')
        
        i = input('Enter "q" or "done" if you would like to close the program.\nEnter the number for the corresponding die, or the name of the die you want to roll: ')

    elif i == '3':
        j = int(input('Enter the number of D10s you would like to roll: '))
        for i in range(j):
            
            z = random.randint(1, 10)
            roll_list.append(z)

            x = sum(roll_list)

            print(f'{z} ', end = '')
        print(f'\nThat is a total roll of {x}!\n')
        
        i = input('Enter "q" or "done" if you would like to close the program.\nEnter the number for the corresponding die, or the name of the die you want to roll: ')

    # Rolling D8s

    elif i == 'D8':
        j = int(input('Enter the number of D8s you would like to roll: '))
        for i in range(j):
            
            z = random.randint(1, 8)
            roll_list.append(z)

            x = sum(roll_list)

            print(f'{z} ', end = '')
        print(f'\nThat is a total roll of {x}!\n')
        
        i = input('Enter "q" or "done" if you would like to close the program.\nEnter the number for the corresponding die, or the name of the die you want to roll: ')

    elif i == '4':
        j = int(input('Enter the number of D8s you would like to roll: '))
        for i in range(j):
            
            z = random.randint(1, 8)
            roll_list.append(z)

            x = sum(roll_list)

            print(f'{z} ', end = '')
        print(f'\nThat is a total roll of {x}!\n')
        
        i = input('Enter "q" or "done" if you would like to close the program.\nEnter the number for the corresponding die, or the name of the die you want to roll: ')

    # Rolling D6s

    elif i == 'D6':
        j = int(input('Enter the number of D6s you would like to roll: '))
        for i in range(j):
            
            z = random.randint(1, 6)
            roll_list.append(z)

            x = sum(roll_list)

            print(f'{z} ', end = '')
        print(f'\nThat is a total roll of {x}!\n')
        
        i = input('Enter "q" or "done" if you would like to close the program.\nEnter the number for the corresponding die, or the name of the die you want to roll: ')

    elif i == '5':
        j = int(input('Enter the number of D6s you would like to roll: '))
        for i in range(j):
            
            z = random.randint(1, 6)
            roll_list.append(z)

            x = sum(roll_list)

            print(f'{z} ', end = '')
        print(f'\nThat is a total roll of {x}!\n')
        
        i = input('Enter "q" or "done" if you would like to close the program.\nEnter the number for the corresponding die, or the name of the die you want to roll: ')

    # Rolling D4s

    elif i == 'D4':
        j = int(input('Enter the number of D4s you would like to roll: '))
        for i in range(j):
            
            z = random.randint(1, 4)
            roll_list.append(z)

            x = sum(roll_list)

            print(f'{z} ', end = '')
        print(f'\nThat is a total roll of {x}!\n')
        
        i = input('Enter "q" or "done" if you would like to close the program.\nEnter the number for the corresponding die, or the name of the die you want to roll: ')

    elif i == '6':
        j = int(input('Enter the number of D4s you would like to roll: '))
        for i in range(j):
            
            z = random.randint(1, 4)
            roll_list.append(z)

            x = sum(roll_list)

            print(f'{z} ', end = '')
        print(f'\nThat is a total roll of {x}!\n')
        
        i = input('Enter "q" or "done" if you would like to close the program.\nEnter the number for the corresponding die, or the name of the die you want to roll: ')

    else:
        print(f'Please enter a valid type of die :)')
        break
        
        