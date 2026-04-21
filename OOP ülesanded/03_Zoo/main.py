"""Zoo exercise."""
from animal import Animal
from zoo import Zoo

if __name__ == '__main__':
    a1 = Animal("Pauka", "Koer", 3)
    a2 = Animal("Pauka", "Koer", 15)
    b3 = Animal("Flipper", "Delfiin", 20)
    b4 = Animal("Jet", "Delfiin", 2)
    b5 = Animal("Jet", "Sebra", 2)
    z1 = Zoo("Tallinna Loomaaed", 3)
    assert True == z1.can_add_animal(a1)
    assert True == z1.can_add_animal(a2)
    z1.add_animal(a1)
    assert False == z1.can_add_animal(a1)
    assert False == z1.can_add_animal(a1)

    assert True == z1.can_remove_animal(a1)
    assert True == z1.can_remove_animal(a1)
    z1.add_animal(a2)
    assert True == z1.can_remove_animal(a1)
    assert True == z1.can_remove_animal(a1)

    assert True == z1.can_add_animal(b3)
    assert True == z1.can_add_animal(b4)
    assert True == z1.can_add_animal(b5)
    z1.add_animal(b3)
    assert False == z1.can_add_animal(b3)
    assert False == z1.can_add_animal(b4)
    assert False == z1.can_add_animal(b5)
    z1.add_animal(a1)
    assert False == z1.can_add_animal(b3)
    assert False == z1.can_add_animal(b4)
    assert False == z1.can_add_animal(b5)

    print(z1.get_all_animals())
    print(z1.get_animals_by_age)





