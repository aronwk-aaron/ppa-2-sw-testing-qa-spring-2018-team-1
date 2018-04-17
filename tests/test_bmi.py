# Austin Parker
# ajp310
# CSE 4283 Software Testing and Quality Assurance
# Professional Practice Assignment 1 --- Behavior-Driven Development and Unit Testing


from app.bmi import calc_bmi
import pytest

# Underweight = <18.5
# Normal weight  = 18.5–24.9
# Overweight = 25–29.9
# Obese = BMI of 30 or greater


def test_null_values_raiseValueError():
    with pytest.raises(ValueError):
        calc_bmi("", "", "")


def test_valid_inputs_return_tuple():
    assert type(calc_bmi(6, 0, 150)) is tuple


def test_UW_inputs_return_UW_BMI():
    # UW is underweight
    assert calc_bmi(6, 3, 110) == ("Underweight", 14.1)


def test_normal_inputs_return_normal_BMI():
    assert calc_bmi(5, 3, 102) == ("Normal weight", 18.5)


def test_OW_inputs_return_OW_BMI():
    # OW is overweight
    assert calc_bmi(5, 7, 180) == ("Overweight", 28.9)


def test_obese_inputs_return_obese_BMI():
    assert calc_bmi(6, 0, 250) == ("Obese", 34.7)


def test_string_inputs_raise_ValueError():
    with pytest.raises(ValueError):
        calc_bmi(5, "world", 185)


def test_list_inputs_raise_TypeError():
    with pytest.raises(TypeError):
        calc_bmi(6, 5, [120])


def test_float_inputs_round_down():
    # calc_bmi(6.1,3.9,110.4) = calc_bmi(6,3,110)
    assert calc_bmi(6.1, 3.9, 110.4) == ("Underweight", 14.1)


def test_feet_input_larger_than_10_raises_ValueError():
    with pytest.raises(ValueError):
        calc_bmi(11, 2, 180)


def test_inches_input_larger_than_11_raises_ValueError():
    with pytest.raises(ValueError):
        calc_bmi(6, 12, 180)


def test_pounds_input_larger_than_1000_raises_ValueError():
    with pytest.raises(ValueError):
        calc_bmi(5, 4, 1001)
