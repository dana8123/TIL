hour, minute = input().split()
hour = int(hour)
minute = int(minute)

if minute < 45:
    minute = minute + 60 - 45
    if hour == 00:
        hour = hour + 23
    else:
        hour = hour - 1
else:
    minute = minute - 45

print(hour, minute)
