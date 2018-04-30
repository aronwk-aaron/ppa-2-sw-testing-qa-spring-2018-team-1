# Austin Parker
# ajp310
# CSE 4283 Software Testing and Quality Assurance
# Professional Practice Assignment 1
# Behavior-Driven Development and Unit Testing

# calc_bmi(f,i,p) takes in 3 integers (feet, inches, pounds)
# and calculates BMI based on input.
# Returns tuple with the form ("category", bmi),
# where category is a string and bmi is your numerical bmi

# feet must be between 0 and 10
# inches must be between 0 and 11
# pounds must be between 0 and 1000
# Floating point input is rounded down


def calc_bmi(f, i, p):
    feet = int(f)
    inches = int(i)
    pounds = int(p)

    if feet > 10:
        raise ValueError
        
    if inches > 11:
        raise ValueError

    if pounds > 1000:
        raise ValueError

    # combine feet and inches
    height = (feet*12) + inches

    kg = pounds * 0.45
    m = height * 0.025
    squared_m = m*m
    bmi = kg / squared_m
    final_bmi = round(bmi, 1)

    if final_bmi >= 30:
        return ("Obese", final_bmi)
    elif 29.9 >= final_bmi >= 25:
        return ("Overweight", final_bmi)
    elif 24.9 >= final_bmi >= 18.5:
        return ("Normal weight", final_bmi)
    else:
        return ("Underweight", final_bmi)
