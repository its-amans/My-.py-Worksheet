#  // Dictionary in python    .
# Dictionary in python will store key and value pair ..Cannot contain duplicate keys.


# d={"Aman":"Srivastava",
#    "Vaibhav":"Dwivedi",
#    "Aman":90,
#    "Vaibhav":92}       # if we use similar keys then it will only print the last declared duplicate key.
d={"Aman is :":"Srivastava",
   "Vaibhav is :":"Dwivedi",
   "Aman":90,
   "Vaibhav":92} 
print(d)
print(d.items())                     # IT will print the dictionary list in form of a tuple.
d.update({"Abhinav":"srivastava"})   # Updates the dictionary and makes adds it to the end.
print(d)
print(d.keys())                      # IT will print the dictionary keys in form of a tuple.
d.get("Aman is :")                 
print(d.get("Aman is :"))            # It will return the value at the key and if the key is not present then it will return None.
d.pop("Vaibhav is :")                # IT will pop the given key
print(d)
print(len(d))                        # print the length of the list.


# // set in python.
#Set is a collection of non repetative elements.

s=set()
# s.update({1})    # we can add elements to the set by uding update function also.
# print(s)
s.add(1)    # add function only takes one argument.
s.add(2)
s.add(2)    # Cannot add repetative values .
print(s) 
s=s.union({1,7,4})
print("After union with the aniother set the set is:\n",s)
print("The length of the set is:",len(s))
s.remove(7)
print("Set after removal of 7 is:\n",s)
s.pop()     # It will pop the first item of the set
print("Set after pop is:\n",s)
s=s.intersection({1,3,4,7})
print(s)
print("After clearing the set it returns empty set:\n",s.clear())   


