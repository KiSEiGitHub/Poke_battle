from battle.Florizar_battle import flo_battle
from battle.Tortank_battle import tortank_battle
from battle.dracaufeu_battle import draco_battle
from fonction.fonction import player_attack

chose_pokemon_fight = {
    'Dracaufeu': draco_battle,
    'Florizar': flo_battle,
    'Tortank': tortank_battle
}

attack_player_dico = {
    1: player_attack,
    2: player_attack,
    3: player_attack,
    4: player_attack
}