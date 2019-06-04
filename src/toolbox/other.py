# -*- coding: utf-8 -*-
"""
Created on 2018/9/25 上午 11:02
@author: Ivan Chiu
"""

import os
import sys

def clear_folder(path):
    for the_file in os.listdir(path):
        filepath = os.path.join(path, the_file)
        try:
            if os.path.isfile(filepath):
                os.unlink(filepath)

        except Exception:
            print('Clear All file')

def printProgressBar(iteration, total, prefix='', suffix='', length=100, fill='#'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str) █, >, O, #, =
    """
    percent = 100 * (iteration / float(total))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + ' ' * (length - filledLength)
    sys.stdout.write(
        '\r{0:s}|{1:s}| {2:>5.1f}% [{3:s}]'.format(prefix, bar, percent, suffix)
    )

    # Print New Line on Complete
    if iteration == total:
        sys.stdout.write('\n')
