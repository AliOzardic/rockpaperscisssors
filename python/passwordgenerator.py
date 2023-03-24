import random
import string

characters = list(string.ascii_letters + string.digits +">£#!]")



def password_generator():
    #make sure password length is atleast 4 characters
    while True:
        print("Password length should atleast be 4")
        length = int(input("How long do you want your password to be: "))
        if length > 4:
            break
    random.shuffle(characters)
    
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    #turn the list into a string
    password = "".join(password)
    print(f"Your password is :{password}")
   
if input("Do you want to create a password (y or n): ") == "y":
    print()
    password_generator()
    
else:
    quit()
        