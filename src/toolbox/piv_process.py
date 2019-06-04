# -*- coding: utf-8 -*-
"""
Created on 2018/10/11 下午 02:30
@author: Ivan Chiu
"""

import numpy as np
import cv2
import src.toolbox.other as tool
import src.toolbox.image as imgtool
import os
import pandas as pd
from scipy.interpolate import interp1d
from scipy.interpolate import griddata
from scipy import signal
from matplotlib import pyplot as plt


def matchblob(cr1, cr2):
    """
    Find the nearest point for cr1 in cr2.
    :param cr1: the numpy array with shape (m, 2).
    :param cr2: the numpy array with shape (n, 2).
    :return: the list of matched points in cr1 and cr2.
    """
    # Calculate the distance between each blob:
    c2 = cr2[:, 0]
    r2 = cr2[:, 1]
    cr1n = []
    cr2n = []
    for i in range(cr1.shape[0]):
        c1 = cr1[i, 0]
        r1 = cr1[i, 1]
        dist12 = ((c2 - c1) ** 2 + (r2 - r1) ** 2) ** 0.5
        min_dis_id = np.argmin(dist12)
        min_dis = np.min(dist12)
        if min_dis <= 1:
            cr1n.append([c1, r1])
            cr2n.append([c2[min_dis_id], r2[min_dis_id]])

    return cr1n, cr2n


def cross_correlation(img1_path, img2_path, grid, param_df, mask=None):
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

    str1 = img1_name + ' and ' + img2_name + ': '
    str2 = 'Completed'
    tool.printProgressBar(0, grid.shape[0], prefix=str1, suffix=str2, length=50)

    # On each grid points:
    for g in range(grid.shape[0]):

        # get grid point (x, y):
        xg, yg = grid[g, :]

        # get cropped image on point:
        IA = img1[int(yg - ia_h/2): int(yg + ia_h/2), int(xg - ia_w/2): int(xg + ia_w/2)]
        IA = IA.flatten()

        SA_startrow = int(yg - ia_h/2 - sa_n)
        SA_endrow = int(yg + ia_h/2 + sa_s)
        SA_startcol = int(xg - ia_w/2 - sa_w)
        SA_endcol = int(xg + ia_w/2 + sa_e)
        ny = np.int(np.floor((SA_endrow - SA_startrow - ia_h) / 1)) + 1
        nx = np.int(np.floor((SA_endcol - SA_startcol - ia_w) / 1)) + 1
        SA = np.zeros([nx*ny, ia_h*ia_w])
        count = 0
        for i in range(ny):
            for j in range(nx):
                sub_sa = img2[SA_startrow + i: SA_startrow + i + ia_h, SA_startcol + j: SA_startcol + j + ia_w]
                SA[count, :] = sub_sa.flatten()
                count += 1

        # cross-correlation: subtract the mean of crop img:
        IA = IA - np.mean(IA)
        SA = SA - np.reshape(np.mean(SA, axis=1), [nx*ny, 1])
        r02 = np.sum(IA**2)
        matrix_cc = np.zeros([nx*ny])
        for rr in range(nx*ny):
            r01 = np.dot(IA, SA[rr, :])
            r03 = np.sum(SA[rr, :]**2)
            # cross-correlation: coefficient matrix:
            matrix_cc[rr] = r01 / (r02 * r03) ** 0.5

        matrix_cc = np.reshape(matrix_cc, [ny, nx])

        # Find the max coefficient index: (get only 1 index)
        iid, jid = np.unravel_index(np.argmax(matrix_cc), matrix_cc.shape)

        if jid != np.nan and iid != np.nan:
            if 1 <= jid <= matrix_cc.shape[1]-2 and 1 <= iid <= matrix_cc.shape[0]-2:
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

        tool.printProgressBar(g + 1, grid.shape[0], prefix=str1, suffix=str2, length=50)

    return DX, DY, sub_DX, sub_DY


