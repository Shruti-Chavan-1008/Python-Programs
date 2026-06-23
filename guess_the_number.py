import random

 
def game():
         
       num = random.randint(1, 100)
       print(num) 
       while True:
           User_input=int(input("enter the number : ")) 
           if(User_input=="quite"):
            print("user is quited the game")
            break
       
           n=int(User_input)
           if (n>num):
             print("too high")
           elif(n<num):
             print("too low")
           elif(n==num):
             print("correct match!!!")
             break
         
           else:
             print("try again shruti")

game()
      



while True:
   user_input=input("enter the value")
   if user_input=="quite":
      print("program is stooped")
      break
   n=float(user_input)
   if n>0:
      print("positive number")
   elif n<0:
      print("negative number")
   else :
      print("n is zero")
    




for i in range(1,100):
   if(i%3==0 & i%5==0):
      print(i)





n=int(input("enter a number"))
sum=1

while n>0:
    digit=n%10
    sum=sum+digit 
    n=n//10

print(sum)





n=input("enter the number")
count= 0
for i in n:
   print(i)
   count+=i

print("count in number present :",count)








a=int(input("enter the value a: "))
b=int(input("enter the value b: "))

for i in range(a,b+1):
    if (i%2==0):
       print(i)









s=int(input("enter your salary: "))

if s<30000:
   Tax_amount=s*5/100
   print("your tax is 5% of your salary so amount to pay tax is: ",Tax_amount)
elif(s>=30000 & s<70000 ):
   Tax_amount=s*15/100
   print("your tax is 15% of your salary so amount to pay tax is: ",Tax_amount)
else:
  Tax_amount=s*25/100
  print("your tax is 25% of your salary so amount to pay tax is: ",Tax_amount)