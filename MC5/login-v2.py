users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}

def login(users):
    anv = input("User: ")
    los = input("Password: ")
    
    if anv in users and los in users.values():
        print("Welcome ", anv)
    else:
        print("Invalid username or password")
    
