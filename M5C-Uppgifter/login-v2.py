def printLoginScreen():
    username = input("User: ")
    password = input("Password: ")
    return (username, password)

def login(users):
    input_loginDetails = printLoginScreen()
    username, passwords = input_loginDetails # <=> (username, password)
    
    for user_loginDetails in users.items():
        if input_loginDetails == user_loginDetails:
            return username

    print("\nInvalid username or password\n")
    return login(users)

if __name__ == "__main__":
    users1 = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
    user1 = login(users1)
    print(f"\nWelcome {user1}\n")

    users2 = {"foo":"123", "bar":"hello", "foobar":"hello123"}
    user2 = login(users2)
    print(f"\nWelcome {user2}\n")
    
    