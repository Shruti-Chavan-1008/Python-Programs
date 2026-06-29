import random

 # ------------------------------------
# Guess the Number Game 🎯
# ------------------------------------
# This is a simple number guessing game.
#
# How to Play:
# 1. The computer randomly generates a secret number.
# 2. The player tries to guess the number.
# 3. If the guess is too high, the program displays "Too High".
# 4. If the guess is too low, the program displays "Too Low".
# 5. The game continues until the correct number is guessed.
# 6. At the end, the program displays the number of attempts taken.
#
# This project demonstrates:
# - Random number generation
# - User input
# - Loops
# - Conditional statements (if-elif-else)
# - Basic game logic
# ------------------------------------

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
      
# game is end here





# Number Sign Checker Program
# This program continuously takes input from the user.
# It checks whether the entered number is positive, negative, or zero.
# The program keeps running until the user types "quite" to stop it.
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
    



 




# Sum of Digits Program
# This program takes a number as input from the user.
# It separates each digit of the number and calculates the sum of all digits.
# Finally, it displays the total sum of digits.
n=int(input("enter a number"))
sum=1

while n>0:
    digit=n%10
    sum=sum+digit 
    n=n//10

print(sum)

# this program is end here



# Count Digits Program
# This program takes a number as input from the user.
# It goes through each digit of the number and counts how many digits are present.
# Finally, it displays the total count of digits.
n=input("enter the number")
count= 0
for i in n:
   print(i)
   count+=i

print("count in number present :",count)

# this program is end here

#Thank you 






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