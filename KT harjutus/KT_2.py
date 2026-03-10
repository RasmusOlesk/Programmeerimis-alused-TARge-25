def pea_programm():
    nimi = input("Sisesta oma nimi: ")
    vanus = int(input("Sisesta oma vanus: "))

    # Tervita ainult, kui nimi on lühem kui vanus ja vanus < 5
    if len(nimi) < vanus and vanus < 5:
        for _ in range(3):
            print(f"Tere, {nimi}!")
    else:
        # Küsi kolm arvu ja kontrolli sum
        a = int(input("Sisesta esimene arv: "))
        b = int(input("Sisesta teine arv: "))
        c = int(input("Sisesta kolmas arv: "))
        summa = int(input("Mis on nende arvude summa? "))
        if a + b + c == summa:
            print("Õige tulemus!")
        else:
            print("Vale tulemus!")

if __name__ == '__main__':
    pea_programm()
