#Jahrell Harris netID: jah1254
#Software Testing Q&A
#Spliting Tip amount among guest is what this code's functionality is
#It accepts only a float value as the tip amount and only an integer value as the guest amount
#Retruns False when the conditions above are violated and also when any value is 0 for either guest or tip

#Function for splitting tips accepts (float,int)
def split_tip(tip, guest_count):

	#Ensures that given input matches desired input(input does not violate accepted data types)
    try:
        float(tip)
    except Exception as e:
        return False
    try :
        int(guest_count)
    except Exception as e:
        return False

    if ((float(tip) == 0) \
    or (int(guest_count) == 0))\
    or (float(tip) == round(float(tip)))\
    or ((float(guest_count)) != round(float(guest_count))):
        return False

	#If given valid input calculates tip values for each guest rounded to 2 decimal places

    guest_count = int(guest_count)
    tip = float(tip)
    tip_split_var = tip / guest_count
    guest_array = [round(tip_split_var, 2)]
    total = tip - guest_array[0]
    for value in range(2, guest_count):
        guest_array.append(round(tip_split_var, 2))
        total = total - guest_array[value - 1]
    guest_array.append(round(total, 2))

    return guest_array
