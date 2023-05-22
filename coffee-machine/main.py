from CoffeeMachine import CoffeeMachine
from CoffeeMachineResources import CoffeeMachineResources
from MenuItem import menu

coffee_machine_resources = CoffeeMachineResources(1000, 750, 200)
coffee_machine = CoffeeMachine(coffee_machine_resources, menu)
while coffee_machine.on:
    coffee_machine.take_instruction()
