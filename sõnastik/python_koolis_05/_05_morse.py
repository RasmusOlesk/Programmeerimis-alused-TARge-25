"""Koosta programm, mis programmi käivitamisel tervitab kasutajat nii tavakeeles kui morse koodina,
lubab seejärel kasutajal sisestada sõnu ning teisendab need sümbolhaaval morsetähestikku (lisades iga sümboli järele tühiku).
Sõnastik ei pruugi sisaldada kõikvõimalikke märke, seega tuleb iga sümboli puhul kontrollida, kas see üldse esineb sõnastikus.
Tähe registrit ehk suur- ja väiketähti ei eristata. Samuti tuleb otsustada, mida ette võtta nende tähtedega,
mida inglise tähestikus pole (näiteks "õ", "ä" jne): ignoreerida või mõned neist teisendada (näiteks "õ" -> "o" vms). """

morse_alphabet = {"a":".-","ä":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....",
            "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---","õ":"---","ö":"---", "p":".--.",
            "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-","ü":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--..", "ä":".-"}

def translate_to_morse(text: str) -> str:
    result = ""
    for char in text:
        test = char.lower()
        if test in morse_alphabet:
            result += morse_alphabet[test] + " "
        else:
            result += char
    return result


if __name__ == "__main__":
    print(f"{"Tere"} & {morse_alphabet["t"]} {morse_alphabet["e"]} {morse_alphabet["r"]} {morse_alphabet["e"]}")
    message = "täna on hea päev"
    print(translate_to_morse(message))
    print("Sisesta tõlgitav lause või vajutage enter lõpetamiseks: ")
    word = input
    while True:
        word = input("")
        if word == "":
            break
        print(translate_to_morse(word))
