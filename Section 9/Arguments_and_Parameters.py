# Parameters represented by name, age, likes

def about(name, age, likes):
	sentence = "Meet {}! They are {} years old and they like {}".format(name,age,likes)
	return sentence

print(about("Jack", 23, "Python"))

# Keyword argument
print(about(name = "Jack", age = 23, likes = "Python"))

# Setting a default value
# default values must go last
def about(name, age, likes = "Python"):
	sentence = "Meet {}! They are {} years old and they like {}".format(name,age,likes)
	return sentence

print(about("Jack", 23))

# Can be overridden
print(about("Jack", 23, "Football"))