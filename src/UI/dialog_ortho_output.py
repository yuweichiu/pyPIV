# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_ortho_output.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_ortho_output(object):
    def setupUi(self, Dialog_ortho_output):
        Dialog_ortho_output.setObjectName("Dialog_ortho_output")
        Dialog_ortho_output.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_ortho_output.resize(359, 402)
        Dialog_ortho_output.setMinimumSize(QtCore.QSize(359, 345))
        Dialog_ortho_output.setMaximumSize(QtCore.QSize(359, 999))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        Dialog_ortho_output.setFont(font)
        self.pushButton_run = QtWidgets.QPushButton(Dialog_ortho_output)
        self.pushButton_run.setGeometry(QtCore.QRect(243, 280, 100, 45))
        self.pushButton_run.setMinimumSize(QtCore.QSize(100, 45))
        self.pushButton_run.setMaximumSize(QtCore.QSize(100, 45))
        self.pushButton_run.setObjectName("pushButton_run")
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog_ortho_output)
        self.pushButton_cancel.setGeometry(QtCore.QRect(243, 340, 100, 45))
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(100, 45))
        self.pushButton_cancel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.groupBox = QtWidgets.QGroupBox(Dialog_ortho_output)
        self.groupBox.setGeometry(QtCore.QRect(13, 130, 220, 258))
        self.groupBox.setMinimumSize(QtCore.QSize(220, 258))
        self.groupBox.setMaximumSize(QtCore.QSize(220, 258))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_all_seq = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_all_seq.setChecked(True)
        self.radioButton_all_seq.setObjectName("radioButton_all_seq")
        self.verticalLayout.addWidget(self.radioButton_all_seq)
        self.radioButton_specify = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_specify.setObjectName("radioButton_specify")
        self.verticalLayout.addWidget(self.radioButton_specify)
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setMinimumSize(QtCore.QSize(200, 170))
        self.listWidget.setMaximumSize(QtCore.QSize(200, 170))
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog_ortho_output)
        self.groupBox_2.setGeometry(QtCore.QRect(243, 130, 100, 140))
        self.groupBox_2.setMinimumSize(QtCore.QSize(100, 140))
        self.groupBox_2.setMaximumSize(QtCore.QSize(100, 140))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_bmp = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_bmp.setChecked(True)
        self.radioButton_bmp.setObjectName("radioButton_bmp")
        self.verticalLayout_2.addWidget(self.radioButton_bmp)
        self.radioButton_png = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_png.setObjectName("radioButton_png")
        self.verticalLayout_2.addWidget(self.radioButton_png)
        self.radioButton_tif = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_tif.setCheckable(False)
        self.radioButton_tif.setObjectName("radioButton_tif")
        self.verticalLayout_2.addWidget(self.radioButton_tif)
        self.radioButton_jpeg = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_jpeg.setObjectName("radioButton_jpeg")
        self.verticalLayout_2.addWidget(self.radioButton_jpeg)
        self.label_outdir = QtWidgets.QLabel(Dialog_ortho_output)
        self.label_outdir.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.label_outdir.setObjectName("label_outdir")
        self.lineEdit_out_dir = QtWidgets.QLineEdit(Dialog_ortho_output)
        self.lineEdit_out_dir.setGeometry(QtCore.QRect(20, 40, 280, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_out_dir.sizePolicy().hasHeightForWidth())
        self.lineEdit_out_dir.setSizePolicy(sizePolicy)
        self.lineEdit_out_dir.setMinimumSize(QtCore.QSize(280, 20))
        self.lineEdit_out_dir.setMaximumSize(QtCore.QSize(280, 20))
        self.lineEdit_out_dir.setReadOnly(True)
        self.lineEdit_out_dir.setObjectName("lineEdit_out_dir")
        self.pushButton_browse = QtWidgets.QPushButton(Dialog_ortho_output)
        self.pushButton_browse.setGeometry(QtCore.QRect(314, 40, 30, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_browse.sizePolicy().hasHeightForWidth())
        self.pushButton_browse.setSizePolicy(sizePolicy)
        self.pushButton_browse.setMinimumSize(QtCore.QSize(30, 23))
        self.pushButton_browse.setMaximumSize(QtCore.QSize(30, 23))
        self.pushButton_browse.setObjectName("pushButton_browse")
        self.label_outdir_2 = QtWidgets.QLabel(Dialog_ortho_output)
        self.label_outdir_2.setGeometry(QtCore.QRect(20, 70, 161, 16))
        self.label_outdir_2.setObjectName("label_outdir_2")
        self.pushButton_browse_2 = QtWidgets.QPushButton(Dialog_ortho_output)
        self.pushButton_browse_2.setGeometry(QtCore.QRect(314, 90, 30, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_browse_2.sizePolicy().hasHeightForWidth())
        self.pushButton_browse_2.setSizePolicy(sizePolicy)
        self.pushButton_browse_2.setMinimumSize(QtCore.QSize(30, 23))
        self.pushButton_browse_2.setMaximumSize(QtCore.QSize(30, 23))
        self.pushButton_browse_2.setObjectName("pushButton_browse_2")
        self.lineEdit_out_dir_2 = QtWidgets.QLineEdit(Dialog_ortho_output)
        self.lineEdit_out_dir_2.setGeometry(QtCore.QRect(20, 90, 280, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_out_dir_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_out_dir_2.setSizePolicy(sizePolicy)
        self.lineEdit_out_dir_2.setMinimumSize(QtCore.QSize(280, 20))
        self.lineEdit_out_dir_2.setMaximumSize(QtCore.QSize(280, 20))
        self.lineEdit_out_dir_2.setReadOnly(True)
        self.lineEdit_out_dir_2.setObjectName("lineEdit_out_dir_2")

        self.retranslateUi(Dialog_ortho_output)
        QtCore.QMetaObject.connectSlotsByName(Dialog_ortho_output)
        Dialog_ortho_output.setTabOrder(self.lineEdit_out_dir, self.pushButton_browse)
        Dialog_ortho_output.setTabOrder(self.pushButton_browse, self.radioButton_all_seq)
        Dialog_ortho_output.setTabOrder(self.radioButton_all_seq, self.radioButton_specify)
        Dialog_ortho_output.setTabOrder(self.radioButton_specify, self.listWidget)
        Dialog_ortho_output.setTabOrder(self.listWidget, self.radioButton_bmp)
        Dialog_ortho_output.setTabOrder(self.radioButton_bmp, self.radioButton_png)
        Dialog_ortho_output.setTabOrder(self.radioButton_png, self.radioButton_tif)
        Dialog_ortho_output.setTabOrder(self.radioButton_tif, self.radioButton_jpeg)
        Dialog_ortho_output.setTabOrder(self.radioButton_jpeg, self.pushButton_run)
        Dialog_ortho_output.setTabOrder(self.pushButton_run, self.pushButton_cancel)

    def retranslateUi(self, Dialog_ortho_output):
        _translate = QtCore.QCoreApplication.translate
        Dialog_ortho_output.setWindowTitle(_translate("Dialog_ortho_output", "Export Options"))
        self.pushButton_run.setText(_translate("Dialog_ortho_output", "Run"))
        self.pushButton_cancel.setText(_translate("Dialog_ortho_output", "Cancel"))
        self.groupBox.setTitle(_translate("Dialog_ortho_output", "Select Images to process"))
        self.radioButton_all_seq.setText(_translate("Dialog_ortho_output", "All sequence"))
        self.radioButton_specify.setText(_translate("Dialog_ortho_output", "Specify"))
        self.groupBox_2.setTitle(_translate("Dialog_ortho_output", "Output Type"))
        self.radioButton_bmp.setText(_translate("Dialog_ortho_output", "BMP"))
        self.radioButton_png.setText(_translate("Dialog_ortho_output", "PNG"))
        self.radioButton_tif.setText(_translate("Dialog_ortho_output", "TIF"))
        self.radioButton_jpeg.setText(_translate("Dialog_ortho_output", "JPEG"))
        self.label_outdir.setText(_translate("Dialog_ortho_output", "Images Output Directory"))
        self.pushButton_browse.setText(_translate("Dialog_ortho_output", "..."))
        self.label_outdir_2.setText(_translate("Dialog_ortho_output", "Image Reference Directory"))
        self.pushButton_browse_2.setText(_translate("Dialog_ortho_output", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_ortho_output = QtWidgets.QDialog()
    ui = Ui_Dialog_ortho_output()
    ui.setupUi(Dialog_ortho_output)
    Dialog_ortho_output.show()
    sys.exit(app.exec_())

