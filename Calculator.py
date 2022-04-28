from Cal_art import *
import os
print(logo)
Calculate = False

while not Calculate:
    num1 = int(input("First number?: "))
    for i in Operations_Dictionary:
        print(i)
    symbol = input("Pick an operation: ")
    function = Operations_Dictionary[symbol]
    num2 = int(input("Second number?: "))
    result = function(num1, num2)
    print(f'{num1} {symbol} {num2} = {result}')
    
    choice = input(f"Type 'y' if you want to continue clculation with {result}, or 'n' to start new one! Or 's' to stop: ")
    if choice == 's':
        Calculate = True
    elif choice == 'y':
        S = ""
        while S != 's':
            os.system('clear')
            # os.system('cls')
            symbol = input("Pick an operation: ")
            num3 = int(input("Another number?: "))
            function = Operations_Dictionary[symbol]
            result = function(result, num3)
            print(f'{result} {symbol} {num3} = {result}')
            S = input("Do you wanna continue calculating?Type 'y' if yes, 's' if not!: ")
        Calculate = True
    elif choice == 'n':
        os.system('clear')
        # os.system('cls')


input()
