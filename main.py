from scipy.fft import fft
import scipy.signal as sig
import numpy as np
import pandas as pd
import pyqtgraph as pg
import os
import time
import pyqtgraph as pg
from matplotlib.figure import Figure
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog,QDialog, QGraphicsScene ,QLabel , QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from PyQt5 import QtWidgets, uic 
from cmath import*
from numpy import *
import sys
import matplotlib
matplotlib.use('Qt5Agg')
from Image import Image as ig

class MyDialog(QtWidgets.QDialog):
    def __init__(self):
        super(MyDialog, self).__init__()
        # Load the UI Page
        uic.loadUi(r'mixer.ui', self)

    

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Load the UI Page
        uic.loadUi(r'task4.ui', self)

        #button connection
        self.component_btn.clicked.connect(self.open_dialog)

        image_graphs = [self.image1, self.image2, self.image3, self.image4]
        ft_image_graphs = [self.ft_compo_1, self.ft_compo_2, self.ft_compo_3, self.ft_compo_4]
        self.combos = [self.ft_combo1, self.ft_combo2, self.ft_combo3, self.ft_combo4]
        # Create a list to store Image instances and associated QLabel objects
        self.images = [ig(graph, ft_image, self.combos) for graph, ft_image in zip(image_graphs, ft_image_graphs)]

        #Connections
        # Connect combobox signals to the corresponding check_combo method
        self.ft_combo1.activated.connect(lambda: self.combo_activated(0))
        self.ft_combo2.activated.connect(lambda: self.combo_activated(1))
        self.ft_combo3.activated.connect(lambda: self.combo_activated(2))
        self.ft_combo4.activated.connect(lambda: self.combo_activated(3))
        # Connect double-click events to each QLabel using a loop
        for label, image_instance in zip(image_graphs, self.images):
            label.mouseDoubleClickEvent = lambda event, instance=image_instance: self.double_click_event(event, instance)

    def double_click_event(self, event, image_instance):
        if event.button() == Qt.LeftButton:
            image_instance.Browse()
    

    def combo_activated(self, index):
        for i, image_instance in enumerate(self.images):
            if i == index:
                # Update the selected combo box
                image_instance.check_combo(index)
            else:
                # Reset other combo boxes or perform other actions if needed
                pass


    def open_dialog(self):
        # Create an instance of the custom dialog
        Mixer = MyDialog()

        # Show the dialog
        Mixer.exec_()

        self.output_channels_controlers = {
            'Output 1': {
                'select1 img': '',
                'select2 img': '',
                'slider1 val': 0,
                'slider2 va;': 0,
                'type1': '',
                'type2': ''
            },
            'Output 2': {
                'select1 img': '',
                'select2 img': '',
                'slider1 val': 0,
                'slider2 val': 0,
                'type1': '',
                'type2': ''
            }
        }
        
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
