# Write a program in Python to check whether a number is palindrome or not using iterative method.
n =input("Enter the number: ")
s=n
rev=n[::-1]
if(s==rev):
    print("palindrome")
else:
    print("not palindrome")