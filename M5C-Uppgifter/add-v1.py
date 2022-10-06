"""

    1. skriva ut listan med ankor
    2. fråga användaren efter namnet på en anka
    3. lägga till den nya ankan sist i listan ducks
    4. skriva ut den uppdaterade listan med ankor.

"""

ducks = ["Huey", "Dewey", "Louie"]

def add(prompt, strings):
    strings = str(input(prompt))
    ducks.append(strings)
    return ducks

print(f"         Ducks: {ducks}")
print()

ducks_alias = add("    Add a duck: ", ducks)

print(f"         Ducks: {ducks}")
print(f"Alias of Ducks: {ducks_alias}")
print()
