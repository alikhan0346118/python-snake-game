import random

def gamewin(Computer , Your):
    if Computer == Your:
        return None
    if Computer == 's':
        if Your == 'w':
            return False
        elif Your == 'g':
            return True
    if Computer == 'w':
        if Your == 'g':
            return False
        elif Your == 's':
            return True
    if Computer == 'g':
        if Your == 's':
            return False
        elif Your == 'w':
            return True



a=input("Computer  turn; Snake(s),Water(w) or gun(g)?")
randno = random.randint(1, 3)
print(randno)
if randno == 1:
    Computer == 's'
elif randno == 2:
    Computer == 'w'    
elif randno == 3:
    Computer == 'g'   
a=input("Your  turn; Snake(s),Water(w) or gun(g)?")

gamewin(Computer, Your)
print(f"computer  choose{computer}")
print(f"You choose{Your}")
if a == None:
    print("the game is tie")
elif a:
    print("you win")    
else:
    print("you loose")      