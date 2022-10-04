def menu(title, prompt, options):
    print(title)
    
    for keys, values in options.items():
        print(keys + ')', values)
    
    svar = ""
    
    while svar not in options:
        svar = input(prompt)
    return svar

users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}


def login(users):
    while True:
        anv = input("User: ")
        los = input("Password: ")
        
        if anv in users and los in users.values():
            print("Welcome ", anv)
        else:
            if menu("Invalid username or password", "Option: ", {"r": "Try again", "q": "Quit"}) == "q":
                return None
