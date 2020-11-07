import time

print("Welcome to Making Toast")
print()



options = ["A", "B", "C", "D"]

def scene2():
    toast = ["butter", "butter", "butter"]

def secretending1():
    TOAST = []

def specialending():
    pass

def end():
    WASTED = []

def scene3():
    pass
def scene1():
    print("You woke up hungry for a early morning snack and head toward the kitchen to get and get ready to make a meal.")
    time.sleep(4)
    print("Man im hungry")
    time.sleep(4)
    print("Hmm i think im hungry for...")

    scene1 = input("What are you hungry for? \nA)Toast \nB)Toast \nC)Toast \n").upper()
    while scene1 not in options:
        scene1 = input("Not an Option. Choose  \nA)Toast \nB)Toast \nC)Toast \n")

    if scene1.upper() == "A":
        scene2()
    if scene1.upper() == "B":
        scene2()
    if scene1.upper() == "C":
        scene2()
    if scene1.upper() == "D":
        secretending1()

def scene2():
    print("You lay the toast on a plate and open the fridge to get")
    scene2 = input("What do you get?\nA) Butter \nB) Golden Butter \nC) Butter")
    
    while scene2 not in options:
        scene2 = input("Not an answer. Pick A, B, or C. What do you get?\nA) Butter \nB) Golden Butter \nC) Butter")

    if scene2.upper() == "A":
        scene3()
    if scene2.upper() == "C":
        scene3()
    elif scene2.upper() == "B":
        print("You are not worthy of Golden Butter, somehow you are dissentergrated")
        end()

def end():
    print("WASTED")

def secretending1():
    print("You some how get transported to the world of toast, where you see a sword in the stone. You reach for the sword and pull it out. You are named the king of toast and are assigned to slay evil with the sword called Toastcalibur")
    specialending()

def specialending():
    print("HAIL THE KING")

scene1()