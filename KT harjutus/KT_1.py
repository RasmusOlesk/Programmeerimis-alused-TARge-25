# 1. Küsi kasutajalt 3 arvu
arvud = []
for i in range(3):
    arv = int(input(f"Sisesta arv {i+1}: "))
    arvud.append(arv)

# 2. Väikseim arv korruta kahega
vaikseim = min(arvud)
piir = vaikseim * 2

print(f"\nVäikseim arv on {vaikseim}, korrutatuna kahega = {piir}\n")

# 3–5. Küsi ruute, kontrolli vastuseid ja loe õiged vastused
oiged = 0

for i in range(1, piir + 1):
    vastus = int(input(f"Mis on arvu {i} ruut? "))
    if vastus == i ** 2:
        print("Õige!\n")
        oiged += 1
    else:
        print(f"Vale! Õige vastus on {i ** 2}\n")

# 5. Teata mitu korda kasutaja vastas õigesti
print(f"Sa vastasid õigesti {oiged} korda.")
