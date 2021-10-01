import os
import random
import string

def password_generator():
    gen_pass = ''
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    both = lower + upper
    digit = string.digits
    symbols = string.punctuation
    print("\n")
    print("Welcome to my Password Generator!!")
    print("-"*20)
    print("\n")
    print("Password Strength:\n1. Easy\n2. Medium\n3. Hard")
    strength = int(input("Choose your option: "))
    pass_num = False 
    if strength == 1:
        n_choice = input("Do you want any digit in your password?\n-- 'y' for yes and 'n' for no: ").upper()
        if n_choice == 'Y':
            pass_num = True
        length = int(input("How many characters do you want in your password?: "))
        if not pass_num:
            for i in range(length):
                gen_pass += random.choice(both)
        
        elif pass_num:
            nums = random.randint(2, 4)
            length -= nums
            for i in range(nums):
                gen_pass += random.choice(digit)
            for j in range(length):
                gen_pass += random.choice(lower)
    
    elif strength == 2:
        pass_num = True
        length = 0
        while length < 8:
            length = int(input("How many characters do you want in your password? "))
            print("\nA password should have a minimum of 8 characters!")
        if length >=8 and length<= 12:
            nums = random.randint(3, 4)
            length -= nums
            for i in range(nums):
                gen_pass += random.choice(digit)
            for i in range(length):
                gen_pass += random.choice(both)
        elif length > 12:
            length -= 5
            for i in range(5):
                gen_pass += random.choice(digit)
            for i in range(length):
                gen_pass += random.chocie(both)

    elif strength == 3:
        length = 0
        while length < 8:
            length = int(input("How many characters do you want in your password? "))
            print("\nA password should have a minimum of 10 characters!")
        if length >=10 and length <=12:
            nums = random.randint(3, 4)
            length -= nums
            for i in range(nums):
                gen_pass += random.choice(digit)
            syms = 3
            length -= syms
            for i in range(syms):
                gen_pass += random.choice(symbols)
            for i in range(length):
                gen_pass += random.choice(both)

    gen_pass = list(gen_pass)
    random.shuffle(gen_pass)
    return ''.join(gen_pass)


def registration():
    print("\n")
    print("Registration Page: ")
    print("-"*20)
    user_name = input("Username: ")
    pass_option = input("Do you want me to suggest you a password?\n--'y' for yes and 'n' for no: ").upper()
    if pass_option == 'Y':
        password = password_generator()
        print(f"Your password is {password}")
    else:
        password = input("Enter your password: ")

    file = open("D:\\Programming\\Python\\login\\docs.txt", "a")
    file.write(f"\n{user_name},{password}")
    print("-"*20)
    print("Your Registration is Successful!!")


def login():
    logged_in = False
    print("\n")
    print("Login Page:")
    print("-"*16)
    user_name = input("Username: ")
    password = input("Password: ")
    file = open("D:\\Programming\\Python\\login\\docs.txt", "r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if (a == user_name and b == password):
            logged_in = True
            break 
    if logged_in:
        print("Login Successful!!")
    else:
        print("Incorrect Username or Password")

print("-"*25)
print("""Welcome to my first project!!
It can Generate a password for you
there is also a registration and login system also!!!""")
print("-"*15)
options = int(input("What do you want to do?\n1. Login\n2. Register Account\nOption: "))
if options == 1:
    login()
elif options == 2:
    registration()
