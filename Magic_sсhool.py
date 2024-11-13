from abc import ABC, abstractmethod

# Абстрактний клас для магічних сутностей
class MagicalEntity(ABC):
    @abstractmethod
    def performSpell(self, spell):
        pass

# Клас для заклинань
class Spell:
    def __init__(self, name, spell_type, power_boost):
        self.name = name
        self.spell_type = spell_type  # тип заклинання (атакуюче, захисне, трансформаційне)
        self.power_boost = power_boost

# Клас для артефактів
class Artifact:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

# Клас для подій
class MagicalEvent:
    def __init__(self, event_name, description):
        self.event_name = event_name
        self.description = description

    def organizeEvent(self):
        print(f"Організація події '{self.event_name}': {self.description}")