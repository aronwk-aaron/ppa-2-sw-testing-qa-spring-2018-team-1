# William Thompson (wtt53)
# Tests for retirement functionality

from app.retirement import retirement


def test_InvalidAgeTypeRaisesValueError():
    assert retirement("string", 50000.00, 35.0, 1000000.00) == False


def test_InvalidSalaryTypeRaisesValueError():
    assert retirement(50, "string", 35.0, 1000000.00) == False


def test_InvalidPercentTypeRaisesValueError():
    assert retirement(50, 50000.00, "string", 1000000.00) == False


def test_InvalidGoalTypeRaisesValueError():
    assert retirement(50, 50000.00, 35.0, "string") == False


def test_InvalidAgeValueRaisesValueError():
    assert retirement(102, 50000.00, 35.0, 1000000.00) == False


def test_InvalidSalaryValueRaisesValueError():
    assert retirement(50, -50.00, 35.0, 1000000.00) == False


def test_InvalidPercentValueRaisesValueError():
    assert retirement(50, 50000.00, -5.0, 1000000.00) == False


def test_InvalidGoalValueRaisesValueError():
    assert retirement(50, 50000.00, 35.0, -75.00) == False


def test_RetirementOutputIfGoalMet():
    assert isinstance(retirement(50, 50000.00, 35.0, 1000000.00), str)


def test_RetirementOutputIfGoalNotMet():
    assert isinstance(retirement(50, 50000.00, 35.0, 10000000000000000.00), str)
