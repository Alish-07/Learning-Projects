
import os
file_path = "Library.txt"
if not os.path.exists(file_path):
    open(file_path, "w").close()

task = (input("Enter 1 to print all books\nEnter 2 to print no of books\nEnter 3 to add book\nChoice:: "))
if task =="1" or task =="2" or task =="3":
    task = int(task)
else:
    print("Invalid Input")

def no():    
    o = open("Library.txt","r")
    items = [o.strip() for o in o.readlines()]
    num_items = len(items)
    o.close()
    return num_items
    
# Print book
if task == 1:
    # print("working")
    o = open("Library.txt","r")
    r = o.read()
    print(r)
    o.close()

# No of books
elif task == 2:
    print(f"No of book is {no()}")
  
# # Add Book
elif task == 3:
    bk = input("Enter the Book name: ")
    o = open("Library.txt","a")
    o.write(f"{no()+1}.{bk}\n")
    o.close()


 
