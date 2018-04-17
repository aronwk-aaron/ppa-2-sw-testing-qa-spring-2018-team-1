from app.distance import calc_distance

def test_distance_same():
	assert calc_distance(1,1,1,1) == 0

def test_distance_one():
	assert calc_distance(0,0,1,0) == 1

def test_distance_offset():
	assert calc_distance(5,2,602,5) == 597.0075

def test_distance_flaot():
	assert calc_distance(1.25,5.2,8.9,8.33) == 8.2656

def test_distance_is_float():
	test_is_float = isinstance(calc_distance(5,5,2,6), float)
	assert test_is_float == True

def test_distance_word_x1():
	assert calc_distance("word",1,2,3) == False

def test_distance_word_x2():
	assert calc_distance(1,2,"word",3) == False

def test_distance_word_y1():
	assert calc_distance(1,"word",2,3) == False

def test_distance_word_y2():
	assert calc_distance(1,2,3,"word") == False

def test_distance_large():
	assert calc_distance(10000000,0,-1000000,5555555) == 12323319.0074

def test_distance_negitive():
	assert calc_distance(-5,-10,1,1) == 12.53