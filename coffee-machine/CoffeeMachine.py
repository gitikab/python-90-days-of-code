class CoffeeMachine:
    def __init__(self, resources, menu):
        self.resources = resources
        self.menu = menu
        self.on = True

    def take_instruction(self):
        instruction = input("What would you like to do? (order/report/off): ").lower()
        if instruction == 'report':
            self.resources.print_report()
        elif instruction == 'off':
            self.on = False
        elif instruction == 'order':
            self.take_order()
        else:
            print("Invalid instruction!! Please try again")

    def take_order(self):
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        recipe = self.menu[order]
        if self.resources.sufficient_resources(recipe):
            inserted_money = self.insert_money(recipe.cost)
            if inserted_money < recipe.cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                self.complete_transaction(recipe, inserted_money)

    def insert_money(self, amount):
        print(f"Please insert coins worth ${amount}")
        quarter = int(input("Insert quarters: "))
        dime = int(input("Insert dimes: "))
        nickel = int(input("Insert nickels: "))
        penny = int(input("Insert pennies: "))
        return 0.25 * quarter + 0.1 * dime + 0.05 * nickel + 0.01 * penny

    def complete_transaction(self, item, amount_inserted):
        if amount_inserted > item.cost:
            print(f"Here is the change ${amount_inserted - item.cost}")
        self.resources.update(item)
        print(f"Here is your {item.name}. Enjoy!!")

