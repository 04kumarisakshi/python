x=["x",'asbh',1,2]
# print length
print(len(x))
# to append element at last
x.append('Sakshi')
# print(x)
#to extent the list
x.extend([1,2,3,4,5])
# print(x)
# to pop and print the last element from the list
print(x.pop())
# we can wrint the index for pop
print(x.pop(1))
# list are mutable
y=["sakshi",'hi',2]
# to copy the list in another list
z=y[:]
y[1]='kumari'
print(y,z)
# we can create list ,tuple inside a list
l=[[],(),[[],()] ,[1,2,3]]

# tuple= a  collection which is ordered and unchangeable /immutable list
t=('apple',8,20)
# no append or extend in tuple
# t.append('sakshi')
print(t[1])
