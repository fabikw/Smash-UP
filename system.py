'''
Created on Jun 22, 2015

@author: fabian
'''

from data import BASES, FACTIONS, Expansion

class Player(object):
    def __init__(self, name, faction1, faction2):
        self.name = name
        self.faction1 = faction1
        self.faction2 = faction2
        self.sets = {FACTIONS[faction1][2], FACTIONS[faction2][2]}
        self.factions = ' '.join([FACTIONS[faction1][0], FACTIONS[faction2][1]])
        self.winner = False
        self.finalScore = 0
        self.finalModifiedScore = 0

    def __str__(self):
        return self.name

    def printFinal(self):
        s = "{} ({})".format(self.factions, self.name)
        if self.winner:
            return "[b]{}[/b]".format(s)
        else: return s

class Base(object):
    def __init__(self, name):
        self.scored = False
        self.name = name
        self.players_points_comments = []
        self.order = 0
        self.destroyed = False
        self.destroyed_with = None
        self.terraformed = False
        self.terraformed_into = None

    def scoreBase(self, players, points, comments, order):
        self.scored = True
        self.players_points_comments = list(zip(players, points, comments))
        self.order = order

    def destroy(self, dest):
        self.destroyed = True
        self.destroyed_with = dest

    def terraform(self, other):
        self.terraformed = True
        self.terraformed_into = other

    def __str__(self):
        return self.name

    def printFinal(self):
        if self.destroyed:
            return '  - {} (destroyed with [b]{}[/b])'.format(self.name, self.destroyed_with)
        elif self.terraformed:
            return '  - {} (terraformed into {})'.format(self.name, self.terraformed_into)
        elif not self.scored:
            return '  - {}'.format(self.name)
        else:
            st = '  - [b]{}[/b] ({:d}): '.format(self.name, self.order)
            def format_player(x):
                s = ' '.join([x[0], str(x[1])])
                if x[2]:
                    s = s + " (" + x[2] + ")"
                return s
            st = st + ', '.join(map(format_player, self.players_points_comments))
            return st

class Game(object):
    '''
    classdocs
    '''
    def __init__(self, number, madness = False):
        self.number = number
        self.players = []
        self.sets = set()
        self.available_bases = []
        self.played_bases = []
        self.madness = madness
        self.scoredBases = 0
        self.finished = False
        self.key_cards = []
        self.specific_cards = []

    def addPlayer(self, player):
        self.players.append(player)
        self.sets.update(player.sets)

    def destroyBase(self, base, dest):
        base.destroy(dest)
        self.available_bases.append(base.name)
        self.available_bases.sort()

    def terraformBase(self, origBase, newBase):
        origBase.terraform(newBase)
        self.playBase(newBase)
        self.available_bases.append(origBase.name)
        self.available_bases.sort()

    def generateBasesList(self):
        for b, v in BASES.items():
            if v[3] in self.sets: self.available_bases.append(b)
        self.available_bases.sort()
        if Expansion.OCS in self.sets: self.madness = True

    def scoreBase(self, base, players, points, comments):
        self.scoredBases += 1
        base.scoreBase(players, points, comments, self.scoredBases)
        self.available_bases.append(base.name)
        self.available_bases.sort()

    def playBase(self, base):
        self.available_bases.remove(base)
        self.played_bases.append(Base(base))

    def unscoredBases(self):
        return [b for b in self.played_bases if not b.scored]

    def printFinal(self):
        s = '[[u]Game {:d}[/u]]: {}\n'.format(self.number, " vs. ".join(map(Player.printFinal, self.players)))
        s = s + "Final Score: {}\n".format(' / '.join(map(lambda x:str(x.finalScore), self.players)))
        if self.madness:
            s = s + "Modified Final Score: {}\n\n".format(' / '.join(map(lambda x:str(x.finalModifiedScore), self.players)))
        else:
            s = s + "Modified Final Score: No madness cards used\n\n"

        s = s + "[u]Bases Used[/u]\n"
        s = s + '\n'.join(map(Base.printFinal, self.played_bases))
        s = s + '\n\n[u]Key Cards[/u]\n'
        s = s + '\n'.join(map(lambda x: '  - ' + x, self.key_cards))
        s = s + '\n\n[u]Specific Card Commentary[/u]\n'
        s = s + '\n'.join(map(lambda x: '  - ' + x, self.specific_cards))
        return s

class GameStates(object):

    def __init__(self):
        self.pastStates = []
        self.futureStates = []
        self.currentState = None

    def newState(self, game):
        self.futureStates = []
        if self.currentState:
            self.pastStates.append(self.currentState)
        self.currentState = game

    def undo(self):
        self.futureStates.append(self.currentState)
        self.currentState = self.pastStates.pop()
        return self.currentState

    def redo(self):
            self.pastStates.append(self.currentState)
            self.currentState = self.futureStates.pop()
            return self.currentState


def test():
    s = Game(4)

    s.addPlayer(Player("Fabian", "Tricksters", "Kitty Cats"))
    s.addPlayer(Player("Jenny", "Tornadoes", "Super Spies"))
    s.players[0].winner = True
    s.players[0].finalScore = 16
    s.players[1].finalScore = 13

    s.generateBasesList()
    s.playBase("Tortuga")
    s.playBase("Ice Castle")
    s.playBase("Oracle at Delphi")

    s.scoreBase(s.played_bases[1], ["Jenny", "Fabian"], [5, 3], ['', 'comment'])
    print(s.printFinal())

if __name__ == "__main__":
    test()
