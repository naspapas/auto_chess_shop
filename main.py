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
unit_c_one = Unit('C1', 1, 1)
unit_c_two = Unit('C2', 1, 1)
unit_d_one = Unit('D1', 1, 1)
unit_d_two = Unit('D2', 1, 1)
unit_e_one = Unit('E1', 1, 1)
unit_e_two = Unit('E2', 1, 1)

available_one_cost_units = [unit_a_one.name, unit_a_two.name]
available_two_cost_units = [unit_b_one.name, unit_b_two.name]
available_three_cost_units = [unit_a_one.name, unit_a_two.name]
available_four_cost_units = [unit_a_one.name, unit_a_two.name]
available_five_cost_units = [unit_a_one.name, unit_a_two.name]


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
        Shop.one_cost_chance = one_rank
        Shop.two_cost_chance = two_rank
        Shop.three_cost_chance = three_rank
        Shop.four_cost_chance = four_rank
        Shop.five_cost_chance = five_rank

    def shop_percent(self, chosen_array):
            Shop.shop_units.clear()
            if random() < Shop.five_cost_chance:
                chosen_array.append(available_five_cost_units[randint(0, len(available_five_cost_units))])
            if random() < Shop.four_cost_chance:
                chosen_array.append(available_four_cost_units[randint(0, len(available_four_cost_units))])
            if random() < Shop.three_cost_chance:
                chosen_array.append(available_three_cost_units[randint(0, len(available_three_cost_units))])
            if random() < Shop.two_cost_chance:
                chosen_array.append(available_two_cost_units[randint(0, len(available_two_cost_units))])
            else:
                chosen_array.append(available_one_cost_units[randint(0, 1)])


    def turn_start_shop(self):
        while Shop.counter <= 4:
            Shop.shop_percent(self, Shop.shop_units)
            Shop.counter += 1
        print(Shop.shop_units)

    def randomize_shop(self):

        while Shop.counter <= 4:
            Shop.shop_percent(self, Shop.shop_units)
            Shop.counter += 1
        print(Shop.shop_units)

    def buy_exp(self):
        if p1.money >= 4:
            p1.exp += 4
            p1.money -= 4
        else:
            print("You don't have enough money to level up!")

    def adjust_shop_chance(self):
        match p1.level:
            case 3:
                Shop.percentage_adjust(Shop, .75, .25, 0, 0, 0)
            case 4:
                Shop.percentage_adjust(Shop, .55, .30, .15, 0, 0)
            case 5:
                Shop.percentage_adjust(Shop, .45, .33, .20, .02, 0)
            case 6:
                Shop.percentage_adjust(Shop, .25, .40, .30, .05, 0)
            case 7:
                Shop.percentage_adjust(Shop, .19, .30, .35, .15, .01)
            case 8:
                Shop.percentage_adjust(Shop, .16, .20, .35, .25, .04)
            case 9:
                Shop.percentage_adjust(Shop, .09, .15, .30, .30, 16)


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

    def level_up(self):
        if p1.exp >= p1.lvl_up_xp_required:
            p1.level += 1
            p1.exp = 0


p1 = Player()


def gameplay_loop(self):
    while True:
        Shop.turn_start_shop(Shop)
        print(f"You are level {p1.level}, {p1.exp}/{p1.lvl_up_xp_required}")
        print(f'You have ${p1.money}')
        Player.level_up(p1)
        adjust_required_exp()
        user_input = input('> ')
        if user_input == 'level':
            Shop.buy_exp(p1)

        if user_input == 'reroll':
            Shop.randomize_shop(Shop)

    Shop.counter = 0


if __name__ == '__main__':
    gameplay_loop(p1)
