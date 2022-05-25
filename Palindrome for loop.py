n=input("Enter the number:")
i=0
for i in range(len(n)):
    if n[i]!=n[-1-i]:
        print("The given number is not a palindrome")
        break
    else:
        print("The given number is a palindrome")
        break
