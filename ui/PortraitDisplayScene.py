# -*- coding: utf-8 -*-

from util.FileUtils import FileUtils
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
            selected_file = str(dialog.getOpenFileName(filter='*.jpg;*.png'))
            self.set_file(selected_file)

    def set_file(self, file_path):
        self.clear()
        self.file_path = file_path
        if file_path and FileUtils.exists(file_path):
            pix_map = QPixmap()
            pix_map.loadFromData(FileUtils.to_array(file_path)) #QPixmap(QString)构造函数不支持中文路径？
            self.addPixmap(pix_map)
