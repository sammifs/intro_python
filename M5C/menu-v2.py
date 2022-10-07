def printActions(options):
    for option, action in options.items():
        print(f"    {option})", action)
    print("")

def chooseOption(prompt, options):
    inputOption = input(f"{prompt}")
    inputOptionFound = False
    
    for option, action in options.items():
        if inputOption == option:
            print(f"\nYou selected option {option})", action)
            inputOptionFound = True

    if(not inputOptionFound):
        return chooseOption(prompt, options)        

def menu(title, prompt, option):
    print(f"{title}\n")
    printActions(option)
    chooseOption(prompt, option)

if __name__ == "__main__":
    options1 = {"a":"Add item", "l":"List items", "q":"Log out"}
    menu("Select an action", "Action: ", options1)
    print()

    options2 = {"r":"Try again", "q":"Quit"}
    menu("What do you want to do?", "My choice: ", options2)
