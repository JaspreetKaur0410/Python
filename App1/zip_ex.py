# The zip() function returns a zip object, which is an iterator of tuples where the first
# item in each passed iterator is paired together, and then the second item in each
# passed iterator are paired together etc.

contents = ["This is A", "This is B", "This is C"]
files = ["A.txt","B.txt","C.txt"]

for content,filename in zip(contents,files):
    file = open(f"files/{filename}",'w')
    file.write(content)