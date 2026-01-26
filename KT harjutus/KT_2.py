nimi = input("Sisesta oma nimi: ")
vanus = int(input("Sisesta oma vanus: "))

if len(nimi) < vanus or vanus < 5:
    for _ in range(3):
        print(f"Tere, {nimi}!")
    else:
        arv1 = int(input("Sisesta esimene arv: "))
        arv2 = int(input("Sisesta teine arv: "))
        arv3 = int(input("Sisesta kolmas arv: "))
        summa = int(input("Mis on nende arvude summa? "))

        if arv1 + arv2 + arv3 == summa:
            print("Õige tulemus!")
        else:
            print("Vale tulemus!")
