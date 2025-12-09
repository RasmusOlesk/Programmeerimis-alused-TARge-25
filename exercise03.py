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
    esimene = input("Sisestage esimene arv: ")
    teine = input("Sisestage teine arv: ")
    op = input("Sisestage tehe: ")
    print(f"Tulemus: {calculate(esimene, teine, op)}")

