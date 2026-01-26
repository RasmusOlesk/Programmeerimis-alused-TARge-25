# 1. Küsi kasutaja vanust ja nime
nimi = input("Sisesta oma nimi: ")
vanus = int(input("Sisesta oma vanus: "))

# 2. Tervita kasutajat nii mitu korda, kui mitu aastat ta on täisealine olnud
taisealine_aastaid = max(0, vanus - 18)

for i in range(taisealine_aastaid):
    print(f"Tere, {nimi}!")

# 3. Kirjuta ekraanile nime lõpust 3 tähte
if len(nimi) >= 3:
    print("Nime viimased 3 tähte:", nimi[-3:])
else:
    print("Nimi on lühem kui 3 tähte.")
