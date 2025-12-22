a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourt number: "))

if(a>b and a>c and a>d):
    print("A is the greatest number")
elif(b>a and b>c and b>d):
    print("B is the greatest number")
elif(c>a and c>b and a>d):
    print("C is the greatest number")
else:
    print("D is the greatest number")

    
