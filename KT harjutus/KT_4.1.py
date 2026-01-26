def tervitus(sugu, vanus):
    if vanus < 13:
        return "Tere poiss!" if sugu == "mees" else "Tere tüdruk!"
    elif vanus < 20:
        return "Tere noormees!" if sugu == "mees" else "Tere neiu!"
    elif vanus < 65:
        return "Tere härra!" if sugu == "mees" else "Tere proua!"
    else:
        return "Tere vanahärra!" if sugu == "mees" else "Tere vanaproua!"


# 1. Küsi kasutaja sugu ja vanus
sugu = input("Sisesta sugu (mees/naine): ").lower()
vanus = int(input("Sisesta vanus: "))

algne_tervitus = tervitus(sugu, vanus)

# 2.–3. Korda tervitust ea suurendamisega
for i in range(10):
    praegune_tervitus = tervitus(sugu, vanus)
    print(f"Vanus {vanus}: {praegune_tervitus}")

    if praegune_tervitus != algne_tervitus:
        break

    vanus += 1
