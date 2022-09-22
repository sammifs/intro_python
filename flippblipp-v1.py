n = 40

for x in range(1, n+1):
    if x % 3 == 0 and x % 5 == 0:
        print("flipp blipp")
    elif x % 3 == 0:
        print("flipp")
    elif x % 5 == 0:
        print("blipp")
    else:
        print(str(x))
