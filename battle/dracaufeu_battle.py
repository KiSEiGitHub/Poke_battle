from pokemon.rival_pokemon.Dracaufeu import *
from fonction.fonction import rival_attack

def draco_battle(
        rival_name, rival_pokemon, player_pokemon,
        a, b, c, d, a1, b1, c1, d1,
        lvl, atq, deff, hp_pokemon_player, player_name
):
    from Dictionary.Dictionary import attack_player_dico
    tour = 1
    print(f"{rival_name} veut se battre avec son {rival_pokemon}\n")
    while True:
        if tour > 1:
            print(f"Tours: {tour}\n")
        else:
            print(f"Tour: {tour}\n")

        print(f"Que doit faire {player_pokemon}")
        print(f"{a}: 1 | {b}: 2 | {c}: 3 | {d}: 4")
        while True:
            try:
                player_attack_choice = int(input(">> "))
                break
            except ValueError:
                print("Vous devez rentrer un nombre")

        # attaque player
        var = attack_player_dico.get(player_attack_choice)
        dmg_dealt = var(player_attack_choice, a, b, c, d, player_pokemon,
                        a1, b1, c1, d1, rival_pokemon, lvl, atq)
        Dracaufeu_stat.pv -= dmg_dealt

        if Dracaufeu_stat.pv < 0:
            print(f"{player_name} et son {player_pokemon} ont gagné")
            break

        # attaque rival
        rival_dmg = rival_attack('Dracaufeu', player_pokemon, Dracaufeu_stat.lvl, Dracaufeu_stat.attaque,
                     Dracaufeu_attack_damage.Boutefeu, Dracaufeu_attack_damage.Canicule,
                     Dracaufeu_attack_damage.LanceFlamme, Dracaufeu_attack_damage.FeuDenfer, deff)

        hp_pokemon_player -= rival_dmg

        if hp_pokemon_player < 0:
            print(f"{rival_name} et son Tortank ont gagné")
            break

        print(f"Dracaufeu: {round(Dracaufeu_stat.pv)} hp")
        print(f"{player_pokemon}: {round(hp_pokemon_player)} hp")
        tour += 1

        print("―" * 70, '\n')