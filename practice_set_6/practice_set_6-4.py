# write a program to count the alphabet, digits and special characters in a string.
# Written by : Aman Srivastava
a=input("Enter the string:\n")
al=0
di=0
sp=0
for i in a:
    if i.isalpha():
        al+=1
    elif i.isdigit():
        di+=1
    else:
        sp+=1
print(f"Alphabets : {al}\nDigits : {di}\nSpecial Characters : {sp}\n")

# Output:
# Enter the string:
# Aman1234@#$%^&*()
# Alphabets : 4
# Digits : 4
# Special Characters : 8






# write a prog to count alphabet in your name using list
# Written by : Aman Srivastava
a=input("Enter your name:\n")
l=[]
for i in a:
    if i.isalpha():
        l.append(i)
print(f"Total alphabets in your name : {len(l)}\n")

