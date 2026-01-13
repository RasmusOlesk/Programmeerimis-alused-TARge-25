def compute_rectangle():
    length = float(input("Sisesta ristküliku pikkus: "))
    width = float(input("Sisesta ristküliku laius: "))
    area = width * length
    circumference = 2 * (length + width)
    print(f"Antud ristküliku pindala on {area}")
    print(f"ümbermõõt on {circumference}")



if __name__ == '__main__':
    compute_rectangle()