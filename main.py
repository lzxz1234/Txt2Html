# -*- coding: utf-8 -*-

import os
import sys
import shutil

from PyQt4 import uic
from PyQt4.Qt import SIGNAL
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QFileDialog

from util.File import scan, write
from ui.Model import ProcessModel
from ui.PortraitDisplayScene import PortraitDisplayScene
from db.SQLites import DB
from util.Log import Log
from trans import HtmlGenerator

reload(sys)
sys.setdefaultencoding('utf8')


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui/MainWindow.ui', self)

        Log.console = self.logBrowser
        Log.status_bar = self.statusbar
        self.portraitView.setScene(PortraitDisplayScene())
        # 选择小说内容所在目录
        self.novelFileSelector.connect(self.novelFileSelector,
                                       SIGNAL("clicked()"),
                                       lambda: self.update_input_text(self.novelFilePath))
        # 选择小说封面所在目录
        self.imageFileSelector.connect(self.imageFileSelector,
                                       SIGNAL("clicked()"),
                                       lambda: self.update_input_text(self.imageFilePath))
        # 内容目录更改后同步更新左面列表
        self.novelFilePath.connect(self.novelFilePath,
                                   SIGNAL("textChanged(QString)"),
                                   self.refresh_file_list)
        # 内容目录更改后保存到历史记录
        self.novelFilePath.connect(self.novelFilePath,
                                   SIGNAL("textChanged(QString)"),
                                   lambda x: DB.save_param('LAST_NOVEL_PATH', str(x)))
        # 图片目录更改后保存到历史记录
        self.imageFilePath.connect(self.imageFilePath,
                                   SIGNAL("textChanged(QString)"),
                                   lambda x: DB.save_param('LAST_IMAGE_PATH', str(x)))
        # 开始转换
        self.startConvert.connect(self.startConvert,
                                  SIGNAL("clicked()"),
                                  self.start_convert)

        self.novelFilePath.setText(DB.get_param('LAST_NOVEL_PATH'))
        self.imageFilePath.setText(DB.get_param('LAST_IMAGE_PATH'))

        Log.info(u'系统初始化完成...')

    def start_convert(self):
        Log.info(u'-------------------------开始生成 HTML-------------------------')
        novel_root_dir = unicode(self.novelFilePath.text())
        target_html_dir = os.path.join(novel_root_dir, 'html')
        if not os.path.exists(target_html_dir):
            os.makedirs(target_html_dir)

        Log.info(u'输出目录定位到：%s'%target_html_dir)
        HtmlGenerator.genAll(self.treeView.model().novels(), target_html_dir)
        Log.info(u'--------------------------任-务-完-成--------------------------')

    def refresh_file_list(self, dir_path):
        novel_file_list = scan(unicode(dir_path))
        Log.debug(u'加载[%s]目录共扫描到[%s]个文件'%(dir_path, len(novel_file_list)))
        self.treeView.setModel(ProcessModel(self.treeView, novel_file_list))
        self.treeView.connect(self.treeView.selectionModel(),
                              SIGNAL("currentRowChanged(QModelIndex, QModelIndex)"),
                              self.save_and_load_novel_info)

    def save_and_load_novel_info(self, current, previous):
        # save previous first
        previous_novel = self.treeView.model().get_novel(previous)
        previous_file_desc = self.descBrowser.toPlainText()
        previous_file_icon = self.portraitView.scene().file_path
        if previous_file_desc or previous_file_icon:
            if str(previous_file_desc):
                DB.save_novel_info(previous_novel.title, str(previous_file_desc))
            if os.path.exists(previous_file_icon):
                DB.save_novel_portrait(previous_novel.title, previous_file_icon)
        # load current
        selected_novel = self.treeView.model().get_novel(current)
        self.descBrowser.setPlainText(DB.query_novel_info(selected_novel.title))
        portrait_file = DB.query_novel_portrait(selected_novel.title)
        if not os.path.exists(portrait_file):
            novel_name, novel_suffix = os.path.splitext(selected_novel.title)
            portrait_file = os.path.join(str(self.imageFilePath.text()), novel_name+'.jpg')
            if not os.path.exists(portrait_file):
                portrait_file = os.path.join(str(self.imageFilePath.text()), novel_name+'.png')
        self.portraitView.scene().set_file(portrait_file)

    @staticmethod
    def update_input_text(input_):
        dialog = QFileDialog()
        dir_path = unicode(dialog.getExistingDirectory())
        if dir_path:
            input_.setText(dir_path)
        dialog.destroy()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
