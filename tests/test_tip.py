from app.tip import split_tip


def test_float_tip_and_integer_guest():
    assert split_tip(15.16, 3) == split_tip(15.16, 3)


def test_string_tip_and_integer_guest():
    assert split_tip("q", 3) == False


def test_float_tip_and_string_guest():
    assert split_tip(15.16, "R") == False


def test_string_tip_and_string_guest():
    assert split_tip("Q", "A") == False


def test_float_tip_and_zero_guest():
    assert split_tip(15.16, 0) == False


def test_string_tip_and_zero_guest():
    assert split_tip("Q", 0) == False


def test_zero_tip_and_integer_guest():
    assert split_tip(0, 3) == False


def test_zero_tip_and_string_guest():
    assert split_tip(0, "U") == False


def test_float_tip_and_float_guest():
    assert split_tip(15.16, 3.5) == [5.81, 5.81, 5.81]


def test_integer_tip_and_integer_guest():
    assert split_tip(4, 4) == [1.15, 1.15, 1.15, 1.15]
