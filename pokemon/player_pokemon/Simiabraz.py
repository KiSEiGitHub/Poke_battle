from dataclasses import dataclass
@dataclass
class Simiabraz_stat:
    pv: int
    attaque: int
    defense: int
    lvl: int

Simiabraz_stat = Simiabraz_stat(356, 337, 265, 100)

@dataclass
class Simiabraz_attack_name:
    Boutefeu: str
    LanceFlamme: str
    Deflagration: str
    Surchauffe: str

Simiabraz_attack_name = Simiabraz_attack_name(
    'Boutefeu', 'Lance flamme',
    'Déflagration', 'Surchauffe'
)

@dataclass
class Simiabraz_attack_damage:
    Boutefeu: int
    LanceFlamme: int
    Deflagration: int
    Surchauffe: int

Simiabraz_attack_damage = Simiabraz_attack_damage(120, 90, 110, 130)