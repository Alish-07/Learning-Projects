# Question List
listq = [ "What is the capital of France?", "Who was the first president of the United States?", "Who painted the Mona Lisa?", "Who wrote the novel To Kill a Mockingbird?", "In what year did World War II end?", "What is the largest ocean in the world?", "Who discovered penicillin?", "What is the smallest country in the world by land area?", "What is the chemical symbol for gold?", "What is the name of the first man to walk on the moon?"]
# Answer List
lista = [ "Paris", "George Washington", "Leonardo da Vinci", "Harper Lee", "1945", "Pacific Ocean", "Alexander Fleming", "Vatican City", "Au", "Neil Armstrong"]
# Wrong Options lists
listw1 = [ "Marseille", "Thomas Jefferson", "Michelangelo", "Mark Twain", "1939", "Atlantic Ocean", "Isaac Newton", "Maldives", "Ag", "Buzz Aldrin"]
listw2 = [ "Lyon", "Barack Obama", "Raphael", "Ernest Hemingway", "1944", "Indian Ocean", "Louis Pasteur", "Bahrain", "Al", "Michael Collins"]
listw3 = [ "Bordeaux", "John Adams", "Titian", "F. Scott Fitzgerald", "1941", "Arctic Ocean", "Albert Einstein", "Monaco", "Ar", "Edwin Aldrin"]
options = [lista,listw1,listw2,listw3]

import random
jpt = input("\nEnter any key to start: ")
print("\n******Welcome******\n You can skip one question.\n Type 'help' for hint \n")

q = 0
h = 1
noofque = len(listq)

while q<noofque:
    n = random.sample(range(1,5), 4)
    p = n.index(1) + 1
    print("*****************")
    print(f"Q{q+1}) ",end="")
    print(listq[q])
    for j in range(4):
            print(f"{j+1} ",end=" ")
            a = n[j]
            if a == 1:
                print(lista[q])
            elif a == 2:
                print(listw1[q])
            elif a == 3:
                print(listw2[q])
            elif a == 4:
                print(listw3[q])

    ans = input("Enter the option no: ")
    ans = ans.lower()
    if ans == "help":
        if h == 1:
            print(f"Hint: {lista[q]} \n")
            h = h - 1
        else:
            print("Hint Already Used \n")   
    
    elif ans != "1" and ans != "2" and ans != "3" and ans != "4":
        print("Invalid input \nStart Again \n")
        break
    else:
        ans = int(ans)
        if ans == p:
            print("\nCongratulations")
            q = q + 1
            print(f"Your Score is {q}/{noofque} \n ")
            if q == noofque:
                 print("You Won\n")
        else:
            print(f"Wrong Answer.\nCorrect answer is: {lista[q]}")
            print(f"Your Final Score is {q}/{noofque} \n")
            break
