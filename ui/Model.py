# -*- coding: utf-8 -*-

import os

from PyQt4.QtCore import QAbstractTableModel
from PyQt4.QtCore import QModelIndex, QVariant, Qt
from PyQt4.QtCore import QString


class ProcessModel(QAbstractTableModel):

    def __init__(self, parent, file_list):
        super(ProcessModel, self).__init__(parent)
        self._file_list = file_list or []
        self.headers = [u'序号', u'名称']

    def rowCount(self, index=QModelIndex(), *args, **kwargs):
        return len(self._file_list)

    def columnCount(self, index=QModelIndex(), *args, **kwargs):
        return 2

    def get_file(self, index):
        return self._file_list[index.row()]

    def files(self):
        return self._file_list

    def data(self, index, role=None):
        row, col = index.row(), index.column()

        if not index.isValid() or not (0 <= row < self.rowCount()) or not (0 <= col < self.columnCount()):
            return QVariant()

        if role == Qt.TextAlignmentRole:
            if col == 0:
                return Qt.AlignVCenter
            else:
                return Qt.AlignLeft
        elif role == Qt.DisplayRole:
            if col == 0:
                return QString(str(row + 1))
            elif col == 1:
                return QVariant(os.path.basename(self._file_list[row]))
        elif role == Qt.ToolTipRole:
            if col == 1:
                return QVariant(self._file_list[row])

        return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]