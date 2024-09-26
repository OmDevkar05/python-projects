import time

timestamp = time.strftime('%H : %M : %S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
if 12 > timestamp > 6:
    print("Good Morning❤️ ")
elif 18 > timestamp > 12:
    print("Good Afternoon❤️ ")
elif 20 > timestamp > 18:
    print("Good Afternoon❤️")
else:
    print("Good Night❤️")
