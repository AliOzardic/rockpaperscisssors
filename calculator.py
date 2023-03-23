def add(a,b):
    answer = a+b
    print(f"Your answer is:  {answer}" + " /n")

def sub(a,b):
    answer = a - b
    print(f"Your answer is:  {answer}" +" /n")
       
def multi(a,b):
    answer = a*b
    print(f"Your answer is:  {answer}" +" /n")
    
def div(a,b):
    answer = a/b
    print(f"Your answer is:  {answer}" +" /n") 
    
def mod(a,b):
    answer = a%b
    print(f"Your answer is:  {answer}" +" /n")
 
while True:
    print("A for addition")
    print("B for substraction")
    print("C for multiplication")
    print("D for division")
    print("E for mod")
    print("F for exit")
    operation = input("Enter the operation you want to execute: ").upper()
    

    if operation == "A":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        add(a,b)
    elif operation =="B":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        sub(a,b)
    elif operation =="C":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        multi(a,b)
    elif operation =="D":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        div(a,b)
    elif operation =="E":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        mod(a,b)
    elif operation =="F":
        quit()
    else:
        quit()