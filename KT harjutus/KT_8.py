while True:
    arv = int(input("Sisesta arv: "))

    if arv > 0:
        print("Proovi pigem negatiivset arvu sisestada.")
    elif arv < 0:
        print("Proovi pigem positiivset arvu sisestada.")
    else:
        print("Õnnitleme! Oled mängu ära teinud ja pääsed igavesest kordusest 🎉")
        break

