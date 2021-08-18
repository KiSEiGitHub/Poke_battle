from dataclasses import dataclass
@dataclass
class Florizar_stat:
    pv: int
    attaque: int
    defense: int
    lvl: int

Florizar_stat = Florizar_stat(364, 289, 291, 100)

@dataclass
class Florizar_attack_name:
    Tempeteflorale: str
    LanceSoleil: str
    Dansefleur: str
    GigaSangsue: str

Florizar_attack_name = Florizar_attack_name(
    'Tempête florale', 'Lance soleil',
    'Danse fleur', 'Giga-sangsue'
)

Florizar_attack_list = [
    'Tempête florale', 'Lance soleil', 'Danse fleur', 'Giga-sangsue'
]

@dataclass
class Florizar_attack_damage:
    Tempeteflorale: int
    LanceSoleil: int
    Dansefleur: int
    GigaSangsue: int

Florizar_attack_damage = Florizar_attack_damage(90, 120, 120, 75)