num=int(input("Enter a number.\nWe'll check it whether it is Palindrome.\n"))
temp=num
s=0
while num!=0:
    rem=num%10
    s=s*10+rem
    num=num//10
if s==temp:
    print("The number you have entered is a Palindrome.")
else:
    print("The number you have entered is not a Palindrome.")
