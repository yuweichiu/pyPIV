# -*- coding: utf-8 -*-
"""
Created on 2018/9/24 下午 07:57
@author: Ivan Chiu
"""

from matplotlib import pyplot as plt
from matplotlib.widgets import RectangleSelector
from matplotlib.patches import Rectangle as RT
from matplotlib.patches import Polygon as PG
from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.path as mpt
import numpy as np
import cv2
import os
from scipy import signal, sparse


def zoom_in(ax, base_scale=1.5):
    def zoom_event(event):
        # get the current x and y limits
        cur_xlim = ax.get_xlim()
        cur_ylim = ax.get_ylim()
        # set the range
        cur_xrange = (cur_xlim[1] - cur_xlim[0]) * .5
        cur_yrange = (cur_ylim[1] - cur_ylim[0]) * .5
        xdata = event.xdata  # get event x location
        ydata = event.ydata  # get event y location
        if event.button == 'up':
            # deal with zoom in
            scale_factor = 1 / base_scale
        elif event.button == 'down':
            # deal with zoom out
            scale_factor = base_scale
        else:
            # deal with something that should never happen
            scale_factor = 1
            print(event.button)
        # set new limits
        new_xlim = [xdata - cur_xrange * scale_factor,
                     xdata + cur_xrange * scale_factor]
        new_ylim = [ydata - cur_yrange * scale_factor,
                     ydata + cur_yrange * scale_factor]
        ax.set_xlim(new_xlim)
        ax.set_ylim(new_ylim)

        ax.figure.canvas.draw()  # force re-draw

    fig = ax.get_figure()  # get the figure of interest
    # attach the call back
    fig.canvas.mpl_connect('scroll_event', zoom_event)

    # return the function
    return zoom_event


def zoom_in_2ax(ax1, ax2, base_scale=1.5):
    """ Used for GUI in checking the intensity threshold. """
    def zoom_event(event):
        # get the current x and y limits
        cur_xlim = ax1.get_xlim()
        cur_ylim = ax1.get_ylim()
        # set the range
        cur_xrange = (cur_xlim[1] - cur_xlim[0]) * .5
        cur_yrange = (cur_ylim[1] - cur_ylim[0]) * .5
        xdata = event.xdata  # get event x location
        ydata = event.ydata  # get event y location
        if event.button == 'up':
            # deal with zoom in
            scale_factor = 1 / base_scale
        elif event.button == 'down':
            # deal with zoom out
            scale_factor = base_scale
        else:
            # deal with something that should never happen
            scale_factor = 1
            print(event.button)
        # set new limits
        new_xlim = [xdata - cur_xrange * scale_factor,
                     xdata + cur_xrange * scale_factor]
        new_ylim = [ydata - cur_yrange * scale_factor,
                     ydata + cur_yrange * scale_factor]
        ax1.set_xlim(new_xlim)
        ax1.set_ylim(new_ylim)
        ax2.set_xlim(new_xlim)
        ax2.set_ylim(new_ylim)

        ax1.figure.canvas.draw()  # force re-draw
        ax2.figure.canvas.draw()  # force re-draw

    fig1 = ax1.get_figure()  # get the figure of interest
    fig2 = ax2.get_figure()  # get the figure of interest
    # attach the call back
    fig1.canvas.mpl_connect('scroll_event', zoom_event)
    fig2.canvas.mpl_connect('scroll_event', zoom_event)

    # return the function
    return zoom_event


def make_grid(start, end, step, end_point=True):
    """
    Make grid numpy array.
    :param start: list [x, y]
    :param end: list [x, y]
    :param step: list [x, y]
    :return: grid array [x, y]
    """
    if end_point:
        x_ar = np.arange(start[0], end[0] + 1e-10, step[0])
        y_ar = np.arange(start[1], end[1] + 1e-10, step[1])
    else:
        x_ar = np.arange(start[0], end[0], step[0])
        y_ar = np.arange(start[1], end[1], step[1])
    xx, yy = np.meshgrid(x_ar, y_ar)
    x_col = np.reshape(xx, [-1, 1])
    y_col = np.reshape(yy, [-1, 1])
    grid = np.column_stack([x_col, y_col])
    return grid
