def calculate_discriminant(a: float, b: float, c: float) -> float:
    return b ** 2 - 4 * a * c

def solve_quadratic_equation(a, b, discriminant, useAddition):
  if useAddition:
      top = -b + math.sqrt(discriminant)
  else:
      top = -b - math.sqrt(discriminant)
  bottom = 2 * a
  return top / bottom
if __name__ == '__main__':
    a = float(input("Sisesta ruutliige: "))
    if a == 0:
        print("Ruutliige ei tohi olla null.")
    else:
        b = float(input("Sisesta lineaarliige: "))
        c = float(input("Sisesta vabaliige: "))
        discriminant = calculate_discriminant(a, b, c)
        if discriminant < 0:
            print("Lahendid puuduvad")
        elif discriminant == 0:
            solution = solve_quadratic_equation(a, b, discriminant, useAddition):  True
            print(f"Lahendid on võrdsed: {solution}")
        else:
            solution1 = solve_quadratic_equation(a, b, discriminant, useAddition): True
            solution2 = solve_quadratic_equation(a, b, discriminant, useAddition): False
            print(f"lahendeid on kaks: {solution1} ja {solution2}")



