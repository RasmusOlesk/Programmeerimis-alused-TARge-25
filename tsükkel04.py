from random import randint

def play_guessing_game():
    correct = randint(1, 20)
    tries = 0
    while tries < 5:
        answer = int(input(f"katse {tries+1}. Sisesta arv vahemikus 1-20: "))
        tries += 1
        if answer > correct:
            print("Liiga suur, proovi uuesti.")
            continue
        if answer < correct:
            print("Liiga väike, proovi uuesti.")
            continue
        print(f"Tubli, arvasid ära. Arv oli {correct}")
        break
    else:
        print(f"Katsed said otsa. Mõtlesinb arvule {correct}")



if __name__ == '__main__':
    play_guessing_game()