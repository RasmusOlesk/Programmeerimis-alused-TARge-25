# Küsi kasutajalt klientide arv (mittenegatiivne täisarv)
while True:
    kliendid = int(input("Sisesta klientide arv (mittenegatiivne): "))
    if kliendid >= 0:
        break
    print("Palun sisesta mittenegatiivne arv.")

lilled_kokku = 0
i = 1

# Arvuta while-tsükliga lillede koguarv
while i <= kliendid:
    lilled_kokku += 1  # eeldame, et iga klient saab 1 lille
    i += 1

# Väljasta tulemus
print("Kingitavate lillede koguarv on:", lilled_kokku)
