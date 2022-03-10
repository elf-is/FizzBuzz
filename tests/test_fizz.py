from src.fizzbuzz import fizz_buzz_converter, list_factory


def test_when_number_is_multiple_of_3_should_return_fizz():
    assert fizz_buzz_converter(3) == "fizz"


def test_when_number_is_multiple_of_5_should_return_buzz():
    assert fizz_buzz_converter(5) == "buzz"


def test_when_number_is_multiple_of_15_should_return_fizzbuzz():
    assert fizz_buzz_converter(15) == "fizzbuzz"


def test_when_number_is_not_multiple_of_3_5_15_should_return_number():
    assert fizz_buzz_converter(16) == "16"


def test_when_given_a_number_return_a_list():
    assert list_factory(5) == [5]
