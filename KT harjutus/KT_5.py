# 1. Küsi kasutaja nime
nimi = input("Sisesta oma nimi: ")

# 2. Kui nime pikkus on 5–10 (kaasa arvatud)
if 5 <= len(nimi) <= 10:
    for i in range(3):
        print(f"Tere, {nimi}!")
else:
    # 3. Muidu küsi kolm arvu ja tagasta nende summa (kordus)
    summa = 0
    for i in range(3):
        arv = float(input(f"Sisesta arv {i + 1}: "))
        summa += arv

    print("Arvude summa on:", summa)
