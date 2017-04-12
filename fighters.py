class Fighter:
    def __init__(self, hp, stamina, attack):
        self.hp = hp
        self.stamina = stamina
        self.attack = attack

class Rogue(Fighter):
    def __init__(self, hp, stamina, attack, special):
        super().__init__(hp, stamina, attack)
        self.special = special


class Shaman(Fighter):
    def __init__(self, hp, stamina, attack, special):
        super().__init__(hp, stamina, attack)
        self.special = special


class Hunter(Fighter):
    def __init__(self, hp, stamina, attack, special):
        super().__init__(hp, stamina, attack)
        self.special = special


class Priest(Fighter):
    def __init__(self, hp, stamina, attack, special):
        super().__init__(hp, stamina, attack)
        self.special = special


class Warrior(Fighter):
    def __init__(self, hp, stamina, attack, special):
        super().__init__(hp, stamina, attack)
        self.special = special
