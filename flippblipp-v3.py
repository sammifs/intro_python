def flippblipp(n):
    if n % 3 == 0 and n % 5 == 0:
        return "flipp blipp"
    elif n % 3 == 0:
        return "flipp"
    elif n % 5 == 0:
        return "blipp"
    else:
        return str(n)

counter = 1
print(counter)   # print(1)

while True:
    counter += 1
    guess = input("Nästa: ")
    
    if guess != flippblipp(counter):
        print("Fel - ", flippblipp(counter)) 
        break
