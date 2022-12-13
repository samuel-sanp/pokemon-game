from pokemon import *
import random


class Person:
    def __init__(self, name=None, pokemons=[]):
        self.name = name or "Anônimo"
        self.pokemons = pokemons

    def __str__(self):
        return self.name

    def show_pokemons(self):
        if self.pokemons:
            print("Pokemons de {}:".format(self.name))
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print("{} não possui pokemons".format(self.name))

    def capture(self, target):
        capture = random.choice([True, False])

        if capture:
            self.pokemons.append(target)
            print("{} capturou {}".format(self.name, target))
        else:
            print("{} escapou!".format(target))


class Player(Person):
    person_type = "player"


class Enemy(Person):
    person_type = "enemy"


picachu = EletricPokemon(poke_specie="rato", poke_level=1, poke_name="Picachu")
charmander = FirePokemon(poke_specie="lagarto", poke_level=6, poke_name="Charmander")

player = Player(name="Samara")

player.show_pokemons()
player.capture(target=charmander)
player.show_pokemons()
