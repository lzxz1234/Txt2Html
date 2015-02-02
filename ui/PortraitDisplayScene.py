# -*- coding: utf-8 -*-

import os
import StringIO

from PIL import Image
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QGraphicsScene
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QPixmap
from PyQt4.QtGui import QFileDialog
from util.File import read


class PortraitDisplayScene(QGraphicsScene):

    file_path = None

    def __init__(self, *args):
        QGraphicsScene.__init__(self, *args)

    def mousePressEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            dialog = QFileDialog()
            selected_file = unicode(dialog.getOpenFileName(filter='*.jpg;*.png')) #解决中文路径问题
            self.set_file(selected_file)

    def set_file(self, file_path):
        self.clear()
        self.file_path = file_path
        if file_path and os.path.exists(file_path):
            pix_map = QPixmap()
            if file_path.endswith('.jpg'):
                jpg_data = read(file_path)
                str_io = StringIO.StringIO(jpg_data)
                img = Image.open(str_io)
                png_data = StringIO.StringIO()
                img.save(png_data, format='png')
                pix_map.loadFromData(QtCore.QByteArray(png_data.getvalue()))
            else:
                pix_map.load(file_path)
            self.addPixmap(pix_map)
