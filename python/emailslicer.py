#define the slice fonction
def slicer():
    print( "Welcome to the email slicer")
    print()
    #get the user input and validate it
    while True:
        email = input("Enter your email: ")
        if "@" in email and "." in email:
            break
        else:
            print("enter a valid input")
    #split the mail from @
    (username , domain) = email.split("@")
    #split the domain and extension from .
    (domain ,extension) = domain.split(".")
    print(f"Username: {username}")
    print(f"Domain: {domain}")
    print(f"extension: {extension}")
#call the fonction in a while loop to use it many times
slicer()
while True:
    #ask the user to slice an another e mail
    if input("Do you want to slice an another email(y or n)").lower() == "y":
        slicer()
    else:
        break