from random import *


class Unit:
    def __init__(self, name, rarity, rank):
        self.name = name
        self.rarity = rarity
        self.rank = rank


unit_a_one = Unit('A1', 1, 1)
unit_a_two = Unit('A2', 1, 1)
unit_b_one = Unit('B1', 2, 1)
unit_b_two = Unit('B2', 2, 1)
unit_c_one = Unit('C1', 3, 1)
unit_c_two = Unit('C2', 3, 1)
unit_d_one = Unit('D1', 4, 1)
unit_d_two = Unit('D2', 4, 1)
unit_e_one = Unit('E1', 5, 1)
unit_e_two = Unit('E2', 5, 1)

available_one_cost_units = [unit_a_one.name, unit_a_two.name]
available_two_cost_units = [unit_b_one.name, unit_b_two.name]
available_three_cost_units = [unit_c_one.name, unit_c_two.name]
available_four_cost_units = [unit_d_one.name, unit_d_two.name]
available_five_cost_units = [unit_e_one.name, unit_e_two.name]


class Shop:
    one_cost_chance = 1
    two_cost_chance = 0
    three_cost_chance = 0
    four_cost_chance = 0
    five_cost_chance = 0
    counter = 0
    shop_units = []

    def __init__(self, player):
        self.player = player

    # Method to set percentages for each level, interacted with by method: adjust_shop_chance
    def percentage_adjust(self, one_rank, two_rank, three_rank, four_rank, five_rank):
        self.one_cost_chance = one_rank
        self.two_cost_chance = two_rank
        self.three_cost_chance = three_rank
        self.four_cost_chance = four_rank
        self.five_cost_chance = five_rank

    def shop_percent(self, chosen_array):

            if random() < self.five_cost_chance:
                chosen_array.append(available_five_cost_units[randint(0, 1)])
            elif random() < self.four_cost_chance:
                chosen_array.append(available_four_cost_units[randint(0, 1)])
            elif random() < self.three_cost_chance:
                chosen_array.append(available_three_cost_units[randint(0, 1)])
            elif random() < self.two_cost_chance:
                chosen_array.append(available_two_cost_units[randint(0, 1)])
            else:
                chosen_array.append(available_one_cost_units[randint(0, 1)])


    def turn_start_shop(self):
        i = 0
        while Shop.counter <= 4:
            Shop.shop_percent(self, Shop.shop_units)
            Shop.counter += 1
        while i <= 4:
            if Shop.shop_units[i].startswith('A'):
                print(f"{Shop.shop_units[i]}", end=" ")
            if Shop.shop_units[i].startswith('B'):
                print(f"\033[32m{Shop.shop_units[i]}\033[0m", end=" ")
            if Shop.shop_units[i].startswith('C'):
                print(f"\033[34m{Shop.shop_units[i]}\033[0m", end=" ")
            if Shop.shop_units[i].startswith('D'):
                print(f"\033[35m{Shop.shop_units[i]}\033[0m", end=" ")
            if Shop.shop_units[i].startswith('E'):
                print(f"\033[33m{Shop.shop_units[i]}\033[0m", end=" ")

            i += 1

    def randomize_shop(self):
        if Shop.counter == 5:
            Shop.shop_units.clear()
            Shop.counter = 0
        while Shop.counter <= 4:
            Shop.shop_percent(self, Shop.shop_units)
            Shop.counter += 1
        p1.money -= 2


    def buy_exp(self):
        if p1.money >= 4:
            p1.exp += 4
            p1.money -= 4
        else:
            print("You don't have enough money to level up!")

    def adjust_shop_chance(self):
        match self.player.level:
            case 3:
                self.percentage_adjust(.75, .25, 0, 0, 0)
            case 4:
                self.percentage_adjust(.55, .30, .15, 0, 0)
            case 5:
                self.percentage_adjust(.45, .33, .20, .02, 0)
            case 6:
                self.percentage_adjust(.25, .40, .30, .05, 0)
            case 7:
                self.percentage_adjust(.19, .30, .35, .15, .01)
            case 8:
                self.percentage_adjust(.16, .20, .35, .25, .04)
            case 9:
                self.percentage_adjust(.09, .15, .30, .30, 16)

    def buy_unit(self, user_input):
        try:
            unit = user_input[4] + user_input[5]
            for i in Shop.shop_units:
                if i == unit:
                    i = ' '
                    print('hehe hoho')
        except IndexError:
            print("Invalid unit!")

    def income(self):
        if 0 <= p1.money <= 9:
            p1.money += 0
        elif 10 <= p1.money <= 19:
            p1.money += 1
        elif 20 <= p1.money <= 29:
            p1.money += 2
        elif 30 <= p1.money <= 39:
            p1.money += 3
        elif 40 <= p1.money <= 49:
            p1.money += 4
        else:
            p1.money += 5

def adjust_required_exp():
    match p1.level:
        case 2:
            p1.lvl_up_xp_required = 2
        case 3:
            p1.lvl_up_xp_required = 6
        case 4:
            p1.lvl_up_xp_required = 10
        case 5:
            p1.lvl_up_xp_required = 20
        case 6:
            p1.lvl_up_xp_required = 36
        case 7:
            p1.lvl_up_xp_required = 56
        case 8:
            p1.lvl_up_xp_required = 80


class Player:
    def __init__(self):
        self.level = 1
        self.money = 50
        self.exp = 0
        self.lvl_up_xp_required = 2
        self.hand = []
        self.turncounter = 0

    def level_up(self):
        if self.exp >= self.lvl_up_xp_required:
            self.level += 1
            self.exp = 0


p1 = Player()


def gameplay_loop():
    p1_shop = Shop(p1)
    while True:
        p1_shop.turn_start_shop()
        print(f"\nYou are level {p1.level}, {p1.exp}/{p1.lvl_up_xp_required}")
        print(f'You have \033[32;1;4m${p1.money}\033[0m')
        p1.level_up()
        adjust_required_exp()
        p1_shop.adjust_shop_chance()
        user_input = input('> ')

        if user_input.lower() == 'level':
            p1_shop.buy_exp()
        elif user_input == 'reroll':
            p1_shop.randomize_shop()
        elif user_input.startswith('buy'):
            p1_shop.buy_unit(user_input)
            print('hehohoho')
        elif user_input == 'end':
            p1.turncounter += 1
            p1_shop.randomize_shop()
            p1.money += 4
            p1_shop.income()

        else:
            print("\033[31;1;4mInvalid Command!\033[0m")
    p1_shop.counter = 0
    p1_shop.randomize_shop()
    print('heheheheh')
    gameplay_loop()


if __name__ == '__main__':
    gameplay_loop()
