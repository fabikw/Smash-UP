'''
Created on Jun 23, 2015

@author: fabian
'''

from PyQt4 import QtGui, QtCore

from ui_endGame import Ui_endGame


class EndGame(QtGui.QDialog,Ui_endGame):
    '''
    classdocs
    '''


    def __init__(self,players,parent,madness=False):
        '''
        Constructor
        '''
        QtGui.QDialog.__init__(self,parent=parent)
        self.setupUi(self)
        self.players = players
        
        self.pl = [self.player1,self.player2,self.player3,self.player4]
        self.sc = [self.score1, self.score2, self.score3, self.score4]
        self.msc = [self.modScore1, self.modScore2, self.modScore3, self.modScore4]
        
        self.player1.setText(players[0].name)
        self.player2.setText(players[1].name)
        if not madness:
            self.modScore1.setEnabled(False)
            self.modScore2.setEnabled(False)
        if len(players) > 2:
            self.player3.setText(players[2].name)
            self.player3.setEnabled(True)
            self.score3.setEnabled(True)
            if madness:
                self.modScore3.setEnabled(True)
        if len(players) > 3:
            self.player4.setText(players[3].name)
            self.player4.setEnabled(True)
            self.player4.setEnabled(True)
            if madness:
                self.modScore4.setEnabled(True)
        self.player1.setChecked(True)
        
    def validate(self):
        for i in range(4):
            if self.sc[i].value() < self.msc[i].value(): return False
        return True
        
    def accept(self):     
        if self.validate():
            for i in range(len(self.players)):
                self.players[i].winner = self.pl[i].isChecked()
                self.players[i].finalScore = self.sc[i].value()
                self.players[i].finalModifiedScore = self.msc[i].value()
            QtGui.QDialog.accept(self)
            
    