"""Koosta programm, mis "viskab täringut" kolm korda ehk väljastab ekraanile 3 juhusliku
täringuviske tulemused. Et ekraanipilt oleks realistlikum, esita tulemused graafiliselt,
selleks kasuta nn. ASCII graafikat (https://en.wikipedia.org/wiki/ASCII_art):
imiteeri tekstisümbolite abil täringu külje kujutist. Täiendamiseks:

Kasutaja võib alguses ise valida, mitu korda täringut visata.
Mängida võib mitu inimest, programmi alguses küsitakse inimeste nimesid.
Täringut imiteeritakse kolmemõõtmelisena. """

from random import randint

def Täringu_viksed():
    for _ in range():
        täringu_vise = int(input("Mitu korda viskame täringut? "))
        print(f"Sa viskad {täringu_vise} korda")

def Saadud_täringu_number():
        print(f"Sa said numbriks {Täringu_number}")






if __name__ == '__main__':
    täringu_vise = int(input("Mitu korda viskame täringut? "))
    print(f"Sa viskad {täringu_vise} korda")
    Täringu_number = randint(1, 6)
    print(f"Sa said numbriks {Täringu_number}")

