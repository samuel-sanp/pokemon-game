class Pokemon:
    def __init__(self, poke_specie, poke_level=1, poke_name=None):
        self.poke_specie = poke_specie
        self.poke_level = poke_level
        self.poke_name = poke_name or poke_specie

    def __str__(self):
        return "{} (level {})".format(self.poke_name, self.poke_level)

    def basic_atack(self, target):
        print("{} usou ataque básico em {}!".format(self.poke_name, target.poke_name))


class EletricPokemon(Pokemon):
    poke_type = "Eletricidade"

    def eletric_atack(self, target):
        print("{} usou ataque elétrico em {}!".format(self.poke_name, target.poke_name))


class FirePokemon(Pokemon):
    poke_type = "Fogo"

    def fire_atack(self, target):
        print("{} usou ataque de fogo em {}!".format(self.poke_name, target.poke_name))