import time

print("Welcome to Making Toast")
print()


options = ["A", "B", "C"]

def start():
    print("You woke up hungry for a early morning snack and head toward the kitchen to get and get ready to make a meal.")
    time.sleep(3)
    print("Man im hungry")
    time.sleep(3)
    print("Hmm i think im hungry for...")

    scene1 = input("What are you hungry for? \nA)Toast \nB)Toast \nC)Toast \n").upper()

while scene1 not iin options:
    scene1 = input("Not an Option. Choose  \nA)Toast \nB)Toast \nC)Toast \n")

start() 