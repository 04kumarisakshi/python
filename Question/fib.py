# Write a program in Python to print the Fibonacci series using iterative method.

n =int(input("Enter the range"))
a=0
b=1

for i in range(0,n):
    if(i<=1):
     result=1
    else:
       result=a+b
       a=b
       b=result
    print(result)
