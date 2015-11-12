#Stefan Knott FA2015
'''Barista Matic program which makes an assortment of drinks and handles inventory
and drink selection accordingly
'''

import fileinput, collections

def makeDrink(drinkName, drinkRecipes, ingredients):
	recipe = drinkRecipes[drinkName]
	
	#Look
	for ingrName, units in recipe.items():
		if ingredients[ingrName]["stock"] < units:
			print "Out of stock: ", drinkName
			return 

	#Make
	print "Dispensing: ", drinkName
	for ingrName, units in recipe.items():
		ingredients[ingrName]["stock"] -= units

def restock():
	for name, info in ingredients.items():
		for attr, num in info.items():
			if attr == "stock" and num < 10:
				info[attr] = 10

def handleMenu(drinkRecipes, ingredients):
	line = raw_input()

	if line == 'q' or line == 'Q':
		exit(1)
	elif line == "r" or line == "R":
		restock()
	elif int(line) == 1:
		makeDrink("Caffe Americano", drinkRecipes, ingredients)
	elif int(line) == 2:
		makeDrink("Caffe Latte", drinkRecipes, ingredients)
	elif int(line) == 3:
		makeDrink("Caffe Mocha", drinkRecipes, ingredients)
	elif int(line) == 4:
		makeDrink("Cappuccino", drinkRecipes, ingredients)
	elif int(line) == 5:
		makeDrink("Coffee", drinkRecipes, ingredients)
	elif int(line) == 6:
		makeDrink("Decaf Coffee", drinkRecipes, ingredients)
	else:
		print "Invalid selection: ", line

	baristaMatic(drinkRecipes, ingredients)

def getDrinkInfo(iD, drinkName, recipe):
	drinkCost = 0
	for ingrName, units in recipe.items():
		drinkCost += ingredients[ingrName]["cost"] *  units
		if ingredients[ingrName]["stock"] <= 0:
			#missing ingredients..
			return str(iD) + "," + drinkName + ",$" + str(drinkCost) + ",false"
				
	#have ingredients..odd how return string is formatted differently here than in for:if (hence the replace() chaining):
	return str((str(iD) + "," + drinkName + ",$" + str(drinkCost), ",true")).replace("(", "").replace("'", "").replace(")", "")


def printInventory(ingredients):
	print "Inventory:"
	for name, info in ingredients.items():
		for attr, num in info.items():
			if attr == "stock":
				print name, ",", num

def printMenu(drinkRecipes):
	print "Menu:"

	iD = 1
	for drinkName, recipe in drinkRecipes.iteritems():
		print getDrinkInfo(iD, drinkName, recipe)
		iD += 1

def baristaMatic(drinkRecipes, ingredients):
	printInventory(ingredients)
	printMenu(drinkRecipes)
	handleMenu(drinkRecipes, ingredients)

if __name__ == '__main__':
	ingredients = collections.OrderedDict()
	drinkRecipes = collections.OrderedDict()

	ingredients["Cocoa"] = {"cost" : 1.10, "stock" : 10}
	ingredients["Coffee"] = {"cost" : 0.85, "stock" : 10}
	ingredients["Cream"] = {"cost" : 0.25, "stock" : 10}
	ingredients["Decaf Coffee"] = {"cost" : 0.85, "stock" : 10}
	ingredients["Espresso"] = {"cost" : 1.10, "stock" : 10}
	ingredients["Foamed Milk"] = {"cost" : .35, "stock" : 10}
	ingredients["Steam Milk"] = {"cost" : 0.4, "stock" : 10}
	ingredients["Sugar"] = {"cost" : 0.20, "stock" : 10}
	ingredients["Whipped Cream"] = {"cost" : 1.00, "stock" : 10}

	drinkRecipes["Caffe Americano"] = {"Espresso" : 3}
	drinkRecipes["Caffe Latte"] = {"Espresso" : 2, "Cocoa" : 1, "Steam Milk" : 1, "Whipped Cream" : 1}
	drinkRecipes["Caffe Mocha"] = {"Espresso" : 2, "Steam Milk" : 1}
	drinkRecipes["Cappuccino"] = {"Espresso" : 2, "Steam Milk" : 1, "Foamed Milk" : 1}
	drinkRecipes["Coffee"] = {"Coffee" : 3, "Sugar" : 1, "Cream" : 1}
	drinkRecipes["Decaf Coffee"] = {"Decaf Coffee" : 3, "Sugar" : 1, "Cream" : 1}

	baristaMatic(drinkRecipes, ingredients)