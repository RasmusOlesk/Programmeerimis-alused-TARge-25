"""Tee programm, mis väljastab failist luuletus.txt kasutaja poolt soovitud rea nt:
Mitmendat rida soovid kuvada:
>> 7
Error tuleb ette siis,

NB! Faili avamiseks ja rea väljastamiseks koosta eraldi alamprogramm (ehk funktsioon). """

from failioperatsioon_ül_2 import write_poem_file


def print_specific_line(linenumber: int, filename: str) -> None:
    message = f"Luuletuse {linenumber}. rida - "
    with open(filename, encoding="utf=8") as f:
        for index, line in enumerate(f):
            if (index + 1) == linenumber:
                print(message + line)
                break
        else:
            print("Viga! Luuletuses pole nii palju ridu.")



if __name__ == "__main__":
    file_name = "luuletus.txt"
    write_poem_file(file_name)
    user_input = input("Mitmendat rida te soovite: ")
    if user_input.isdigit() and int(user_input) > 0:
        print_specific_line(int(user_input), file_name)
    else:
        print("Viga! Sisesta nullist suurem täisarv.")