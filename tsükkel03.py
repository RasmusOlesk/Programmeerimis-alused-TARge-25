from random import randint, choice

operations = ["+", "-", "*", "**", "//"]

def get_calculation(min_value: int, max_value: int) -> tuple[str, int]:
    num1 = randint(min_value, max_value)
    num2 = randint(min_value, max_value)
    operation = choice(operations)
    if operation == "+":
        correct_answer = num1 + num2
        return f"{num1} {operation} {num2} = ", correct_answer
    elif operation == "-":
        correct_answer = num1 - num2
        return f"{num1} {operation} {num2} = ", correct_answer
    elif operation == "*":
        correct_answer = num1 * num2
        return f"{num1} {operation} {num2} = ", correct_answer
    elif operation == "**":
        correct_answer = num1 ** num2
        return f"{num1} {operation} {num2} = ", correct_answer
    elif operation == "//":
        correct_answer = num1 // num2
        return f"{num1} {operation} {num2} = ", correct_answer
    return "Tundmatu tehe", 0

def test_user_knowledge(min_value: int, max_value: int) -> tuple [bool, int]:
    calculation, correct_answer = get_calculation(min_value, max_value)
    user_answer = int(input(calculation))
    return user_answer == correct_answer, correct_answer

def practice_addition(count: int, min_value: int, max_value: int) -> None:
    correct_count = 0
    for i in range(count):
        print(f"Exercise {i+1}/{count}")
        is_answer_correct, correct_answer = test_user_knowledge(min_value, max_value)
        if is_answer_correct:
            print("Tubli! Vastasid õigesti.")
            correct_count += 1
        else:
            print(f"Vale vastus. Õige vastus on {correct_answer}. Harjuta rohkem.")
    print(f"See oli viimane ülesanne. Kogusid {count}-st punktist {correct_count}.")

if __name__ == '__main__':
    count = int(input("Mitu korda soovid harjutada?"))
    min_value = int(input("Milline peaks olema väikseim täisarv harjutuses? "))
    max_value = int(input("Milline peaks olema suurim täisarv harjutuses?"))
    practice_addition(count, min_value, max_value)
