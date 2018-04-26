# Jahrell Harris netID: jah1254
# Software Testing Q&A
# Spliting bill amount among guest is what this code's functionality is
# It accepts only a float value as the bill amount and
# only an integer value as the guest amount
# Retruns False when the conditions above are violated and
# also when any value is 0 for either guest or bill
# Function for splitting tips accepts (float,int)


def split_tip(bill, guest_count):

    # Ensures that given input matches desired
    # input(input does not violate accepted data types)
    try:
        bill = float(bill)
        guest_count == int(guest_count)
    except Exception:
        return False

    if ((bill == 0) or (guest_count == 0.0)):
        return False

    # If given valid input calculates bill values for each guest
    # rounded to 2 decimal places

    guest_count = int(guest_count)
    bill *= 1.15

    split = bill / guest_count
    guest_array = [round(split, 2)]
    total = bill - guest_array[0]

    for value in range(2, guest_count):
        guest_array.append(round(split, 2))
        total = total - guest_array[value - 1]
    guest_array.append(round(total, 2))

    return guest_array
