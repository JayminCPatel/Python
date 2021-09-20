#Author :- Jaymin Patel
#Practice :- WAP to check if the given number is a palindrome.

def reverse(num) :
    temp = num
    reversenum = 0
    while num > 0:
        digit = num %10
        reversenum = reversenum * 10 + digit
        num = num // 10
    if temp == reversenum :
        print ("Number is Palindrom")
    else :
        print ("Numer is not Palindrom")

x = int(input("Enter Number : "))
if x<=0 :
  print ("Enter Number greater than 0")
elif x>0 :
    reverse(x)
  
