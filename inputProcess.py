# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inputProcess.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Ui_Dialog(QtWidgets.QWidget):
    def __init__(self):

        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, TopographicCorrection):
        TopographicCorrection.setObjectName("TopographicCorrection")
        TopographicCorrection.resize(920, 684)
        self.groupBox_loadRaster = QtWidgets.QGroupBox(TopographicCorrection)
        self.groupBox_loadRaster.setGeometry(QtCore.QRect(40, 30, 801, 281))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_loadRaster.setFont(font)
        self.groupBox_loadRaster.setObjectName("groupBox_loadRaster")
        self.textEdit_folderInputRaster = QtWidgets.QTextEdit(self.groupBox_loadRaster)
        self.textEdit_folderInputRaster.setGeometry(QtCore.QRect(60, 50, 491, 41))
        self.textEdit_folderInputRaster.setObjectName("textEdit_folderInputRaster")
        self.textEdit_folderOutputRaster = QtWidgets.QTextEdit(self.groupBox_loadRaster)
        self.textEdit_folderOutputRaster.setGeometry(QtCore.QRect(60, 150, 491, 41))
        self.textEdit_folderOutputRaster.setObjectName("textEdit_folderOutputRaster")
        self.pushButton_folderInputRaster = QtWidgets.QPushButton(self.groupBox_loadRaster)
        self.pushButton_folderInputRaster.setGeometry(QtCore.QRect(590, 50, 93, 41))
        self.pushButton_folderInputRaster.setObjectName("pushButton_folderInputRaster")
        self.pushButton_folderOutputRaster = QtWidgets.QPushButton(self.groupBox_loadRaster)
        self.pushButton_folderOutputRaster.setGeometry(QtCore.QRect(590, 150, 93, 41))
        self.pushButton_folderOutputRaster.setObjectName("pushButton_folderOutputRaster")
        self.groupBox_Output = QtWidgets.QGroupBox(TopographicCorrection)
        self.groupBox_Output.setGeometry(QtCore.QRect(40, 330, 801, 281))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_Output.setFont(font)
        self.groupBox_Output.setObjectName("groupBox_Output")
        self.checkBox_blue = QtWidgets.QCheckBox(self.groupBox_Output)
        self.checkBox_blue.setGeometry(QtCore.QRect(40, 50, 311, 31))
        self.checkBox_blue.setObjectName("checkBox_blue")
        self.checkBox_green = QtWidgets.QCheckBox(self.groupBox_Output)
        self.checkBox_green.setGeometry(QtCore.QRect(40, 100, 341, 31))
        self.checkBox_green.setObjectName("checkBox_green")
        self.checkBox_red = QtWidgets.QCheckBox(self.groupBox_Output)
        self.checkBox_red.setGeometry(QtCore.QRect(40, 150, 341, 31))
        self.checkBox_red.setObjectName("checkBox_red")
        self.checkBox_nearInfrared = QtWidgets.QCheckBox(self.groupBox_Output)
        self.checkBox_nearInfrared.setGeometry(QtCore.QRect(400, 50, 311, 31))
        self.checkBox_nearInfrared.setObjectName("checkBox_nearInfrared")
        self.checkBox_shortwave1 = QtWidgets.QCheckBox(self.groupBox_Output)
        self.checkBox_shortwave1.setGeometry(QtCore.QRect(400, 100, 311, 31))
        self.checkBox_shortwave1.setObjectName("checkBox_shortwave1")
        self.checkBox_shortwave2 = QtWidgets.QCheckBox(self.groupBox_Output)
        self.checkBox_shortwave2.setGeometry(QtCore.QRect(400, 150, 311, 31))
        self.checkBox_shortwave2.setObjectName("checkBox_shortwave2")
        self.pushButton = QtWidgets.QPushButton(TopographicCorrection)
        self.pushButton.setGeometry(QtCore.QRect(590, 630, 171, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(TopographicCorrection)
        QtCore.QMetaObject.connectSlotsByName(TopographicCorrection)

    def retranslateUi(self, TopographicCorrection):
        _translate = QtCore.QCoreApplication.translate
        TopographicCorrection.setWindowTitle(_translate("TopographicCorrection", "TopographicCorrection"))
        self.groupBox_loadRaster.setTitle(_translate("TopographicCorrection", "Load Raster Data"))
        self.textEdit_folderInputRaster.setHtml(_translate("TopographicCorrection", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt; color:#7c7c7c;\">.tiff file</span></p></body></html>"))
        self.textEdit_folderOutputRaster.setHtml(_translate("TopographicCorrection", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt; color:#838383;\">.tiff file</span></p></body></html>"))
        self.pushButton_folderInputRaster.setText(_translate("TopographicCorrection", "..."))
        self.pushButton_folderOutputRaster.setText(_translate("TopographicCorrection", "..."))
        self.groupBox_Output.setTitle(_translate("TopographicCorrection", "Output"))
        self.checkBox_blue.setText(_translate("TopographicCorrection", "Blue"))
        self.checkBox_green.setText(_translate("TopographicCorrection", "Green"))
        self.checkBox_red.setText(_translate("TopographicCorrection", "Red"))
        self.checkBox_nearInfrared.setText(_translate("TopographicCorrection", "Near Infrared (NIR)"))
        self.checkBox_shortwave1.setText(_translate("TopographicCorrection", "Shortwave Infrared (SWIR) 1"))
        self.checkBox_shortwave2.setText(_translate("TopographicCorrection", "Shortwave Infrared (SWIR) 2"))
        self.pushButton.setText(_translate("TopographicCorrection", "Processing"))

        self.pushButton_folderInputRaster.clicked.connect(self.openInputRaster)
        self.pushButton_folderOutputRaster.clicked.connect(self.openOutputRaster)
        self.pushButton.clicked.connect(self.executeCode)

    def openInputRaster(self):
        fileName = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select directory')
        self.textEdit_folderInputRaster.setText(fileName)
        
    def openOutputRaster(self):
        fileName = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select directory')
        self.textEdit_folderOutputRaster.setText(fileName)

    def executeCode(self):
        msgRun = QMessageBox(self)

        msgRun.setAttribute(Qt.WA_DeleteOnClose)
        msgRun.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        msgRun.setIcon(QMessageBox.Warning)
        msgRun.setBaseSize(QSize(1000, 500))

        msgRun.setText("Please wait, Its better to keep this dialog open")
        msgRun.setWindowTitle("Running")
        msgRun.setStandardButtons(QMessageBox.Ignore)
        msgRun.setWindowModality(Qt.NonModal)
        QCoreApplication.processEvents()
        msgRun.show()

        folderInput = self.textEdit_folderInputRaster.toPlainText() # ini path folder input
        folderOutput = self.textEdit_folderOutputRaster.toPlainText() # ini path folder output
        blue = self.checkBox_blue.isChecked() 
        green = self.checkBox_green.isChecked() 
        red = self.checkBox_red.isChecked() 
        nir = self.checkBox_nearInfrared.isChecked() 
        swir1 = self.checkBox_shortwave1.isChecked()
        swir2 = self.checkBox_shortwave2.isChecked()
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Dialog()
    ex.show()
    sys.exit(app.exec_())