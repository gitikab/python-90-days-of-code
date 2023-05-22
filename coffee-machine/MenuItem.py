class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost


ESPRESSO = MenuItem("espresso", 50, 0, 18, 1.5)
LATTE = MenuItem("latte", 200, 150, 24, 2.5)
CAPPUCCINO = MenuItem("cappuccino", 250, 100, 24, 3)

menu = {
    "espresso": ESPRESSO,
    "latte": LATTE,
    "cappuccino": CAPPUCCINO
}
