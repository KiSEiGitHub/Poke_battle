from dataclasses import dataclass
@dataclass
class Tortank_stat:
    pv: int
    attaque: int
    defense: int
    lvl: int

Tortank_stat = Tortank_stat(362, 291, 328, 100)

@dataclass
class Tortank_attack_name:
    Hydrocanon: str
    Virbraqua: str
    Ebullition: str
    Surf: str

Tortank_attack_name = Tortank_attack_name(
    'Hydrocanon', 'Virbraqua',
    'Ébullition', "Surf"
)

Tortank_attack_list = [
    'Hydrocanon', 'Vibraqua', 'Ébullition', 'Surf'
]

@dataclass
class Tortank_attack_damage:
    Hydrocanon: int
    Virbraqua: int
    Ebullition: int
    Surf: int

Tortank_attack_damage = Tortank_attack_damage(110, 60, 80, 90)