# This is to test python's writing to files

test_file = open("test.txt", "w")

# Lets try iterating numbers 1-100 in a text file

for i in range(1, 101):
    num = str(i)
    test_file.write(num+"\n")

test_file.close()
