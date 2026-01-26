# a. Loo järjend 3 nimega
nimed = ["", "", ""]

# Funktsioon tundmatu nime asendamiseks
def asenda_nimi(jarjend, index, uus_nimi):
    jarjend[index] = uus_nimi

# b. Küsi kasutajalt iga nime kohta
for i in range(len(nimed)):
    nimi = input(f"Sisesta nimi {i+1}: ")
    tundmatu = True
    while tundmatu:
        tunne = input(f"Kas sa tunned {nimi}? (jah/ei): ").lower()
        if tunne == "jah":
            nimed[i] = nimi
            tundmatu = False
        else:
            # Kui ei tunne, lase uus nimi sisestada
            uus_nimi = input("Sisesta uus nimi: ")
            asenda_nimi(nimed, i, uus_nimi)
            nimi = uus_nimi  # uuenda nimi tsükli kontrolliks

# d. Kirjuta ekraanile kõik nimed, igaüks eraldi reale
print("\nKõik nimed:")
for nimi in nimed:
    print(nimi)
