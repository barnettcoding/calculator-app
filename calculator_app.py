from webbrowser import get


logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(num1, num2):
  return num1 + num2

def subract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2



operations = {"+": add, "-": subract, "*": multiply, "/": divide}
print(logo)
num1 = int(input("What's the first number? "))

def check_if_keep_going():
  keep_going = input("'C' to continue, 'S' to stop  ").upper()
  if keep_going == 'S':
    print("Thank you for using the calculator")
  elif keep_going == 'C':
    choose_operator()
    num1 = answer
    num2 = int(input("What is the next number?  "))
    get_solution(num1, num2, functi_n)
  else:
    print("invalid response. Try again")
    check_if_keep_going()

    

def choose_operator():
  global functi_n
  for symbol in operations:
    print(symbol)
  functi_n = input("What math function would you like to perform? ")
  

choose_operator()

num2 = int(input("What's the second number? "))


def get_solution(num1, num2, functi_n):
  global solution
  global answer
  answer = operations[functi_n](num1, num2)
  solution = (f" {num1} {functi_n} {num2} = {answer}") 
  print(solution)
  check_if_keep_going()

get_solution(num1, num2, functi_n)

  
