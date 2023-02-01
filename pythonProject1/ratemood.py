date = input("Enter Date")
mood = input("How do you rate you mood today from 1 to 10")
journal = input("Let your thoughts flow:\n")

with open(f"Journal/{date}.txt",'w') as file:
    file.write(mood +"\n")
    file.write(journal)