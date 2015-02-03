# -*- coding: utf-8 -*-

import os
import sys
import threading

from PyQt4 import QtCore
from PyQt4.Qt import SIGNAL
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QFileDialog
from PyQt4.QtGui import QSplashScreen, QPixmap

from util.File import scan
from ui.Model import ProcessModel
from ui.PortraitDisplayScene import PortraitDisplayScene
from ui.MainWindow import Ui_MainWindow
from db.SQLites import DB
from util.Log import Log
from trans import HtmlGenerator


reload(sys)
sys.setdefaultencoding('utf8')


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # uic.loadUi('ui/MainWindow.ui', self)
        self.setupUi(self)
        self.timer = QtCore.QTimer()
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
        self.imageFilePath.connect(self.imageFilePath,
                                   SIGNAL("textChanged(QString)"),
                                   self.refresh_image_list)
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
                                  lambda: threading.Thread(target=self.start_convert).start())
        # 日志定时刷新
        self.timer.connect(self.timer, SIGNAL("timeout()"), self.showLog)

        self.novelFilePath.setText(DB.get_param('LAST_NOVEL_PATH'))
        self.imageFilePath.setText(DB.get_param('LAST_IMAGE_PATH'))

        self.timer.start(100)
        Log.info(u'系统初始化完成...')

    def showLog(self):
        while True:
            if Log.messages.empty():
                break
            self.logBrowser.append(Log.messages.get())

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
        self.treeView.setModel(ProcessModel(self.treeView, novel_file_list))
        self.treeView.connect(self.treeView.selectionModel(),
                              SIGNAL("currentRowChanged(QModelIndex, QModelIndex)"),
                              self.save_and_load_novel_info)
        Log.info(u'加载小说目录[%s]完成'%dir_path)

    def refresh_image_list(self, dir_path):
        for novel in self.treeView.model().novels():
            desc, portrait = DB.query_novel_info(novel.title)
            if not os.path.exists(portrait):
                portrait = os.path.join(str(self.imageFilePath.text()), novel.title+'.jpg')
                if not os.path.exists(portrait):
                    portrait = os.path.join(str(self.imageFilePath.text()), novel.title+'.png')
                DB.save_novel_info(novel.title, desc, portrait)
        Log.info(u'加载封面目录[%s]完成'%dir_path)

    def save_and_load_novel_info(self, current, previous):
        # save previous first
        previous_novel = self.treeView.model().get_novel(previous)
        previous_file_desc = self.descBrowser.toPlainText()
        previous_file_icon = self.portraitView.scene().file_path
        if previous_file_desc or previous_file_icon:
            DB.save_novel_info(previous_novel.title, str(previous_file_desc), previous_file_icon)
        # load current
        selected_novel = self.treeView.model().get_novel(current)
        desc, portrait = DB.query_novel_info(selected_novel.title)
        self.descBrowser.setPlainText(desc)
        self.portraitView.scene().set_file(portrait)

    @staticmethod
    def update_input_text(input_):
        dialog = QFileDialog()
        dir_path = unicode(dialog.getExistingDirectory())
        if dir_path:
            input_.setText(dir_path)
        dialog.destroy()

    def getWidget(self, splash):
        t = QtCore.QElapsedTimer()
        t.start()
        while (t.elapsed() < 5000):
            str = QtCore.QString("times = ") + QtCore.QString.number(t.elapsed())
            splash.showMessage(str)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    splash_pix = QPixmap("resources/splash.png")
    splash = QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()

    window = MainWindow()
    splash.finish(window.getWidget(splash))
    window.show()
    sys.exit(app.exec_())
