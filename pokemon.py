import random


class Pokemon:
    POKE_LIFE = 10
    BASIC_ATACK = 3

    def __init__(self, poke_specie, poke_level=None, poke_name=None):
        self.poke_specie = poke_specie
        self.poke_level = poke_level or random.randint(1, 100)
        self.poke_name = poke_name or poke_specie
        self.poke_life = self.poke_level * self.POKE_LIFE
        self.poke_atack = self.poke_level * self.BASIC_ATACK
        self.poke_defense = 2 * self.poke_level

    def __str__(self):
        return "{} (level {})".format(self.poke_name, self.poke_level)

    def atack(self, target):
        defense = int(self.poke_defense * random.random())
        damage = int(self.poke_atack * random.random())
        final_damage = (damage - defense) if (damage - defense > 0) else 0

        target.poke_life -= final_damage

        print("{} usou ataque {}({}) em {}!".format(self.poke_name, self.poke_type, damage, target.poke_name))
        print("{} usou defesa ({})".format(self.poke_name, defense))
        print("{} perdeu {} de vida\n".format(target.poke_name, final_damage))

        return target.poke_life <= 0

class EletricPokemon(Pokemon):
    poke_type = "Eletricidade"
    ELETRIC_ATACK = 5

    def __init__(self, poke_specie, poke_level=None, poke_name=None):
        super().__init__(poke_specie=poke_specie, poke_level=poke_level, poke_name=poke_name)
        self.poke_atack = self.poke_level * self.ELETRIC_ATACK

    def atack(self, target):
        return super().atack(target)


class FirePokemon(Pokemon):
    poke_type = "Fogo"
    FIRE_ATACK = 5

    def __init__(self, poke_specie, poke_level=None, poke_name=None):
        super().__init__(poke_specie=poke_specie, poke_level=poke_level, poke_name=poke_name)
        self.poke_atack = self.poke_level * self.FIRE_ATACK

    def atack(self, target):
        return super().atack(target)