# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')  #允许程序通过双击的形式执行

py2exe_options = {
        "includes": ["sip", "resources"],
        "dll_excludes": ["MSVCP90.dll",],
        "compressed": 1, #压缩文件
        "optimize": 2, #优化级别，默认为0
        "ascii": 0, #不自动包含encodings和codecs
        }

setup(
      name = 'PyQt Demo',
      version = '1.0',
      windows = ['main.py',],
      zipfile = None,
      options = {'py2exe': py2exe_options}
      )
