def view(description, strings):
    print(description)
    for string in strings:
        print (f"{strings.index(string)}) {string}")
        
names   = ["nisse", "stina", "bosse", "mimmi"]
animals = ["giraff", "myrslok", "tapir"]

view("Lista med namn", names)
print()
view("Lista med djur", animals)