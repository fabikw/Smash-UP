# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'endGame.ui'
#
# Created: Mon Jun 29 15:09:42 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_endGame(object):
    def setupUi(self, endGame):
        endGame.setObjectName(_fromUtf8("endGame"))
        endGame.resize(461, 252)
        self.gridLayout_2 = QtGui.QGridLayout(endGame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.player1 = QtGui.QRadioButton(endGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player1.setFont(font)
        self.player1.setText(_fromUtf8(""))
        self.player1.setObjectName(_fromUtf8("player1"))
        self.buttonGroup = QtGui.QButtonGroup(endGame)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.player1)
        self.gridLayout.addWidget(self.player1, 0, 0, 1, 1)
        self.player3 = QtGui.QRadioButton(endGame)
        self.player3.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player3.setFont(font)
        self.player3.setText(_fromUtf8(""))
        self.player3.setObjectName(_fromUtf8("player3"))
        self.buttonGroup.addButton(self.player3)
        self.gridLayout.addWidget(self.player3, 2, 0, 1, 1)
        self.player2 = QtGui.QRadioButton(endGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player2.setFont(font)
        self.player2.setText(_fromUtf8(""))
        self.player2.setObjectName(_fromUtf8("player2"))
        self.buttonGroup.addButton(self.player2)
        self.gridLayout.addWidget(self.player2, 1, 0, 1, 1)
        self.modScore2 = QtGui.QSpinBox(endGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.modScore2.setFont(font)
        self.modScore2.setObjectName(_fromUtf8("modScore2"))
        self.gridLayout.addWidget(self.modScore2, 1, 2, 1, 1)
        self.modScore3 = QtGui.QSpinBox(endGame)
        self.modScore3.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.modScore3.setFont(font)
        self.modScore3.setObjectName(_fromUtf8("modScore3"))
        self.gridLayout.addWidget(self.modScore3, 2, 2, 1, 1)
        self.score1 = QtGui.QSpinBox(endGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.score1.setFont(font)
        self.score1.setProperty("value", 0)
        self.score1.setObjectName(_fromUtf8("score1"))
        self.gridLayout.addWidget(self.score1, 0, 1, 1, 1)
        self.score2 = QtGui.QSpinBox(endGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.score2.setFont(font)
        self.score2.setObjectName(_fromUtf8("score2"))
        self.gridLayout.addWidget(self.score2, 1, 1, 1, 1)
        self.score3 = QtGui.QSpinBox(endGame)
        self.score3.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.score3.setFont(font)
        self.score3.setObjectName(_fromUtf8("score3"))
        self.gridLayout.addWidget(self.score3, 2, 1, 1, 1)
        self.modScore4 = QtGui.QSpinBox(endGame)
        self.modScore4.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.modScore4.setFont(font)
        self.modScore4.setObjectName(_fromUtf8("modScore4"))
        self.gridLayout.addWidget(self.modScore4, 3, 2, 1, 1)
        self.score4 = QtGui.QSpinBox(endGame)
        self.score4.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.score4.setFont(font)
        self.score4.setObjectName(_fromUtf8("score4"))
        self.gridLayout.addWidget(self.score4, 3, 1, 1, 1)
        self.modScore1 = QtGui.QSpinBox(endGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.modScore1.setFont(font)
        self.modScore1.setObjectName(_fromUtf8("modScore1"))
        self.gridLayout.addWidget(self.modScore1, 0, 2, 1, 1)
        self.player4 = QtGui.QRadioButton(endGame)
        self.player4.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player4.setFont(font)
        self.player4.setText(_fromUtf8(""))
        self.player4.setObjectName(_fromUtf8("player4"))
        self.buttonGroup.addButton(self.player4)
        self.gridLayout.addWidget(self.player4, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(endGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(endGame)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), endGame.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), endGame.reject)
        QtCore.QMetaObject.connectSlotsByName(endGame)

    def retranslateUi(self, endGame):
        endGame.setWindowTitle(_translate("endGame", "End of game", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    endGame = QtGui.QDialog()
    ui = Ui_endGame()
    ui.setupUi(endGame)
    endGame.show()
    sys.exit(app.exec_())

