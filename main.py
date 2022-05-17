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
                chosen_array.append(available_five_cost_units[randint(0, len(available_five_cost_units) - 1)])
            elif random() < self.four_cost_chance:
                chosen_array.append(available_four_cost_units[randint(0, len(available_four_cost_units) - 1)])
            elif random() < self.three_cost_chance:
                chosen_array.append(available_three_cost_units[randint(0, len(available_three_cost_units) - 1)])
            elif random() < self.two_cost_chance:
                chosen_array.append(available_two_cost_units[randint(0, len(available_two_cost_units) - 1)])
            else:
                chosen_array.append(available_one_cost_units[randint(0, len(available_one_cost_units) - 1)])

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
        p1.money >= 4
        p1.exp += 4
        p1.money -= 4


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
                self.percentage_adjust(.09, .15, .30, .30, .16)

    def buy_unit(self, user_input):
        try:
            unit = user_input[4].upper() + user_input[5]
            for i in range(len(Shop.shop_units)):
                if Shop.shop_units[i].upper() == unit:
                    print(f'\nYou have purchased {Shop.shop_units[i]}\n')
                    p1.hand.append(unit)

                    if unit in available_one_cost_units:
                        p1.money -= 1
                    elif unit in available_two_cost_units:
                        p1.money -= 2
                    elif unit in available_two_cost_units:
                        p1.money -= 3
                    elif unit in available_two_cost_units:
                        p1.money -= 4
                    else:
                        p1.money -= 5
                    Shop.shop_units[i] = ' '
                    break
            else:
                print(f"{user_input.removeprefix('buy')} is not a valid unit!")
        except IndexError:
            print("Invalid unit!")

    def sell_unit(self, user_input):
        refund = 0
        try:
            unit = user_input[5].upper() + user_input[6] + user_input[7] + user_input[8]
            for i in range(len(p1.hand)):
                if p1.hand[i].upper() == unit:
                    print(f'\nYou have sold {p1.hand[i]}\n')
                    p1.hand.remove(unit)
                    if user_input[5].upper() + user_input[6].upper() in available_one_cost_units:
                        refund = 1
                        if unit.count('*') == 1:
                            p1.money += (3 * refund)
                        if unit.count('*') == 2:
                            p1.money += (9 * refund)

                    elif user_input[5].upper() + user_input[6].upper() in available_two_cost_units:
                        refund = 2
                        if unit.count('*') == 1:
                            p1.money += (3 * refund)
                        if unit.count('*') == 2:
                            p1.money += (9 * refund)

                    elif user_input[5].upper() + user_input[6].upper() in available_three_cost_units:
                        refund = 3
                        if unit.count('*') == 1:
                            p1.money += (3 * refund)
                        if unit.count('*') == 2:
                            p1.money += (9 * refund)

                    elif user_input[5].upper() + user_input[6].upper() in available_four_cost_units:
                        refund = 4
                        if unit.count('*') == 1:
                            p1.money += (3 * refund)
                        if unit.count('*') == 2:
                            p1.money += (9 * refund)

                    else:
                        refund = 5
                        if unit.count('*') == 1:
                            p1.money += (3 * refund)
                        if unit.count('*') == 2:
                            p1.money += (9 * refund)
                    Shop.shop_units[i] = ' '
                    break
            else:
                print(f"{user_input.removeprefix('sell')} is not a valid unit!")
        except IndexError:
            print("Invalid unit!")

    def combine_units(self):
        for unit_copies in p1.hand:
            if p1.hand.count(unit_copies) > 2:
                print(f'\033[31;1;4mYou have combined three copies of {unit_copies}!\033[0m')
                for unit_combination in p1.hand:
                    if unit_combination == unit_copies:
                        p1.hand.remove(unit_combination)
                p1.hand.remove(unit_copies)
                p1.hand.append(unit_combination + '*')

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

    def endturnlogic():
        p1.turncounter += 1
        p1_shop.randomize_shop()
        p1.money += 4
        p1_shop.income()
        print(f"\033[35;1;4mIt is Turn: {p1.turncounter + 1}\033[0m\n")

    while True:
        p1_shop.turn_start_shop()
        print(f"\n\nYou are level {p1.level}, {p1.exp}/{p1.lvl_up_xp_required}")
        print(f'You have \033[32;1;4m${p1.money}\033[0m')
        print(f'Your hand: \n{p1.hand}')
        p1.level_up()
        adjust_required_exp()
        p1_shop.adjust_shop_chance()
        user_input = input('> ')

        if user_input.lower() == 'level':
            if p1.money >= 4:
                p1_shop.buy_exp()
            else:
                print("\033[31;1;4mYou don't have enough money to level!\033[0m")
        elif user_input.lower() == 'reroll':
            if p1.money >= 2:
                p1_shop.randomize_shop()
            else:
                print("\033[31;1;4mYou don't have enough money to reroll!\033[0m")

        elif user_input.lower().startswith('buy'):
            if len(p1.hand) < 10:
                p1_shop.buy_unit(user_input)
            else:
                print(f'\033[31;1;4mYou have a full hand!\033[0m')

        elif user_input.lower().startswith('sell'):
            p1_shop.sell_unit(user_input)

        elif user_input == 'end':
            endturnlogic()

        else:
            print("\033[31;1;4mInvalid Command!\033[0m")

        # Double method, very filthy, must clean
        p1_shop.combine_units()
        p1_shop.combine_units()


if __name__ == '__main__':
    print(f"\033[35;1;4mIt is Turn: {p1.turncounter + 1}\033[0m\n")
    if p1.turncounter <= 50:
        gameplay_loop()
    else:
        print(f"\033[35;1;4mIt is Turn: {p1.turncounter + 1}\033[0m\n")
