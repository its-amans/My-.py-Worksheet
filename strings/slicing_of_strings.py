a= "Aman's"     # if a string starts with single qoute thwn it will end on the single quote only and it will ignore any single or double quote and just print it.
# b='aman""s'   # output:aman""s
print(a)

# // Concatenation of two strings
a="Good Night "
b="Honey"
c=a+b      #concatenation can be done by using +operator directely to strings.can be done with multiple strings also.
print(c)

# // Multiplication of strings

# print(a*3)      #it will print the string 3 times.


# // slicing of string
c="aman sri"          # note:space is also counted as a character.
# print(c[0:8])       #it will print the string from 0 to 7 index.
# print(c[:4])        #if the starting index is not given then by default it will take 0 as starting index.
# print(c[2:])        #if the ending index is not given then by default it will take the last index as ending index.
# print(c[0:5:2])     #The third parameter will decide  the skipping sequence like 2 indicates that it will skip 1 character and print the next character continiously


# // NEGATIVE INDEXES
# print(c[-1:-4])       #it will print nothing because the starting index is greater than the ending index.
# print(c[-4:-1])       #it will print the string from -4 to -2 index.refer the negative indexes by comparing it with the positive indexes.
print(c[::-2])          #it will print the string from the last index to the first index with the skipping sequence of 2.