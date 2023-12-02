# WAP to strore name of fruits entered by user in list
i=0
l=[]     # intialising an empty list
while i in range(2):
    a=input("Enter the name of a fruit:\n")
    l.append(a)
    i=i+1
print(l)


# Wap to accept the marks of 6 students and display them in a sorted manner.
l1=[]
i=0
while i in range(6):
    a=int(input("Enter your number:\n"))
    l.append(a)
    i=i+1
l.sort()
print(l)

# Check thet a topuple cannot be changed in python

t=(1,3,2,4)
# These are the function which not work with touple hence it is confirmed that it cannot be changed.
# t.insert(3,8)
# t.pop(4)
# t.remove(3)
# t.sort()
# t.append(4)
# t.reverse()
print("The touple is:\n",t)

# WAP to sum a list with 4 numbers
l3=[1,45,23,4]
i=0
s=0
a=0
# s = sum(l3)       # Can be directly printed by using "sum" function
# print(s)
while i in range(4):
      a=l3.pop()
      s=s+a
      i=i+1
print("\nThe sum of all elements of the list is:\n",s)
