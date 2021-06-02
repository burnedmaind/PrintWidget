####################################مكاتب gui#######################
from os import path, popen
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt5.Qt import QFileInfo

MainUI, _ = loadUiType('/home/work/myproject/printjob_code/printapp.ui')
####################################################################


# FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__),"/home/work/myproject/printjob_code/printapp.ui"))

class Mainapp(QMainWindow, MainUI):
    def __init__(self, parent=None):
        super(Mainapp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Hndel_ui()
        # self.top = 270
        # self.left = 500
        # self.width = 680
        # self.height = 480
        # self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon("print.png"))
        self.setWindowIconText("print.png")
        self.cansel.clicked.connect(exit)
        self.PrintFile.clicked.connect(self.printDialog)
        self.exportPDF.clicked.connect(self.BrowseFilePDF)
        self.ChooseFile.clicked.connect(self.BrowseFile)
        self.convert.clicked.connect(self.exportpdf)

    def Hndel_ui(self):

        self.setWindowTitle('print')
        #self.setFixedSize(1015, 376)

    def Hnadel_Progress(self):
        read = blocknum * blocksize
        if totalsize > 0:
            percent = read * 100 / totalsize
            self.progressBar.setValue(percent)

    def BrowseFile(self):
        saveplace = QFileDialog.getOpenFileName(
            self, caption="open", directory=".", filter="All Files (*.*)")
        print(saveplace)
        text = str(saveplace)
        name = (text[2:].split(',')[0].replace("'", ''))
        self.lineEdit.setText(name)

    def BrowseFilePDF(self):
        saveplace2 = QFileDialog.getOpenFileName(self, caption="open", directory=".", filter="All Files (*.*)")
        print(saveplace2)
        text = str(saveplace2)
        name = (text[2:].split(',')[0].replace("'", ''))
        self.lineEdit_2.setText(name)

    def printDialog(self):
        filename = self.lineEdit.text()
        try:
            popen(f'lp {filename}')
        except Exception:
            QMessageBox.warning(self, "", "تأكد من وصل الطابعة بالجهاز")

    def exportpdf(self):
        filename2 = self.lineEdit_2.text()
        saveplace2 = QFileDialog.getSaveFileName(self, caption="save as", directory=".", filter="All Files (*.*)")
        export=popen(f'lowriter --convert-to pdf --outdir {filename2} {saveplace2}')
        #QMessageBox.iلم يتم التحويل")nformation(self,"",  "تم") 
        QMessageBox.warning(self, "" ,"لم يتم التحويل")


def main():
    app = QApplication(sys.argv)
    window = Mainapp()
    window.setWindowTitle("print")
    window.setWindowIcon(QIcon('print.png'))
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
