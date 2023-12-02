# // Creating a list
l1 = ["Aman", 2, 13, "Alash", True]
print(l1)
print(type(l1))   # class - List

l = [1, 4, 2, 2, 3, 0]
l.reverse()
print(l)
l.append(8)
print(l)
l.sort()
print(l)
l.insert(3, 99)
print(l)
l.remove(4)
print(l)
print(l.pop(0))        # It returns the value of the popped element
print(l.index(2))      # It returns the index of the first occurence of the element
print(l.count(2))      # It returns the total no of occurence of the element



#  // Creating  a tuple
t=()        # Initialisation of an empty touple
print(t)    # Here it will print an empty touple
t1=(1,)     # Comma is imp to initialise a touple with single value.
print(t1)
t2=(1,2,2,3)  #Tuple is an immutable(not changable) datatype so we cannot make changes to elements of touple once it is defined.
print(t2)
print(t2.count(2))  # retuns total occurence of 2
print(t2.index(2))  # it will return the first occurence index of 2.

