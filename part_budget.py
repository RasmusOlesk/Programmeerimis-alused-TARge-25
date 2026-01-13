def calculate_budget(guests: int) -> int:

    place_price = 55
    price_per_guest = 10
    return place_price * price_per_guest * guests

if __name__ == '__main__':
    invited_guests = int(input("Mitu inimest on peole kutsutud?"))
    confirmed_guests = int(input("Mitu inimest tuleb? "))
    min_budget = calculate_budget(confirmed_guests)
    max_budget = calculate_budget(invited_guests)
    print(f"maksimaalne eelarve on {max_budget} eurot")
    print(f"Minimaalne eelarve on {min_budget} eurot")