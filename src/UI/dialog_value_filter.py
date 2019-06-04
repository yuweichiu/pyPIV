# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_value_filter.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_value_filter(object):
    def setupUi(self, Dialog_value_filter):
        Dialog_value_filter.setObjectName("Dialog_value_filter")
        Dialog_value_filter.resize(800, 600)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog_value_filter)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.retranslateUi(Dialog_value_filter)
        QtCore.QMetaObject.connectSlotsByName(Dialog_value_filter)

    def retranslateUi(self, Dialog_value_filter):
        _translate = QtCore.QCoreApplication.translate
        Dialog_value_filter.setWindowTitle(_translate("Dialog_value_filter", "Value Filter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_value_filter = QtWidgets.QDialog()
    ui = Ui_Dialog_value_filter()
    ui.setupUi(Dialog_value_filter)
    Dialog_value_filter.show()
    sys.exit(app.exec_())

