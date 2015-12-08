#Stefan Knott FA2015
'''Barista Matic program which makes an assortment of drinks and handles inventory
and drink selection accordingly
'''

import collections
from decimal import *

def makeDrink(drinkName, drinkRecipes, ingredients):
	recipe = drinkRecipes[drinkName]
	
	#Look
	for ingr, units in recipe.items():
		if ingredients[ingr]["stock"] < units:
			print "\nOut of stock: ", drinkName, "\n"
			return 
	#Make
	print "\nDispensing: ", drinkName, "\n"
	for ingr, units in recipe.items():
		ingredients[ingr]["stock"] -= units

def restock():
	for _, info in ingredients.items():
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
		print "\nInvalid selection: ", line, "\n"

def getDrinkInfo(iD, drinkName, recipe):
	drinkCost = 0
	ret = str(iD) + "," + drinkName + ",$"

	inStock = ",true"
	for ingr, units in recipe.items():
		drinkCost += ingredients[ingr]["cost"] *  units
		if ingredients[ingr]["stock"] < units:
			inStock = ",false"
			
	return ret + str("%0.2f" % drinkCost) + inStock						


def printInventory(ingredients):
	print "Inventory:"
	for ingr, info in ingredients.items():
		for attr, num in info.items():
			if attr == "stock":
				print str(ingr + ","+ str(num))
	print "\n"

def printMenu(drinkRecipes):
	print "Menu:"

	iD = 1
	for drinkName, recipe in drinkRecipes.iteritems():
		print getDrinkInfo(iD, drinkName, recipe)
		iD += 1

def baristaMatic(drinkRecipes, ingredients):
	while True:
		printInventory(ingredients)
		printMenu(drinkRecipes)
		handleMenu(drinkRecipes, ingredients)

if __name__ == '__main__':
	ingredients = collections.OrderedDict()
	drinkRecipes = collections.OrderedDict()

	ingredients["Cocoa"] = {"cost" : Decimal(1.00), "stock" : 10}
	ingredients["Coffee"] = {"cost" : Decimal(0.85), "stock" : 10}
	ingredients["Cream"] = {"cost" : Decimal(0.25), "stock" : 10}
	ingredients["Decaf Coffee"] = {"cost" : Decimal(0.85), "stock" : 10}
	ingredients["Espresso"] = {"cost" : Decimal(1.10), "stock" : 10}
	ingredients["Foamed Milk"] = {"cost" : Decimal(.35), "stock" : 10}
	ingredients["Steamed Milk"] = {"cost" : Decimal(0.40), "stock" : 10}
	ingredients["Sugar"] = {"cost" : Decimal(0.20), "stock" : 10}
	ingredients["Whipped Cream"] = {"cost" : Decimal(1.00), "stock" : 10}

	drinkRecipes["Caffe Americano"] = {"Espresso" : 3}
	drinkRecipes["Caffe Latte"] = {"Espresso" : 2, "Steamed Milk" : 1}
	drinkRecipes["Caffe Mocha"] = {"Espresso" : 1, "Cocoa" : 1, "Steamed Milk" : 1, "Whipped Cream" : 1}
	drinkRecipes["Cappuccino"] = {"Espresso" : 2, "Steamed Milk" : 1, "Foamed Milk" : 1}
	drinkRecipes["Coffee"] = {"Coffee" : 3, "Sugar" : 1, "Cream" : 1}
	drinkRecipes["Decaf Coffee"] = {"Decaf Coffee" : 3, "Sugar" : 1, "Cream" : 1}

	baristaMatic(drinkRecipes, ingredients)