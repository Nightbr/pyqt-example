#!/usr/bin/python
# -*- coding: UTF-8 -*-
#***************************************************************************#
#                                                                           #
#                              appName.py                                   #
#                                                                           #
#***************************************************************************#
#                                                                           #
# Main file for our Application                                             #
#                                                                           #
#                                                                           #
#                                                                           #
#***************************************************************************#
# Création     : 29.07.2015  T. Benoit       Version 1.0                    #
# Vérifié      : @@.@@.@@@@  T. Benoit                                      #
# Modification :                                                            #
#***************************************************************************#

import sys
from MainUI import MainUI
from App import App
from PyQt4 import QtCore, QtGui

def main():
    app = QtGui.QApplication(sys.argv) #create a Qt app
    gui = MainUI() # create GUI instance
    myApp = App(gui,app)
    myApp.main() # init the App
    sys.exit(app.exec_()) # lauch Qt App

#---------------------------------------------------------------------------#
#                                Main                                       #
#---------------------------------------------------------------------------#

if __name__=='__main__':
    main()