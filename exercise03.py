def calculate(arv1: float, arv2: float, operation: str) -> str:
    result = ""
    if operation == "+":
        result = arv1 + arv2
    elif operation == "-":
        result = arv1 - arv2

    if result == "":
        return f"tundmatu tehe: {operation}"
    return f"{arv1}{operation}{arv2}={result}"


if __name__ == '__main__':
    arv1 = input("Sisestage esimene arv: ")
    arv2 = input("Sisestage teine arv: ")
    operation = input("Sisestage tehe: ")
    print(f"Tulemus: {calculate(arv1, arv2, operation)}")

