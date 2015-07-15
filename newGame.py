'''
Created on Jun 22, 2015

@author: fabian
'''

from PyQt4 import QtGui, QtCore
from data import FACTIONS
from system import Game, Player, GameStates, Base
from ui_newGame import Ui_newGame

class NewGame(QtGui.QDialog, Ui_newGame):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.raise_()
        self.activateWindow()

        factions = [f for f in FACTIONS.keys()]
        factions.sort()

        self.player1faction1.addItems(factions)
        self.player1faction2.addItems(factions)
        self.player2faction1.addItems(factions)
        self.player2faction2.addItems(factions)
        self.player3faction1.addItems(factions)
        self.player3faction2.addItems(factions)
        self.player4faction1.addItems(factions)
        self.player4faction2.addItems(factions)



        self.player1faction1.currentIndexChanged.connect(self.player1Change)
        self.player1faction2.currentIndexChanged.connect(self.player1Change)
        self.player2faction1.currentIndexChanged.connect(self.player2Change)
        self.player2faction2.currentIndexChanged.connect(self.player2Change)
        self.player3faction1.currentIndexChanged.connect(self.player3Change)
        self.player3faction2.currentIndexChanged.connect(self.player3Change)
        self.player4faction1.currentIndexChanged.connect(self.player4Change)
        self.player4faction2.currentIndexChanged.connect(self.player4Change)
        self.loadGame.clicked.connect(self.load)

        self.player1Change()
        self.player2Change()
        self.player3Change()
        self.player4Change()

#         self.player1.textChanged.connect(self.validate)
#         self.player2.textChanged.connect(self.validate)
#         self.player3.textChanged.connect(self.validate)
#         self.player4.textChanged.connect(self.validate)
#
#         self.buttonBox.

    def load(self):
        load_file = QtGui.QFileDialog.getOpenFileName(parent = self, caption = 'Open file', directory = '.')
        if load_file:
            import pickle
            try:
                f = open(load_file, 'rb')
                game_state = pickle.load(f)
                assert(isinstance(game_state, GameStates))
                import types
                self.validate = types.MethodType(lambda x: True, self)
                self.values = types.MethodType(lambda x: game_state, self)
                self.done(2)
            except Exception as e:
                print(e)
                QtGui.QMessageBox.critical(self, "Error", "The file could not be loaded")
            finally:
                f.close()



    def accept(self):
        if self.validate():
            QtGui.QDialog.accept(self)

    def player1Change(self):
        self.changeName(self.player1faction1.currentText(), self.player1faction2.currentText(), self.player1name)

    def player2Change(self):
        self.changeName(self.player2faction1.currentText(), self.player2faction2.currentText(), self.player2name)

    def player3Change(self):
        self.changeName(self.player3faction1.currentText(), self.player3faction2.currentText(), self.player3name)

    def player4Change(self):
        self.changeName(self.player4faction1.currentText(), self.player4faction2.currentText(), self.player4name)

    def changeName(self, faction1, faction2, label):
        label.setText(' '.join([FACTIONS[faction1][0], FACTIONS[faction2][1]]))

    def validate(self):
        players = 0
        p1 = self.player1.text()
        p2 = self.player2.text()
        p3 = self.player3.text()
        p4 = self.player4.text()
        factions = set()
        if p1:
            players += 1
            p11 = self.player1faction1.currentIndex()
            p12 = self.player1faction2.currentIndex()
            if  p11 == p12:
                QtGui.QMessageBox.critical(self, "Error", "Player 1's factions are the same", buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.NoButton)
                return False
            factions.add(p11)
            factions.add(p12)

        if p2:
            players += 1
            p21 = self.player2faction1.currentIndex()
            p22 = self.player2faction2.currentIndex()
            if  p21 == p22:
                QtGui.QMessageBox.critical(self, "Error", "Player 2's factions are the same", buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.NoButton)
                return False
            factions.add(p21)
            factions.add(p22)
        if p3:
            players += 1
            p31 = self.player3faction1.currentIndex()
            p32 = self.player3faction2.currentIndex()
            if  p31 == p32:
                QtGui.QMessageBox.critical(self, "Error", "Player 3's factions are the same", buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.NoButton)
                return False
            factions.add(p31)
            factions.add(p32)
        if p4:
            players += 1
            p41 = self.player4faction1.currentIndex()
            p42 = self.player4faction2.currentIndex()
            if  p41 == p42:
                QtGui.QMessageBox.critical(self, "Error", "Player 4's factions are the same", buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.NoButton)
                return False
            factions.add(p41)
            factions.add(p42)
        if players < 2:
            QtGui.QMessageBox.critical(self, "Error", "At least 2 players are needed", buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.NoButton)
            return False
        if len(factions) < players * 2:
            QtGui.QMessageBox.critical(self, "Error", "Players have the same factions", buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.NoButton)
            return False
        return True

    def values(self):
        p1 = self.player1.text()
        p2 = self.player2.text()
        p3 = self.player3.text()
        p4 = self.player4.text()
        players = []
        if p1: players.append(Player(p1, self.player1faction1.currentText(), self.player1faction2.currentText()))
        if p2: players.append(Player(p2, self.player2faction1.currentText(), self.player2faction2.currentText()))
        if p3: players.append(Player(p3, self.player3faction1.currentText(), self.player3faction2.currentText()))
        if p4: players.append(Player(p4, self.player4faction1.currentText(), self.player4faction2.currentText()))
        return self.game.value(), players



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    newGame = NewGame()
    print(newGame.exec_())
    print(newGame.values())
