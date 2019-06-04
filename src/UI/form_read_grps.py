# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_read_grps.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_read_csv(object):
    def setupUi(self, Form_read_csv):
        Form_read_csv.setObjectName("Form_read_csv")
        Form_read_csv.resize(1108, 792)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        Form_read_csv.setFont(font)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form_read_csv)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_load_grp_img = QtWidgets.QPushButton(Form_read_csv)
        self.pushButton_load_grp_img.setMinimumSize(QtCore.QSize(140, 50))
        self.pushButton_load_grp_img.setObjectName("pushButton_load_grp_img")
        self.gridLayout_2.addWidget(self.pushButton_load_grp_img, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 177, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 2, 1)
        self.tableWidget_grp = QtWidgets.QTableWidget(Form_read_csv)
        self.tableWidget_grp.setMinimumSize(QtCore.QSize(820, 180))
        self.tableWidget_grp.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_grp.setColumnCount(4)
        self.tableWidget_grp.setObjectName("tableWidget_grp")
        self.tableWidget_grp.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_grp.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_grp.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_grp.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_grp.setHorizontalHeaderItem(3, item)
        self.tableWidget_grp.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_grp.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_grp.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_grp.horizontalHeader().setStretchLastSection(False)
        self.gridLayout_2.addWidget(self.tableWidget_grp, 0, 2, 2, 1)
        self.pushButton_load_grp = QtWidgets.QPushButton(Form_read_csv)
        self.pushButton_load_grp.setMinimumSize(QtCore.QSize(140, 50))
        self.pushButton_load_grp.setObjectName("pushButton_load_grp")
        self.gridLayout_2.addWidget(self.pushButton_load_grp, 1, 0, 1, 1)
        self.groupBox_fig = QtWidgets.QGroupBox(Form_read_csv)
        self.groupBox_fig.setMinimumSize(QtCore.QSize(1080, 580))
        self.groupBox_fig.setObjectName("groupBox_fig")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_fig)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.groupBox_fig)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_fig, 2, 0, 1, 3)

        self.retranslateUi(Form_read_csv)
        QtCore.QMetaObject.connectSlotsByName(Form_read_csv)

    def retranslateUi(self, Form_read_csv):
        _translate = QtCore.QCoreApplication.translate
        Form_read_csv.setWindowTitle(_translate("Form_read_csv", "Read CSV"))
        self.pushButton_load_grp_img.setText(_translate("Form_read_csv", "Load GRPs image"))
        item = self.tableWidget_grp.horizontalHeaderItem(0)
        item.setText(_translate("Form_read_csv", "x (m)"))
        item = self.tableWidget_grp.horizontalHeaderItem(1)
        item.setText(_translate("Form_read_csv", "y (m)"))
        item = self.tableWidget_grp.horizontalHeaderItem(2)
        item.setText(_translate("Form_read_csv", "j (pix)"))
        item = self.tableWidget_grp.horizontalHeaderItem(3)
        item.setText(_translate("Form_read_csv", "i (pix)"))
        self.pushButton_load_grp.setText(_translate("Form_read_csv", "Load csv file"))
        self.groupBox_fig.setTitle(_translate("Form_read_csv", "Figure"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_read_csv = QtWidgets.QWidget()
    ui = Ui_Form_read_csv()
    ui.setupUi(Form_read_csv)
    Form_read_csv.show()
    sys.exit(app.exec_())

