# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGame.ui'
#
# Created: Wed Jun 24 16:00:10 2015
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

class Ui_mainGame(object):
    def setupUi(self, mainGame):
        mainGame.setObjectName(_fromUtf8("mainGame"))
        mainGame.resize(823, 812)
        self.splitter_2 = QtGui.QSplitter(mainGame)
        self.splitter_2.setGeometry(QtCore.QRect(20, 10, 791, 791))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.allBases = QtGui.QListWidget(self.widget)
        self.allBases.setObjectName(_fromUtf8("allBases"))
        self.horizontalLayout.addWidget(self.allBases)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.newBase = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newBase.sizePolicy().hasHeightForWidth())
        self.newBase.setSizePolicy(sizePolicy)
        self.newBase.setMinimumSize(QtCore.QSize(101, 0))
        self.newBase.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.newBase.setAutoDefault(False)
        self.newBase.setObjectName(_fromUtf8("newBase"))
        self.horizontalLayout.addWidget(self.newBase)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.playingBases = QtGui.QListWidget(self.widget)
        self.playingBases.setObjectName(_fromUtf8("playingBases"))
        self.horizontalLayout_2.addWidget(self.playingBases)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.terraform = QtGui.QPushButton(self.widget)
        self.terraform.setAutoDefault(False)
        self.terraform.setObjectName(_fromUtf8("terraform"))
        self.verticalLayout_2.addWidget(self.terraform)
        self.scoreBase = QtGui.QPushButton(self.widget)
        self.scoreBase.setAutoDefault(False)
        self.scoreBase.setObjectName(_fromUtf8("scoreBase"))
        self.verticalLayout_2.addWidget(self.scoreBase)
        self.destroy = QtGui.QPushButton(self.widget)
        self.destroy.setAutoDefault(False)
        self.destroy.setObjectName(_fromUtf8("destroy"))
        self.verticalLayout_2.addWidget(self.destroy)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.undo = QtGui.QPushButton(self.widget)
        self.undo.setObjectName(_fromUtf8("undo"))
        self.verticalLayout.addWidget(self.undo)
        self.redo = QtGui.QPushButton(self.widget)
        self.redo.setObjectName(_fromUtf8("redo"))
        self.verticalLayout.addWidget(self.redo)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.finish = QtGui.QPushButton(self.widget)
        self.finish.setAutoDefault(False)
        self.finish.setObjectName(_fromUtf8("finish"))
        self.horizontalLayout_3.addWidget(self.finish)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.updateCards = QtGui.QPushButton(self.widget1)
        self.updateCards.setObjectName(_fromUtf8("updateCards"))
        self.horizontalLayout_4.addWidget(self.updateCards)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.keyCards = QtGui.QPlainTextEdit(self.widget1)
        self.keyCards.setMinimumSize(QtCore.QSize(400, 0))
        self.keyCards.setObjectName(_fromUtf8("keyCards"))
        self.verticalLayout_4.addWidget(self.keyCards)
        self.output = QtGui.QTextEdit(self.splitter_2)
        self.output.setMinimumSize(QtCore.QSize(0, 400))
        self.output.setUndoRedoEnabled(False)
        self.output.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.output.setReadOnly(True)
        self.output.setObjectName(_fromUtf8("output"))

        self.retranslateUi(mainGame)
        QtCore.QMetaObject.connectSlotsByName(mainGame)

    def retranslateUi(self, mainGame):
        mainGame.setWindowTitle(_translate("mainGame", "Game", None))
        self.newBase.setText(_translate("mainGame", "New Base", None))
        self.terraform.setText(_translate("mainGame", "Terraform Base", None))
        self.scoreBase.setText(_translate("mainGame", "Score Base", None))
        self.destroy.setText(_translate("mainGame", "Destroy Base", None))
        self.undo.setText(_translate("mainGame", "Undo", None))
        self.redo.setText(_translate("mainGame", "Redo", None))
        self.finish.setText(_translate("mainGame", "Finish Game", None))
        self.label.setText(_translate("mainGame", "Key Cards", None))
        self.updateCards.setText(_translate("mainGame", "Update", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainGame = QtGui.QDialog()
    ui = Ui_mainGame()
    ui.setupUi(mainGame)
    mainGame.show()
    sys.exit(app.exec_())

