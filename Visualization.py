# -*- coding: utf-8 -*-
"""
Created on 2019/3/18 下午 04:09
@author: Ivan Y.W.Chiu
"""

from src.UI.piv_visual import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox, QTableWidgetItem, QListWidgetItem
from PyQt5.QtCore import QThread, pyqtSignal
from src.UI.form_results import Ui_Form_results
from src.UI.dialog_value_filter import Ui_Dialog_value_filter
import sys
import os
import pandas as pd
import numpy as np
import cv2
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle as RT
from mpl_toolkits.axes_grid1 import make_axes_locatable
import src.toolbox.piv_process as piv
from scipy.interpolate import griddata
import shutil

class Child_results(QWidget, Ui_Form_results):
    def __init__(self):
        super(Child_results, self).__init__()
        self.setupUi(self)
        self.figure = Figure((5, 5))
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout_3.addWidget(self.canvas)
        plt.rcParams.update({'font.size': 14})
        # Set combo box:
        self.comboBox.addItems(['Red', 'Yellow', 'Green', 'Cyan', 'Blue', 'Magenta', 'White', 'Black'])

class Child_val_filt(QWidget, Ui_Dialog_value_filter):
    def __init__(self):
        super(Child_val_filt, self).__init__()
        self.setupUi(self)
        self.figure = Figure((4, 3))
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout.addWidget(self.canvas)

class MainWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)

        # child:
        self.chd_results = Child_results()
        self.chd_val_filt = Child_val_filt()

        # results
        self.chd_results.pushButton_field.clicked.connect(self.results_clc_btn_field)
        self.chd_results.horizontalSlider_q_scale.valueChanged.connect(self.results_drag_slider)
        self.chd_results.horizontalSlider_q_head_length.valueChanged.connect(self.results_drag_slider)
        self.chd_results.horizontalSlider_q_head_width.valueChanged.connect(self.results_drag_slider)
        self.chd_results.horizontalSlider_q_width.valueChanged.connect(self.results_drag_slider)
        self.chd_results.comboBox.currentIndexChanged.connect(self.results_quiv_color_chg)
        self.chd_results.pushButton_browse.clicked.connect(self.vis_browse_inst)
        self.chd_results.pushButton_valuefilter.clicked.connect(self.chd_val_filt_show)
        self.chd_results.pushButton_contour.clicked.connect(self.results_clc_btn_contour)
        self.chd_results.pushButton_streamline.clicked.connect(self.results_clc_btn_streamline)
        self.chd_results.pushButton_save.clicked.connect(self.save_fig)
        self.chd_results.pushButton_save_vel.clicked.connect(self.save_vel)

        self.MainGridLayout.addWidget(self.chd_results)
        self.chd_results.figure.clear()
        self.axrt = self.chd_results.figure.add_subplot(1, 1, 1)
        self.O1_results_pb(False)
        self.O1_results_sd(False)
        self.chd_results.show()
        # self.results_init()

        self.root_path = None

    def chd_val_filt_show(self):
        self.chd_val_filt.figure.clear()
        self.axvf = self.chd_val_filt.figure.add_subplot(1, 1, 1)
        self.axvf.plot(self.uinst, self.vinst, 'b.')
        self.rect_vf = self.axvf.add_patch(RT((0, 0), 0, 0, linewidth=1, edgecolor='r', fill=False))
        if self.calib is True:
            self.axvf.set_xlabel('u (m/s)'), self.axvf.set_ylabel('v (m/s)')
        else:
            self.axvf.set_xlabel('u (pix/frame)'), self.axvf.set_ylabel('v (pix/frame)')
        self.chd_val_filt.canvas.draw()
        self.chd_val_filt.show()
        self.vf_press = None
        self.mpl_on_val_filt()

    def results_get_slider(self):
        self.sl_scale = self.chd_results.horizontalSlider_q_scale.value() / 5
        self.sl_hl = self.chd_results.horizontalSlider_q_head_length.value() / 10
        self.sl_hw = self.chd_results.horizontalSlider_q_head_width.value() / 10
        self.sl_w = self.chd_results.horizontalSlider_q_width.value() / 10000

    def vis_browse_inst(self):
        fod = QFileDialog.getExistingDirectory(self, 'Select the results folder of PIV analysis')
        if not fod: pass
        else:
            self.root_path = fod
            self.inst_dir = os.path.join(self.root_path, 'inst_vel')
            self.param = os.path.join(self.root_path, 'param')
            self.results_init()

    def results_init(self):
        imgp = os.path.join(self.root_path, "param", "basemap.bmp")
        paramp = os.path.join(self.root_path, "param", "piv_param.csv")
        gridp = os.path.join(self.root_path, "param", "piv_grid.csv")
        gridnump = os.path.join(self.root_path, "param", "piv_grid_nx_ny.csv")
        instvelp = os.path.join(self.root_path, "inst_vel")
        instvel_list = os.listdir(instvelp)
        success = False
        if os.path.exists(imgp):
            if os.path.exists(paramp):
                if os.path.exists(gridp):
                    if os.path.exists(gridnump):
                        if instvel_list:
                           success = True
                           self.chd_results.lineEdit_vel_dir.setText(instvelp)
                        else:
                            QMessageBox.warning(self, "Not Found Error.",
                                                "The instantaneous velocity file is not found.", QMessageBox.Ok,
                                                QMessageBox.Ok)
                    else:
                        success = False
                        QMessageBox.warning(self, "Not Found Error.",
                                            "The file 'piv_grid_nx_ny.csv' is not found.", QMessageBox.Ok, QMessageBox.Ok)
                else:
                    success = False
                    QMessageBox.warning(self, "Not Found Error.",
                                        "The file 'piv_grid.csv' is not found.", QMessageBox.Ok,
                                        QMessageBox.Ok)
            else:
                success = False
                QMessageBox.warning(self, "Not Found Error.",
                                    "The file 'piv_param.csv' is not found.", QMessageBox.Ok, QMessageBox.Ok)
        else:
            success = False
            QMessageBox.warning(self, "Not Found Error.",
                                "The ortho image is not found.", QMessageBox.Ok, QMessageBox.Ok)
        if success:
            os.chdir(os.path.join(self.root_path, "param"))
            self.bsmp = cv2.imread("basemap.bmp", cv2.IMREAD_GRAYSCALE)
            self.grid_num_df = pd.read_csv(gridnump)
            imgrefp = os.path.join(self.root_path, "param", "img_ref.csv")
            if os.path.exists(imgrefp):
                self.calib = True
                self.img_ref_df = pd.read_csv(imgrefp)
                self.xmin = self.img_ref_df['xmin'][0]
                self.xmax = self.img_ref_df['xmax'][0]
                self.ymin = self.img_ref_df['ymin'][0]
                self.ymax = self.img_ref_df['ymax'][0]
                self.res = self.img_ref_df['res'][0]
                self.xref = self.xmin
                self.yref = self.ymin - 0.075 * self.res * self.bsmp.shape[0]
                self.y_rtext = self.yref + 0.03 * self.res * self.bsmp.shape[0]
            else:
                self.xmin, self.xmax = 0, self.bsmp.shape[1]
                self.ymin, self.ymax = self.bsmp.shape[0], 0
                self.xref = self.xmin
                self.yref = self.ymin + 0.075 * self.bsmp.shape[0]
                self.y_rtext = self.yref - 0.03 * self.bsmp.shape[0]
                self.calib = False

            self.xrt, self.yrt, self.uinst, self.vinst, self.grid_num = piv.load_vel_data(self.root_path)
            if self.uinst.shape[1] > 1:
                self.uinstf, self.vinstf = self.uinst.copy(), self.vinst.copy()
                self.umean, self.vmean = np.nanmean(self.uinst, axis=1), np.nanmean(self.vinst, axis=1)
                self.umeanf, self.vmeanf = self.umean.copy(), self.vmean.copy()
            else:
                self.uinstf, self.vinstf = self.uinst.copy(), self.vinst.copy()
                self.umean, self.vmean = self.uinst.copy(), self.vinst.copy()
                self.umeanf, self.vmeanf = self.uinst.copy(), self.vinst.copy()

            while self.chd_results.listWidget_inst_vel.count() > 0:
                self.chd_results.listWidget_inst_vel.clear()

            for ivid, iv in enumerate(instvel_list):
                self.chd_results.listWidget_inst_vel.insertItem(ivid + 1, QListWidgetItem('{0:s}'.format(iv)))
            self.chd_results.listWidget_inst_vel.setCurrentRow(0)

            while len(self.axrt.images) > 0:
                self.axrt.images.pop()
            self.results_get_slider()
            self.O1_results_pb(True)
            self.O1_results_sd(True)
            self.results_init_graph()
            self.show_field()

    def results_init_graph(self):
        if self.calib:
            self.axrt.imshow(self.bsmp, cmap='gray', extent=[self.xmin, self.xmax, self.ymin, self.ymax], vmin=0, vmax=255)
            self.quivtxt = self.axrt.text(self.xref, self.y_rtext, '', color='r')
            self.axrt.set_xlabel('X (m)'), self.axrt.set_ylabel('Y (m)')
            self.axrt.set_ylim([self.yref - 0.05 * self.res * self.bsmp.shape[0],
                                self.ymax + 0.05 * self.res * self.bsmp.shape[0]])
            self.axrt.set_xlim([self.xmin - 0.05 * self.res * self.bsmp.shape[1],
                                self.xmax + 0.05 * self.res * self.bsmp.shape[1]])
        else:
            self.axrt.imshow(self.bsmp, cmap='gray', vmin=0, vmax=255)
            self.quivtxt = self.axrt.text(self.xref, self.y_rtext, '', color='r')
            self.axrt.set_xlabel('X (pix)'), self.axrt.set_ylabel('Y (pix)')
            self.axrt.set_ylim([1.1 * self.bsmp.shape[0], 0 - 0.05 * self.bsmp.shape[0]])
            self.axrt.set_xlim(
                [self.xmin - 0.05 * self.bsmp.shape[1], self.xmax + 0.05 * self.bsmp.shape[1]])
        self.chd_results.canvas.draw()

    def show_field(self):
        self.quiv = self.axrt.quiver(
            self.xrt, self.yrt, np.zeros_like(self.xrt), np.zeros_like(self.xrt),
            width=self.sl_w,
            scale=self.sl_scale,
            headwidth=self.sl_hw,
            headlength=self.sl_hl,
            color='r'
        )
        self.quiv_ref = self.axrt.quiver(
            self.xref, self.yref, 0, 0,
            width=self.sl_w,
            scale=self.sl_scale,
            headwidth=self.sl_hw,
            headlength=self.sl_hl,
            color='r'
        )
        if self.chd_results.radioButton_inst.isChecked() is True:
            if self.calib:
                idx = int(self.chd_results.listWidget_inst_vel.currentRow())
                self.quiv.U = self.uinstf[:, idx]
                self.quiv.V = self.vinstf[:, idx]
                maxvel = np.nanmax((self.uinstf[:, idx]**2+self.vinstf[:, idx]**2)**0.5)
                self.quiv_ref.U = maxvel
                self.quivtxt.set_text('Max : {0:5.4f} (m/s)'.format(maxvel))
            else:
                idx = int(self.chd_results.listWidget_inst_vel.currentRow())
                self.quiv.U = self.uinstf[:, idx]
                self.quiv.V = -self.vinstf[:, idx]
                maxvel = np.nanmax((self.uinstf[:, idx]**2+self.vinstf[:, idx]**2)**0.5)
                self.quiv_ref.U = maxvel
                self.quivtxt.set_text('Max : {0:5.4f} (pix/frame)'.format(maxvel))
        elif self.chd_results.radioButton_avg.isChecked() is True:
            if self.calib:
                self.quiv.U = self.umeanf
                self.quiv.V = self.vmeanf
                maxvel = np.nanmax((self.umeanf**2+self.vmeanf**2)**0.5)
                self.quiv_ref.U = maxvel
                self.quivtxt.set_text('Max : {0:5.4f} (m/s)'.format(maxvel))
            else:
                self.quiv.U = self.umeanf
                self.quiv.V = -self.vmeanf
                maxvel = np.nanmax((self.umeanf**2+self.vmeanf**2)**0.5)
                self.quiv_ref.U = maxvel
                self.quivtxt.set_text('Max : {0:5.4f} (pix/frame)'.format(maxvel))
        self.chd_results.canvas.draw()

    def results_clc_btn_field(self):
        self.chd_results.figure.clear()
        self.axrt = self.chd_results.figure.add_subplot(1, 1, 1)
        self.results_init_graph()
        self.show_field()

    def results_drag_slider(self):
        self.results_get_slider()
        self.quiv.scale, self.quiv_ref.scale = self.sl_scale, self.sl_scale
        self.quiv.headlength, self.quiv_ref.headlength = self.sl_hl, self.sl_hl
        self.quiv.headwidth, self.quiv_ref.headwidth = self.sl_hw, self.sl_hw
        self.quiv.width, self.quiv_ref.width = self.sl_w, self.sl_w
        self.chd_results.canvas.draw()

    def results_quiv_color_chg(self):
        cstr = ['r', 'y', 'g', 'c', 'b', 'm', 'w', 'k']
        cid = self.chd_results.comboBox.currentIndex()
        self.quiv.set_color(cstr[cid])
        # self.quiv_ref.set_color(cstr[cid])
        self.chd_results.canvas.draw()

    def val_filt_press(self, event):
        if event.inaxes != self.axvf.axes:
            return
        contains, attrd = self.axvf.contains(event)
        if not contains:
            return
        self.vf_press = [event.xdata, event.ydata]

    def val_filt_motion(self, event):
        if self.vf_press is None:
            return
        if event.inaxes != self.axvf.axes:
            return
        x0, y0 = self.vf_press
        xmv, ymv = event.xdata, event.ydata
        dx = xmv - x0
        dy = ymv - y0
        self.rect_vf.set_x(x0)
        self.rect_vf.set_y(y0)
        self.rect_vf.set_width(dx)
        self.rect_vf.set_height(dy)
        self.chd_val_filt.canvas.draw()

    def val_filt_rls(self, event):
        self.vf_press = None
        self.umin, self.vmax = self.rect_vf.xy
        self.umax, self.vmin = self.umin + self.rect_vf._width, self.vmax + self.rect_vf._height
        self.axvf.set_xlim([self.umin, self.umax])
        self.axvf.set_ylim([self.vmin, self.vmax])
        self.rect_vf.set_width(0), self.rect_vf.set_height(0)
        self.chd_val_filt.canvas.draw()
        self.uinstf, self.vinstf = piv.FilterCL95(self.uinst, self.vinst, self.grid_num_df, [self.umin, self.umax], [self.vmin, self.vmax])
        self.umeanf, self.vmeanf = np.nanmean(self.uinstf, axis=1), np.nanmean(self.vinstf, axis=1)
        self.show_field()

    def level_creator(self, mat_u, mat_v):
        all_mag = (mat_u**2 + mat_v**2)**0.5
        vmin = np.nanmin(all_mag)
        vmax = np.nanmax(all_mag)
        level = np.linspace(vmin, vmax, 10).tolist()
        # print(level)
        dl = level[1] - level[0]
        level = [level[0] - dl] + level + [level[-1] + dl]
        # for iid, i in enumerate(level):
        #     level[iid] = float('%.2f' % i)
        # print(level)
        return level

    def results_clc_btn_contour(self):
        self.chd_results.figure.clear()
        self.axrt = self.chd_results.figure.add_subplot(1, 1, 1)
        self.results_init_graph()
        step1 = max((np.nanmax(self.xrt) - np.nanmin(self.xrt)), np.nanmax(self.yrt) - np.nanmin(self.yrt)) / 200
        xstep = np.arange(np.nanmin(self.xrt), np.nanmax(self.xrt), step1)
        ystep = np.arange(np.nanmin(self.yrt), np.nanmax(self.yrt), step1)
        xi, yi = np.meshgrid(xstep, ystep)
        dvd = make_axes_locatable(self.axrt)
        cax = dvd.append_axes("right", size='2.5%', pad=0.5)

        if self.chd_results.radioButton_inst.isChecked() is True:
            idx = int(self.chd_results.listWidget_inst_vel.currentRow())
            u, v = self.uinstf[:, idx], self.vinstf[:, idx]
            velmag = (u**2 + v**2)**0.5
            maxvel = np.nanmax(velmag)
            vel_grid = griddata((self.xrt, self.yrt), velmag, (xi, yi), method='linear')
            level = self.level_creator(self.uinstf, self.vinstf)
            CS = self.axrt.contourf(xi, yi, vel_grid, level, cmap='inferno', alpha=0.9)
        elif self.chd_results.radioButton_avg.isChecked() is True:
            u, v = self.umeanf, self.vmeanf
            velmag = (u**2 + v**2)**0.5
            maxvel = np.nanmax(velmag)
            vel_grid = griddata((self.xrt, self.yrt), velmag, (xi, yi), method='linear')
            level = self.level_creator(self.umeanf, self.vmeanf)
            CS = self.axrt.contourf(xi, yi, vel_grid, level, cmap='inferno', alpha=0.9)

        self.show_field()
        self.quiv.set_color('w')
        self.quiv_ref.U = maxvel

        if self.calib:
            self.quiv.U, self.quiv.V = u, v
            cb = self.chd_results.figure.colorbar(CS, label='Velocity Magnitude (m/s)', cax=cax, ticks=level)
            self.quivtxt.set_text('Max : {0:5.4f} (m/s)'.format(maxvel))
        else:
            self.quiv.U, self.quiv.V = u, -v
            cb = self.chd_results.figure.colorbar(CS, label='Velocity Magnitude (pix/frame)', cax=cax, ticks=level)
            self.quivtxt.set_text('Max : {0:5.4f} (pix/frame)'.format(maxvel))
        self.chd_results.canvas.draw()
        self.chd_results.figure.tight_layout()

    def results_clc_btn_streamline(self):
        self.chd_results.figure.clear()
        self.axrt = self.chd_results.figure.add_subplot(1, 1, 1)
        self.results_init_graph()
        step1 = max((np.nanmax(self.xrt) - np.nanmin(self.xrt)), np.nanmax(self.yrt) - np.nanmin(self.yrt)) / 200
        xstep = np.arange(np.nanmin(self.xrt), np.nanmax(self.xrt), step1)
        ystep = np.arange(np.nanmin(self.yrt), np.nanmax(self.yrt), step1)
        xi, yi = np.meshgrid(xstep, ystep)
        dvd = make_axes_locatable(self.axrt)
        cax = dvd.append_axes("right", size='2.5%', pad=0.5)

        if self.chd_results.radioButton_inst.isChecked() is True:
            idx = int(self.chd_results.listWidget_inst_vel.currentRow())
            u, v = self.uinstf[:, idx], self.vinstf[:, idx]
            velmag = (u**2 + v**2)**0.5
            u_grid = griddata((self.xrt, self.yrt), u, (xi, yi), method='linear')
            v_grid = griddata((self.xrt, self.yrt), v, (xi, yi), method='linear')
            vel_grid = griddata((self.xrt, self.yrt), velmag, (xi, yi), method='linear')
            strm = self.axrt.streamplot(xi, yi, u_grid, v_grid, density=[1, 1], color=vel_grid, cmap='jet', linewidth=1)
        elif self.chd_results.radioButton_avg.isChecked() is True:
            u, v = self.umeanf, self.vmeanf
            velmag = (u**2 + v**2)**0.5
            u_grid = griddata((self.xrt, self.yrt), u, (xi, yi), method='linear')
            v_grid = griddata((self.xrt, self.yrt), v, (xi, yi), method='linear')
            vel_grid = griddata((self.xrt, self.yrt), velmag, (xi, yi), method='linear')
            strm = self.axrt.streamplot(xi, yi, u_grid, v_grid, density=[1, 1], color=vel_grid, cmap='jet', linewidth=1)
        if self.calib:
            cb = self.chd_results.figure.colorbar(strm.lines, label='Velocity Magnitude (m/s)', cax=cax)
        else:
            cb = self.chd_results.figure.colorbar(strm.lines, label='Velocity Magnitude (pix/frame)', cax=cax)
        self.chd_results.canvas.draw()
        self.chd_results.figure.tight_layout()

    def save_fig(self):
        sp = QFileDialog.getSaveFileName(self, "Save the current figure", self.root_path, "PNG Files (*png)")
        if not sp[0]: pass
        else:
            self.chd_results.figure.savefig(sp[0], dpi=300)

    def save_vel(self):
        keep_going = False
        fdir = os.path.join(self.root_path, "Filtered_vel")
        if not os.path.exists(fdir):
            os.mkdir(fdir)
            keep_going = True
        else:
            ls = os.listdir(fdir)
            if len(os.listdir(fdir)) != 0:
                reply = QMessageBox.warning(self, 'Warning', 'Directory is not empty!\nDo you want to cover it?',
                                        QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    try:
                        shutil.rmtree(fdir)
                        os.mkdir(fdir)
                        keep_going = True
                    except:
                        QMessageBox.warning(self, "Warning", "Can not re-create the directory!", QMessageBox.Ok,
                                            QMessageBox.Ok)
                else:
                    keep_going = False
            else:
                keep_going = True

        if keep_going:
            self.avgvel_df = pd.DataFrame(
                {'x': self.xrt, 'y': self.yrt, 'u_mean': self.umeanf.flatten(), 'v_mean': self.vmeanf.flatten()},
                index=list(range(len(self.yrt))),
                columns=['x', 'y', 'u_mean', 'v_mean']
            )
            self.avgvel_df = piv.save_vel(self.root_path, self.avgvel_df, self.uinstf, self.vinstf)
            QMessageBox.information(self, "Done", "Filtered data has been saved successfully!", QMessageBox.Ok, QMessageBox.Ok)

    def mpl_on_val_filt(self):
        self.cid_press_valfilt = self.chd_val_filt.canvas.mpl_connect('button_press_event', self.val_filt_press)
        self.cid_motion_valfilt = self.chd_val_filt.canvas.mpl_connect('motion_notify_event', self.val_filt_motion)
        self.cid_release_valfilt = self.chd_val_filt.canvas.mpl_connect('button_release_event', self.val_filt_rls)

    def O1_results_pb(self, O1):
        self.chd_results.pushButton_valuefilter.setEnabled(O1)
        self.chd_results.pushButton_polygon.setEnabled(O1)
        self.chd_results.pushButton_save_vel.setEnabled(O1)
        self.chd_results.pushButton_save.setEnabled(O1)
        self.chd_results.pushButton_field.setEnabled(O1)
        self.chd_results.pushButton_contour.setEnabled(O1)
        self.chd_results.pushButton_vorticity.setEnabled(O1)
        self.chd_results.pushButton_streamline.setEnabled(O1)
        self.chd_results.pushButton_profile.setEnabled(O1)
        self.chd_results.pushButton_discharge.setEnabled(O1)
        self.chd_results.listWidget_inst_vel.setEnabled(O1)
        self.chd_results.lineEdit_vel_dir.setEnabled(O1)
        self.chd_results.listWidget_inst_vel.setEnabled(O1)

    def O1_results_sd(self, O1):
        self.chd_results.horizontalSlider_q_width.setEnabled(O1)
        self.chd_results.horizontalSlider_q_head_width.setEnabled(O1)
        self.chd_results.horizontalSlider_q_head_length.setEnabled(O1)
        self.chd_results.horizontalSlider_q_scale.setEnabled(O1)
        self.chd_results.comboBox.setEnabled(O1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
