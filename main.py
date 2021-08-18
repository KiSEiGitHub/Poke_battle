from Dictionary.Dictionary import chose_pokemon_fight
from fonction.fonction import get_name, get_pokemon
from pokemon.player_pokemon.Simiabraz import *
from pokemon.player_pokemon.Torterra import *
from pokemon.player_pokemon.Pingoleon import *

if __name__ == '__main__':
   # fonction pour set les noms
   player_name, rival_name = get_name()

   # fonction pour set les pokémons
   player_pokemon, rival_pokemon = get_pokemon()

   # battle
   if player_pokemon == 'Simiabraz':
      battle = chose_pokemon_fight.get(rival_pokemon)
      battle(rival_name, rival_pokemon, player_pokemon,
             Simiabraz_attack_name.Boutefeu, Simiabraz_attack_name.LanceFlamme,
             Simiabraz_attack_name.Deflagration, Simiabraz_attack_name.Surchauffe,
             Simiabraz_attack_damage.Boutefeu, Simiabraz_attack_damage.LanceFlamme,
             Simiabraz_attack_damage.Deflagration, Simiabraz_attack_damage.Surchauffe,
             Simiabraz_stat.lvl, Simiabraz_stat.attaque, Simiabraz_stat.defense,
             Simiabraz_stat.pv, player_name)

   elif player_pokemon == 'Torterra':
      battle = chose_pokemon_fight.get(rival_pokemon)
      battle(rival_name, rival_pokemon, player_pokemon,
             Torterra_attack_name.Tempeteverte, Torterra_attack_name.LanceSoleil,
             Torterra_attack_name.EcoSphere, Torterra_attack_name.GigaSangsue,
             Torterra_attack_damage.Tempeteverte, Torterra_attack_damage.LanceSoleil,
             Torterra_attack_damage.EcoSphere, Torterra_attack_damage.GigaSangsue,
             Torterra_stat.lvl, Torterra_stat.attaque, Torterra_stat.defense,
             Torterra_stat.pv, player_name)

   elif player_pokemon == 'Pingoléon':
      battle = chose_pokemon_fight.get(rival_pokemon)
      battle(rival_name, rival_pokemon, player_pokemon,
             Pingoleon_attack_name.Hydrocanon, Pingoleon_attack_name.Ebullition,
             Pingoleon_attack_name.Surf, Pingoleon_attack_name.Cascade,
             Pingoleon_attack_damage.Hydrocanon, Pingoleon_attack_damage.Ebullition,
             Pingoleon_attack_damage.Surf, Pingoleon_attack_damage.Cascade,
             Pingoleon_stat.lvl, Pingoleon_stat.attaque, Pingoleon_stat.defense,
             Pingoleon_stat.pv, player_name)