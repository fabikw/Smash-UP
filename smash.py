'''
Created on Jun 23, 2015

@author: fabian
'''

from PyQt4 import QtGui

from MainGame import MainGame
from newGame import NewGame
from system import GameStates, Game


stylesheet = """
QDialog{background-color: rgb(227, 184, 241)}
QInputDialog QLabel{font-size: 12pt}
QInputDialog QComboBox{font-size: 12pt}
"""


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    newGame = NewGame()
    res = newGame.exec_()
    if res == 1:
        state = GameStates()
        num, players = newGame.values()
        game = Game(num)
        state.newState(game)
        for p in players:
            game.addPlayer(p)
        game.generateBasesList()
        mainGame = MainGame(state)
        mainGame.exec_()
    elif res == 2:
        state = newGame.values()
        mainGame = MainGame(state)
        mainGame.exec_()