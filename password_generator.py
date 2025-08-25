import random
import string
import os
import time
import sys

def generate_password():
    letters = random.choices(string.ascii_letters, k=4)
    digits = random.choices(string.digits, k=2)
    symbols = random.choices(string.punctuation, k=2)
    password_list = letters + digits + symbols
    random.shuffle(password_list)
    return ''.join(password_list)

def show_header():
    os.system("cls" if os.name == "nt" else "clear")
    print("="*40)
    print("     🔐 PASSWORD GENERATOR 🔐")
    print("="*40 + "\n")

def loading_animation(text="Generating password"):
    for i in range(3):
        sys.stdout.write("\r" + text + "." * (i+1))
        sys.stdout.flush()
        time.sleep(0.5)
    print("\n")

# langsung eksekusi program
show_header()
input("Press ENTER to generate your password...")
loading_animation("Generating password")
print("\nYour password is:\n")
print(generate_password())
print("\nUse it wisely")
