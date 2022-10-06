def view(description, strings):
    print(description + "\n")
    for string in strings:
        print (f"    {strings.index(string)+1}) {string}")

def add(prompt, strings):
    string = str(input(prompt))
    strings.append(string)
    return strings

n = 3
strings = []
description = f"Du har matat in följande {n} strängar"

if __name__ == "__main__":
    print(f"n = {n} \n")
    for i in range(n):
        add("Lägg till en sträng: ", strings)
    print()
    view(description, strings)
    
