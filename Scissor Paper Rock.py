import random
import time
play = True

def spr(a):
    if a == 1:
        dis = "Scissor"
    elif a ==2:
        dis = "Paper"
    elif a ==3:
        dis = "Rock"
    else:
        print("Invalid Input")
        exit()
    return dis

def result(rn,c):
    
    if rn-c == 0:
        rslt = "Draw" 
    elif rn-c == 1 or rn-c == -2:
        rslt = "You Win"
    elif rn-c == 2 or rn-c == -1:
        rslt = "You Lose"
    return rslt

def algo():
    # User input 
    c = input("Enter 1 for Scissor\nEnter 2 for Paper\nEnter 3 for Rock\nEnter::")
    if c == "1" or c == "2" or c =="3":
        c = int(c)
    else:  
        print("invalid input")
        exit()

    # Display
    time.sleep(0.75)
    print(f"\nYour Choice: \n{spr(c)}")
    time.sleep(1.5)

    print("Computer Choice: ")
    for i in range(0,30):
        rn = random.randint(1,3)
        print(f"{spr(rn)}   \r",end ="",flush=True)
        time.sleep(0.1)
    print(f"{spr(rn)}   \r")
    

    time.sleep(1)
    print(f"Result:: {result(rn,c)} \n")

while play == True:
    algo()
    time.sleep(0.5)
    ag = input("Enter p to play again ")
    
    if ag.lower() != "p":
        print("Thank You for playing")
        play = False
    else:
        time.sleep(1)
        print("\nNew Game")
 
    

