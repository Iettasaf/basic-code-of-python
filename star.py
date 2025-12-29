'''
*
**
***
'''
n = int(input("Enter a number: "))
for i in range(1,n+1):
    #print(" "*(n-i),end="") #it's for space it calculate [(3-1) for first star][(2-1) for second star] if n=3 
    print("*"*(i),end="")
    print("")