users = {"nisse":"apa", "bosse":"ko", "stina":"t-rex"}

print("Användare: \n")
for user in users:
    print(f"    {user}")

print()

print("Användare och lösenord: \n")
for user, password in users.items():
    print(f"    {user})", password)

print()

data = {"nisse":["luva", "vante"], "bosse":["spik", "skruv", "hammare"], "stina":["tidsmaskin"]}

print("Användare och deras data: \n")
for user, userdata in data.items():
    print(f"    {user})", userdata)
    
print()

söktAnvändare = input("Slå upp användare: ")

found = False
for user in data:
    if user == söktAnvändare:
        print(f"Data lagrat för {user}", data[user])
        found = True
  
if(not found):
    print(f"Användare \"{söktAnvändare}\" finns inte")
