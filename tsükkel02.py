def solve_using_for():
    total = 0
    for i in range(10):
        number = float(input(f"FOR Sisesta {i+1}. arv: "))
        total += number
    print(f"Sisestatud arvude summa on {total}")

def solve_using_while():
    total = 0
    count = 0
    while count < 10:
        number = float(input(f"WHILE Sisesta {count + 1}. arv: "))
        total += number
        count += 1
    print(f"Sisestatud arvude summa on {total}")


if __name__ == '__name__':
    solve_using_for()
    solve_using_while()