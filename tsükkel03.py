from random import randint

def get_addition_calculation(min_value: int, max_value: int) -> tuple[str, int]:
    num1 = randint(min_value, max_value)
    num2 = randint(min_value, max_value)
    correct_answer = num1 + num2
    return f"{num1} + {num2} = ", correct_answer

def test_user_knowledge(min_value: int, max_value: int) -> tuple [bool, int]:
    calculation, correct_answer = get_addition_calculation(min_value, max_value)
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
    min_value = 1
    max_value = 50
    count = 10
    practice_addition(count, min_value, max_value)
