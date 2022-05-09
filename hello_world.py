# 1. TASK: print "Hello World"
from unittest.util import three_way_cmp


print( "Hello World" )
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print(name , ",")	# with a comma
print(name , "+")	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print(name , ",")	# with a comma
print(name , "+" )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1 , fave_food2) ) # with .format()
print(f"I Love to eat {fave_food1} and {fave_food2}./n/n") # with an f string

# 1a
print ("Hello World")
# 2a
they = "Cesar"
print( "Hello" , they)
# 2b
print("Hello" + they)
# 3a
num = 67
print("Hello" , num)
# 3b
print ("Hello" + str(num))
# extra
fave_f1 = "Pizza"
fave_f2 = "Chinese"
print ("I love to eat {} and {}" .format(fave_f1 , fave_f2))
# extra 2 
print (f"i love to eat {fave_f1} and {fave_f2}")
