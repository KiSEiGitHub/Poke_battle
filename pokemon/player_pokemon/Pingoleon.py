from dataclasses import dataclass
@dataclass
class Pingoleon_stat:
    pv: int
    attaque: int
    defense: int
    lvl: int

Pingoleon_stat = Pingoleon_stat(372, 298, 302, 100)

@dataclass
class Pingoleon_attack_name:
    Hydrocanon: str
    Ebullition: str
    Surf: str
    Cascade: str

Pingoleon_attack_name = Pingoleon_attack_name(
    'Hydrocanon', 'Ébullition',
    'Surf', 'Cascade'
)

@dataclass
class Pingoleon_attack_damage:
    Hydrocanon: int
    Ebullition: int
    Surf: int
    Cascade: int

Pingoleon_attack_damage = Pingoleon_attack_damage(110, 80, 90, 80)