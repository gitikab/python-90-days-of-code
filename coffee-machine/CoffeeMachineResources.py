class CoffeeMachineResources:
    def __init__(self, water_in_ml, milk_in_ml, coffee_in_gm):
        self.water_in_ml = water_in_ml
        self.milk_in_ml = milk_in_ml
        self.coffee_in_gm = coffee_in_gm
        self.money = 0

    def sufficient_resources(self, menu_item):
        if self.water_in_ml < menu_item.water:
            print("Sorry there is not enough water")
            return False
        elif self.milk_in_ml < menu_item.milk:
            print("Sorry there is not enough milk")
            return False
        elif self.coffee_in_gm < menu_item.coffee:
            print("Sorry there is not enough coffee")
            return False
        else:
            return True

    def print_report(self):
        print(f"Water: {self.water_in_ml}ml")
        print(f"Milk: {self.milk_in_ml}ml")
        print(f"Coffee: {self.coffee_in_gm}gm")
        print(f"Money: ${self.money}")

    def update(self, menu_item):
        self.water_in_ml -= menu_item.water
        self.milk_in_ml -= menu_item.milk
        self.coffee_in_gm -= menu_item.coffee
        self.money += menu_item.cost
