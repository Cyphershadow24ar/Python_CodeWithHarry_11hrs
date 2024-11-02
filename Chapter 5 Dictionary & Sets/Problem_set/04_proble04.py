#what will be the length of following set s:

s= set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(s)
print(len(s)) # here the length of the set is TWO.

#This behavior is part of Python's design to facilitate intuitive comparisons between numeric types. 
# In many programming languages, including Python, comparisons between integers and 
# floating-point numbers are often allowed and automatically handled by converting one type to the other as needed.