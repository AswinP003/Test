import cmath
a=int(input("Enter the coefficient of x squared:"))            
b=int(input("Enter the coefficient of x:"))
c=int(input("Enter the constant:"))
#discriminant
d =(b**2)-(4*a*c)
if d>0:
    print("The roots are real and distinct")
elif d==0:
    print("The roots are real and equal")
elif d<0:
    print("The roots are imaginary")

# find two roots
r1 = (-b-cmath.sqrt(d))/(2*a)
r2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(r1,r2))
