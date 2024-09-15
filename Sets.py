# Set is a data type in python used to store several items in a single variable
x=set()
s={4,32,2,2}
s2={'asd','vdch',4,32,2}
print(s)
# to add in a set
s.add(5)
print(s)
# to remove any element
s.remove(32)
print(s)
# to check element is in set or not
# set is faster then list
print(2 in s)
# add to list
print(s.union(s2))
# diffrence between two sets
print(s.difference(s2))
# intersection
print(s.intersection(s2))