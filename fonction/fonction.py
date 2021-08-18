from pokemon.rival_pokemon.Dracaufeu import *
from pokemon.rival_pokemon.Tortank import *
from pokemon.rival_pokemon.Florizar import *

def get_name():
    print("Quel est votre nom ?")
    a = input(">> ")
    print("Quel est le nom de votre rival ?")
    b = input(">> ")
    return a, b

def get_pokemon():
    from random import choice
    print("Quel pokémon voulez-vous ?")
    a = ['Simiabraz', 'Pingoléon', 'Torterra']
    for i in a:
        print(i)
    u = ""
    while u not in a:
        u = input(">> ")

    b = ['Florizar', 'Dracaufeu', 'Tortank']
    p = choice(b)

    return u, p

def calcul_damage(lvl, atq, pui, deff, stab):
    a = (lvl * 0.4 + 2) * atq * 1 * pui
    b = deff * 1 * 50
    c = a / b
    d = c + 2
    return d * stab * 0.5 * 1

def player_attack(x, a, b, c, d, player_pokemon,
                  a1, b1, c1, d1, rival_pokemon, lvl, atq):

    if player_pokemon == 'Simiabraz':
        if rival_pokemon == 'Tortank':
            if x == 1:
                print(f"{player_pokemon} utilise {a}")
                dmg = calcul_damage(lvl, atq, a1, Tortank_stat.defense, 1)
                print(f"Ce n'est pas très efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 2:
                print(f"{player_pokemon} utilise {b}")
                dmg = calcul_damage(lvl, atq, b1, Tortank_stat.defense, 1)
                print(f"Ce n'est pas très efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 3:
                print(f"{player_pokemon} utilise {c}")
                dmg = calcul_damage(lvl, atq, c1, Tortank_stat.defense, 1)
                print(f"Ce n'est pas très efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 4:
                print(f"{player_pokemon} utilise {d}")
                dmg = calcul_damage(lvl, atq, d1, Tortank_stat.defense, 1)
                print(f"Ce n'est pas très efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")

        elif rival_pokemon == 'Florizar':
            if x == 1:
                print(f"{player_pokemon} utilise {a}")
                dmg = calcul_damage(lvl, atq, a1, Florizar_stat.defense, 2)
                print(f"C'est super efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 2:
                print(f"{player_pokemon} utilise {b}")
                dmg = calcul_damage(lvl, atq, b1, Florizar_stat.defense, 2)
                print(f"C'est super efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 3:
                print(f"{player_pokemon} utilise {c}")
                dmg = calcul_damage(lvl, atq, c1, Florizar_stat.defense, 2)
                print(f"C'est super efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 4:
                print(f"{player_pokemon} utilise {d}")
                dmg = calcul_damage(lvl, atq, d1, Florizar_stat.defense, 2)
                print(f"C'est super efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")

        elif rival_pokemon == 'Dracaufeu':
            if x == 1:
                print(f"{player_pokemon} utilise {a}")
                dmg = calcul_damage(lvl, atq, a1, Dracaufeu_stat.defense, 1.5)
                print(f"C'est peu efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 2:
                print(f"{player_pokemon} utilise {b}")
                dmg = calcul_damage(lvl, atq, b1, Dracaufeu_stat.defense, 1.5)
                print(f"C'est peu efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 3:
                print(f"{player_pokemon} utilise {c}")
                dmg = calcul_damage(lvl, atq, c1, Dracaufeu_stat.defense, 1.5)
                print(f"C'est peu efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 4:
                print(f"{player_pokemon} utilise {d}")
                dmg = calcul_damage(lvl, atq, d1, Dracaufeu_stat.defense, 1.5)
                print(f"C'est peu efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")

    elif player_pokemon == 'Pingoléon':
        if rival_pokemon == 'Tortank':
            if x == 1:
                print(f"{player_pokemon} utilise {a}")
                dmg = calcul_damage(lvl, atq, a1, Tortank_stat.defense, 1)
                print(f"Ce n'est pas très efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            if x == 2:
                print(f"{player_pokemon} utilise {b}")
                dmg = calcul_damage(lvl, atq, b1, Tortank_stat.defense, 1)
                print(f"Ce n'est pas très efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            if x == 3:
                print(f"{player_pokemon} utilise {c}")
                dmg = calcul_damage(lvl, atq, c1, Tortank_stat.defense, 1)
                print(f"Ce n'est pas très efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            if x == 4:
                print(f"{player_pokemon} utilise {d}")
                dmg = calcul_damage(lvl, atq, d1, Tortank_stat.defense, 1)
                print(f"Ce n'est pas très efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
        elif rival_pokemon == 'Dracaufeu':
            if x == 1:
                print(f"{player_pokemon} utilise {a}")
                dmg = calcul_damage(lvl, atq, a1, Dracaufeu_stat.defense, 2)
                print(f"C'est super efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 2:
                print(f"{player_pokemon} utilise {b}")
                dmg = calcul_damage(lvl, atq, b1, Dracaufeu_stat.defense, 2)
                print(f"C'est super efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 3:
                print(f"{player_pokemon} utilise {c}")
                dmg = calcul_damage(lvl, atq, c1, Dracaufeu_stat.defense, 2)
                print(f"C'est super efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 4:
                print(f"{player_pokemon} utilise {d}")
                dmg = calcul_damage(lvl, atq, d1, Dracaufeu_stat.defense, 2)
                print(f"C'est super efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
        elif rival_pokemon == 'Florizar':
            if x == 1:
                print(f"{player_pokemon} utilise {a}")
                dmg = calcul_damage(lvl, atq, a1, Florizar_stat.defense, 1)
                print(f"Ce n'est pas très efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 2:
                print(f"{player_pokemon} utilise {b}")
                dmg = calcul_damage(lvl, atq, b1, Florizar_stat.defense, 1)
                print(f"Ce n'est pas très efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 3:
                print(f"{player_pokemon} utilise {c}")
                dmg = calcul_damage(lvl, atq, c1, Florizar_stat.defense, 1)
                print(f"Ce n'est pas très efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 4:
                print(f"{player_pokemon} utilise {d}")
                dmg = calcul_damage(lvl, atq, d1, Florizar_stat.defense, 1)
                print(f"Ce n'est pas très efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")

    elif player_pokemon == 'Torterra':
        if rival_pokemon == 'Tortank':
            if x == 1:
                print(f"{player_pokemon} utilise {a}")
                dmg = calcul_damage(lvl, atq, a1, Tortank_stat.defense, 2)
                print(f"C'est super efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 2:
                print(f"{player_pokemon} utilise {b}")
                dmg = calcul_damage(lvl, atq, b1, Tortank_stat.defense, 2)
                print(f"C'est super efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 3:
                print(f"{player_pokemon} utilise {c}")
                dmg = calcul_damage(lvl, atq, c1, Tortank_stat.defense, 2)
                print(f"C'est super efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 4:
                print(f"{player_pokemon} utilise {d}")
                dmg = calcul_damage(lvl, atq, d1, Tortank_stat.defense, 2)
                print(f"C'est super efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
        elif rival_pokemon == 'Dracaufeu':
            if x == 1:
                print(f"{player_pokemon} utilise {a}")
                dmg = calcul_damage(lvl, atq, a1, Dracaufeu_stat.defense, 1)
                print(f"Ce n'est pas très efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 2:
                print(f"{player_pokemon} utilise {b}")
                dmg = calcul_damage(lvl, atq, b1, Dracaufeu_stat.defense, 1)
                print(f"Ce n'est pas très efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 3:
                print(f"{player_pokemon} utilise {c}")
                dmg = calcul_damage(lvl, atq, c1, Dracaufeu_stat.defense, 1)
                print(f"Ce n'est pas très efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 4:
                print(f"{player_pokemon} utilise {d}")
                dmg = calcul_damage(lvl, atq, d1, Dracaufeu_stat.defense, 1)
                print(f"Ce n'est pas très efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")

        elif rival_pokemon == 'Florizar':
            if x == 1:
                print(f"{player_pokemon} utilise {a}")
                dmg = calcul_damage(lvl, atq, a1, Florizar_stat.defense, 1.5)
                print(f"C'est peu efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 2:
                print(f"{player_pokemon} utilise {b}")
                dmg = calcul_damage(lvl, atq, b1, Florizar_stat.defense, 1.5)
                print(f"C'est peu efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 3:
                print(f"{player_pokemon} utilise {c}")
                dmg = calcul_damage(lvl, atq, c1, Florizar_stat.defense, 1.5)
                print(f"C'est peu efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
            elif x == 4:
                print(f"{player_pokemon} utilise {d}")
                dmg = calcul_damage(lvl, atq, d1, Florizar_stat.defense, 1.5)
                print(f"C'est peu efficace, les pv de {rival_pokemon} baisse de {round(dmg)}\n")
    return dmg

def rival_attack(rival_pokemon, player_pokemon, lvl, atq,
                 w, x, y, z, deff):
    from random import choice
    if rival_pokemon == 'Dracaufeu':
        draco_attaque = choice(Dracaufeu_attack_list)
        if player_pokemon == 'Simiabraz':
            if draco_attaque == 'Boutefeu':
                print(f"Dracaufeu utilise boutefeu")
                dmg = calcul_damage(lvl, atq, w, deff, 1.5)
                print(f"C'est peu efficace, les pv de Simiabraz baisse de {round(dmg)}\n")
            elif draco_attaque == 'Canicule':
                print(f"Dracaufeu utilise canicule")
                dmg = calcul_damage(lvl, atq, x, deff, 1.5)
                print(f"C'est peu efficace, les pv de Simiabraz baisse de {round(dmg)}\n")
            elif draco_attaque == 'Lance flamme':
                print(f"Dracaufeu utilise lance flamme")
                dmg = calcul_damage(lvl, atq, y, deff, 1.5)
                print(f"C'est peu efficace, les pv de Simiabraz baisse de {round(dmg)}\n")
            elif draco_attaque == "Fen d'enfer":
                print(f"Dracaufeu utilise feu d'enfer")
                dmg = calcul_damage(lvl, atq, z, deff, 1.5)
                print(f"C'est peu efficace, les pv de Simiabraz baisse de {round(dmg)}\n")

        elif player_pokemon == 'Torterra':
            draco_attaque = choice(Dracaufeu_attack_list)
            if draco_attaque == 'Boutefeu':
                print(f"Dracaufeu utilise boutefeu")
                dmg = calcul_damage(lvl, atq, w, deff, 2)
                print(f"C'est super efficace, les pv de Torterra baisse de {round(dmg)}\n")
                print('―' * 70, '\n')
            elif draco_attaque == 'Canicule':
                print(f"Dracaufeu utilise canicule")
                dmg = calcul_damage(lvl, atq, x, deff, 2)
                print(f"C'est super efficace, les pv de Torterra baisse de {round(dmg)}\n")
                print('―' * 70, '\n')
            elif draco_attaque == 'Lance flamme':
                print(f"Dracaufeu utilise lance flamme")
                dmg = calcul_damage(lvl, atq, y, deff, 2)
                print(f"C'est super efficace, les pv de Torterra baisse de {round(dmg)}\n")
                print('―' * 70, '\n')
            elif draco_attaque == "Fen d'enfer":
                print(f"Dracaufeu utilise feu d'enfer")
                dmg = calcul_damage(lvl, atq, z, deff, 2)
                print(f"C'est super efficace, les pv de Torterra baisse de {round(dmg)}\n")
                print('―' * 70, '\n')

        elif player_pokemon == 'Pingoléon':
            draco_attaque = choice(Dracaufeu_attack_list)
            if draco_attaque == 'Boutefeu':
                print(f"Dracaufeu utilise boutefeu")
                dmg = calcul_damage(lvl, atq, w, deff, 1)
                print(f"C'est peu efficace, les pv de Pingoléon baisse de {round(dmg)}\n")
            elif draco_attaque == 'Canicule':
                print(f"Dracaufeu utilise canicule")
                dmg = calcul_damage(lvl, atq, x, deff, 1)
                print(f"C'est peu efficace, les pv de Pingoléon baisse de {round(dmg)}\n")
            elif draco_attaque == 'Lance flamme':
                print(f"Dracaufeu utilise lance flamme")
                dmg = calcul_damage(lvl, atq, y, deff, 1)
                print(f"C'est peu efficace, les pv de Pingoléon baisse de {round(dmg)}\n")

            elif draco_attaque == "Fen d'enfer":
                print(f"Dracaufeu utilise feu d'enfer")
                dmg = calcul_damage(lvl, atq, z, deff, 1)
                print(f"C'est peu efficace, les pv de Pingoléon baisse de {round(dmg)}\n")


    elif rival_pokemon == 'Tortank':
        if player_pokemon == 'Simiabraz':
            tortank_attack = choice(Tortank_attack_list)
            if tortank_attack == 'Hydrocanon':
                print(f"Tortank utilise Hydrocranon")
                dmg = calcul_damage(lvl, atq, w, deff, 2)
                print(f"C'est super efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")
            elif tortank_attack == 'Vibraqua':
                print(f"Tortank utilise Vibraqua")
                dmg = calcul_damage(lvl, atq, x, deff, 2)
                print(f"C'est super efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")
            elif tortank_attack == 'Ébullition':
                print(f"Tortank utilise Ébullition")
                dmg = calcul_damage(lvl, atq, y, deff, 2)
                print(f"C'est super efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")
            elif tortank_attack == 'Surf':
                print(f"Tortank utilise Surf")
                dmg = calcul_damage(lvl, atq, z, deff, 2)
                print(f"C'est super efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")

        elif player_pokemon == 'Pingoléon':
            tortank_attack = choice(Tortank_attack_list)
            if tortank_attack == 'Hydrocanon':
                print(f"Tortank utilise Hydrocranon")
                dmg = calcul_damage(lvl, atq, w, deff, 1.5)
                print(f"C'est super efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")
            elif tortank_attack == 'Vibraqua':
                print(f"Tortank utilise Vibraqua")
                dmg = calcul_damage(lvl, atq, x, deff, 1.5)
                print(f"C'est super efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")
            elif tortank_attack == 'Ébullition':
                print(f"Tortank utilise Ébullition")
                dmg = calcul_damage(lvl, atq, y, deff, 1.5)
                print(f"C'est super efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")
            elif tortank_attack == 'Surf':
                print(f"Tortank utilise Surf")
                dmg = calcul_damage(lvl, atq, z, deff, 1.5)
                print(f"C'est super efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")


        elif player_pokemon == 'Torterra':
            tortank_attack = choice(Tortank_attack_list)
            if tortank_attack == 'Hydrocanon':
                print(f"Tortank utilise Hydrocranon")
                dmg = calcul_damage(lvl, atq, w, deff, 1)
                print(f"C'est peu efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")

            elif tortank_attack == 'Vibraqua':
                print(f"Tortank utilise Vibraqua")
                dmg = calcul_damage(lvl, atq, x, deff, 1)
                print(f"C'est peu efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")

            elif tortank_attack == 'Ébullition':
                print(f"Tortank utilise Ébullition")
                dmg = calcul_damage(lvl, atq, y, deff, 1)
                print(f"C'est peu efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")

            elif tortank_attack == 'Surf':
                print(f"Tortank utilise Surf")
                dmg = calcul_damage(lvl, atq, z, deff, 1)
                print(f"C'est peu efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")


    elif rival_pokemon == 'Florizar':
        flo_attaque = choice(Florizar_attack_list)
        if player_pokemon == 'Simiabraz':
            if flo_attaque == 'Tempête florale':
                print(f"Florizar utilise tempête florale")
                dmg = calcul_damage(lvl, atq, w, deff, 1)
                print(f"Ce peu efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")
            elif flo_attaque == 'Lance soleil':
                print(f"Florizar utilise lance soleil")
                dmg = calcul_damage(lvl, atq, x, deff, 1)
                print(f"Ce peu efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")
            elif flo_attaque == 'Danse fleur':
                print(f"Florizar utilise danse fleur")
                dmg = calcul_damage(lvl, atq, y, deff, 1)
                print(f"Ce peu efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")
            elif flo_attaque == 'Giga-sangsue':
                print(f"Florizar utilise Giga-sangsue")
                dmg = calcul_damage(lvl, atq, z, deff, 1)
                print(f"Ce peu efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")

        elif player_pokemon == 'Torterra':
            if flo_attaque == 'Tempête florale':
                print(f"Florizar utilise tempête florale")
                dmg = calcul_damage(lvl, atq, w, deff, 1.5)
                print(f"Ce peu efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")

            elif flo_attaque == 'Lance soleil':
                print(f"Florizar utilise lance soleil")
                dmg = calcul_damage(lvl, atq, x, deff, 1.5)
                print(f"Ce peu efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")

            elif flo_attaque == 'Danse fleur':
                print(f"Florizar utilise danse fleur")
                dmg = calcul_damage(lvl, atq, y, deff, 1.5)
                print(f"Ce peu efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")

            elif flo_attaque == 'Giga-sangsue':
                print(f"Florizar utilise Giga-sangsue")
                dmg = calcul_damage(lvl, atq, z, deff, 1.5)
                print(f"Ce peu efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")

        elif player_pokemon == 'Pingoléon':
            if flo_attaque == 'Tempête florale':
                print(f"Florizar utilise tempête florale")
                dmg = calcul_damage(lvl, atq, w, deff, 2)
                print(f"Ce peu efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")

            elif flo_attaque == 'Lance soleil':
                print(f"Florizar utilise lance soleil")
                dmg = calcul_damage(lvl, atq, x, deff, 2)
                print(f"Ce peu efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")

            elif flo_attaque == 'Danse fleur':
                print(f"Florizar utilise danse fleur")
                dmg = calcul_damage(lvl, atq, y, deff, 2)
                print(f"Ce peu efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")

            elif flo_attaque == 'Giga-sangsue':
                print(f"Florizar utilise Giga-sangsue")
                dmg = calcul_damage(lvl, atq, z, deff, 2)
                print(f"Ce peu efficace, les pv de {player_pokemon} baisse de {round(dmg)}\n")


    return dmg