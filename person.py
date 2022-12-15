from pokemon import *
import random


def get_pokemon_list():
    POKEMON_LIST = [
        EletricPokemon(poke_specie="rato", poke_name="Picachu"),
        EletricPokemon(poke_specie="rato", poke_name="Raiuchu"),
        FirePokemon(poke_specie="lagarto", poke_name="Charmander"),
        FirePokemon(poke_specie="desconhecido", poke_name="Desconhecido"),
        EletricPokemon(poke_specie="desconhecido", poke_name="Desconhecido"),
    ]
    pokemons = []

    for i in range(random.randint(1, 6)):
        pokemons.append(random.choice(POKEMON_LIST))
    return pokemons


class Person:
    PERSON_NAMES = [
        'Pessoa 1',
        'Pessoa 2',
        'Pessoa 3',
    ]

    def __init__(self, name=None, pokemons=[], name_list=PERSON_NAMES):
        self.name = name or random.choice(name_list)
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
    ENEMY_NAMES = [
        'Vilão 1',
        'Vilão 2',
        'Vilão 3',
    ]

    def __init__(self, name=None, pokemons=[]):
        super().__init__(name=name, pokemons=pokemons or get_pokemon_list(), name_list=self.ENEMY_NAMES)


picachu = EletricPokemon(poke_specie="rato", poke_name="Picachu")
charmander = FirePokemon(poke_specie="lagarto", poke_name="Charmander")

# player = Player(name="Samara")

# player.show_pokemons()
# player.capture(target=charmander)
# player.show_pokemons()

enemy = Enemy()
print(enemy)
enemy.show_pokemons()
