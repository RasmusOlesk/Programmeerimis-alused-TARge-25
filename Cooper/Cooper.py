def hinda(meetrid: int, sugu: str) -> str:
    if sugu == "M":
        vaga_hea = 2800
        nork = 2000
    else:
        vaga_hea = 2600
        nork = 1800

    if meetrid >= vaga_hea:
        return "väga hea"

    if meetrid < nork:
        puudujääk = nork - meetrid
        return f"nõrk, järgmisest hindest puudu {puudujääk} m"

    puudujääk = vaga_hea - meetrid
    return f"rahuldav, järgmisest hindest puudu {puudujääk} m"


def main():
    failinimi = input("Sisestage failinimi: ")

    mehed = []
    naised = []

    with open(failinimi, "r", encoding="utf-8") as f:
        for rida in f:
            rida = rida.strip()
            if not rida:
                continue
            meetrid_str, sugu = rida.split()
            meetrid = int(meetrid_str)

            # Väljasta jooksja tulemus
            hinnang = hinda(meetrid, sugu)
            print(f"{sugu} {meetrid} m, {hinnang}")

            # Kogu keskmiste jaoks
            if sugu == "M":
                mehed.append(meetrid)
            else:
                naised.append(meetrid)

    print("Keskmised:")

    # Meeste keskmine
    if mehed:
        keskmine_m = round(sum(mehed) / len(mehed))
        print(f"M {keskmine_m} m, {hinda(keskmine_m, 'M')}")
    else:
        print("M -")

    # Naiste keskmine
    if naised:
        keskmine_n = round(sum(naised) / len(naised))
        print(f"N {keskmine_n} m, {hinda(keskmine_n, 'N')}")
    else:
        print("N -")


if __name__ == "__main__":
    main()
