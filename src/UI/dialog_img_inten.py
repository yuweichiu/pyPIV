# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_img_inten.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_img_inten(object):
    def setupUi(self, Dialog_img_inten):
        Dialog_img_inten.setObjectName("Dialog_img_inten")
        Dialog_img_inten.resize(731, 860)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog_img_inten)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 711, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_left = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_left.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_left.setObjectName("verticalLayout_left")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog_img_inten)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 430, 711, 421))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_right = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_right.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_right.setObjectName("verticalLayout_right")

        self.retranslateUi(Dialog_img_inten)
        QtCore.QMetaObject.connectSlotsByName(Dialog_img_inten)

    def retranslateUi(self, Dialog_img_inten):
        _translate = QtCore.QCoreApplication.translate
        Dialog_img_inten.setWindowTitle(_translate("Dialog_img_inten", "Image Intensity Threshold"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_img_inten = QtWidgets.QDialog()
    ui = Ui_Dialog_img_inten()
    ui.setupUi(Dialog_img_inten)
    Dialog_img_inten.show()
    sys.exit(app.exec_())

