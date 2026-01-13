def ask_name_age (name: str) -> str:
    return f"su nimi on {name} ja vanus on {age}"




if __name__ == '__main__':
    name = input("sisesta oma nimi: ")
    age = int(input("Sisesta oma vanus: "))
    if name < age:
        for i in range(3):
            print (f"{i + 1}. tervist {name} ")


