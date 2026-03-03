"""Tee uus fail luuletus.txt ning lisa sinna järgmine luuletus:
Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin.

Koosta programm, mis kuvab ekraanile luuletuse read, kuid lisab nende ette rea järjekorranumbri
ja iga rea järele sulgudesse reas asuvate sümbolite arvu e. rea pikkuse. """

def write_poem_file(filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        f.write("""Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin.""")

def read_poem_lines(file_name :str) -> list[str]:
    with open (file_name, encoding="utf=8") as f:
        result = []
        for line in f:
            result.append(line.strip())
        return result

def print_numbered_lines_with_length(poem_lines : list[str]):
    for index,content in enumerate(poem_lines):
        print(f"{index+1} {content} ({len(content)})")

if __name__ == "__main__":
    file_name = "luuletus.txt"
    write_poem_file(file_name)
    poem_lines = read_poem_lines(file_name)
    print_numbered_lines_with_length(poem_lines)
    
