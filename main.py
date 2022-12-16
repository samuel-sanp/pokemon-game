from person import *
from pokemon import *


def set_initial_pokemon(player, pokemon):
    player.set_pokemons([pokemon])
    print("Parabéns, você escolheu seu primeiro pokemon: {}\n".format(pokemon.poke_name))


def choose_initial_pokemon(player):
    pikachu = EletricPokemon(poke_specie="rato", poke_level=1, poke_name="Pikachu")
    charmander = FirePokemon(poke_specie="lagarto", poke_level=1, poke_name="Charmander")

    print()
    print('Olá {}, você poderá escolher um pokemon!'.format(player.name))

    while True:
        print('Você possui 2 escolhas:')
        print('1 - {}'.format(pikachu.poke_name))
        print('2 - {}'.format(charmander.poke_name))

        choose = input()
        if choose == '1':
            set_initial_pokemon(player, pikachu)
            break
        elif choose == '2':
            set_initial_pokemon(player, charmander)
            break


if __name__ == '__main__':
    print("Bem vindo ao mundo Pokemon!")
    # player_name = input("Qual seu nome?\n")
    # player = Player(name=player_name)
    player = Player(name="Samuel")
    choose_initial_pokemon(player)

    charmander = FirePokemon(poke_specie="lagarto", poke_level=1)
    enemy = Enemy(pokemons=[charmander])

    player.battle(enemy)