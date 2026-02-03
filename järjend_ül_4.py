"""Moodusta järjend järgnevate sõnedega:

Jah, kindlasti!
Jah!
Võib-olla!
Ei!

Tee programm, kus kasutaja saab küsida jah/ei küsimuse ja
programm annab vastuse ühe suvalise elemendi eelnevast järjendist.

Lisa ka sisse- ja väljajuhatavad tekstid, et dialoog kasutajaga oleks võimalikult loomulik.

Kui valmis, siis lisa järjendisse 20 erinevat vastusevarianti"""

from random import randint

answers = ["Jah, kindlasti!",
"Jah!",
"Võib-olla!",
"Ei!"
]

def ask_magic_eight_ball():
    question = input("Palun sisesta oma Jah/ei küsimus ennustajale:")
    random_number = randint(0, len(answers)-1)
    return answers[random_number]

if __name__ == '__main__':
    print("Tere tulemast maailmakuulsa ennustaja jutule!")
    answer = ask_magic_eight_ball()
    print(f"Ennustaja kaalus sinu küsimust põhjalikult ja tuli järeldusele, et {answer}")

