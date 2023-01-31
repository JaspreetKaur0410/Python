#Coding Exercise 3
# Please download the members.txt file from the resources of this article.
#
# Then, create a program that, whenever executed, asks the user to enter a new member in the command line:
#
#
# Then, the member is added to members.txt. In this case, the text file content would be:
#
# John Smith
#
# Sen Lakmi
#
# Sono Octonot
#
# Solomon Right
#
#first open file, read contents, add newly added member to contents and then write into the file
while True:
    member = input("Add a new member")
    file = open("files/members.txt",'r')
    contents = file.readlines()
    contents.append(member)
    file.close()
    file_1 = open("files/members.txt",'w')
    file_1.writelines(contents)
    file_1.close()