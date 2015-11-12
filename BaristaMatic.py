import fileinput

def makeDrink(drinkName, drinkRecipes, ingredients):
	recipe = drinkRecipes[drinkName]
	for ingrName, units in recipe.iteritems():
		if ingredients[ingrName]["stock"] >= units:
			ingredients[ingrName]["stock"] -= units
		else:
			print "Not enough ingredients to make ", drinkName, " choose another"
			return 

	print "Dispensing: ", drinkName

def restock():
	for name, info in ingredients.iteritems():
		for attr, num in info.iteritems():
			if attr == "stock" and num < 10:
				info[attr] = 10

def handleMenu(drinkRecipes, ingredients):
	line = raw_input()
	if line == 'q' or line == 'Q':
		exit(1)
	elif line == "r" or line == "R":
		restock()
	elif int(line) == 1:
		makeDrink("Coffee", drinkRecipes, ingredients)
	elif int(line) == 2:
		makeDrink("Cappuccino", drinkRecipes, ingredients)
	elif int(line) == 3:
		makeDrink("DecafCoffee", drinkRecipes, ingredients)
	elif int(line) == 4:
		makeDrink("CaffeLatte", drinkRecipes, ingredients)
	elif int(line) == 5:
		makeDrink("CaffeAmericano", drinkRecipes, ingredients)
	elif int(line) == 6:
		makeDrink("CaffeMocha", drinkRecipes, ingredients)
	baristaMatic(drinkRecipes, ingredients)

def getDrinkInfo(iD, drinkName, recipe):
	drinkCost = 0
	for ingrName, units in recipe.iteritems():
		drinkCost += ingredients[ingrName]["cost"] *  units
		if ingredients[ingrName]["stock"] <= 0:
			#missing ingredients..
			return str(iD) + ", " + drinkName + ", $" + str(drinkCost) + ",false"
				
	#have ingredients..
	return str((str(iD) + ", " + drinkName + ", $" + str(drinkCost), ",true")).replace("(", "").replace("'", "").replace(")", "")


def printInventory(ingredients):
	print "Inventory:"
	for name, info in ingredients.iteritems():
		for attr, num in info.iteritems():
			if attr == "stock":
				print name, ",", num

def printMenu(drinkRecipes):
	print "Menu:"
	#could make optionMenu dict for dynamic number selection
	iD = 1
	for drinkName, recipe in drinkRecipes.iteritems():
		print getDrinkInfo(iD, drinkName, recipe)
		iD += 1

def baristaMatic(drinkRecipes, ingredients):
	printInventory(ingredients)
	printMenu(drinkRecipes)
	handleMenu(drinkRecipes, ingredients)

if __name__ == '__main__':
	ingredients = {"coffee" : {"cost" : 0.85, "stock" : 10}, 
					"decafCoffe" : {"cost" : 0.85, "stock" : 10}, 
					"sugar" : {"cost" : 0.20, "stock" : 10}, 
					"cream" : {"cost" : 0.25, "stock" : 10}, 
					"steamMilk" : {"cost" : 0.4, "stock" : 10},
					"foamMilk" : {"cost" : .35, "stock" : 10},
					"espresso" : {"cost" : 1.10, "stock" : 10},
					"cocoa" : {"cost" : 1.10, "stock" : 10},
					"whippedCream" : {"cost" : 1.00, "stock" : 10}}
	
	drinkRecipes = {"Coffee" : {"coffee" : 3, "sugar" : 1, "cream" : 1},
				"DecafCoffee" : {"decafCoffe" : 3, "sugar" : 1, "cream" : 1},
				"CaffeLatte" : {"espresso" : 2, "steamMilk" : 1},
				"CaffeAmericano" : {"espresso" : 3},
				"CaffeMocha" : {"espresso" : 1, "cocoa" : 1, "steamMilk" : 1, "whippedCream" : 1},
				"Cappuccino" : {"espresso" : 2, "steamMilk" : 1, "foamMilk" : 1}}

	baristaMatic(drinkRecipes, ingredients)