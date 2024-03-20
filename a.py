n=int(input("Enter a number"))
for i in range(1,n+1):
    
        
    s=i+(i-1)
        
    for k in range(0,s):
        if k%2==0:
            print("*",end="")
        else:
            print(" ",end="")
    print("\r")