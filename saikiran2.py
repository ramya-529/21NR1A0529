import random
n=random.randint(1,10)
num=int(input("enter your guess number"))
if(n==num):
   print("your guess is correct")
else:
    print("your guess is wrong");
print("your guess number is:",n)
