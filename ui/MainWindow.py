# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Workspaces\Python\Txt2Html\ui\MainWindow.ui'
#
# Created: Mon Feb 02 09:44:54 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(789, 635)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.logBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.logBrowser.setAcceptRichText(False)
        self.logBrowser.setObjectName(_fromUtf8("logBrowser"))
        self.gridLayout.addWidget(self.logBrowser, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.novelLabel = QtGui.QLabel(self.centralwidget)
        self.novelLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.novelLabel.setObjectName(_fromUtf8("novelLabel"))
        self.horizontalLayout_2.addWidget(self.novelLabel)
        self.novelFilePath = QtGui.QLineEdit(self.centralwidget)
        self.novelFilePath.setReadOnly(True)
        self.novelFilePath.setObjectName(_fromUtf8("novelFilePath"))
        self.horizontalLayout_2.addWidget(self.novelFilePath)
        self.novelFileSelector = QtGui.QPushButton(self.centralwidget)
        self.novelFileSelector.setObjectName(_fromUtf8("novelFileSelector"))
        self.horizontalLayout_2.addWidget(self.novelFileSelector)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setRootIsDecorated(False)
        self.treeView.setItemsExpandable(False)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.horizontalLayout.addWidget(self.treeView)
        self.descBrowser = QtGui.QPlainTextEdit(self.centralwidget)
        self.descBrowser.setReadOnly(False)
        self.descBrowser.setMaximumBlockCount(0)
        self.descBrowser.setObjectName(_fromUtf8("descBrowser"))
        self.horizontalLayout.addWidget(self.descBrowser)
        self.portraitView = QtGui.QGraphicsView(self.centralwidget)
        self.portraitView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.portraitView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.portraitView.setBackgroundBrush(brush)
        self.portraitView.setInteractive(True)
        self.portraitView.setRenderHints(QtGui.QPainter.Antialiasing)
        self.portraitView.setCacheMode(QtGui.QGraphicsView.CacheNone)
        self.portraitView.setObjectName(_fromUtf8("portraitView"))
        self.horizontalLayout.addWidget(self.portraitView)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.imageLabel = QtGui.QLabel(self.centralwidget)
        self.imageLabel.setObjectName(_fromUtf8("imageLabel"))
        self.horizontalLayout_5.addWidget(self.imageLabel)
        self.imageFilePath = QtGui.QLineEdit(self.centralwidget)
        self.imageFilePath.setReadOnly(True)
        self.imageFilePath.setObjectName(_fromUtf8("imageFilePath"))
        self.horizontalLayout_5.addWidget(self.imageFilePath)
        self.imageFileSelector = QtGui.QPushButton(self.centralwidget)
        self.imageFileSelector.setObjectName(_fromUtf8("imageFileSelector"))
        self.horizontalLayout_5.addWidget(self.imageFileSelector)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.startConvert = QtGui.QPushButton(self.centralwidget)
        self.startConvert.setObjectName(_fromUtf8("startConvert"))
        self.horizontalLayout_3.addWidget(self.startConvert)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.m_file = QtGui.QMenu(self.menubar)
        self.m_file.setObjectName(_fromUtf8("m_file"))
        self.m_help = QtGui.QMenu(self.menubar)
        self.m_help.setObjectName(_fromUtf8("m_help"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.a_open = QtGui.QAction(MainWindow)
        self.a_open.setObjectName(_fromUtf8("a_open"))
        self.a_save = QtGui.QAction(MainWindow)
        self.a_save.setObjectName(_fromUtf8("a_save"))
        self.a_exit = QtGui.QAction(MainWindow)
        self.a_exit.setObjectName(_fromUtf8("a_exit"))
        self.a_tutorial = QtGui.QAction(MainWindow)
        self.a_tutorial.setObjectName(_fromUtf8("a_tutorial"))
        self.a_about = QtGui.QAction(MainWindow)
        self.a_about.setObjectName(_fromUtf8("a_about"))
        self.a_text_dir__select = QtGui.QAction(MainWindow)
        self.a_text_dir__select.setObjectName(_fromUtf8("a_text_dir__select"))
        self.a_icon_dir_select = QtGui.QAction(MainWindow)
        self.a_icon_dir_select.setObjectName(_fromUtf8("a_icon_dir_select"))
        self.a_portrait_select = QtGui.QAction(MainWindow)
        self.a_portrait_select.setObjectName(_fromUtf8("a_portrait_select"))
        self.m_file.addAction(self.a_open)
        self.m_file.addAction(self.a_save)
        self.m_file.addSeparator()
        self.m_file.addAction(self.a_exit)
        self.m_help.addAction(self.a_tutorial)
        self.m_help.addSeparator()
        self.m_help.addAction(self.a_about)
        self.menu.addAction(self.a_text_dir__select)
        self.menu.addAction(self.a_icon_dir_select)
        self.menubar.addAction(self.m_file.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.m_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.a_exit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.a_text_dir__select, QtCore.SIGNAL(_fromUtf8("triggered()")), self.novelFileSelector.click)
        QtCore.QObject.connect(self.a_icon_dir_select, QtCore.SIGNAL(_fromUtf8("triggered()")), self.imageFileSelector.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "小说网页生成器", None))
        self.novelLabel.setText(_translate("MainWindow", "选择文本文件所在目录：", None))
        self.novelFileSelector.setText(_translate("MainWindow", "...", None))
        self.imageLabel.setText(_translate("MainWindow", "选择图片文件所在目录：", None))
        self.imageFileSelector.setText(_translate("MainWindow", "...", None))
        self.startConvert.setText(_translate("MainWindow", "开始转换", None))
        self.m_file.setTitle(_translate("MainWindow", "文件", None))
        self.m_help.setTitle(_translate("MainWindow", "帮助", None))
        self.menu.setTitle(_translate("MainWindow", "编辑", None))
        self.a_open.setText(_translate("MainWindow", "打开", None))
        self.a_open.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.a_save.setText(_translate("MainWindow", "保存", None))
        self.a_save.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.a_exit.setText(_translate("MainWindow", "退出", None))
        self.a_exit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.a_tutorial.setText(_translate("MainWindow", "使用说明", None))
        self.a_tutorial.setShortcut(_translate("MainWindow", "Ctrl+T", None))
        self.a_about.setText(_translate("MainWindow", "关于", None))
        self.a_about.setShortcut(_translate("MainWindow", "Ctrl+H", None))
        self.a_text_dir__select.setText(_translate("MainWindow", "选择小说所在路径", None))
        self.a_icon_dir_select.setText(_translate("MainWindow", "选择封面所在路径", None))
        self.a_portrait_select.setText(_translate("MainWindow", "选择封面", None))
