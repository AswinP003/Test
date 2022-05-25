a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=int(input("Enter the 3rd number: "))
if a>b:
    if a>c:
        print(a,"is the greatest number")
    else:
        print(c,"is the greatest number")
else:
    if(b>c):
        print(b,"is the greatest number")
    else:
        print(c,"is the greatest number")
