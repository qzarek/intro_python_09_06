####### Game
import random


class StandartUnit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self._max_health = 100
        self._min_health = 1
        self.health = self._max_health
        self._max_skill = 10
        self.base_skill = None
        self.skills = {"intelligence": 1,
                       "agility": 1,
                       "power": 1}


    def health_up(self):
        if self._min_health <= self.health < self._max_health and self.health + 10 <= self._max_health:
            self.health += 10
        elif self.health + 10 > self._max_health:
            self.health = self._max_health
        else:
            pass

    def skill_up(self):
        skill = self.skills[self.base_skill]
        self.skills[self.base_skill] += 1 if skill < self._max_skill else skill



class MageUnit(StandartUnit):
    def __init__(self, name, clan):
        super().__init__(name, clan)
        self.magic_type = random.choice(["air", "fire", "water"])
        self.base_skill = "intelligence"


class ArcherUnit(StandartUnit):
    def __init__(self, name, clan):
        super().__init__(name, clan)
        self.bow_type = random.choice(["bow", "crossbow"])
        self.base_skill = "agility"


class KnightUnit(StandartUnit):
    def __init__(self, name, clan):
        super().__init__(name, clan)
        self.weapon_type = random.choice(["sword", "ax", "lance"])
        self.base_skill = "power"


person_mage = MageUnit("lol", "kek")
person_mage.skill_up()
person_mage.skill_up()
person_mage.skill_up()
person_archer = ArcherUnit("lol2", "kek2")
person_archer.skill_up()
person_knight = KnightUnit("lol3", "kek3")
person_knight.skill_up()


# print(person_mage.skills["intelligence"], person_mage.base_skill)
# print(person_archer.skills["agility"], person_archer.base_skill)
# print(person_knight.skills["power"], person_knight.base_skill)
# print(person_mage.health)
