import art
from replit import clear
def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mult (n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2

math_operation = {
"+" : add,
"-" : sub,
"*" : mult,
"/" : div,
}
def calculator():
  num1 = float (input("Input a first symbols\n"))
  more_cal = True
  for i in math_operation:
    print(i)
  answer = num1

  while more_cal:
    operation_symbols = input("Pick an operation: ")
    new_num = float (input("Input a next symbols\n"))
    last_answer = answer
    answer = math_operation[operation_symbols]  (last_answer, new_num)
    print (f"{last_answer} {operation_symbols} {new_num} = {answer}")
    load = input ("Type'y' to continue, or type 'n' to exit from thic calculation   and start new")
    if load == "n":
      more_cal = False  
      clear ()
      calculator()

calculator()