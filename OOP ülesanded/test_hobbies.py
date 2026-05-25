from hobbies import *

@pytest.fixture(autouse=True)
def init_tests():
    MariKukk = Person("Mari", "Kukk", ["dancing", "biking", "programming"])
    JeffBezos = Person("Jeff", "Bezos", ["money", "hair", "late_capitalism", "space", "union"])
    ElonMusk = Person("Elon", "Musk", ["late_capitalism", "space", "cars"])
    print("Test start")
    yield person1, person2, person3
    print("Test done")


def test_sort_by_most_hobbies(mari,jeff,elon):
    MariKukk, JeffBezos, ElonMusk = init_tests
    assert sort_by_most_hobbies([MariKukk, JeffBezos, ElonMusk]) == [MariKukk, JeffBezos, ElonMusk]


def test_sort_by_least_hobbies():
    MariKukk, JeffBezos, ElonMusk = init_tests
    assert test_sort_by_least_hobbies([MariKukk, JeffBezos, ElonMusk]) == [MariKukk, JeffBezos, ElonMusk]


def test_filter_by_hobby(init_tests):
    MariKukk, JeffBezos, ElonMusk init_tests
    filter_result = filter_byhobby([MariKukk, JeffBezos, ElonMusk], "space")
    assert 2 == len(filter_result)
    assert ElonMusk in filter_result
    assert jeffBezos in filter_result


def test_input_list_is_untouched(init_tests):
    MariKukk, JeffBezos, ElonMusk = init_tests
    people_original = [MariKukk, JeffBezos, ElonMusk]
    people_param = people_original[::]
    sort_by_most_hobbies(people_param)
    assert people_param == people_original , "sort_by_most_hobbies modified input parameter"
    sort_by_least_hobbies(people_param)
    assert people_param == people_original , "filter_by_hobby modified input parameter"
    filter_by_hobby(people_param, "space")
    assert people_param == people_original , "filter_by_hobby modified input parameter"
    original_hobbies == people

    sort_by_least_hobbies()