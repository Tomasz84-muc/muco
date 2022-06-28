class Animal:

	numAnimals = 0

	def __init__(self, length, weight, color, presenceOfFur):
		self.length = length
		self.weight = weight
		self.color = color
		self.presenceOfFur = presenceOfFur
		Animal.numAnimals += 1

myDog = Animal(49, 12, "brazowy", "true")

print (myDog.length)
print (myDog.color)
