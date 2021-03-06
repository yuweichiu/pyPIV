# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_piv_cnn.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_piv_cnn(object):
    def setupUi(self, Form_piv_cnn):
        Form_piv_cnn.setObjectName("Form_piv_cnn")
        Form_piv_cnn.resize(1401, 914)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        Form_piv_cnn.setFont(font)
        self.gridLayout_9 = QtWidgets.QGridLayout(Form_piv_cnn)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox_4 = QtWidgets.QGroupBox(Form_piv_cnn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(430, 90))
        self.groupBox_4.setMaximumSize(QtCore.QSize(9999, 90))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_roi_y = QtWidgets.QLabel(self.groupBox_4)
        self.label_roi_y.setObjectName("label_roi_y")
        self.gridLayout_2.addWidget(self.label_roi_y, 0, 1, 1, 1)
        self.label_roi_width = QtWidgets.QLabel(self.groupBox_4)
        self.label_roi_width.setObjectName("label_roi_width")
        self.gridLayout_2.addWidget(self.label_roi_width, 0, 2, 1, 1)
        self.lineEdit_roi_y = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_roi_y.setObjectName("lineEdit_roi_y")
        self.gridLayout_2.addWidget(self.lineEdit_roi_y, 1, 1, 1, 1)
        self.lineEdit_roi_height = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_roi_height.setObjectName("lineEdit_roi_height")
        self.gridLayout_2.addWidget(self.lineEdit_roi_height, 1, 3, 1, 1)
        self.lineEdit_roi_width = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_roi_width.setObjectName("lineEdit_roi_width")
        self.gridLayout_2.addWidget(self.lineEdit_roi_width, 1, 2, 1, 1)
        self.pushButton_draw_roi = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_draw_roi.setObjectName("pushButton_draw_roi")
        self.gridLayout_2.addWidget(self.pushButton_draw_roi, 0, 4, 1, 1)
        self.label_roi_height = QtWidgets.QLabel(self.groupBox_4)
        self.label_roi_height.setObjectName("label_roi_height")
        self.gridLayout_2.addWidget(self.label_roi_height, 0, 3, 1, 1)
        self.lineEdit_roi_x = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_roi_x.setObjectName("lineEdit_roi_x")
        self.gridLayout_2.addWidget(self.lineEdit_roi_x, 1, 0, 1, 1)
        self.pushButton_reset_roi = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_reset_roi.setObjectName("pushButton_reset_roi")
        self.gridLayout_2.addWidget(self.pushButton_reset_roi, 1, 4, 1, 1)
        self.label_roi_x = QtWidgets.QLabel(self.groupBox_4)
        self.label_roi_x.setObjectName("label_roi_x")
        self.gridLayout_2.addWidget(self.label_roi_x, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_4, 0, 2, 2, 1)
        self.groupBox = QtWidgets.QGroupBox(Form_piv_cnn)
        self.groupBox.setMinimumSize(QtCore.QSize(240, 90))
        self.groupBox.setMaximumSize(QtCore.QSize(240, 90))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_Step_x = QtWidgets.QLabel(self.groupBox)
        self.label_Step_x.setObjectName("label_Step_x")
        self.horizontalLayout_2.addWidget(self.label_Step_x)
        self.spinBox_step_x = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_step_x.setMinimum(1)
        self.spinBox_step_x.setMaximum(999)
        self.spinBox_step_x.setProperty("value", 32)
        self.spinBox_step_x.setObjectName("spinBox_step_x")
        self.horizontalLayout_2.addWidget(self.spinBox_step_x)
        spacerItem = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_Step_y = QtWidgets.QLabel(self.groupBox)
        self.label_Step_y.setObjectName("label_Step_y")
        self.horizontalLayout_2.addWidget(self.label_Step_y)
        self.spinBox_step_y = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_step_y.setMinimum(1)
        self.spinBox_step_y.setMaximum(999)
        self.spinBox_step_y.setProperty("value", 32)
        self.spinBox_step_y.setObjectName("spinBox_step_y")
        self.horizontalLayout_2.addWidget(self.spinBox_step_y)
        self.gridLayout_9.addWidget(self.groupBox, 0, 4, 2, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Form_piv_cnn)
        self.groupBox_3.setMinimumSize(QtCore.QSize(290, 180))
        self.groupBox_3.setMaximumSize(QtCore.QSize(400, 180))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.groupBox_3)
        self.scrollArea_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 280, 149))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_maxloop = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_maxloop.setObjectName("label_maxloop")
        self.gridLayout_7.addWidget(self.label_maxloop, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(72, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 0, 1, 1, 1)
        self.spinBox_maxloop = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_maxloop.setMinimum(100)
        self.spinBox_maxloop.setMaximum(1000000)
        self.spinBox_maxloop.setSingleStep(100)
        self.spinBox_maxloop.setProperty("value", 3000)
        self.spinBox_maxloop.setObjectName("spinBox_maxloop")
        self.gridLayout_7.addWidget(self.spinBox_maxloop, 0, 2, 1, 1)
        self.label_bt_size = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_bt_size.setObjectName("label_bt_size")
        self.gridLayout_7.addWidget(self.label_bt_size, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(72, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 1, 1, 1, 1)
        self.spinBox_bt_size = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_bt_size.setMinimum(1)
        self.spinBox_bt_size.setMaximum(10000)
        self.spinBox_bt_size.setSingleStep(5)
        self.spinBox_bt_size.setProperty("value", 20)
        self.spinBox_bt_size.setObjectName("spinBox_bt_size")
        self.gridLayout_7.addWidget(self.spinBox_bt_size, 1, 2, 1, 1)
        self.label_loss_thresh = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_loss_thresh.setObjectName("label_loss_thresh")
        self.gridLayout_7.addWidget(self.label_loss_thresh, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(72, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem3, 2, 1, 1, 1)
        self.doubleSpinBox_loss_thresh = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents_6)
        self.doubleSpinBox_loss_thresh.setDecimals(6)
        self.doubleSpinBox_loss_thresh.setMaximum(1.0)
        self.doubleSpinBox_loss_thresh.setSingleStep(0.0001)
        self.doubleSpinBox_loss_thresh.setProperty("value", 0.001)
        self.doubleSpinBox_loss_thresh.setObjectName("doubleSpinBox_loss_thresh")
        self.gridLayout_7.addWidget(self.doubleSpinBox_loss_thresh, 2, 2, 1, 1)
        self.label_lr = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_lr.setObjectName("label_lr")
        self.gridLayout_7.addWidget(self.label_lr, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(72, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem4, 3, 1, 1, 1)
        self.doubleSpinBox_lr = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents_6)
        self.doubleSpinBox_lr.setDecimals(6)
        self.doubleSpinBox_lr.setMaximum(1.0)
        self.doubleSpinBox_lr.setSingleStep(0.0001)
        self.doubleSpinBox_lr.setProperty("value", 0.0001)
        self.doubleSpinBox_lr.setObjectName("doubleSpinBox_lr")
        self.gridLayout_7.addWidget(self.doubleSpinBox_lr, 3, 2, 1, 1)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_5.addWidget(self.scrollArea_5, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_3, 4, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form_piv_cnn)
        self.groupBox_2.setMinimumSize(QtCore.QSize(290, 360))
        self.groupBox_2.setMaximumSize(QtCore.QSize(400, 360))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_IA = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.label_IA.setFont(font)
        self.label_IA.setObjectName("label_IA")
        self.gridLayout_3.addWidget(self.label_IA, 0, 0, 1, 5)
        self.label_ia_w = QtWidgets.QLabel(self.groupBox_2)
        self.label_ia_w.setObjectName("label_ia_w")
        self.gridLayout_3.addWidget(self.label_ia_w, 1, 0, 1, 1)
        self.spinBox_ia_w = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_ia_w.setMinimum(4)
        self.spinBox_ia_w.setMaximum(512)
        self.spinBox_ia_w.setSingleStep(8)
        self.spinBox_ia_w.setProperty("value", 64)
        self.spinBox_ia_w.setObjectName("spinBox_ia_w")
        self.gridLayout_3.addWidget(self.spinBox_ia_w, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 1, 2, 1, 1)
        self.label_ia_h = QtWidgets.QLabel(self.groupBox_2)
        self.label_ia_h.setObjectName("label_ia_h")
        self.gridLayout_3.addWidget(self.label_ia_h, 1, 3, 1, 1)
        self.spinBox_ia_h = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_ia_h.setMinimum(4)
        self.spinBox_ia_h.setMaximum(512)
        self.spinBox_ia_h.setSingleStep(8)
        self.spinBox_ia_h.setProperty("value", 64)
        self.spinBox_ia_h.setObjectName("spinBox_ia_h")
        self.gridLayout_3.addWidget(self.spinBox_ia_h, 1, 4, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.line_6 = QtWidgets.QFrame(self.groupBox_2)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_4.addWidget(self.line_6)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_SA = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.label_SA.setFont(font)
        self.label_SA.setObjectName("label_SA")
        self.gridLayout.addWidget(self.label_SA, 0, 0, 1, 4)
        self.label_SA_n = QtWidgets.QLabel(self.groupBox_2)
        self.label_SA_n.setObjectName("label_SA_n")
        self.gridLayout.addWidget(self.label_SA_n, 1, 0, 1, 1)
        self.label_SA_s = QtWidgets.QLabel(self.groupBox_2)
        self.label_SA_s.setObjectName("label_SA_s")
        self.gridLayout.addWidget(self.label_SA_s, 1, 1, 1, 1)
        self.label_SA_e = QtWidgets.QLabel(self.groupBox_2)
        self.label_SA_e.setObjectName("label_SA_e")
        self.gridLayout.addWidget(self.label_SA_e, 1, 2, 1, 1)
        self.label_SA_w = QtWidgets.QLabel(self.groupBox_2)
        self.label_SA_w.setObjectName("label_SA_w")
        self.gridLayout.addWidget(self.label_SA_w, 1, 3, 1, 1)
        self.spinBox_sa_n = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_sa_n.setProperty("value", 10)
        self.spinBox_sa_n.setObjectName("spinBox_sa_n")
        self.gridLayout.addWidget(self.spinBox_sa_n, 2, 0, 1, 1)
        self.spinBox_sa_s = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_sa_s.setProperty("value", 10)
        self.spinBox_sa_s.setObjectName("spinBox_sa_s")
        self.gridLayout.addWidget(self.spinBox_sa_s, 2, 1, 1, 1)
        self.spinBox_sa_e = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_sa_e.setProperty("value", 10)
        self.spinBox_sa_e.setObjectName("spinBox_sa_e")
        self.gridLayout.addWidget(self.spinBox_sa_e, 2, 2, 1, 1)
        self.spinBox_sa_w = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_sa_w.setProperty("value", 10)
        self.spinBox_sa_w.setObjectName("spinBox_sa_w")
        self.gridLayout.addWidget(self.spinBox_sa_w, 2, 3, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.line_3 = QtWidgets.QFrame(self.groupBox_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_pixdiam = QtWidgets.QLabel(self.groupBox_2)
        self.label_pixdiam.setObjectName("label_pixdiam")
        self.gridLayout_6.addWidget(self.label_pixdiam, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem6, 1, 1, 1, 1)
        self.spinBox_pixdiam = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_pixdiam.setMinimum(1)
        self.spinBox_pixdiam.setProperty("value", 3)
        self.spinBox_pixdiam.setObjectName("spinBox_pixdiam")
        self.gridLayout_6.addWidget(self.spinBox_pixdiam, 1, 2, 1, 1)
        self.label_inte_thresh = QtWidgets.QLabel(self.groupBox_2)
        self.label_inte_thresh.setObjectName("label_inte_thresh")
        self.gridLayout_6.addWidget(self.label_inte_thresh, 2, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem7, 2, 1, 1, 1)
        self.doubleSpinBox_inten_thresh = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_inten_thresh.setDecimals(5)
        self.doubleSpinBox_inten_thresh.setMinimum(1e-05)
        self.doubleSpinBox_inten_thresh.setSingleStep(0.01)
        self.doubleSpinBox_inten_thresh.setProperty("value", 0.5)
        self.doubleSpinBox_inten_thresh.setObjectName("doubleSpinBox_inten_thresh")
        self.gridLayout_6.addWidget(self.doubleSpinBox_inten_thresh, 2, 2, 1, 1)
        self.pushButton_check = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_check.setObjectName("pushButton_check")
        self.gridLayout_6.addWidget(self.pushButton_check, 3, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_6)
        self.line_5 = QtWidgets.QFrame(self.groupBox_2)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_4.addWidget(self.line_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_tinv = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.label_tinv.setFont(font)
        self.label_tinv.setObjectName("label_tinv")
        self.horizontalLayout.addWidget(self.label_tinv)
        spacerItem8 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.doubleSpinBox_tinv = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_tinv.setDecimals(5)
        self.doubleSpinBox_tinv.setSingleStep(0.0001)
        self.doubleSpinBox_tinv.setProperty("value", 1.0)
        self.doubleSpinBox_tinv.setObjectName("doubleSpinBox_tinv")
        self.horizontalLayout.addWidget(self.doubleSpinBox_tinv)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem9 = QtWidgets.QSpacerItem(289, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem9)
        self.gridLayout_9.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(Form_piv_cnn)
        self.groupBox_5.setMinimumSize(QtCore.QSize(880, 730))
        self.groupBox_5.setMaximumSize(QtCore.QSize(999999, 999999))
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame = QtWidgets.QFrame(self.groupBox_5)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.gridLayout_8.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_5, 2, 2, 3, 6)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(Form_piv_cnn)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_img_dir = QtWidgets.QLineEdit(Form_piv_cnn)
        self.lineEdit_img_dir.setMinimumSize(QtCore.QSize(230, 20))
        self.lineEdit_img_dir.setMaximumSize(QtCore.QSize(350, 20))
        self.lineEdit_img_dir.setObjectName("lineEdit_img_dir")
        self.gridLayout_4.addWidget(self.lineEdit_img_dir, 1, 0, 1, 1)
        self.pushButton_browse = QtWidgets.QPushButton(Form_piv_cnn)
        self.pushButton_browse.setMinimumSize(QtCore.QSize(35, 20))
        self.pushButton_browse.setMaximumSize(QtCore.QSize(35, 20))
        self.pushButton_browse.setObjectName("pushButton_browse")
        self.gridLayout_4.addWidget(self.pushButton_browse, 1, 1, 1, 1)
        self.listWidget_img = QtWidgets.QListWidget(Form_piv_cnn)
        self.listWidget_img.setMinimumSize(QtCore.QSize(290, 230))
        self.listWidget_img.setMaximumSize(QtCore.QSize(400, 99999))
        self.listWidget_img.setObjectName("listWidget_img")
        self.gridLayout_4.addWidget(self.listWidget_img, 2, 0, 1, 2)
        self.gridLayout_9.addLayout(self.gridLayout_4, 0, 0, 3, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 833, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem10, 0, 1, 5, 1)
        self.pushButton_reset_mask = QtWidgets.QPushButton(Form_piv_cnn)
        self.pushButton_reset_mask.setMinimumSize(QtCore.QSize(90, 40))
        self.pushButton_reset_mask.setMaximumSize(QtCore.QSize(90, 40))
        self.pushButton_reset_mask.setObjectName("pushButton_reset_mask")
        self.gridLayout_9.addWidget(self.pushButton_reset_mask, 0, 7, 1, 1)
        self.pushButton_run = QtWidgets.QPushButton(Form_piv_cnn)
        self.pushButton_run.setMinimumSize(QtCore.QSize(190, 40))
        self.pushButton_run.setMaximumSize(QtCore.QSize(190, 40))
        self.pushButton_run.setObjectName("pushButton_run")
        self.gridLayout_9.addWidget(self.pushButton_run, 1, 6, 1, 2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 87, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem11, 0, 3, 2, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 87, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem12, 0, 5, 2, 1)
        self.pushButton_mask = QtWidgets.QPushButton(Form_piv_cnn)
        self.pushButton_mask.setMinimumSize(QtCore.QSize(90, 40))
        self.pushButton_mask.setMaximumSize(QtCore.QSize(90, 40))
        self.pushButton_mask.setObjectName("pushButton_mask")
        self.gridLayout_9.addWidget(self.pushButton_mask, 0, 6, 1, 1)

        self.retranslateUi(Form_piv_cnn)
        QtCore.QMetaObject.connectSlotsByName(Form_piv_cnn)
        Form_piv_cnn.setTabOrder(self.lineEdit_img_dir, self.pushButton_browse)
        Form_piv_cnn.setTabOrder(self.pushButton_browse, self.listWidget_img)
        Form_piv_cnn.setTabOrder(self.listWidget_img, self.spinBox_ia_w)
        Form_piv_cnn.setTabOrder(self.spinBox_ia_w, self.spinBox_ia_h)
        Form_piv_cnn.setTabOrder(self.spinBox_ia_h, self.spinBox_sa_n)
        Form_piv_cnn.setTabOrder(self.spinBox_sa_n, self.spinBox_sa_s)
        Form_piv_cnn.setTabOrder(self.spinBox_sa_s, self.spinBox_sa_e)
        Form_piv_cnn.setTabOrder(self.spinBox_sa_e, self.spinBox_sa_w)
        Form_piv_cnn.setTabOrder(self.spinBox_sa_w, self.spinBox_pixdiam)
        Form_piv_cnn.setTabOrder(self.spinBox_pixdiam, self.doubleSpinBox_inten_thresh)
        Form_piv_cnn.setTabOrder(self.doubleSpinBox_inten_thresh, self.pushButton_check)
        Form_piv_cnn.setTabOrder(self.pushButton_check, self.doubleSpinBox_tinv)
        Form_piv_cnn.setTabOrder(self.doubleSpinBox_tinv, self.scrollArea_5)
        Form_piv_cnn.setTabOrder(self.scrollArea_5, self.spinBox_maxloop)
        Form_piv_cnn.setTabOrder(self.spinBox_maxloop, self.spinBox_bt_size)
        Form_piv_cnn.setTabOrder(self.spinBox_bt_size, self.doubleSpinBox_loss_thresh)
        Form_piv_cnn.setTabOrder(self.doubleSpinBox_loss_thresh, self.doubleSpinBox_lr)
        Form_piv_cnn.setTabOrder(self.doubleSpinBox_lr, self.lineEdit_roi_x)
        Form_piv_cnn.setTabOrder(self.lineEdit_roi_x, self.lineEdit_roi_y)
        Form_piv_cnn.setTabOrder(self.lineEdit_roi_y, self.lineEdit_roi_width)
        Form_piv_cnn.setTabOrder(self.lineEdit_roi_width, self.lineEdit_roi_height)
        Form_piv_cnn.setTabOrder(self.lineEdit_roi_height, self.pushButton_draw_roi)
        Form_piv_cnn.setTabOrder(self.pushButton_draw_roi, self.pushButton_reset_roi)
        Form_piv_cnn.setTabOrder(self.pushButton_reset_roi, self.spinBox_step_x)
        Form_piv_cnn.setTabOrder(self.spinBox_step_x, self.spinBox_step_y)
        Form_piv_cnn.setTabOrder(self.spinBox_step_y, self.pushButton_mask)
        Form_piv_cnn.setTabOrder(self.pushButton_mask, self.pushButton_reset_mask)
        Form_piv_cnn.setTabOrder(self.pushButton_reset_mask, self.pushButton_run)

    def retranslateUi(self, Form_piv_cnn):
        _translate = QtCore.QCoreApplication.translate
        Form_piv_cnn.setWindowTitle(_translate("Form_piv_cnn", "Form"))
        self.groupBox_4.setTitle(_translate("Form_piv_cnn", "ROI"))
        self.label_roi_y.setText(_translate("Form_piv_cnn", "y"))
        self.label_roi_width.setText(_translate("Form_piv_cnn", "width"))
        self.pushButton_draw_roi.setText(_translate("Form_piv_cnn", "Draw"))
        self.label_roi_height.setText(_translate("Form_piv_cnn", "height"))
        self.pushButton_reset_roi.setText(_translate("Form_piv_cnn", "Reset"))
        self.label_roi_x.setText(_translate("Form_piv_cnn", "x"))
        self.groupBox.setTitle(_translate("Form_piv_cnn", "Grid Step"))
        self.label_Step_x.setText(_translate("Form_piv_cnn", "X-dir"))
        self.label_Step_y.setText(_translate("Form_piv_cnn", "Y-dir"))
        self.groupBox_3.setTitle(_translate("Form_piv_cnn", "Training Parameter"))
        self.label_maxloop.setText(_translate("Form_piv_cnn", "Max Epoch"))
        self.label_bt_size.setText(_translate("Form_piv_cnn", "Batch Size"))
        self.label_loss_thresh.setText(_translate("Form_piv_cnn", "Loss Threshold"))
        self.label_lr.setText(_translate("Form_piv_cnn", "Learning Rate"))
        self.groupBox_2.setTitle(_translate("Form_piv_cnn", "Image Parameter"))
        self.label_IA.setText(_translate("Form_piv_cnn", "Interrogation Area (pix)"))
        self.label_ia_w.setText(_translate("Form_piv_cnn", "Width"))
        self.label_ia_h.setText(_translate("Form_piv_cnn", "Height"))
        self.label_SA.setText(_translate("Form_piv_cnn", "Searching Area (pix)"))
        self.label_SA_n.setText(_translate("Form_piv_cnn", "N"))
        self.label_SA_s.setText(_translate("Form_piv_cnn", "S"))
        self.label_SA_e.setText(_translate("Form_piv_cnn", "E"))
        self.label_SA_w.setText(_translate("Form_piv_cnn", "W"))
        self.label_2.setText(_translate("Form_piv_cnn", "Sub-pixel Fix"))
        self.label_pixdiam.setText(_translate("Form_piv_cnn", "Pixel Diameter (pix)"))
        self.label_inte_thresh.setText(_translate("Form_piv_cnn", "Intensity Threshold"))
        self.pushButton_check.setText(_translate("Form_piv_cnn", "Check..."))
        self.label_tinv.setText(_translate("Form_piv_cnn", "Time Interval (sec)"))
        self.groupBox_5.setTitle(_translate("Form_piv_cnn", "Figure"))
        self.label.setText(_translate("Form_piv_cnn", "Image Directory"))
        self.pushButton_browse.setText(_translate("Form_piv_cnn", "..."))
        self.pushButton_reset_mask.setText(_translate("Form_piv_cnn", "Reset Mask"))
        self.pushButton_run.setText(_translate("Form_piv_cnn", "Run..."))
        self.pushButton_mask.setText(_translate("Form_piv_cnn", "Mask"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_piv_cnn = QtWidgets.QWidget()
    ui = Ui_Form_piv_cnn()
    ui.setupUi(Form_piv_cnn)
    Form_piv_cnn.show()
    sys.exit(app.exec_())

