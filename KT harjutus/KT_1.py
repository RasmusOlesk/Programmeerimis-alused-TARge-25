def leia_vaikseim_korruta(a, b, c):
    """Leiab kolme arvu väikseima ja korrutab selle kahega."""
    vaikseim = min(a, b, c)
    return vaikseim * 2

def kontrolli_ruudud(kordus, max_arv):
    """Kontrollib kasutaja vastuseid arvude ruutude kohta ja loendab õiged vastused."""
    korrektne = 0
    for i in range(1, max_arv + 1):
        try:
            vastus = int(input(f"Mis on {i} ruut? "))
            if vastus == i ** 2:
                print("Õige!")
                korrektne += 1
            else:
                print(f"Vale! Õige vastus on {i ** 2}.")
        except ValueError:
            print("Palun sisesta number.")
    return korrektne

def pea_programm():
    """Peafunktsioon, mis juhib programmi käiku."""
    try:
        a = int(input("Sisesta esimene arv: "))
        b = int(input("Sisesta teine arv: "))
        c = int(input("Sisesta kolmas arv: "))
    except ValueError:
        print("Palun sisesta terved arvud!")
        return

    max_arv = leia_vaikseim_korruta(a, b, c)
    print(f"Väikseim arv korrutatud kahega on: {max_arv}")

    kordus = kontrolli_ruudud(a, max_arv)
    print(f"Kasutaja vastas õigesti {kordus} korda.")

if __name__ == '__main__':
    pea_programm()
