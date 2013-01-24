# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Secursive\Github\workspace\webscan\ui\mainwindow.ui'
#
# Created: Thu Jan 24 16:14:57 2013
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.txtUrl = QtGui.QLineEdit(self.centralWidget)
        self.txtUrl.setObjectName(_fromUtf8("txtUrl"))
        self.horizontalLayout.addWidget(self.txtUrl)
        self.btnView = QtGui.QPushButton(self.centralWidget)
        self.btnView.setObjectName(_fromUtf8("btnView"))
        self.horizontalLayout.addWidget(self.btnView)
        self.btnScan = QtGui.QPushButton(self.centralWidget)
        self.btnScan.setObjectName(_fromUtf8("btnScan"))
        self.horizontalLayout.addWidget(self.btnScan)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.webView = QtWebKit.QWebView(self.centralWidget)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout.addWidget(self.webView, 2, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.centralWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 1)
        self.txtScanOutput = QtGui.QPlainTextEdit(self.centralWidget)
        self.txtScanOutput.setObjectName(_fromUtf8("txtScanOutput"))
        self.gridLayout.addWidget(self.txtScanOutput, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "WebScan (Secursive)", None))
        self.txtUrl.setText(_translate("MainWindow", "http://", None))
        self.btnView.setText(_translate("MainWindow", "View", None))
        self.btnScan.setText(_translate("MainWindow", "Scan", None))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

