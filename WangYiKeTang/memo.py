import random
class GameCharacter():
    vitality = 0
    attack = 0
    defense = 0
    def displayState(self):
        print 'Current Values:'
        print 'Life:%d' % self.vitality
        print 'Attack:%d' % self.attack
        print 'Defence:%d' % self.defense
    def initState(self,vitality,attack,defense):
        self.vitality = vitality
        self.attack = attack
        self.defense = defense
    def saveState(self):
        return Memento(self.vitality, self.attack, self.defense)
    def recoverState(self, memento):
        self.vitality = memento.vitality
        self.attack = memento.attack
        self.defense = memento.defense
class FightCharactor(GameCharacter):
    def fight(self):
        self.vitality -= random.randint(1,10)
class Memento:
    vitality = 0
    attack = 0
    defense = 0
    def __init__(self, vitality, attack, defense):
        self.vitality = vitality
        self.attack = attack
        self.defense = defense
if __name__=="__main__":
    game_chrctr = FightCharactor()
    game_chrctr.initState(100,79,60)
    game_chrctr.displayState()
    memento = game_chrctr.saveState()
    game_chrctr.fight()
    game_chrctr.displayState()
    game_chrctr.recoverState(memento)
    game_chrctr.displayState()
