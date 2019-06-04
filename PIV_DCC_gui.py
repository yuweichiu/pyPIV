# -*- coding: utf-8 -*-
"""
Created on 2019/5/19
@author: Ivan Y.W.Chiu
"""

from src.UI.piv_dcc import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox, QListWidgetItem
from PyQt5.QtCore import QThread, pyqtSignal
from src.UI.form_piv_dcc import Ui_Form_piv_dcc
from src.UI.dialog_piv_out_opt import Ui_Dialog_piv_outopt
from src.UI.dialog_piv_progress import Ui_Dialog_piv_progress
import sys
import os
import pandas as pd
import numpy as np
import cv2
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle as RT
import src.toolbox.image as imgtool
import src.toolbox.ui_tool as uit
import shutil


class Child_piv_dcc(QWidget, Ui_Form_piv_dcc):
    def __init__(self):
        super(Child_piv_dcc, self).__init__()
        self.setupUi(self)
        self.figure = Figure((5, 5))
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout_3.addWidget(self.canvas)

class Child_piv_out_opt(QWidget, Ui_Dialog_piv_outopt):
    def __init__(self):
        super(Child_piv_out_opt, self).__init__()
        self.setupUi(self)

class Child_piv_progress(QWidget, Ui_Dialog_piv_progress):
    def __init__(self):
        super(Child_piv_progress, self).__init__()
        self.setupUi(self)

class MainWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)

        # child:
        self.chd_piv_outopt = Child_piv_out_opt()
        self.chd_piv_prog = Child_piv_progress()
        self.chd_piv_dcc = Child_piv_dcc()

        """ Triggered / connected  """
        # # PIVDCC
        self.chd_piv_dcc.pushButton_browse.clicked.connect(self.piv_read_img)
        self.chd_piv_dcc.listWidget_img.itemClicked.connect(self.piv_show_basemap)
        self.chd_piv_dcc.spinBox_ia_h.valueChanged.connect(self.ref_ia_sa_plot)
        self.chd_piv_dcc.spinBox_ia_w.valueChanged.connect(self.ref_ia_sa_plot)
        self.chd_piv_dcc.spinBox_sa_n.valueChanged.connect(self.ref_ia_sa_plot)
        self.chd_piv_dcc.spinBox_sa_s.valueChanged.connect(self.ref_ia_sa_plot)
        self.chd_piv_dcc.spinBox_sa_e.valueChanged.connect(self.ref_ia_sa_plot)
        self.chd_piv_dcc.spinBox_sa_w.valueChanged.connect(self.ref_ia_sa_plot)
        self.chd_piv_dcc.doubleSpinBox_tinv.valueChanged.connect(self.piv_get_param)
        self.chd_piv_dcc.lineEdit_roi_x.editingFinished.connect(self.piv_edit_roi_grid)
        self.chd_piv_dcc.lineEdit_roi_y.editingFinished.connect(self.piv_edit_roi_grid)
        self.chd_piv_dcc.lineEdit_roi_width.editingFinished.connect(self.piv_edit_roi_grid)
        self.chd_piv_dcc.lineEdit_roi_height.editingFinished.connect(self.piv_edit_roi_grid)
        self.chd_piv_dcc.spinBox_step_x.valueChanged.connect(self.piv_edit_roi_grid)
        self.chd_piv_dcc.spinBox_step_y.valueChanged.connect(self.piv_edit_roi_grid)
        self.chd_piv_dcc.pushButton_draw_roi.clicked.connect(self.start_drawing_roi)
        self.chd_piv_dcc.pushButton_reset_roi.clicked.connect(self.piv_draw_roi_reset)
        self.chd_piv_dcc.pushButton_run.clicked.connect(self.chd_piv_out_opt_show)
        self.chd_piv_outopt.pushButton_browse.clicked.connect(self.browse_piv_outdir)
        self.chd_piv_outopt.pushButton_browse_3.clicked.connect(self.browse_imgref)
        self.chd_piv_outopt.radioButton_calib.toggled.connect(self.piv_calib)
        self.chd_piv_outopt.radioButton_no_calib.toggled.connect(self.piv_calib)
        self.chd_piv_outopt.radioButton_all_seq.toggled.connect(self.piv_select_img_btn)
        self.chd_piv_outopt.radioButton_specify.toggled.connect(self.piv_select_img_btn)
        self.chd_piv_outopt.pushButton_run.clicked.connect(self.piv_init_run)
        self.chd_piv_outopt.pushButton_cancel.clicked.connect(self.chd_piv_outopt_quit)

        """ Main window object"""
        self.root_path = None
        self.piv_img_dir = None
        self.imgref_df = None
        self.calib = False
        self.axpi = None
        self.ROI = None
        self.ia_box = None
        self.grid_plot = None
        self.piv_param_dir = None
        self.piv_outdir = None

        self.MainGridLayout.addWidget(self.chd_piv_dcc)
        if not self.axpi:
            self.axpi = self.chd_piv_dcc.figure.add_subplot(1, 1, 1)
        else: pass
        self.axpi.set_xlabel('j (pix)')
        self.axpi.set_ylabel('i (pix)')
        self.axpi.set_title('Grid: N/A')
        self.O1_piv_dcc_pb(False)
        self.chd_piv_dcc.show()

    def piv_read_img(self):
        pid = QFileDialog.getExistingDirectory(self, 'Select the image folder for PIV analysis')
        if not pid: pass
        else:
            self.piv_img_dir = pid
            self.chd_piv_dcc.lineEdit_img_dir.setText(self.piv_img_dir)
            self.O1_piv_dcc_pb(True)
            self.piv_get_im_list()

    def piv_get_im_list(self):
        self.chd_piv_dcc.listWidget_img = uit.list_cleaner(self.chd_piv_dcc.listWidget_img)
        templist = os.listdir(self.piv_img_dir)
        self.piv_img_list = []
        for piid, pi in enumerate(sorted(templist)):
            self.piv_img_list.append(pi)
            self.chd_piv_dcc.listWidget_img.insertItem(piid + 1, QListWidgetItem('{0:s}'.format(pi)))
        self.chd_piv_dcc.listWidget_img.setCurrentRow(0)
        os.chdir(self.piv_img_dir)
        self.piv_show_basemap()

    def piv_show_basemap(self):
        if len(self.axpi.images) > 0:
            self.axpi.images.pop()
        os.chdir(self.piv_img_dir)
        imgname = self.chd_piv_dcc.listWidget_img.currentItem().text()
        if imgname:
            self.piv_bsmp = cv2.imread(imgname, cv2.IMREAD_GRAYSCALE)
            self.axpi.imshow(self.piv_bsmp, cmap='gray', vmin=0, vmax=255)
            self.chd_piv_dcc.canvas.draw()
            self.midx, self.midy = self.piv_bsmp.shape[1]/2, self.piv_bsmp.shape[0]/2
            self.piv_get_param()
            if not self.ia_box:
                self.draw_ia_sa()
            else: self.ref_ia_sa_plot()
        else: pass

    def piv_get_param(self):
        self.ia_h, self.ia_w = self.chd_piv_dcc.spinBox_ia_h.value(), self.chd_piv_dcc.spinBox_ia_w.value()
        self.sa_n, self.sa_s = self.chd_piv_dcc.spinBox_sa_n.value(), self.chd_piv_dcc.spinBox_sa_s.value()
        self.sa_e, self.sa_w = self.chd_piv_dcc.spinBox_sa_e.value(), self.chd_piv_dcc.spinBox_sa_w.value()
        self.step_x, self.step_y = self.chd_piv_dcc.spinBox_step_x.value(), self.chd_piv_dcc.spinBox_step_y.value()
        self.tinv = self.chd_piv_dcc.doubleSpinBox_tinv.value()

    def draw_ia_sa(self):
        self.piv_get_param()
        ia_luc = (self.midx - self.ia_w/2, self.midy - self.ia_h/2)  # IA left-up corner
        sa_luc = (self.midx - self.ia_w/2 - self.sa_w, self.midy - self.ia_h/2 - self.sa_n)
        sa_width = self.ia_w + self.sa_e + self.sa_w
        sa_height = self.ia_h + self.sa_n + self.sa_s
        self.ia_box = self.axpi.add_patch(RT(ia_luc, self.ia_w, self.ia_h, linewidth=1, edgecolor='r', fill=False))
        self.sa_box = self.axpi.add_patch(RT(sa_luc, sa_width, sa_height, linewidth=1, edgecolor='c', fill=False))
        self.ia_btxt = self.axpi.text(self.midx, self.midy, 'IA\n{0:d}x{1:d}'.format(self.ia_w, self.ia_h),
                                      va='center', ha='center', color='r')
        self.sa_btxt_n = self.axpi.text(
            self.midx, self.midy - self.ia_h/2 - self.sa_n - 1, 'N:{0:d}'.format(self.sa_n),
            va='bottom', ha='center', color='c')
        self.sa_btxt_s = self.axpi.text(
            self.midx, self.midy + self.ia_h/2 + self.sa_s + 1, 'S:{0:d}'.format(self.sa_s),
            va='top', ha='center', color='c')
        self.sa_btxt_e = self.axpi.text(
            self.midx + self.ia_w/2 + self.sa_e + 1, self.midy, 'E:{0:d}'.format(self.sa_e),
            va='center', ha='left', color='c')
        self.sa_btxt_w = self.axpi.text(
            self.midx - self.ia_w/2 - self.sa_w - 1, self.midy, 'W:{0:d}'.format(self.sa_w),
            va='center', ha='right', color='c')
        self.chd_piv_dcc.canvas.draw()

    def ref_ia_sa_plot(self):
        self.piv_get_param()
        self.midx, self.midy = self.piv_bsmp.shape[1] / 2, self.piv_bsmp.shape[0] / 2
        ia_luc = (self.midx - self.ia_w/2, self.midy - self.ia_h/2)  # IA left-up corner
        sa_luc = (self.midx - self.ia_w/2 - self.sa_w, self.midy - self.ia_h/2 - self.sa_n)
        sa_width = self.ia_w + self.sa_e + self.sa_w
        sa_height = self.ia_h + self.sa_n + self.sa_s
        self.ia_box.set_x(ia_luc[0]), self.ia_box.set_y(ia_luc[1])
        self.ia_box.set_width(self.ia_w), self.ia_box.set_height(self.ia_h)
        self.ia_btxt.set_x(self.midx)
        self.ia_btxt.set_y(self.midy)
        self.ia_btxt.set_text('IA\n{0:d}x{1:d}'.format(self.ia_w, self.ia_h))
        self.sa_box.set_x(sa_luc[0]), self.sa_box.set_y(sa_luc[1])
        self.sa_box.set_width(sa_width), self.sa_box.set_height(sa_height)
        self.sa_btxt_n.set_x(self.midx)
        self.sa_btxt_n.set_y(self.midy - self.ia_h /  - self.sa_n - 1), self.sa_btxt_n.set_text('N:{0:d}'.format(self.sa_n))
        self.sa_btxt_s.set_x(self.midx)
        self.sa_btxt_s.set_y(self.midy + self.ia_h / 2 + self.sa_s + 1), self.sa_btxt_s.set_text('S:{0:d}'.format(self.sa_s))
        self.sa_btxt_e.set_y(self.midy)
        self.sa_btxt_e.set_x(self.midx + self.ia_w / 2 + self.sa_e + 1), self.sa_btxt_e.set_text('E:{0:d}'.format(self.sa_e))
        self.sa_btxt_w.set_y(self.midy)
        self.sa_btxt_w.set_x(self.midx - self.ia_w / 2 - self.sa_w - 1), self.sa_btxt_w.set_text('W:{0:d}'.format(self.sa_w))
        self.chd_piv_dcc.canvas.draw()


    def roi2corner_num_grid(self, ROI, IA, SA, step):
        """
        Get ROI to the corner without SA and the grid with the amount.
        :param ROI: [x, y, width, height]
        :param IA: [ia_h, ia_w]
        :param SA: [N, S, E, W]
        :param step: [x, y]
        :return: corner, num_x, num_y, grid_all
        """
        roi_x, roi_y, roi_width, roi_height = ROI
        x0p, y0p = roi_x + SA[3], roi_y + SA[0]
        xmv, ymv = roi_x + roi_width, roi_y + roi_height
        xmvp, ymvp = xmv - SA[2], ymv - SA[1]
        corner = np.array([[x0p, y0p], [x0p, ymvp], [xmvp, ymvp], [xmvp, y0p], [x0p, y0p]])

        dxp, dyp = roi_width - SA[2] - SA[3], roi_height - SA[0] - SA[1]
        num_x = np.int(np.floor((dxp - IA[1]) / step[0]) + 1)
        num_y = np.int(np.floor((dyp - IA[0]) / step[1]) + 1)

        # make_grid:
        x_start, x_end = int(corner[0, 0] + IA[1] / 2), int(corner[3, 0] - IA[1] / 2)
        y_start, y_end = int(corner[0, 1] + IA[0] / 2), int(corner[1, 1] - IA[0] / 2)
        grid_all = imgtool.make_grid([x_start, y_start], [x_end, y_end], step)
        return corner, num_x, num_y, grid_all

    def piv_grid_gen(self):
        if self.roi_width >= self.ia_w + self.sa_e + self.sa_w and self.roi_height >= self.ia_h + self.sa_s + self.sa_n:
            self.piv_corner, self.num_x, self.num_y, self.grid_all = self.roi2corner_num_grid(
                [self.roi_x, self.roi_y, self.roi_width, self.roi_height],
                [self.ia_h, self.ia_w],
                [self.sa_n, self.sa_s, self.sa_e, self.sa_w],
                [self.step_x, self.step_y]
            )
            if not self.grid_plot:
                self.grid_plot = self.axpi.plot(self.grid_all[:, 0], self.grid_all[:, 1], 'w+')[0]
            else:
                self.grid_plot.set_xdata(self.grid_all[:, 0])
                self.grid_plot.set_ydata(self.grid_all[:, 1])
            self.axpi.set_title('Grid: {0:d} x {1:d}'.format(self.num_x, self.num_y))
        else:
            self.grid_plot.set_xdata(0)
            self.grid_plot.set_ydata(0)
            self.axpi.set_title('Grid: N/A')

    def piv_edit_roi_grid(self):
        if self.chd_piv_dcc.lineEdit_roi_x.text() and self.chd_piv_dcc.lineEdit_roi_y.text() and self.chd_piv_dcc.lineEdit_roi_width.text() and self.chd_piv_dcc.lineEdit_roi_height.text():
            self.roi_x, self.roi_y, self.roi_width, self.roi_height = int(self.chd_piv_dcc.lineEdit_roi_x.text()), int(self.chd_piv_dcc.lineEdit_roi_y.text()), int(self.chd_piv_dcc.lineEdit_roi_width.text()), int(self.chd_piv_dcc.lineEdit_roi_height.text())
            self.piv_get_param()
            if not self.ROI:
                self.ROI = self.axpi.add_patch(
                    RT((self.roi_x, self.roi_y), self.roi_width, self.roi_height, linewidth=1, edgecolor='w', facecolor='r', alpha=0.3)
                )
            else:
                self.ROI.set_x(self.roi_x)
                self.ROI.set_y(self.roi_y)
                self.ROI.set_width(self.roi_width)
                self.ROI.set_height(self.roi_height)
            self.piv_grid_gen()
            self.chd_piv_dcc.canvas.draw()

    def piv_draw_roi_press(self, event):
        if event.inaxes != self.axpi:
            return
        contains, attrd = self.axpi.contains(event)
        if not contains:
            return
        self.roi_press = int(event.xdata), int(event.ydata)
        self.roi_x, self.roi_y = self.roi_press
        self.chd_piv_dcc.lineEdit_roi_x.setText(str(self.roi_x))
        self.chd_piv_dcc.lineEdit_roi_y.setText(str(self.roi_y))
        self.chd_piv_dcc.canvas.draw()

    def piv_draw_roi_move(self, event):
        if self.roi_press is None:
            return
        if event.inaxes != self.axpi.axes:
            return
        dx, dy = int(event.xdata) - self.roi_x, int(event.ydata) - self.roi_y
        self.roi_width, self.roi_height = dx, dy
        self.ROI.set_x(self.roi_x), self.ROI.set_y(self.roi_y)
        self.ROI.set_width(self.roi_width), self.ROI.set_height(self.roi_height)
        self.piv_grid_gen()
        self.chd_piv_dcc.lineEdit_roi_width.setText(str(self.roi_width))
        self.chd_piv_dcc.lineEdit_roi_height.setText(str(self.roi_height))
        self.chd_piv_dcc.canvas.draw()

    def piv_draw_roi_rls(self, event):
        self.roi_press = None
        self.mpl_off_roi_draw()
        self.chd_piv_dcc.canvas.draw()

    def piv_draw_roi_reset(self):
        if not self.ROI: pass
        else:
            self.ROI.set_width(0), self.ROI.set_height(0)
        if not self.grid_plot: pass
        else:
            self.grid_plot.set_xdata(0), self.grid_plot.set_ydata(0)
        self.axpi.set_title('N/A')
        self.chd_piv_dcc.lineEdit_roi_x.setText(str(''))
        self.chd_piv_dcc.lineEdit_roi_y.setText(str(''))
        self.chd_piv_dcc.lineEdit_roi_width.setText(str(''))
        self.chd_piv_dcc.lineEdit_roi_height.setText(str(''))
        self.chd_piv_dcc.canvas.draw()

    def start_drawing_roi(self):
        self.piv_get_param()
        self.roi_press = None
        if not self.ROI:
            self.ROI = self.axpi.add_patch(RT((0, 0), 0, 0, linewidth=1, edgecolor='w', facecolor='r', alpha=0.3))
        else:
            self.ROI.set_width(0), self.ROI.set_height(0)
        if not self.grid_plot:
            self.grid_plot = self.axpi.plot(0, 0, 'w+')[0]
        else:
            self.grid_plot.set_xdata(0)
            self.grid_plot.set_ydata(0)
        self.mpl_on_roi_draw()

    def mpl_on_roi_draw(self):
        self.cid_press_roi_draw = self.chd_piv_dcc.canvas.mpl_connect('button_press_event', self.piv_draw_roi_press)
        self.cid_motion_roi_draw = self.chd_piv_dcc.canvas.mpl_connect('motion_notify_event', self.piv_draw_roi_move)
        self.cid_release_roi_draw = self.chd_piv_dcc.canvas.mpl_connect('button_release_event', self.piv_draw_roi_rls)

    def mpl_off_roi_draw(self):
        self.chd_piv_dcc.canvas.mpl_disconnect(self.cid_press_roi_draw)
        self.chd_piv_dcc.canvas.mpl_disconnect(self.cid_motion_roi_draw)
        self.chd_piv_dcc.canvas.mpl_disconnect(self.cid_release_roi_draw)

    def chd_piv_out_opt_show(self):
        # self.piv_get_param()
        self.chd_piv_outopt.show()
        self.piv_calib()
        while self.chd_piv_outopt.listWidget.count() > 0:
            self.chd_piv_outopt.listWidget.clear()
        for piid, pi in enumerate(self.piv_img_list):
            self.chd_piv_outopt.listWidget.insertItem(piid + 1, QListWidgetItem('{0:s}'.format(pi)))
        self.piv_select_img_btn()
        self.imgref_df = None
        self.chd_piv_outopt.pushButton_run.setEnabled(False)

    def chd_piv_progress_show(self):
        self.chd_piv_prog.show()
        self.chd_piv_prog.pushButton.setEnabled(True)

    def chd_piv_outopt_quit(self):
        self.chd_piv_outopt.close()

    def browse_piv_outdir(self):
        outdir = QFileDialog.getExistingDirectory(self, "Select the directory to save the results.")
        if not outdir: pass
        else:
            self.piv_outdir = os.path.join(outdir, "inst_vel")
            self.chd_piv_outopt.lineEdit_out_dir.setText(self.piv_outdir)
            self.piv_param_dir = os.path.join(outdir, "param")
            self.chd_piv_outopt.lineEdit_out_dir_2.setText(self.piv_param_dir)
            if self.chd_piv_outopt.lineEdit_out_dir.text() and self.chd_piv_outopt.lineEdit_out_dir_2.text():
                self.chd_piv_outopt.pushButton_run.setEnabled(True)
            self.chd_piv_outopt.show()

    def browse_imgref(self):
        irp, _ = QFileDialog.getOpenFileNames(self, 'Read Image Reference CSV file', self.root_path, "CSV Files (*.csv)")
        if not irp: pass
        else:
            try:
                self.imgref_df = pd.read_csv(irp[0])
                self.calib = True
                self.chd_piv_outopt.lineEdit_calib_dir.setText(irp[0])
            except:
                self.calib = False
                self.imgref_df = None

    def piv_select_img_btn(self):
        if self.chd_piv_outopt.radioButton_all_seq.isChecked() is True:
            self.chd_piv_outopt.listWidget.setEnabled(False)
        elif self.chd_piv_outopt.radioButton_specify.isChecked() is True:
            self.chd_piv_outopt.listWidget.setEnabled(True)

    def piv_calib(self):
        if self.chd_piv_outopt.radioButton_no_calib.isChecked() is True:
            self.chd_piv_outopt.lineEdit_calib_dir.setEnabled(False)
            self.chd_piv_outopt.pushButton_browse_3.setEnabled(False)
            self.calib = False
        elif self.chd_piv_outopt.radioButton_calib.isChecked() is True:
            self.chd_piv_outopt.lineEdit_calib_dir.setEnabled(True)
            self.chd_piv_outopt.pushButton_browse_3.setEnabled(True)

    def piv_init_run(self):
        if not self.calib and self.chd_piv_outopt.radioButton_calib.isChecked() is True:
            QMessageBox.warning(self, "Warning", "No Image Reference has been selected !", QMessageBox.Ok, QMessageBox.Ok)
        else:
            keep_going = False
            if not os.path.exists(self.piv_outdir):
                os.mkdir(self.piv_outdir)
            if not os.path.exists(self.piv_param_dir):
                os.mkdir(self.piv_param_dir)
            if len(os.listdir(self.piv_outdir)) == 0 and len(os.listdir(self.piv_param_dir)) == 0:
                keep_going = True
            else:
                reply = QMessageBox.warning(self, 'Warning', 'Directory is not empty!\nDo you want to cover it?',
                                        QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    try:
                        shutil.rmtree(self.piv_outdir)
                        shutil.rmtree(self.piv_param_dir)
                        os.mkdir(self.piv_outdir)
                        os.mkdir(self.piv_param_dir)
                        keep_going = True
                    except:
                        QMessageBox.warning(self, "Warning", "Can not re-create the directory!", QMessageBox.Ok,
                                            QMessageBox.Ok)
                else:
                    keep_going = False

            if keep_going:
                if self.piv_outdir and self.piv_param_dir:
                    if self.chd_piv_outopt.radioButton_all_seq.isChecked() is True:
                        self.run_piv_list = self.piv_img_list
                    elif self.chd_piv_outopt.radioButton_specify.isChecked() is True:
                        items = self.chd_piv_outopt.listWidget.selectedItems()
                        self.run_piv_list = []
                        for i in range(len(items)):
                            self.run_piv_list.append(str(items[i].text()))
                    if self.run_piv_list:
                        self.piv_get_param()
                        self.param_df = pd.DataFrame(
                            {'IA_h': self.ia_h, 'IA_w': self.ia_w, 'SAn': self.sa_n, 'SAs': self.sa_s, 'SAe': self.sa_e,
                             'SAw': self.sa_w,
                             'tinv': self.tinv},
                            index=[0],
                            columns=['IA_h', 'IA_w', 'SAn', 'SAs', 'SAe', 'SAw', 'tinv']
                        )
                        if self.calib:
                            self.imgref_df.to_csv(os.path.join(self.piv_param_dir, 'img_ref.csv'), index=False)
                        os.chdir(self.piv_param_dir)
                        cv2.imwrite('basemap.bmp', self.piv_bsmp)
                        self.param_df.to_csv(os.path.join(self.piv_param_dir, 'piv_param.csv'), index=False)
                        self.grid_df = pd.DataFrame(
                            {'j': self.grid_all[:, 0], 'i': self.grid_all[:, 1]}, index=list(range(self.grid_all.shape[0])), columns=['j', 'i'])
                        self.grid_df.to_csv(os.path.join(self.piv_param_dir, 'piv_grid.csv'), index=False)
                        self.grid_num_df = pd.DataFrame(
                            {'j_num': self.num_x, 'i_num': self.num_y}, index=[0], columns=['j_num', 'i_num'])
                        self.grid_num_df.to_csv(os.path.join(self.piv_param_dir, 'piv_grid_nx_ny.csv'), index=False)
                        self.chd_piv_progress_show()
                        self.chd_piv_prog.progressBar.setValue(0)
                        total_count = self.grid_all.shape[0] * (len(self.run_piv_list) - 1)
                        self.chd_piv_prog.progressBar.setMaximum(total_count)
                        self.getPIVDCC_Thread = runPIVDCC_Thread(
                            self.piv_img_dir, self.run_piv_list, self.piv_corner, self.param_df, self.grid_all, self.calib,
                            self.tinv, self.piv_outdir, self.imgref_df
                        )
                        self.getPIVDCC_Thread.cur_img_sig.connect(self.refr_piv_pg_txt)
                        self.getPIVDCC_Thread.start()
                        self.chd_piv_prog.pushButton.clicked.connect(self.getPIVDCC_Thread.terminate)
                    else:
                        QMessageBox.warning(self, "Warning", "No image has been selected !", QMessageBox.Ok, QMessageBox.Ok)
                else:
                    QMessageBox.warning(self, "Warning", "No directory has been selected !", QMessageBox.Ok, QMessageBox.Ok)

    def refr_piv_pg_txt(self, cur_imgname, count, run_done):
        if run_done == 0:
            self.chd_piv_prog.label_imgname.setText(cur_imgname)
            self.chd_piv_prog.progressBar.setValue(count)
        elif run_done == 1:
            QMessageBox.information(
                self, "Done.", "The PIV process is done successfully.",
                QMessageBox.Ok, QMessageBox.Ok
            )
            self.chd_piv_prog.progressBar.setValue(len(self.run_piv_list) - 1)
            self.chd_piv_prog.close()
            self.chd_piv_prog.progressBar.setValue(0)

    def O1_piv_dcc_pb(self, O1):
        self.chd_piv_dcc.spinBox_ia_h.setEnabled(O1)
        self.chd_piv_dcc.spinBox_ia_w.setEnabled(O1)
        self.chd_piv_dcc.spinBox_sa_n.setEnabled(O1)
        self.chd_piv_dcc.spinBox_sa_s.setEnabled(O1)
        self.chd_piv_dcc.spinBox_sa_e.setEnabled(O1)
        self.chd_piv_dcc.spinBox_sa_w.setEnabled(O1)
        self.chd_piv_dcc.doubleSpinBox_tinv.setEnabled(O1)
        self.chd_piv_dcc.lineEdit_roi_x.setEnabled(O1)
        self.chd_piv_dcc.lineEdit_roi_y.setEnabled(O1)
        self.chd_piv_dcc.lineEdit_roi_width.setEnabled(O1)
        self.chd_piv_dcc.lineEdit_roi_height.setEnabled(O1)
        self.chd_piv_dcc.spinBox_step_x.setEnabled(O1)
        self.chd_piv_dcc.spinBox_step_y.setEnabled(O1)
        self.chd_piv_dcc.pushButton_reset_roi.setEnabled(O1)
        self.chd_piv_dcc.pushButton_draw_roi.setEnabled(O1)
        self.chd_piv_dcc.pushButton_run.setEnabled(O1)
        self.chd_piv_dcc.pushButton_mask.setEnabled(O1)
        self.chd_piv_dcc.pushButton_reset_mask.setEnabled(O1)
        self.chd_piv_dcc.listWidget_img.setEnabled(O1)


class runPIVDCC_Thread(QThread):
    cur_img_sig = pyqtSignal(str, int, int)
    def __init__(self, piv_img_dir, run_piv_list, corner, param, grid_all, calib, tinv, piv_outdir, imgref_df=None):
        QThread.__init__(self)
        self.piv_img_dir = piv_img_dir
        self.run_piv_list = run_piv_list
        self.corner = corner
        self.param = param
        self.grid_all = grid_all
        self.calib = calib
        self.tinv = tinv
        self.piv_outdir = piv_outdir
        self.count = 0
        self.imgref_df = imgref_df

    def __del__(self):
        self.wait()

    def _dcc(self, img1_path, img2_path, grid, param_df, mask=None):
        current_path = os.getcwd()
        img1_name = os.path.basename(img1_path)
        img1_dir = img1_path.split(img1_name)[0]
        img2_name = os.path.basename(img2_path)
        img2_dir = img2_path.split(img2_name)[0]
        os.chdir(img1_dir)
        img1 = cv2.imread(img1_name, cv2.IMREAD_GRAYSCALE)
        os.chdir(img2_dir)
        img2 = cv2.imread(img2_name, cv2.IMREAD_GRAYSCALE)
        os.chdir(current_path)
        if mask is None:
            img1 = np.float64(img1)
            img2 = np.float64(img2)
            pass
        else:
            img1 = np.float64(cv2.bitwise_and(img1, mask))
            img2 = np.float64(cv2.bitwise_and(img2, mask))

        # Initialize interrogation area and expansion of searching area:
        ia_w = param_df['IA_w'][0]
        ia_h = param_df['IA_h'][0]
        sa_n, sa_s, sa_e, sa_w = param_df['SAn'][0], param_df['SAs'][0], param_df['SAe'][0], param_df['SAw'][0]

        # Initialize the array:
        DX, DY = np.zeros([grid.shape[0]]), np.zeros([grid.shape[0]])
        sub_DX, sub_DY = np.zeros([grid.shape[0]]), np.zeros([grid.shape[0]])

        # On each grid points:
        for g in range(grid.shape[0]):
            self.cur_img_sig.emit(img1_name + " and " + img2_name, self.count, 0)

            # get grid point (x, y):
            xg, yg = grid[g, :]

            # get cropped image on point:
            IA = img1[int(yg - ia_h / 2): int(yg + ia_h / 2), int(xg - ia_w / 2): int(xg + ia_w / 2)]
            IA = IA.flatten()

            SA_startrow = int(yg - ia_h / 2 - sa_n)
            SA_endrow = int(yg + ia_h / 2 + sa_s)
            SA_startcol = int(xg - ia_w / 2 - sa_w)
            SA_endcol = int(xg + ia_w / 2 + sa_e)
            ny = np.int(np.floor((SA_endrow - SA_startrow - ia_h) / 1)) + 1
            nx = np.int(np.floor((SA_endcol - SA_startcol - ia_w) / 1)) + 1
            SA = np.zeros([nx * ny, ia_h * ia_w])
            count = 0
            for i in range(ny):
                for j in range(nx):
                    sub_sa = img2[SA_startrow + i: SA_startrow + i + ia_h, SA_startcol + j: SA_startcol + j + ia_w]
                    SA[count, :] = sub_sa.flatten()
                    count += 1

            # cross-correlation: subtract the mean of crop img:
            IA = IA - np.mean(IA)
            SA = SA - np.reshape(np.mean(SA, axis=1), [nx * ny, 1])
            r02 = np.sum(IA ** 2)
            matrix_cc = np.zeros([nx * ny])
            for rr in range(nx * ny):
                r01 = np.dot(IA, SA[rr, :])
                r03 = np.sum(SA[rr, :] ** 2)
                # cross-correlation: coefficient matrix:
                matrix_cc[rr] = r01 / (r02 * r03) ** 0.5

            matrix_cc = np.reshape(matrix_cc, [ny, nx])

            # Find the max coefficient index: (get only 1 index)
            iid, jid = np.unravel_index(np.argmax(matrix_cc), matrix_cc.shape)

            if jid != np.nan and iid != np.nan:
                if 1 <= jid <= matrix_cc.shape[1] - 2 and 1 <= iid <= matrix_cc.shape[0] - 2:
                    try:
                        # # Gaussian Interpolation:
                        f0 = np.log(matrix_cc[iid, jid])
                        f1 = np.log(matrix_cc[iid - 1, jid])
                        f2 = np.log(matrix_cc[iid + 1, jid])
                        sub_dy = (f1 - f2) / (2 * f1 - 4 * f0 + 2 * f2)
                        f1 = np.log(matrix_cc[iid, jid - 1])
                        f2 = np.log(matrix_cc[iid, jid + 1])
                        sub_dx = (f1 - f2) / (2 * f1 - 4 * f0 + 2 * f2)

                        DX[g], DY[g] = jid - sa_w, iid - sa_n
                        sub_DX[g], sub_DY[g] = sub_dx, sub_dy

                    except:
                        DX[g], DY[g] = np.nan, np.nan
                        sub_DX[g], sub_DY[g] = np.nan, np.nan
                else:
                    DX[g], DY[g] = np.nan, np.nan
                    sub_DX[g], sub_DY[g] = np.nan, np.nan
            else:
                DX[g], DY[g] = np.nan, np.nan
                sub_DX[g], sub_DY[g] = np.nan, np.nan

            self.count += 1

        return DX, DY, sub_DX, sub_DY

    def run(self):
        for im in range(len(self.run_piv_list) - 1):
            img1name = self.run_piv_list[im].split('.')[0]
            img2name = self.run_piv_list[im + 1].split('.')[0]
            DX, DY, sub_DX, sub_DY = self._dcc(
                os.path.join(self.piv_img_dir, self.run_piv_list[im]),
                os.path.join(self.piv_img_dir, self.run_piv_list[im + 1]),
                self.grid_all, self.param, None
            )
            if self.calib:
                xmin = self.imgref_df['xmin'][0]
                ymax = self.imgref_df['ymax'][0]
                res = self.imgref_df['res'][0]
                xpos = xmin + res * self.grid_all[:, 0]
                ypos = ymax - res * self.grid_all[:, 1]
                u_vel = (DX + sub_DX) * res / self.tinv
                v_vel = -(DY + sub_DY) * res / self.tinv

            else:
                xpos = self.grid_all[:, 0]
                ypos = self.grid_all[:, 1]
                u_vel = DX + sub_DX
                v_vel = DY + sub_DY

            pivresults = pd.DataFrame(
                {'x': xpos, 'y': ypos, 'u': u_vel, 'v': v_vel},
                index=[list(range(self.grid_all.shape[0]))],
                columns=['x', 'y', 'u', 'v']
            )
            filename = 'inst_[{0:s}]_[{1:s}].csv'.format(img1name, img2name)
            pivresults.to_csv(os.path.join(self.piv_outdir, filename), index=False)
        self.cur_img_sig.emit('Done.', self.count, 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
