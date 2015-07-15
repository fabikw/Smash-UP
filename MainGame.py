'''
Created on Jun 23, 2015

@author: fabian
'''

from copy import deepcopy

from PyQt4 import QtGui, QtCore

import data
from endGame import EndGame
from scoreBase import ScoreBase
from system import Player, Game, GameStates
from ui_mainGame import Ui_mainGame


class BaseListItem(QtGui.QListWidgetItem):

    def __init__(self, base):
        QtGui.QListWidgetItem.__init__(self, base.name)
        self.base = base

def newSetText(self, text):
    self.text = text
    t = text.replace("[b]", "<b>")
    t = t.replace("[u]", "<u>")
    t = t.replace("[/b]", "</b>")
    t = t.replace("[/u]", "</u>")
    t = t.replace("\n", "<br>")
    self.setHtml(t)

def newMimeData(self):
    q = QtCore.QMimeData()
    q.setText(self.text)
    return q

class MainGame(QtGui.QDialog, Ui_mainGame):
    '''
    classdocs
    '''


    def __init__(self, gameState):
        '''
        Constructor
        '''
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowMinMaxButtonsHint | QtCore.Qt.WindowCloseButtonHint)
        self.state = gameState
        self.raise_()
        self.activateWindow()
        self.undo.setEnabled(False)
        self.redo.setEnabled(False)

        import types
        self.output.setText = types.MethodType(newSetText, self.output)
        self.output.createMimeDataFromSelection = types.MethodType(newMimeData, self.output)
        self.output.setText(self.state.currentState.printFinal())

        (self.keyCards.append(x) for x in self.state.currentState.key_cards)
        (self.specificCards.append(x) for x in self.state.currentState.specific_cards)

        self.allBases.addItems(self.state.currentState.available_bases)
        for b in self.state.currentState.played_bases:
            if not b.scored and not b.destroyed and not b.terraformed: self.playingBases.addItem(BaseListItem(b))
        self.allBases.currentItemChanged.connect(self.enableNewBase)
        self.playingBases.currentItemChanged.connect(self.enableScoreBase)
        self.newBase.clicked.connect(self.addBase)
        self.scoreBase.clicked.connect(self.scBase)
        self.finish.clicked.connect(self.end)
        self.destroy.clicked.connect(self.destroyBase)
        self.undo.clicked.connect(self.undoAction)
        self.redo.clicked.connect(self.redoAction)
        self.updateCards.clicked.connect(self.updateKeyCards)
        self.terraform.clicked.connect(self.terra)

        self.newBase.setEnabled(False)
        self.scoreBase.setEnabled(False)
        self.terraform.setEnabled(False)
        self.destroy.setEnabled(False)
        self.allBases.setCurrentRow(-1)
        self.playingBases.setCurrentRow(-1)
        self.enableNewBase()
        self.enableScoreBase()
        if self.state.pastStates: self.undo.setEnabled(True)
        if self.state.futureStates:self.redo.setEnabled(True)

    def terra(self):
        game = deepcopy(self.state.currentState)
        newBase = self.allBases.currentItem().text()
        name = self.playingBases.currentItem().base.name
        b = next(x for x in reversed(game.played_bases) if x.name == name)
        game.terraformBase(b, newBase)
        self.state.newState(game)
        self.undo.setEnabled(True)
        self.redo.setEnabled(False)
        self.updateStuff()


    def enableNewBase(self):
        self.newBase.setEnabled(not self.allBases.currentRow() == -1)
        self.terraform.setEnabled(not self.allBases.currentRow() == -1 and not self.playingBases.currentRow() == -1)

    def updateKeyCards(self):
        game = deepcopy(self.state.currentState)
        text = self.keyCards.toPlainText().strip()
        import re
        text = re.sub("\n+", "\n", text)
        text = re.sub("[*](.*?)[*]", r"[b]\1[/b]", text)
        game.key_cards = text.splitlines()
        text = self.specificCards.toPlainText().strip()
        text = re.sub("\n+", "\n", text)
        text = re.sub("[*](.*?)[*]", r"[b]\1[/b]", text)
        game.specific_cards = text.splitlines()
        self.state.newState(game)
        self.undo.setEnabled(True)
        self.redo.setEnabled(False)
        self.updateStuff()

    def enableScoreBase(self):
        self.scoreBase.setEnabled(not self.playingBases.currentRow() == -1)
        self.destroy.setEnabled(not self.playingBases.currentRow() == -1)
        self.terraform.setEnabled(not self.allBases.currentRow() == -1 and not self.playingBases.currentRow() == -1)


    def addBase(self):
        game = deepcopy(self.state.currentState)
        game.playBase(self.allBases.currentItem().text())
        self.state.newState(game)
        self.undo.setEnabled(True)
        self.redo.setEnabled(False)
        self.updateStuff()

    def destroyBase(self):
        game = deepcopy(self.state.currentState)
        name = self.playingBases.currentItem().base.name
        b = next(x for x in reversed(game.played_bases) if x.name == name)
        dest = QtGui.QInputDialog.getItem(self, "Select action", "Card:", data.destroying_actions, editable = False)
        if not dest[1]:
            return
        game.destroyBase(b, dest[0])
        self.state.newState(game)
        self.undo.setEnabled(True)
        self.redo.setEnabled(False)
        self.updateStuff()

    def scBase(self):
        scoreBase = ScoreBase(self.playingBases.currentItem().base, self.state.currentState.players, self)
        result = scoreBase.exec_()
        if result == 1:
            game = deepcopy(self.state.currentState)
            players, points, comments = scoreBase.values()
            name = self.playingBases.currentItem().base.name
            b = next(x for x in reversed(game.played_bases) if x.name == name)
            game.scoreBase(b, players, points, comments)
            self.state.newState(game)
            self.undo.setEnabled(True)
            self.redo.setEnabled(False)
            self.updateStuff()

    def end(self):
        game = deepcopy(self.state.currentState)
        endGame = EndGame(game.players, self, game.madness)
        result = endGame.exec_()
        if result == 1:
            self.state.newState(game)
            self.undo.setEnabled(True)
            self.redo.setEnabled(False)
            self.updateStuff()
            game.finished = True
            self.setFinished()

    def undoAction(self):
        self.state.undo()
        self.updateStuff()
        self.redo.setEnabled(True)
        if not self.state.pastStates: self.undo.setEnabled(False)
        self.setFinished()

    def redoAction(self):
        self.state.redo()
        self.updateStuff()
        self.undo.setEnabled(True)
        if not self.state.futureStates: self.redo.setEnabled(False)
        self.setFinished()

    def setFinished(self):
        fin = not self.state.currentState.finished
        self.allBases.setEnabled(fin)
        self.playingBases.setEnabled(fin)

    def updateStuff(self):
        game = self.state.currentState
        self.allBases.clear()
        self.allBases.addItems(game.available_bases)
        self.allBases.setCurrentRow(-1)
        self.output.setText(game.printFinal())
        self.playingBases.clear()
        for b in game.played_bases:
            if not b.scored and not b.destroyed and not b.terraformed: self.playingBases.addItem(BaseListItem(b))
        self.playingBases.setCurrentRow(-1)
        with open('./smash_up.backup.txt', 'w') as f:
            f.write(game.printFinal())
        import pickle
        with open('./smash_up.game', 'wb') as f:
            pickle.dump(self.state, f)



def test():
    s = Game(4)

    s.addPlayer(Player("Fabian", "Tricksters", "Kitty Cats"))
    s.addPlayer(Player("Jenny", "Tornadoes", "Super Spies"))

    s.generateBasesList()

    state = GameStates()
    state.newState(s)

    import sys
    app = QtGui.QApplication(sys.argv)
    mainGame = MainGame(state)
    print(mainGame.exec_())

if __name__ == "__main__":
    test()


