# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4 import QtCore
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QTextCursor
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import QUrl,  QThread
import datetime
from core.scanthread import ScanThread
from Ui_mainwindow import Ui_MainWindow

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
        self.scanThread = None
        self.scanTimer = QtCore.QTimer()
        self.scanTimer.setInterval(1000); # 1 second
        self.connect(self.scanTimer, QtCore.SIGNAL("timeout()"), self.on_scanTimer_Timeout)
        self.scanStartedTime = datetime.datetime.now();
        self.textCursor = self.txtScanOutput.textCursor();
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
        self.textCursor.movePosition(QTextCursor.Start);
        self.textCursor.select(QTextCursor.Document);
        self.textCursor.removeSelectedText();
        #clearing unneeded views and making needed views visible
        self.webView.setVisible(False);
        self.progressBar.setVisible(False);
        self.txtScanOutput.setVisible(True);
        #performing scan and displaying results
        if (self.scanThread is not None and self.scanThread.isRunning()):
            self.scanThread.quit();
            self.scanThread = None
        self.scanThread = ScanThread(self);
        self.connect(self.scanThread, QtCore.SIGNAL('printOutput(QString)'), self.on_scanThread_printOutput);
        self.connect(self.scanThread, QtCore.SIGNAL('started()'), self.on_scanThread_started);
        self.connect(self.scanThread, QtCore.SIGNAL('finished()'), self.on_scanThread_finished);
        self.connect(self.scanThread, QtCore.SIGNAL('terminated()'), self.on_scanThread_terminated);
        self.scanThread.start();

    @pyqtSignature("")
    def on_scanTimer_Timeout(self):
        self.textCursor.movePosition(QTextCursor.StartOfLine);
        self.textCursor.select(QTextCursor.LineUnderCursor);
        self.textCursor.removeSelectedText();
        time_diff = datetime.datetime.now() - self.scanStartedTime;
        time_diff = time_diff - datetime.timedelta(microseconds=time_diff.microseconds); #removing microseconds from output
        self.textCursor.insertText("[" + str(time_diff) + "] ");
    
    @pyqtSignature("QString")
    def on_scanThread_printOutput(self,  msg=None):
        if msg is not None:
            self.textCursor.insertText(str(msg) + "\n");
    
    @pyqtSignature("")
    def on_scanThread_started(self):
        self.textCursor.insertText(">> Scan started (" + datetime.datetime.now().strftime("%A, %d %B %Y %I:%M%p") + ")\n\n");
        self.on_scanTimer_Timeout();
        self.scanStartedTime = datetime.datetime.now();
        self.scanTimer.start();
    
    @pyqtSignature("")
    def on_scanThread_finished(self):
        self.scanTimer.stop();
        self.textCursor.insertText(">> Scan finished (" + datetime.datetime.now().strftime("%A, %d %B %Y %I:%M%p") + ")\n\n");
    
    @pyqtSignature("")
    def on_scanThread_terminated(self):
        self.scanTimer.stop();
        self.textCursor.insertText(">> Scan terminated (" + datetime.datetime.now().strftime("%A, %d %B %Y %I:%M%p") + ")\n\n");
    
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
    
