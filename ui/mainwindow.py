# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature

from Ui_mainwindow import Ui_MainWindow

from PyQt4.QtCore import QUrl

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
        self.progressBar.setVisible(False);
    
    @pyqtSignature("")
    def on_btnScan_released(self):
        """
        Public slot invoked when the user clicks the Scan Button.
        """
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
    
