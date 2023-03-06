number_list = []
while True:
    k = input("Type a for ascending \nType d for decending \n")
    k = k.lower()
    if k== "a":
        mode = False
        status = "Ascending order"
        break
    elif k== "d":
        mode = True
        status = "Decending order"
        break
    else:
        print("Invalid input, Try again")
i = int(input("How many numbers?"))
for l in range(i):
    num = int(input("Enter your number"))
    number_list.append(num)
print(status,sorted(number_list, reverse=True))
