options = {"a":"Add item", "l":"List items", "q":"Log out"}

def printActions():
    print("Select an action\n")
    for option, action in options.items():
        print(f"    {option})", action)

def chooseOption():
    inputOption = input("Option: ")
    found = False
    
    for option, action in options.items():
        if inputOption == option:
            print(f"You selected option {option})", action)
            found = True

    if(not found):
        chooseOption()        

if __name__ == "__main__":
    printActions()
    print()
    chooseOption()
