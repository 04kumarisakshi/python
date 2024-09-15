# Write a program to reverse an integer in Python.
n=int(input("Enter number : "))
print("befour reverse: ", n)
reverse=0
while(n!=0):
    last=n%10
    reverse=reverse*10+last
    n=n//10
print(reverse)   

# second method
s=input("Enter number : ")
print("befour reverse: ", s)
rev=s[::-1]
print(rev)