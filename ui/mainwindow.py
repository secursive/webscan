# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature

from Ui_mainwindow import Ui_MainWindow

from PyQt4.QtCore import QUrl,  QThread
from PyQt4.QtGui import QTextCursor
import datetime

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.txtScanOutput.setReadOnly(True);
        self.txtScanOutput.setVisible(False);
        self.webView.setVisible(True);
        self.progressBar.setVisible(False);
        # Testing input url
        self.txtUrl.setText("http://www.google.com")
    
    @pyqtSignature("")
    def on_btnScan_released(self):
        """
        Public slot invoked when the user clicks the Scan Button.
        """
        #clearing previous text
        textCursor = self.txtScanOutput.textCursor();
        textCursor.movePosition(0);
        textCursor.select(QTextCursor.Document);
        textCursor.removeSelectedText();
        #clearing unneeded views and making needed views visible
        self.webView.setVisible(False);
        self.progressBar.setVisible(False);
        self.txtScanOutput.setVisible(True);
        #performing scan and displaying results
        textCursor.insertText(">> Starting Scan (" + str(datetime.datetime.now()) + ")\n");
        textCursor.insertText(">> Finished Scan (" + str(datetime.datetime.now()) + ")\n");
    
    @pyqtSignature("")
    def on_btnView_released(self):
        """
        Public slot invoked when the user clicks the Scan Button.
        """
        self.txtScanOutput.setVisible(False);
        self.webView.setVisible(True);
        self.webView.load(QUrl(self.txtUrl.text()))
    
    @pyqtSignature("")
    def on_webView_loadStarted(self):
        """
        Public slot invoked when the web view started loading.
        """
        self.progressBar.setValue(0);
        self.progressBar.setVisible(True);
    
    @pyqtSignature("int")
    def on_webView_loadProgress(self,  progress):
        """
        Public slot invoked when the web view makes progress while loading.
        """
        self.progressBar.setValue(progress);
    
    @pyqtSignature("bool")
    def on_webView_loadFinished(self,  ok):
        """
        Public slot invoked when the web view finished loading.
        """
        self.progressBar.setVisible(False);
    
    @pyqtSignature("QString")
    def on_webView_titleChanged(self, title):
        """
        Public Slot invoked when the title of the page changes. All we do is to display it as the main window title.
        """
        self.setWindowTitle('WebScan (Secursive) | ' + title)
    
    @pyqtSignature("QUrl")
    def on_webView_urlChanged(self, url):
        """
        Public Slot invoked when the url changes. All we do is display the current url in txtUrl.
        """
        self.txtUrl.setText(url.toString())
    
