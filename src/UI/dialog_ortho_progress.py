# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_ortho_progress.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_ortho_progress(object):
    def setupUi(self, Dialog_ortho_progress):
        Dialog_ortho_progress.setObjectName("Dialog_ortho_progress")
        Dialog_ortho_progress.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_ortho_progress.setEnabled(True)
        Dialog_ortho_progress.resize(362, 127)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_ortho_progress.sizePolicy().hasHeightForWidth())
        Dialog_ortho_progress.setSizePolicy(sizePolicy)
        Dialog_ortho_progress.setMinimumSize(QtCore.QSize(362, 127))
        Dialog_ortho_progress.setMaximumSize(QtCore.QSize(362, 127))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        Dialog_ortho_progress.setFont(font)
        self.progressBar = QtWidgets.QProgressBar(Dialog_ortho_progress)
        self.progressBar.setGeometry(QtCore.QRect(20, 50, 331, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_process = QtWidgets.QLabel(Dialog_ortho_progress)
        self.label_process.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label_process.setObjectName("label_process")
        self.label_imgname = QtWidgets.QLabel(Dialog_ortho_progress)
        self.label_imgname.setGeometry(QtCore.QRect(110, 20, 181, 16))
        self.label_imgname.setText("")
        self.label_imgname.setObjectName("label_imgname")
        self.pushButton = QtWidgets.QPushButton(Dialog_ortho_progress)
        self.pushButton.setGeometry(QtCore.QRect(240, 90, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog_ortho_progress)
        QtCore.QMetaObject.connectSlotsByName(Dialog_ortho_progress)

    def retranslateUi(self, Dialog_ortho_progress):
        _translate = QtCore.QCoreApplication.translate
        Dialog_ortho_progress.setWindowTitle(_translate("Dialog_ortho_progress", "Status"))
        self.label_process.setText(_translate("Dialog_ortho_progress", "Processing on: "))
        self.pushButton.setText(_translate("Dialog_ortho_progress", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_ortho_progress = QtWidgets.QDialog()
    ui = Ui_Dialog_ortho_progress()
    ui.setupUi(Dialog_ortho_progress)
    Dialog_ortho_progress.show()
    sys.exit(app.exec_())

