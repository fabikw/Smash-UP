# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGame.ui'
#
# Created: Wed Jul 15 15:29:36 2015
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
        mainGame.resize(1005, 708)
        self.gridLayout_4 = QtGui.QGridLayout(mainGame)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.splitter_2 = QtGui.QSplitter(mainGame)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.newBase = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newBase.sizePolicy().hasHeightForWidth())
        self.newBase.setSizePolicy(sizePolicy)
        self.newBase.setMinimumSize(QtCore.QSize(101, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.newBase.setFont(font)
        self.newBase.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.newBase.setAutoDefault(False)
        self.newBase.setObjectName(_fromUtf8("newBase"))
        self.gridLayout_3.addWidget(self.newBase, 0, 1, 1, 1)
        self.allBases = QtGui.QListWidget(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allBases.sizePolicy().hasHeightForWidth())
        self.allBases.setSizePolicy(sizePolicy)
        self.allBases.setMinimumSize(QtCore.QSize(241, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.allBases.setFont(font)
        self.allBases.setAlternatingRowColors(True)
        self.allBases.setObjectName(_fromUtf8("allBases"))
        self.gridLayout_3.addWidget(self.allBases, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.playingBases = QtGui.QListWidget(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playingBases.sizePolicy().hasHeightForWidth())
        self.playingBases.setSizePolicy(sizePolicy)
        self.playingBases.setMinimumSize(QtCore.QSize(240, 152))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.playingBases.setFont(font)
        self.playingBases.setAlternatingRowColors(True)
        self.playingBases.setObjectName(_fromUtf8("playingBases"))
        self.gridLayout_2.addWidget(self.playingBases, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.terraform = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.terraform.sizePolicy().hasHeightForWidth())
        self.terraform.setSizePolicy(sizePolicy)
        self.terraform.setMinimumSize(QtCore.QSize(101, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.terraform.setFont(font)
        self.terraform.setAutoDefault(False)
        self.terraform.setObjectName(_fromUtf8("terraform"))
        self.verticalLayout_2.addWidget(self.terraform)
        self.scoreBase = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scoreBase.sizePolicy().hasHeightForWidth())
        self.scoreBase.setSizePolicy(sizePolicy)
        self.scoreBase.setMinimumSize(QtCore.QSize(101, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scoreBase.setFont(font)
        self.scoreBase.setAutoDefault(False)
        self.scoreBase.setObjectName(_fromUtf8("scoreBase"))
        self.verticalLayout_2.addWidget(self.scoreBase)
        self.destroy = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.destroy.sizePolicy().hasHeightForWidth())
        self.destroy.setSizePolicy(sizePolicy)
        self.destroy.setMinimumSize(QtCore.QSize(101, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.destroy.setFont(font)
        self.destroy.setAutoDefault(False)
        self.destroy.setObjectName(_fromUtf8("destroy"))
        self.verticalLayout_2.addWidget(self.destroy)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.undo = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.undo.sizePolicy().hasHeightForWidth())
        self.undo.setSizePolicy(sizePolicy)
        self.undo.setMinimumSize(QtCore.QSize(101, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.undo.setFont(font)
        self.undo.setObjectName(_fromUtf8("undo"))
        self.verticalLayout.addWidget(self.undo)
        self.redo = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.redo.sizePolicy().hasHeightForWidth())
        self.redo.setSizePolicy(sizePolicy)
        self.redo.setMinimumSize(QtCore.QSize(101, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.redo.setFont(font)
        self.redo.setObjectName(_fromUtf8("redo"))
        self.verticalLayout.addWidget(self.redo)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.finish = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finish.sizePolicy().hasHeightForWidth())
        self.finish.setSizePolicy(sizePolicy)
        self.finish.setMinimumSize(QtCore.QSize(101, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.finish.setFont(font)
        self.finish.setAutoDefault(False)
        self.finish.setObjectName(_fromUtf8("finish"))
        self.horizontalLayout_3.addWidget(self.finish)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.updateCards = QtGui.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.updateCards.setFont(font)
        self.updateCards.setObjectName(_fromUtf8("updateCards"))
        self.horizontalLayout.addWidget(self.updateCards)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.keyCards = QtGui.QPlainTextEdit(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keyCards.sizePolicy().hasHeightForWidth())
        self.keyCards.setSizePolicy(sizePolicy)
        self.keyCards.setMinimumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.keyCards.setFont(font)
        self.keyCards.setObjectName(_fromUtf8("keyCards"))
        self.gridLayout.addWidget(self.keyCards, 0, 0, 1, 1)
        self.specificCards = QtGui.QPlainTextEdit(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.specificCards.sizePolicy().hasHeightForWidth())
        self.specificCards.setSizePolicy(sizePolicy)
        self.specificCards.setMinimumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.specificCards.setFont(font)
        self.specificCards.setObjectName(_fromUtf8("specificCards"))
        self.gridLayout.addWidget(self.specificCards, 0, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.output = QtGui.QTextEdit(self.splitter_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy)
        self.output.setMinimumSize(QtCore.QSize(791, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.output.setFont(font)
        self.output.setUndoRedoEnabled(False)
        self.output.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.output.setReadOnly(True)
        self.output.setObjectName(_fromUtf8("output"))
        self.gridLayout_4.addWidget(self.splitter_2, 0, 0, 1, 1)

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
        self.label_2.setText(_translate("mainGame", "Specific Cards", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainGame = QtGui.QDialog()
    ui = Ui_mainGame()
    ui.setupUi(mainGame)
    mainGame.show()
    sys.exit(app.exec_())

