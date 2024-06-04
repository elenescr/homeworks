import math


def add_spaces(expr):

  operators = "+-*/^"
  result = ""
  for char in expr:
    if char in operators:
      result += f" {char} "
      expr = result
    else:
      result += char
      expr = result
  return expr


def calculate (i) :
    i= add_spaces(i)
    a = i.split()

    try: int(a[0])
    except (IndexError, ValueError):
        return "Error in input"

    try: int(a[2])
    except (IndexError, ValueError):
        return "Error in input"

    a[0] = int(a[0])
    a[2] = int(a[2])
    if a[2] == 0 and a[1]=='/':
        return "can't divide by 0 "
    elif a[1] == "+":
        return f"{i} = {a[0] + a[2]}"
    elif a[1] == "-":
        return f"{i} = {a[0] - a[2]}"
    elif a[1] == "/":
        return f"{i} = {a[0] / a[2]}"
    elif a[1] == "*":
        return f"{i} = {a[0] * a[2]}"
    else:
        return f"{i} = {a[0] ** a[2]}"


problem = input("Enter problem: ")
answer = calculate(problem)
print(answer)
