class Fighter:
    def __init__(self, hp, stamina, attack, special):
        self.hp = hp
        self.stamina = stamina
        self.attack = attack
        self.special = special

class Rogue(Fighter):
    def __init__(self, hp, stamina, attack, special):
        super().__init__(hp, stamina, attack, special)

    def bonus(self):
        self.hp += 2
        self.stamina += 2
        self.attack += 1

    def get_special_attack(self):
        return 3 * self.attack

    def cost_stamina(self):
        self.stamina -= 3

    def cost_stamina_special_attack(self):
        self.stamina -= 8

    def regen_stamina(self):
        self.stamina += 2

    def regen_health(self):
        self.hp += 2


class Shaman(Fighter):
    def __init__(self, hp, stamina, attack, special):
        super().__init__(hp, stamina, attack, special)

    def bonus(self):
        self.hp += 3
        self.stamina += 3

    def get_special_attack(self):
        return 3 * self.attack

    def cost_stamina(self):
        self.stamina -= 2

    def cost_stamina_special_attack(self):
        self.stamina -= 7

    def regen_stamina(self):
        self.stamina += 2

    def regen_health(self):
        self.hp += 2


class Hunter(Fighter):
    def __init__(self, hp, stamina, attack, special):
        super().__init__(hp, stamina, attack, special)

    def bonus(self):
        self.attack += 2

    def get_special_attack(self):
        return 3 * self.attack

    def cost_stamina(self):
        self.stamina -= 3

    def cost_stamina_special_attack(self):
        self.stamina -= 8

    def regen_stamina(self):
        self.stamina += 2

    def regen_health(self):
        self.hp += 2


class Priest(Fighter):
    def __init__(self, hp, stamina, attack, special):
        super().__init__(hp, stamina, attack, special)

    def bonus(self):
        self.hp += 3
        self.stamina += 3

    def get_special_attack(self):
        return 3 * self.attack

    def cost_stamina(self):
        self.stamina -= 2

    def cost_stamina_special_attack(self):
        self.stamina -= 7

    def regen_stamina(self):
        self.stamina += 2

    def regen_health(self):
        self.hp += 2


class Warrior(Fighter):
    def __init__(self, hp, stamina, attack, special):
        super().__init__(hp, stamina, attack, special)

    def bonus(self):
        self.attack += 2

    def get_special_attack(self):
        return 3 * self.attack

    def cost_stamina(self):
        self.stamina -= 3

    def cost_stamina_special_attack(self):
        self.stamina -= 8

    def regen_stamina(self):
        self.stamina += 2

    def regen_health(self):
        self.hp += 2
