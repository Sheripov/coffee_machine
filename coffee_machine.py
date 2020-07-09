class Coffee_machine:
    def __init__(self):
        self.water_in = 400
        self.milk_in = 540
        self.coffee_in = 120
        self.cups_in = 9
        self.money_in = 550
        self.start_menu()

    def remaining(self):
        print("\nThe coffee machine has:")
        print(self.water_in, "of water")
        print(self.milk_in, "of milk")
        print(self.coffee_in, "of coffee beans")
        print(self.cups_in, "of disposable cups")
        print("$" + str(self.money_in), "of money")

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water_in += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk_in += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.coffee_in += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups_in += int(input())
    def safe_division(a, b):
        if not b:
            return a
        return a // b

    def buy(self):
        def type_of_coffee(water, milk, coffee, costs, need_cups_coffee):
            ingredients_need = {
                "milk": safe_division(self.milk_in, milk),
                "coffee": safe_division(self.coffee_in, coffee),
                "water": safe_division(self.water_in, water),
                "cups": safe_division(self.cups_in, need_cups_coffee)
            }
            can_make = min(
                int(ingredients_need["milk"]),
                int(ingredients_need["coffee"]),
                int(ingredients_need["water"]),
                int(ingredients_need["cups"])
            )
            if can_make >= need_cups_coffee:
                self.water_in -= water * need_cups_coffee
                self.milk_in -= milk * need_cups_coffee
                self.coffee_in -= coffee * need_cups_coffee
                self.cups_in -= need_cups_coffee
                self.money_in += costs * need_cups_coffee
                print("I have enough resources, making you a coffee!")
            else:
                if water > self.water_in:
                    print("Sorry, not enough water!")
                elif milk > self.milk_in:
                    print("Sorry, not enough milk!")
                elif coffee > self.coffee_in:
                    print("Sorry, not enough coffee!")
                elif self.cups_in < 1:
                    print("Sorry, not enough cups!")

        print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        switch2 = input()
        if switch2 == "1":
            type_of_coffee(250, 0, 16, 4, 1)  # espresso
        elif switch2 == "2":
            type_of_coffee(350, 75, 20, 7, 1)  # latte
        elif switch2 == "3":
            type_of_coffee(200, 100, 12, 6, 1)  # cappuccino
        elif switch2 == "back":
            self.start_menu()  # back

    def take(self):
        print("I gave you $", self.money_in)
        self.money_in = 0

    def start_menu(self):
        while True:
            print("\nWrite action (buy, fill, take, remaining, exit):")
            switch = input()
            if switch == "buy":
                self.buy()
            elif switch == "fill":
                self.fill()
            elif switch == "take":
                self.take()
            elif switch == "remaining":
                self.remaining()
            elif switch == "exit":
                exit()
            else:
                print("Please, choose from the list")
                continue


coffee_maker = Coffee_machine()
