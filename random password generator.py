# Ask user if they want to generate a password or not
# If yes, ask for password lenght
# Generate password
# Print password
# If initial response is no, exit program


import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()?><.,`~_+=-';.,/{}[]" + " ")

def generate_password():
    password_lenght = int(input("Ikiwe refu aje? "))

    random.shuffle(characters)

    password = []

    for x in range(password_lenght):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Unadai password? (Yes/Zii) :")

if option == "Yes":
    generate_password()
elif option == "Zii":
    print("Ni sawa Boss")
    quit()
else:
    print("Hizo ndyo gani Boss,weka Yes ama Zii")
    quit()