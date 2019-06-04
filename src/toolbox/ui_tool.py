# -*- coding: utf-8 -*-
"""
@author: Ivan Y.W.Chiu
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox, QTableWidgetItem, QListWidgetItem
from PyQt5.QtCore import QThread, pyqtSignal


def tabel_cleaner(object):
    if not object:
        pass
    else:
        while object.rowCount() > 0:
            object.removeRow(0)
    return object


def figure_cleaner(object):
    if not object:
        pass
    else:
        object.clear()
    return object


def list_cleaner(object):
    if not object:
        pass
    else:
        while object.count() > 0:
            object.clear()
    return object
