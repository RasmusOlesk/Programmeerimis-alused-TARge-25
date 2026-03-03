"""Koosta programm, mis küsib kasutajalt rea, mille järele ta soovib failis luuletus.txt
uut rida lisada ning seejärel lisab kasutaja poolt sisestatud rea nt:
Sisesta rida, mille järele soovid uut rida lisada:
>> Padja, teki viskan maha,
Sisesta rida, mida soovid lisada:
>> üles ärgata ma ei taha,

Tulemus failis luuletus.txt:
Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
üles ärgata ma ei taha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin."""

# TODO lahenda ülesanne
"""1. loe faili read mällu
    2. käime läbi rida haaval ja võrdleme käesoleva rea teksti kasutaja sisestatud tekstiga
        kui kattub siis, 
            jäta rea number meelde ja katkesta tsükkel
        kui ei leidnud sobivat rida siis,
            teata, et soovitud rida ei leitud ja lõpetame programmi
    3. lisa mälus olevasse järjendisse meelde jäetud kohale kasutaja lisatud tekst
    4. kirjuta failis ja prindi uus luuletus
    """

from failioperatsioon_ül_2 import write_poem_file, read_poem_lines

def read_lines_from_file(filename: str) -> list[str]:
    result = []
    with open(filename, encoding="utf-8") as f:
        result = [line.strip() for line in f]
    return result


if __name__ == "__main__":
    file_name = "luuletus4.txt"
    write_poem_file(file_name)
    poem_line = input("Sisesta rida, mille järele soovid uut rida lisada: ")
    line_to_append = input("Sisesta rida, mida soovid lisada: ")
    poem_lines = read_lines_from_file(file_name)
    new_line_position = -1
    for index, line in enumerate(poem_lines):
        if line == poem_line:
            new_line_position = index + 1
            break
    else:
        print("Soovitud rida ei leitud.")
        exit()
    poem_lines.insert(new_line_position, line_to_append)
    with open (file_name, "w", encoding="utf-8") as f:
        for line in poem_lines:
            f.write(line + "\n")
    with open(file_name, encoding="utf-8") as f:
        print(f.read())