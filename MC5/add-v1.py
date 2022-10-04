def add(prompt, strings):
    print(strings)
    return strings.append(input(prompt))


def main():
    ducks = ["Huey", "Dewey", "Louie"]
    
    add("Ge namnet på en anka: ", ducks)
    
    print(ducks)
        
if __name__ == "__main__":
    main()