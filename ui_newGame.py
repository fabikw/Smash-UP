# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newGame.ui'
#
# Created: Mon Jun 29 15:08:15 2015
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

class Ui_newGame(object):
    def setupUi(self, newGame):
        newGame.setObjectName(_fromUtf8("newGame"))
        newGame.resize(696, 181)
        self.gridLayout_2 = QtGui.QGridLayout(newGame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.player4name = QtGui.QLabel(newGame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player4name.sizePolicy().hasHeightForWidth())
        self.player4name.setSizePolicy(sizePolicy)
        self.player4name.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player4name.setFont(font)
        self.player4name.setText(_fromUtf8(""))
        self.player4name.setObjectName(_fromUtf8("player4name"))
        self.gridLayout.addWidget(self.player4name, 3, 6, 1, 1)
        self.label_8 = QtGui.QLabel(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)
        self.player1faction2 = QtGui.QComboBox(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player1faction2.setFont(font)
        self.player1faction2.setObjectName(_fromUtf8("player1faction2"))
        self.gridLayout.addWidget(self.player1faction2, 0, 5, 1, 1)
        self.label = QtGui.QLabel(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.player4faction2 = QtGui.QComboBox(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player4faction2.setFont(font)
        self.player4faction2.setObjectName(_fromUtf8("player4faction2"))
        self.gridLayout.addWidget(self.player4faction2, 3, 5, 1, 1)
        self.label_11 = QtGui.QLabel(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 3, 2, 1, 1)
        self.player4faction1 = QtGui.QComboBox(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player4faction1.setFont(font)
        self.player4faction1.setObjectName(_fromUtf8("player4faction1"))
        self.gridLayout.addWidget(self.player4faction1, 3, 3, 1, 1)
        self.label_4 = QtGui.QLabel(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.player1name = QtGui.QLabel(newGame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player1name.sizePolicy().hasHeightForWidth())
        self.player1name.setSizePolicy(sizePolicy)
        self.player1name.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player1name.setFont(font)
        self.player1name.setText(_fromUtf8(""))
        self.player1name.setObjectName(_fromUtf8("player1name"))
        self.gridLayout.addWidget(self.player1name, 0, 6, 1, 1)
        self.label_12 = QtGui.QLabel(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 3, 4, 1, 1)
        self.player3name = QtGui.QLabel(newGame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player3name.sizePolicy().hasHeightForWidth())
        self.player3name.setSizePolicy(sizePolicy)
        self.player3name.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player3name.setFont(font)
        self.player3name.setText(_fromUtf8(""))
        self.player3name.setObjectName(_fromUtf8("player3name"))
        self.gridLayout.addWidget(self.player3name, 2, 6, 1, 1)
        self.label_3 = QtGui.QLabel(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        self.player2faction1 = QtGui.QComboBox(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player2faction1.setFont(font)
        self.player2faction1.setObjectName(_fromUtf8("player2faction1"))
        self.gridLayout.addWidget(self.player2faction1, 1, 3, 1, 1)
        self.label_2 = QtGui.QLabel(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.player2name = QtGui.QLabel(newGame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player2name.sizePolicy().hasHeightForWidth())
        self.player2name.setSizePolicy(sizePolicy)
        self.player2name.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player2name.setFont(font)
        self.player2name.setText(_fromUtf8(""))
        self.player2name.setObjectName(_fromUtf8("player2name"))
        self.gridLayout.addWidget(self.player2name, 1, 6, 1, 1)
        self.label_6 = QtGui.QLabel(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 4, 1, 1)
        self.label_7 = QtGui.QLabel(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.player3faction2 = QtGui.QComboBox(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player3faction2.setFont(font)
        self.player3faction2.setObjectName(_fromUtf8("player3faction2"))
        self.gridLayout.addWidget(self.player3faction2, 2, 5, 1, 1)
        self.label_9 = QtGui.QLabel(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 2, 4, 1, 1)
        self.player1faction1 = QtGui.QComboBox(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player1faction1.setFont(font)
        self.player1faction1.setObjectName(_fromUtf8("player1faction1"))
        self.gridLayout.addWidget(self.player1faction1, 0, 3, 1, 1)
        self.player3faction1 = QtGui.QComboBox(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player3faction1.setFont(font)
        self.player3faction1.setObjectName(_fromUtf8("player3faction1"))
        self.gridLayout.addWidget(self.player3faction1, 2, 3, 1, 1)
        self.label_10 = QtGui.QLabel(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.player2faction2 = QtGui.QComboBox(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player2faction2.setFont(font)
        self.player2faction2.setObjectName(_fromUtf8("player2faction2"))
        self.gridLayout.addWidget(self.player2faction2, 1, 5, 1, 1)
        self.player1 = QtGui.QLineEdit(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player1.setFont(font)
        self.player1.setObjectName(_fromUtf8("player1"))
        self.gridLayout.addWidget(self.player1, 0, 1, 1, 1)
        self.player2 = QtGui.QLineEdit(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player2.setFont(font)
        self.player2.setObjectName(_fromUtf8("player2"))
        self.gridLayout.addWidget(self.player2, 1, 1, 1, 1)
        self.player3 = QtGui.QLineEdit(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player3.setFont(font)
        self.player3.setObjectName(_fromUtf8("player3"))
        self.gridLayout.addWidget(self.player3, 2, 1, 1, 1)
        self.player4 = QtGui.QLineEdit(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player4.setFont(font)
        self.player4.setObjectName(_fromUtf8("player4"))
        self.gridLayout.addWidget(self.player4, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_13 = QtGui.QLabel(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout.addWidget(self.label_13)
        self.game = QtGui.QSpinBox(newGame)
        self.game.setMaximum(300)
        self.game.setObjectName(_fromUtf8("game"))
        self.horizontalLayout.addWidget(self.game)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(newGame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(newGame)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), newGame.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), newGame.reject)
        QtCore.QMetaObject.connectSlotsByName(newGame)
        newGame.setTabOrder(self.player1, self.player1faction1)
        newGame.setTabOrder(self.player1faction1, self.player1faction2)
        newGame.setTabOrder(self.player1faction2, self.player2)
        newGame.setTabOrder(self.player2, self.player2faction1)
        newGame.setTabOrder(self.player2faction1, self.player2faction2)
        newGame.setTabOrder(self.player2faction2, self.player3)
        newGame.setTabOrder(self.player3, self.player3faction1)
        newGame.setTabOrder(self.player3faction1, self.player3faction2)
        newGame.setTabOrder(self.player3faction2, self.player4)
        newGame.setTabOrder(self.player4, self.player4faction1)
        newGame.setTabOrder(self.player4faction1, self.player4faction2)
        newGame.setTabOrder(self.player4faction2, self.game)
        newGame.setTabOrder(self.game, self.buttonBox)

    def retranslateUi(self, newGame):
        newGame.setWindowTitle(_translate("newGame", "New Game", None))
        self.label_8.setText(_translate("newGame", "Faction 1", None))
        self.label.setText(_translate("newGame", "Player 1 Name", None))
        self.label_11.setText(_translate("newGame", "Faction 1", None))
        self.label_4.setText(_translate("newGame", "Player 2 Name", None))
        self.label_12.setText(_translate("newGame", "Faction 2", None))
        self.label_3.setText(_translate("newGame", "Faction 2", None))
        self.label_2.setText(_translate("newGame", "Faction 1", None))
        self.label_6.setText(_translate("newGame", "Faction 2", None))
        self.label_7.setText(_translate("newGame", "Player 3 Name", None))
        self.label_5.setText(_translate("newGame", "Faction 1", None))
        self.label_9.setText(_translate("newGame", "Faction 2", None))
        self.label_10.setText(_translate("newGame", "Player 4 Name", None))
        self.label_13.setText(_translate("newGame", "Game Number", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    newGame = QtGui.QDialog()
    ui = Ui_newGame()
    ui.setupUi(newGame)
    newGame.show()
    sys.exit(app.exec_())

