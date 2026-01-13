def draw_square(size: int, symbol: str, alt: str):
    for row in range(size):
        for col in range(size):
        # print(f"{symbol} ")
            if row == col or row + col == size - 1:
                print(f"{'x'}", end=" ")
            else:
                print(f"{'o'}", end=" ")
    print()


if __name__ == '__main__':
    size = int(input("Kui suurt ruutu soovid? "))
    draw_square(size, "o", "x")
    draw_square(size * 2, "I", "-")