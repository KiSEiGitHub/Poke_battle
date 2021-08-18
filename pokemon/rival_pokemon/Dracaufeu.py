from dataclasses import dataclass
@dataclass
class Dracaufeu_stat:
    pv: int
    attaque: int
    defense: int
    lvl: int

Dracaufeu_stat = Dracaufeu_stat(360, 293, 280, 100)

@dataclass
class Dracaufeu_attack_name:
    Boutefeu: str
    Canicule: str
    LanceFlamme: str
    FeuDenfer: str

Dracaufeu_attack_name = Dracaufeu_attack_name(
    'Boutefeu', 'Canicule',
    'Lance flamme', "Feu d'enfer"
)

Dracaufeu_attack_list = [
    'Boutefeu', 'Canicule', 'Lance flamme', "Feu d'enfer"
]

@dataclass
class Dracaufeu_attack_damage:
    Boutefeu: int
    Canicule: int
    LanceFlamme: int
    FeuDenfer: int

Dracaufeu_attack_damage = Dracaufeu_attack_damage(120, 95, 90, 100)