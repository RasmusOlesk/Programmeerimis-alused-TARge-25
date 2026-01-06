from random import randint

def play_guessing_game():
    correct = randint(1, 20)
    while True:
        answer = int(input("Sisesta arv vahemikus 1-20: "))
        if answer > correct:
            print("Liiga suur, proovi uuesti.")
            continue
        if answer < correct:
            print("Liiga väike, proovi uuesti.")
            continue
        print(f"Tubli, arvasid ära. Arv oli {correct}")
        break



if __name__ == '__main__':
    play_guessing_game()