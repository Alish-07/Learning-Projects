import requests
import random

# API URL to fetch trivia questions
url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple"

# Make a GET request to the API
response = requests.get(url)

# Parse the response JSON data
data = response.json()
questions = data["results"]

# Store the questions and answers in lists
listq = [question["question"] for question in questions]
lista = [question["correct_answer"] for question in questions]
listw = [answer for question in questions for answer in question["incorrect_answers"]]

# Mix the incorrect answers with the correct answer
options = []
for i in range(len(listq)):
    options.append([lista[i]] + random.sample(listw[i*3:(i+1)*3], 3))

# Start the quiz
q = 0
noofque = len(listq)
while q < noofque:
    # Randomly choose the answer order
    n = random.sample(range(1, 5), 4)
    p = n.index(1) + 1
    
    print("*****************")
    print(f"Q{q + 1}) ", end="")
    print(listq[q])
    for j in range(4):
        print(f"{j + 1} ", end=" ")
        a = n[j]
        print(options[q][a - 1])
    
    # Get the user's answer
    ans = input("Enter the option no: ")
    if ans not in ["1", "2", "3", "4"]:
        print("Invalid input \nStart Again \n")
        break
    ans = int(ans)
    
    # Check the answer
    if ans == p:
        print("\nCongratulations")
        q = q + 1
        print(f"Your Score is {q}/{noofque} \n ")
        if q == noofque:
            print("You Won\n")
    else:
        print("Wrong Answer")
        print(f"Your Final Score is {q}/{noofque} \n")
        break
