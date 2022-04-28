logo = '''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
\n\n'''



def add(number_1, number_2):
    return number_1 + number_2

def sub(number_1, number_2):
    return (number_1 - number_2)

def mult(number_1, number_2):
    return number_1*number_2

def div(number_1, number_2):
    return number_1/number_2
    
Operations_Dictionary = {
                    "+": add,
                    "-": sub,
                    "*": mult,
                    "/": div
                  }