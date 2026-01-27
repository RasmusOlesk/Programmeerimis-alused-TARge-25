"""Kontrolltöö harjutus 2
On traditsioon, et rõõmsatel puhkudel kingitakse paaritu arv lilli. Lillepoel on sünnipäev ja pood otsustas klientidele kinkida lilli nii, et päeva esimene ostja saab ühe lille, teine ei saa ühtegi, kolmas ostja saab kolm lille, neljas ei saa midagi, viies ostja saab viis lille jne.

Koostada programm, mis

•küsib kasutajalt klientide arvu (mittenegatiivne täisarv);

•arvutab while-tsükli abil lillede koguarvu, mida pood kingib;

•väljastab saadud lillede arvu ekraanile."""


# Siin peaks küsima kasutajalt klientide arvu
def klientide_arv():
    while True:
        kliendid = int(input("Palun sisesta klientide arv (arv peab olema mittenegatiivne): "))
        if kliendid >= 0:
            break
        print("Palun sisesta mittenegatiivne arv.")

def lillede_arv():
    lilled_kokku = 0
    i = 1

# Siin peaks arvuta lillede koguarvu
def lillede_koguarv():
    while i <= kliendid:
        lilled_kokku += 1
        i += 1

# See peaks väljastama tulemuse
def Tulemus():
    print("Kingitavate lillede koguarv on:", lilled_kokku)


if __name__ == '__main__':
    klientide_arv()
    lillede_arv()
    lillede_koguarv()
    Tulemus()
