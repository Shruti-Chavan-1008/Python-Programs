import random
# -------------------------------
# Snake Water Gun Game 🐍💧🔫
# -------------------------------
# Rules:
# Snake drinks Water   -> Snake wins
# Water drowns Gun     -> Water wins
# Gun kills Snake      -> Gun wins
#
# Choice Mapping:
# 1 = Snake
# 2 = Water
# 3 = Gun
#
# The computer randomly selects one option.
# The user enters their choice.
# The program compares both choices and
# declares the Winner, Loser, or Draw.

computor_value= random.randint(1, 3)
# User enters their choice
user_value=int(input("selecte value from 1,3 accoding your chosse as   1:snake , 2:water , 3:Gun :  " ))

# Winning combinations for the user
winner=[[1,2],[2,3],[3,1]]

# Losing combinations for the user
Looser=[[1,3],[2,1],[3,2]]

# Draw combinations
Draw=[[1,1],[2,2],[3,3]]

# Store both computer and user choices in a list
Condition_list=[computor_value,user_value]


if Condition_list in winner:
    print("You are the winner! 🎉")
elif Condition_list in Looser:
     print("You lose the game. 😢")
elif Condition_list in Draw:
     print("Game Draw! Both selected the same option.")  
else:
     print("you selectes the wrong option")   




