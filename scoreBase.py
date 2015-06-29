'''
Created on Jun 22, 2015

@author: fabian
'''

from PyQt4 import QtGui, QtCore
from ui_scoreBase import Ui_scoreBase
from data import BASES
from system import Player, Base


class ScoreBase(QtGui.QDialog, Ui_scoreBase):
    '''
    classdocs
    '''
    def __init__(self, base, players, parent):
        '''
        Constructor
        '''
        QtGui.QDialog.__init__(self, parent = parent)
        self.setupUi(self)
        self.baseName.setText(base.name)
        self.name2.addItem('')
        self.name3.addItem('')
        self.name4.addItem('')
        for pl in players:
            self.name1.addItem(pl.name)
            self.name2.addItem(pl.name)
            self.name3.addItem(pl.name)
            self.name4.addItem(pl.name)
        self.points1.setCurrentIndex(BASES[base.name][0])
        self.points2.setCurrentIndex(BASES[base.name][1])
        self.points3.setCurrentIndex(BASES[base.name][2])
        if (len(players) < 4):
            self.name4.setEnabled(False)
            self.points4.setEnabled(False)
            self.comments4.setEnabled(False)
        if (len(players) < 3):
            self.name3.setEnabled(False)
            self.points3.setEnabled(False)
            self.comments3.setEnabled(False)

    def accept(self):
        if self.validate():
            QtGui.QDialog.accept(self)

    def validate(self):
        names = set()
        names.add(self.name1.currentText())
        if self.name2.currentText() and self.name2.currentText() in names:
            QtGui.QMessageBox.critical(self, "Error", "Same player cannot score twice.", buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.NoButton)
            return False
        else:
            names.add(self.name2.currentText())
        if self.name3.currentText() and self.name3.currentText() in names:
            QtGui.QMessageBox.critical(self, "Error", "Same player cannot score twice.", buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.NoButton)
            return False
        else:
            names.add(self.name3.currentText())
        if self.name4.currentText() and self.name4.currentText() in names:
            QtGui.QMessageBox.critical(self, "Error", "Same player cannot score twice.", buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.NoButton)
            return False
        return True

    def values(self):
        players = []
        points = []
        comments = []
        players.append(self.name1.currentText())
        points.append(self.points1.currentIndex())
        comments.append(self.comments1.text())
        import re
        if self.name2.currentIndex() != 0:
            players.append(self.name2.currentText())
            points.append(self.points2.currentIndex())
            comments.append(self.comments2.text())
        if self.name3.currentIndex() != 0:
            players.append(self.name3.currentText())
            points.append(self.points3.currentIndex())
            comments.append(self.comments3.text())
        if self.name4.currentIndex() != 0:
            players.append(self.name4.currentText())
            points.append(self.points4.currentIndex())
            comments.append(self.comments4.text())
        comments2 = []
        for t in comments:
            comments2.append(re.sub("[*](.*?)[*]", r"[b]\1[/b]", t))
        return players, points, comments2


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    players = [Player("Fabian", "Tricksters", "Kitty Cats"), Player("Jenny", "Tornadoes", "Super Spies")]
    scoreBase = ScoreBase(Base("Tortuga"), players, None)
    # scoreBase.show()
    print(scoreBase.exec_())
    print(scoreBase.values())
