names = ["Rita","Getta","Setta","Ram"]
names_sort = [names.sort()]
for index,item in enumerate(names):
    print(index,'-',item)

# enumerate is a list of tuples
print(enumerate(names))
print(list(enumerate(names)))

# SORT LIST
#The sort() method has no return value and directly modifies the original list, changing the order of the elements contained in it.
print(f"Sorted LIST: {names_sort}")

print()
# You have to use as many variables as there are items in the internal tuples or lists
# Note that the enumerate function always produces a sequence of tuples each containing two items.
# Therefore, when using enumerate, you have to use two variables, not less, not more.
buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
for first, second, third in buttons:
    print(first, second, third)