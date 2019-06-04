# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_piv_progress.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_piv_progress(object):
    def setupUi(self, Dialog_piv_progress):
        Dialog_piv_progress.setObjectName("Dialog_piv_progress")
        Dialog_piv_progress.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_piv_progress.resize(474, 129)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        Dialog_piv_progress.setFont(font)
        self.pushButton = QtWidgets.QPushButton(Dialog_piv_progress)
        self.pushButton.setGeometry(QtCore.QRect(370, 90, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.label_process = QtWidgets.QLabel(Dialog_piv_progress)
        self.label_process.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label_process.setObjectName("label_process")
        self.label_imgname = QtWidgets.QLabel(Dialog_piv_progress)
        self.label_imgname.setGeometry(QtCore.QRect(110, 20, 351, 16))
        self.label_imgname.setText("")
        self.label_imgname.setObjectName("label_imgname")
        self.progressBar = QtWidgets.QProgressBar(Dialog_piv_progress)
        self.progressBar.setGeometry(QtCore.QRect(20, 50, 441, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Dialog_piv_progress)
        QtCore.QMetaObject.connectSlotsByName(Dialog_piv_progress)

    def retranslateUi(self, Dialog_piv_progress):
        _translate = QtCore.QCoreApplication.translate
        Dialog_piv_progress.setWindowTitle(_translate("Dialog_piv_progress", "Status"))
        self.pushButton.setText(_translate("Dialog_piv_progress", "Cancel"))
        self.label_process.setText(_translate("Dialog_piv_progress", "Processing on: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_piv_progress = QtWidgets.QDialog()
    ui = Ui_Dialog_piv_progress()
    ui.setupUi(Dialog_piv_progress)
    Dialog_piv_progress.show()
    sys.exit(app.exec_())

