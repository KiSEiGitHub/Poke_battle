from dataclasses import dataclass
@dataclass
class Torterra_stat:
    pv: int
    attaque: int
    defense: int
    lvl: int

Torterra_stat = Torterra_stat(394, 348, 339, 100)

@dataclass
class Torterra_attack_name:
    Tempeteverte: str
    LanceSoleil: str
    EcoSphere: str
    GigaSangsue: str

Torterra_attack_name = Torterra_attack_name(
    'Tempête verte', 'Lance soleil',
    'Éco-Sphère', 'Giga-sangsue'
)

@dataclass
class Torterra_attack_damage:
    Tempeteverte: int
    LanceSoleil: int
    EcoSphere: int
    GigaSangsue: int

Torterra_attack_damage = Torterra_attack_damage(130, 120, 90, 75)