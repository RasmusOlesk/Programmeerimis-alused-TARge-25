# 1. Küsi kasutaja nime ja vanust
nimi = input("Sisesta oma nimi: ")
vanus_str = input("Sisesta oma vanus: ")

# Kontrollime, et vanus oleks arv
try:
    vanus = int(vanus_str)
except ValueError:
    print("Vanus peab olema täisarv.")
    exit()

# 2. Kui nime pikkus on väiksem kui vanus või vanus on alla 5,
#    siis tervita nime pidi 3 korda (kordus)
if len(nimi) < vanus or vanus < 5:
    for i in range(3):
        print(f"Tere, {nimi}!")
else:
    # 3. Muidu küsi kolm arvu ja nende summa
    try:
        arv1 = float(input("Sisesta esimene arv: "))
        arv2 = float(input("Sisesta teine arv: "))
        arv3 = float(input("Sisesta kolmas arv: "))
    except ValueError:
        print("Palun sisesta ainult arve.")
        exit()

    oige_summa = arv1 + arv2 + arv3
    kasutaja_summa_str = input("Mis on nende kolme arvu summa? ")

    try:
        kasutaja_summa = float(kasutaja_summa_str)
    except ValueError:
        print("Summa peab olema arv.")
        exit()

    # 4. Teata, kas said õige tulemuse
    if abs(kasutaja_summa - oige_summa) < 1e-9:
        print("Õige tulemus!")
    else:
        print(f"Vale tulemus. Õige summa on {oige_summa}.")
