
from PyQt4 import QtCore
from PyQt4.QtCore import QUrl,  QThread
from PyQt4.QtCore import pyqtSignature
import datetime

class ScanThread(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        
    @pyqtSignature("QString")
    def appendToOutput(self,  msg):
        self.emit(QtCore.SIGNAL('printOutput(QString)'),  msg);
        
    @pyqtSignature("")
    def run(self):
        self.appendToOutput("Test 1 Start.\n");
        QThread.sleep(10); #sleep for 10 seconds
        self.appendToOutput("Test 1 End.\n");