def load_vel_data(project_folder):
    grid_num = pd.read_csv(os.path.join(project_folder, 'param', 'piv_grid_nx_ny.csv'))
    # load a temporary velocity file:
    instvel_folder = os.path.join(project_folder, "inst_vel")
    i_list = os.listdir(instvel_folder)
    instvellist = []
    for fl in sorted(i_list):
        instvellist.append(fl)

    temp = pd.DataFrame(pd.read_csv(os.path.join(instvel_folder, instvellist[0])))

    # initialize matrix:
    xnew = temp['x'].values
    ynew = temp['y'].values
    uinst = np.zeros([temp.shape[0], len(instvellist)])
    uinst[:] = np.nan
    vinst = np.zeros([temp.shape[0], len(instvellist)])
    vinst[:] = np.nan

    # get each column:
    for listID in range(len(instvellist)):
        velfile = pd.DataFrame(pd.read_csv(os.path.join(instvel_folder, instvellist[listID])))
        uinst[:, listID] = velfile['u'].values
        vinst[:, listID] = velfile['v'].values

    return xnew, ynew, uinst, vinst, grid_num


def FilterCL95(uinst, vinst, grid_num, ulim, vlim):
    num_x, num_y = grid_num['j_num'][0], grid_num['i_num'][0]
    umin, umax = ulim
    vmin, vmax = vlim

    xqg, yqg = np.arange(0, num_x), np.arange(0, num_y)
    xx, yy = np.meshgrid(xqg, yqg)

    unew = np.zeros_like(uinst)
    unew[:] = np.nan
    vnew = np.zeros_like(uinst)
    vnew[:] = np.nan

    unew = np.where((uinst < umin) | (uinst > umax) | (vinst < vmin) | (vinst > vmax), np.nan, uinst)
    vnew = np.where((uinst < umin) | (uinst > umax) | (vinst < vmin) | (vinst > vmax), np.nan, vinst)

    for fid in range(uinst.shape[1]):
        u_matrix = np.reshape(unew[:, fid], [num_y, num_x])
        u_gd = np.ma.masked_invalid(u_matrix)
        xx1, yy1 = xx[~u_gd.mask], yy[~u_gd.mask]
        u_gd_1 = u_gd[~u_gd.mask]
        u_temp = griddata((xx1, yy1), u_gd_1.ravel(), (xx, yy), method='linear')
        unew[:, fid] = np.reshape(u_temp, [num_x*num_y])

        v_matrix = np.reshape(vnew[:, fid], [num_y, num_x])
        v_gd = np.ma.masked_invalid(v_matrix)
        xx1, yy1 = xx[~v_gd.mask], yy[~v_gd.mask]
        v_gd_1 = v_gd[~v_gd.mask]
        v_temp = griddata((xx1, yy1), v_gd_1.ravel(), (xx, yy), method='linear')
        vnew[:, fid] = np.reshape(v_temp, [num_x*num_y])
    return unew, vnew


def save_vel(project_folder, avgvel_df, unew, vnew):
    instvel_folder = os.path.join(project_folder, "inst_vel")
    i_list = os.listdir(instvel_folder)
    instvellist = []
    for fl in sorted(i_list):
        instvellist.append(fl)

    ufilt = avgvel_df['u_mean'].values
    vfilt = avgvel_df['v_mean'].values
    for listID in range(len(instvellist)):
        unew[:, listID] = np.where(ufilt == np.nan, np.nan, unew[:, listID])
        vnew[:, listID] = np.where(vfilt == np.nan, np.nan, vnew[:, listID])
        velname = instvellist[listID].split('inst_')[1]
        filter_df = pd.DataFrame(
            {'x': avgvel_df['x'].values, 'y': avgvel_df['y'].values, 'u': unew[:, listID], 'v': vnew[:, listID]},
            index=list(range(len(avgvel_df['x'].values))),
            columns=['x', 'y', 'u', 'v']
        )
        filtdataname = 'vel_{0:s}'.format(velname)
        filter_df.to_csv(os.path.join(project_folder, "Filtered_vel", filtdataname), index=False)

    avgvel_df.to_csv(os.path.join(project_folder, "average_vel.csv"), index=False)
    return avgvel_df