from pokemon import *
import random


def get_pokemon_list():
    POKEMON_LIST = [
        EletricPokemon(poke_specie="rato", poke_name="Pikachu"),
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

    def __init__(self, name=None, pokemons=[], name_list=PERSON_NAMES, money=100):
        self.name = name or random.choice(name_list)
        self.pokemons = pokemons
        self.money = money

    def __str__(self):
        return self.name

    def show_pokemons(self):
        if self.pokemons:
            print("Pokemons de {}:".format(self.name))
            for i, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(i, pokemon))
        else:
            print("{} não possui pokemons".format(self.name))
        print()

    def set_pokemons(self, pokemons):
        for pokemon in pokemons:
            self.pokemons.append(pokemon)

    def capture(self, target):
        capture = random.choice([True, False])

        if capture:
            self.pokemons.append(target)
            print("{} capturou {}".format(self.name, target))
        else:
            print("{} escapou!".format(target))

    def choose_pokemon(self):
        if not self.pokemons:
            print("Não há pokemons para ser escolhidos")
            return False

        while True:
            try:
                selected_pokemon = random.choice(self.pokemons)
                print("{} escolheu {}\n".format(self.name, selected_pokemon.poke_name))
                return selected_pokemon
            except Exception as e:
                print(e.args)
                print("Escolha inválida")

    def battle(self, target):
        print("Você iniciou uma batalha com {}\n".format(target.name))
        target.show_pokemons()
        enemy_pokemon = target.choose_pokemon()
        player_pokemon = self.choose_pokemon()

        if not player_pokemon or not enemy_pokemon:
            return False

        while True:
            print("Vida de {}: {}".format(enemy_pokemon.poke_name, enemy_pokemon.poke_life))
            print("Vida de {}: {}\n".format(player_pokemon.poke_name, player_pokemon.poke_life))

            enemy_victory = enemy_pokemon.atack(player_pokemon)
            if(enemy_victory):
                print("{} ganhou a batalha".format(enemy_pokemon.poke_name))
                self.decrement_money(10)
                break

            player_victory = player_pokemon.atack(enemy_pokemon)
            if(player_victory):
                print("{} ganhou a batalha".format(enemy_pokemon.poke_name))
                self.increment_money(10)
                break


class Player(Person):
    person_type = "player"

    def __init__(self, name=None, pokemons=[], money=100):
        super().__init__(name=name, pokemons=pokemons, money=money)

    def choose_pokemon(self):
        if not self.pokemons:
            print("Não há pokemons para ser escolhidos")
            return False

        self.show_pokemons()
        while True:
            try:
                choose = int(input("Escolha seu pokemon:\n"))
                selected_pokemon = self.pokemons[choose]
                print("{} escolheu {}\n".format(self.name, selected_pokemon.poke_name))
                return selected_pokemon
            except Exception as e:
                print(e.args)
                print("Escolha inválida")

    def increment_money(self, value):
        self.money += value
        print("{} ganhou {} moedas".format(self.name, value))

    def decrement_money(self, value):
        self.money -= value
        print("{} perdeu {} moedas".format(self.name, value))

    def explore(self):
        if random.random() < 0.5:
            print("Essa exploração não deu em nada")
            return False

        pokemon = random.choice(get_pokemon_list())

        capture = input("{} apareceu! Deseja captura-lo? (s/n):\n".format(pokemon))
        if capture != 's':
            return False

        if random.random() < 0.5:
            print("{} fugiu!".format(pokemon.poke_name))
            return False

        self.capture(pokemon)


class Enemy(Person):
    person_type = "enemy"
    ENEMY_NAMES = [
        'Vilão 1',
        'Vilão 2',
        'Vilão 3',
    ]

    def __init__(self, name=None, pokemons=[]):
        super().__init__(name=name, pokemons=pokemons or get_pokemon_list(), name_list=self.ENEMY_NAMES)
