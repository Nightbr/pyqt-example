#!/usr/bin/python
# -*- coding: UTF-8 -*-
#***************************************************************************#
#                                                                           #
#                              MainUI.py                                    #
#                                                                           #
#***************************************************************************#
#                                                                           #
# Class MainUI extend from Ui_MainWindow which is generated with #
# py2uic and QtDesigner.                                                    #
#                                                                           #
#                                                                           #
#***************************************************************************#
# Création     : 29.07.2015  T. Benoit       Version 1.0                    #
# Vérifié      : @@.@@.@@@@  T. Benoit                                      #
# Modification :                                                            #
#***************************************************************************#

import sys
import UI.MyUI as MyUI
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class MainUI(QtGui.QMainWindow, MyUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainUI, self).__init__(parent)
        self.setupUi(self)

        # customize UI here

 
    def main(self):
        self.show()
