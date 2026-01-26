# 1. Küsi kasutajalt sõna
sona = input("Sisesta sõna: ")

# 2. Küsi kasutajalt number
number = int(input("Sisesta number: "))

# 4. Kui number on suurem kui 10, tagasta viga
if number > 10:
    print("Viga")
else:
    # 3. Prindi sõna number * 2 korda (kordus)
    for i in range(number * 2):
        print(sona)
