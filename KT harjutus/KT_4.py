# 1. Küsi kasutaja sugu ja vanus
sugu = input("Sisesta oma sugu (m/n): ").lower()
vanus = int(input("Sisesta oma vanus: "))

# Funktsioon tervituse leidmiseks
def tervitus(sugu, vanus):
    if vanus < 18:
        return "Tere, poiss!" if sugu == "m" else "Tere, tüdruk!"
    elif vanus < 65:
        return "Tere, mees!" if sugu == "m" else "Tere, naine!"
    else:
        return "Tere, härra!" if sugu == "m" else "Tere, proua!"

# 2. Leia algne tervitus
algne_tervitus = tervitus(sugu, vanus)

# 3. Korda tervitust ea suurendamisega
kordused = 0
praegune_vanus = vanus

while kordused < 10:
    uus_tervitus = tervitus(sugu, praegune_vanus)

    if uus_tervitus != algne_tervitus:
        break

    print(f"{uus_tervitus} (vanus {praegune_vanus})")
    praegune_vanus += 1
    kordused += 1
