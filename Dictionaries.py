x={'key':4}
x['key2']=5
x[2]=[2,3,4,5]
print(x)
# to find element
print('key' in x)
# to print values in  dis
print(list(x.values()))
print(list(x.keys()))
# delete
del x['key']
print(x)
# for iterative 
for key,values in x.items():
    print(key,values)
# or
for key2 in x:
    print(key2,x['key2'])
for key in x:
    print(key)





