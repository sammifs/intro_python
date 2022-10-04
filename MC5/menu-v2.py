options = {"a":"Add item", "l":"List items", "q":"Log out"}

def menu(title, prompt, options):
    print(title)
    
    for keys, values in options.items():
        print(keys + ')', values)
    
    svar = ""
    
    while svar not in options:
        svar = input(prompt)
    return svar