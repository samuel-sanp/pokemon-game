from pokemon import *


class Person:
    def __init__(self, name=None, pokemons=[]):
        self.name = name or "Anônimo"
        self.pokemons = pokemons

    def __str__(self):
        return self.name

    def show_pokemons(self):
        for pokemon in self.pokemons:
            print(pokemon)


class Player(Person):
    person_type = "player"


class Enemy(Person):
    person_type = "enemy"


picachu = EletricPokemon(poke_specie="rato", poke_level=1, poke_name="Picachu")
charmander = FirePokemon(poke_specie="lagarto", poke_level=6, poke_name="Charmander")

player = Player(name="Samara", pokemons=[picachu, charmander])

player.show_pokemons()
