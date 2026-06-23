import time

current_time = time.strftime("%H:%M:%S")

print(current_time)
current_time=time.strftime("%H")
print(int(current_time))
current_time=time.strftime("%M")
print(int(current_time))
current_time=time.strftime("%S")
print(int(current_time))

hour = int(time.strftime("%H"))

if hour >= 5 and hour < 12:
    print("Good Morning")
elif hour >= 12 and hour < 17:
    print("Good Afternoon")
elif hour >= 17 and hour < 21:
    print("Good Evening")
else:
    print("Good Night")
