# Function examples

def func():
    print("This is a generic function.")


def my_name_is(name):
    print(f"My name is {name}.")


def sum_six(num):
    return num + 6


def sum_numbers(numbers):
    return sum(numbers)


def usd_to_eur(usd, rate=0.92):
    return usd * rate


# Main program
if __name__ == "__main__":
    func()

    my_name_is("Rasmus")

    result = sum_six(10)
    print(f"10 + 6 = {result}")

    numbers = [1, 2, 3, 4, 5]
    total = sum_numbers(numbers)
    print(f"Sum of {numbers} = {total}")

    usd = 100
    eur = usd_to_eur(usd)
    print(f"{usd} USD = {eur:.2f} EUR")