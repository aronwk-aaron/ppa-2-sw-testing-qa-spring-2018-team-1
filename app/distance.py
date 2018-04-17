def calc_distance(x1, y1, x2, y2):
	# checking for non int or float inputs
	try: 
		x1 = float(x1) 
	except: 
		return False 
	try: 
		x2 = float(x2) 
	except:     
		return False 
	try: 
		y1 = float(y1) 
	except: 
		return False 
	try: 
		y2 = float(y2) 
	except: 
		return False 

	# if the points are the same
	if ((x1 == x2) and (y1 == y2)):
		return 0
	# Calc distance
	else:
		distance = ((((x2-x1)**2)+((y2-y1)**2))**0.5)
		return round(distance,4)