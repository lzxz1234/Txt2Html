# -*- coding: utf-8 -*-

import os

from PyQt4.QtGui import QGraphicsScene
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QPixmap
from PyQt4.QtGui import QFileDialog


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
            pix_map = QPixmap(file_path)
            self.addPixmap(pix_map)
