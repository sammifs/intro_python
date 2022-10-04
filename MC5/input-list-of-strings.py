def add(prompt, strings):
    print(strings)
    return strings.append(input(prompt))

def view(description, strings):
    print(description)
    for i,x in enumerate(strings):
        print(str(i+1)+')', x)

strings = []
n = 10

def main():
    print(n)
    for x in range(n):
        add("Lägg till sträng: ", strings)
    stinggg = f"Du har matat in följande {n} strängar"
    view(stinggg, strings)