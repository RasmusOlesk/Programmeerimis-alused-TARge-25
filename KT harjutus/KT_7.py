while True:
    # 1. Küsi kasutajalt arv
    arv = float(input("Sisesta arv: "))

    # Astmed 2, 3, 4 ja 5 (kordus)
    for aste in range(2, 6):
        print(f"{arv} astmes {aste} = {arv ** aste}")

    # 2. Küsi, kas kasutaja soovib jätkata
    vastus = input("Kas soovid teise arvuga jätkata? (jah/ei): ").lower()

    if vastus != "jah":
        print("Programm lõpetatud.")
        break
