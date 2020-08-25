from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyPDF2 import PdfFileMerger


class Ui_PDFMerger(object):
    def setupUi(self, PDFMerger):
        PDFMerger.setObjectName("PDFMerger")
        PDFMerger.resize(471, 427)
        self.centralwidget = QtWidgets.QWidget(PDFMerger)
        self.centralwidget.setObjectName("centralwidget")
        
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 30, 331, 192))
        self.listWidget.setObjectName("listWidget")
        
               
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(360, 60, 93, 28))
        self.btnAdd.setObjectName("btnAdd")
        self.btnMoveUp = QtWidgets.QPushButton(self.centralwidget)
        self.btnMoveUp.setGeometry(QtCore.QRect(360, 90, 93, 28))
        self.btnMoveUp.setObjectName("btnMoveUp")
        self.btnMoveDown = QtWidgets.QPushButton(self.centralwidget)
        self.btnMoveDown.setGeometry(QtCore.QRect(360, 120, 93, 28))
        self.btnMoveDown.setObjectName("btnMoveDown")
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setGeometry(QtCore.QRect(360, 150, 93, 28))
        self.btnDelete.setObjectName("btnDelete")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 240, 331, 31))
        self.lineEdit.setObjectName("lineEdit")
        
        self.btnOutDir = QtWidgets.QPushButton(self.centralwidget)
        self.btnOutDir.setGeometry(QtCore.QRect(360, 240, 93, 28))
        self.btnOutDir.setObjectName("btnOutDir")
        
        self.btnMerge = QtWidgets.QPushButton(self.centralwidget)
        self.btnMerge.setGeometry(QtCore.QRect(300, 330, 151, 41))
        self.btnMerge.setObjectName("btnMerge")
        
        self.outputFile = QtWidgets.QLineEdit(self.centralwidget)
        self.outputFile.setGeometry(QtCore.QRect(20, 280, 331, 31))
        self.outputFile.setText("")
        self.outputFile.setObjectName("outputFile")
        
        PDFMerger.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PDFMerger)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 458, 25))
        self.menubar.setObjectName("menubar")
        PDFMerger.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PDFMerger)
        self.statusbar.setObjectName("statusbar")
        PDFMerger.setStatusBar(self.statusbar)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 340, 131, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 301, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(PDFMerger)
        QtCore.QMetaObject.connectSlotsByName(PDFMerger)
        
   
        self.btnAdd.clicked.connect(lambda: self.addButtonClicked())
        self.btnMoveUp.clicked.connect(lambda: self.moveUpButtonClicked())
        self.btnMoveDown.clicked.connect(lambda: self.moveDownButtonClicked())
        self.btnDelete.clicked.connect(lambda: self.deleteButtonClicked())
        self.btnOutDir.clicked.connect(lambda: self.outDirButtonClicked())
        self.btnMerge.clicked.connect(lambda: self.mergeButtonClicked())
        


    def retranslateUi(self, PDFMerger):
        _translate = QtCore.QCoreApplication.translate
        PDFMerger.setWindowTitle(_translate("PDFMerger", "PDF Merger"))
        PDFMerger.setWindowIcon(QIcon('pdf.png')) 
        self.btnAdd.setText(_translate("PDFMerger", "Add Files"))
        self.btnMoveUp.setText(_translate("PDFMerger", "Move Up"))
        self.btnMoveDown.setText(_translate("PDFMerger", "Move Down"))
        self.btnDelete.setText(_translate("PDFMerger", "Delete"))
        self.lineEdit.setPlaceholderText(_translate("PDFMerger", "Output Directory"))
        self.btnOutDir.setText(_translate("PDFMerger", "Ouptut Dir"))
        self.btnMerge.setText(_translate("PDFMerger", "Merge PDFs"))
        self.outputFile.setPlaceholderText(_translate("PDFMerger", "Output Filename"))
        self.label_2.setText(_translate("PDFMerger", "Files will be merged in the below order"))

        
    def addButtonClicked(self):
        filter_mask = "Python/Text files (*.pdf)"
        caption = "Open Files"
        filename = QFileDialog.getOpenFileNames(None,caption, None, filter_mask)        
        self.path = filename[0]
        for i in self.path:
            self.listWidget.addItem(i)
            
    def moveUpButtonClicked(self):            
        self.currentRow = self.listWidget.currentRow()
        if self.currentRow == -1:
            self.showdialog("Select an item to move") 
            return 
        else:             
            if self.currentRow == 0:
                return
            else:
                self.currentItem = self.listWidget.takeItem(self.currentRow)
                self.listWidget.insertItem(self.currentRow - 1, self.currentItem) 
                self.currentRow = self.currentRow - 1
                self.listWidget.setCurrentRow(self.currentRow)
        
    def moveDownButtonClicked(self):            
        self.currentRow = self.listWidget.currentRow()
        
        if self.currentRow == -1:
            self.showdialog("Select an item to move") 
            return
        else:      
            if self.currentRow == len(self.listWidget) - 1:
                return
            else:
                self.currentItem = self.listWidget.takeItem(self.currentRow)
                self.listWidget.insertItem(self.currentRow + 1, self.currentItem) 
                self.currentRow = self.currentRow + 1
                self.listWidget.setCurrentRow(self.currentRow)
            
    def deleteButtonClicked(self): 
        self.currentRow = self.listWidget.currentRow()
        self.listWidget.takeItem(self.currentRow)

    def outDirButtonClicked(self):
        self.outputfolder = QFileDialog.getExistingDirectory()
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit.setText(_translate("PDFMerger", self.outputfolder))     

    def mergeButtonClicked(self):
        _translate = QtCore.QCoreApplication.translate
        if self.lineEdit.text() == "":   
            self.showdialog("Select the output directory") 

        else:
            if self.outputFile.text() == "":
                self.showdialog("Enter the output filename") 
            else:
                try:
                    if len(self.listWidget) == 0:
                        self.showdialog("Add the pdfs to merge") 
                    merger = PdfFileMerger()
                    readedFileList = [self.listWidget.item(i).text() for i in range(self.listWidget.count())]
                    for pdf in readedFileList:      
                        merger.append(pdf)
                    mergedfile = str(self.outputfolder)+"/"+str(self.outputFile.text())+".pdf"
                    merger.write(mergedfile)
                    #TODO: Ask for overwrite if file already exists
                    merger.close()
                    self.label.setText(_translate("PDFMerger", "Merged successfully!"))
                    self.label.setStyleSheet("color: green") 
                except Exception as e:
                    print(e)
     
    def showdialog(self,displaytext):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Warning")
        msg.setWindowIcon(QIcon('warning.png')) 
        msg.setText(displaytext)        
        msg.setStandardButtons(QMessageBox.Ok)
        # msg.buttonClicked.connect(msgbtn)            
        retval = msg.exec_()
        # print "value of pressed message box button:", retval   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PDFMerger = QtWidgets.QMainWindow()
    ui = Ui_PDFMerger()
    ui.setupUi(PDFMerger)
    PDFMerger.show()
    sys.exit(app.exec_())
