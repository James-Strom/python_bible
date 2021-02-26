# Class is a base template for object
# Objects act independently from each other

class Pound:

	#States
	value = 1.00
	colour = "gold"
	num_edges = 1
	diameter = 22.5 #mm
	thickness = 3.15 #mm
	heads = True



coin1 = Pound()
print(coin1.colour)
coin1.colour = "blue"
print(coin1.colour)

coin2 = Pound()
print(coin2.colour)
