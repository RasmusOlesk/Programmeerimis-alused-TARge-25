def greet_by_name(name: str) -> str:
    return f"tervist {name}!"

def verify_age(name: int) -> str:
    if 7 <= age <= 18:
        return "oled 7-18 aastane"
    return "Oled noorem või vanem kui 7-18 aastased"

if __name__ == '__main__':
    name = input("Sisesta oma nimi: ")
    age = int(input("Sisesta oma vanus aastates täisarvuna: "))
    greeting = greet_by_name(name)
    age_text = verify_age(age)
    print(greeting, age_text, sep="\n")
