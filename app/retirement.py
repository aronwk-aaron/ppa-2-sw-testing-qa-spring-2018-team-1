# William Thompson (wtt53)
# Software Testing and QA
# Assignment 1: Test Driven Development
# Retirement: Takes current age (int), annual salary (float),
# percent of annual salary saved (float), and savings goal (float)
# and outputs what age savings goal will be met


def calc_retirement(age, salary, percent, goal):

    # cast each variable as its proper data type
    try:
        age = int(age)
        salary = float(salary)
        percent = float(percent)
        goal = float(goal)
    except Exception:
        return (False)

    # check each value to make sure it is in the proper range
    if ((age < 15 or age > 99)
            or (salary <= 0)
            or (percent <= 0)
            or (goal <= 0)):
        return (False)
    # savings from salary without employer's 35%
    rawAnnualSavings = salary * (percent / 100)
    # total annual savings including employer's 35%
    annualSavings = rawAnnualSavings + (rawAnnualSavings * 0.35)
    # total savings so far
    currentSavings = 0.00

    # add annual savings to total savings for each year until age 100
    for i in range(age, 100):
        currentSavings += annualSavings
        if currentSavings >= goal:
            return("You will meet your savings goal at age "+str(i))
    # Notify user if they will not meet their goal
    return("Sorry, your goal won't be met.")
