# Trying to use WHILE loop

days = ["Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"]

print("\n\nWHILE loop")
count = 0
while count < len(days):
    print(days[count])
    count += 1


print("\n\nWHILE nested loop")
i = 2
while i < 100:
    j = 2
    while j <= (i/j):
        if not(i % j): break
        j = j + 1
    if j > (i/j): print(str(i) + " is prime")
    i = i + 1

print("good bye!")