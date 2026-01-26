# Küsi kasutajalt klientide arv
kliendid = int(input("Sisesta klientide arv: "))

lilled_kokku = 0
i = 1

# Arvuta while-tsükliga lillede koguarv
while i <= kliendid:
    lilled_kokku += i
    i += 1

# Väljasta tulemus
print("Pood kingib kokku", lilled_kokku, "lille.")
