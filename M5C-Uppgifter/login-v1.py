users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}

def printLoginScreen():
    username = input("User: ")
    password = input("Password: ")
    return (username, password)

def login():
    input_loginDetails = printLoginScreen()
    username, password = input_loginDetails # <=> (username, password)
    
    for user_loginDetails in users.items():
        if input_loginDetails == user_loginDetails:
            print(f"\nWelcome {username}\n")
            return None

    print("\nInvalid username or password\n")
    return login()

if __name__ == "__main__":
    login()
    
    