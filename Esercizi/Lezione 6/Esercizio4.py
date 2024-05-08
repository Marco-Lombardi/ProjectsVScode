# Marco Lombardi
# Exercise 4 Folder 9
# 08/05/2024

class Food:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

class Menu:
    def __init__(self, foods=None):
        if foods is None:
            self.foods = []
        else:
            self.foods = foods

    def addFood(self, food):
        self.foods.append(food)
        print(f"{food.name} has been added to the menu.")

    def removeFood(self, food):
        if food in self.foods:
            self.foods.remove(food)
            print(f"{food.name} has been removed from the menu.")
        else:
            print(f"{food.name} is not in the menu.")

    def printPrices(self):
        print("Menu Prices:")
        for food in self.foods:
            print(f"{food.name}: ${food.price}")

# Instantiate some food items
pizza = Food("Pizza", 10.99, "Delicious pizza with cheese, tomato sauce, and toppings.")
burger = Food("Burger", 8.99, "Juicy beef patty with lettuce, tomato, onion, and pickles.")
salad = Food("Salad", 6.99, "Fresh greens with assorted vegetables and choice of dressing.")

# Instantiate the menu with some initial foods
menu = Menu([pizza, burger])

# Add more foods to the menu
menu.addFood(salad)

# Print menu prices
menu.printPrices()
 
   

   

   

  

  

  

  

  





  