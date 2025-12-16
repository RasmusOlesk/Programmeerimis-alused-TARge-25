def solve_infinite_sum():
    total = 0
    count = 0
    while True:
        text_input = input(f"Infinite Sisesta {count + 1}. arv: ")
        if text_input == "":
            break
        total += number
        count += 1
    print(f"Sisestatud arvude summa on {total}")


if __name__ == '__name__':
    solve_using_for()
    solve_using_while()
    solve_infinite_sum()