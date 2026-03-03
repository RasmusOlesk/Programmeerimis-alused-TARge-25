"""Loo fail tuttavad.txt ja lisa sinna vähemalt 6 tuttava perekonna- ja eesnimed (iga tuttav uuele reale, perekonna- ja eesnimi tühikuga eraldatult).
 programm, mis loeb failist andmed ja väljastab need ekraanile tähestikulises järjekorras.
 Mõistlik on ilmselt kasutada järjendit ja sellega seonduvaid võimalusi (järjestamist).
 Tähestikulises järjekorras salvestage tuttavate nimed ka uude faili tuttavad1.txt. """

def write_to_file(filename: str, values: list[str]) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        for name in values:
            f.write(name + "\n")

def create_familiars_file(filename: str) -> None:
    familiars = [
        "Tiit Sukk",
        "Teet Pukk",
        "Peep Nukk",
        "",
        "Tina Kukk",
        "Allan Kukk",
        "Mari Tukk",
        "Sari Lukk"
    ]
    write_to_file(filename, familiars)

def read_names_from(filename: str) -> list[str]:
    result = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            name = line.strip()
            if len(name) > 0:
                result.append(name)
    return result


def sort_names(names: list[str]) -> list[str]:
    last_name__full_name_list =  [ (name.split()[-1], name) for name in names]


     # for name in names:
     #     last_name = name.split()[-1]
     #     last_name__full_name_list += [(last_name, name)]
    sorted_names = sorted(list(last_name__full_name_list))
    result = []
    for name in sorted_names:
        result_name = name[-1]
        result.append(result_name)
    return result
    return [item[-1] for item in sorted_names]


if __name__ == "__main__":
    filename = "tuttavad.txt"
    create_familiars_file(filename)
    names_from_file = read_names_from(filename)
    sorted_by_last_name = sort_names(names_from_file)
    for name in sorted_by_last_name:
        print(name)

    write_to_file("tuttavad1.txt", sorted_by_last_name)