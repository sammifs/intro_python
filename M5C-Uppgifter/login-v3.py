def printLoginScreen():
    print("")
    username = input("User: ")
    password = input("Password: ")
    return (username, password)

def printActions(options):
    for option, action in options.items():
        print(f"    {option})", action)
    print("")

def chooseOption(prompt, options):
    input_option = input(f"{prompt}")
    
    for option, action in options.items():
        if input_option == option:
            return option

    return chooseOption(prompt, options)

def login(users):
    options = {"r":"Try again", "q":"Quit"}
    input_loginDetails = printLoginScreen()
    username, passwords = input_loginDetails # <=> (username, password)
    
    for user_loginDetails in users.items():
        if input_loginDetails == user_loginDetails:
            print(f"\nWelcome {username}\n")
            return username

    print("\nInvalid username or password\n")

    input_option = menu("", "Option: ", options)

    if (input_option == "r"): 
        return login(users)
    elif (input_option == "q"):
        return None

def menu(title, prompt, option):
    printActions(option)
    return chooseOption(prompt, option)

if __name__ == "__main__":
    users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
    user = login(users)    
    