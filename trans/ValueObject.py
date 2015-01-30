# -*- coding: utf-8 -*-
__author__ = 'lzxz1234@gmail.com'

import os
import re
from codecs import open

from util.Log import Log


class NovelInfo():

    def __init__(self):
        self._volumes = []
        self._title = None

    @staticmethod
    def fromFile(novel_path):
        p = re.compile(r'(§+)\s*([^\r\n]+)([^§]+)')
        if novel_path.endswith("txt"):
            for encode in ['utf8', 'gb2312', 'gb18030']:
                fileInput = open(novel_path, encoding=encode)
                try :
                    allText = fileInput.read()
                    result = NovelInfo()
                    result.title = os.path.basename(novel_path).split('.')[0]
                    last_volume = None
                    for flag, name, content in p.findall(allText):
                        chapter = Chapter()
                        chapter.name = name
                        chapter.content = content
                        if flag == u"§§":
                            result._volumes.append(chapter)
                        else:
                            last_volume.addChapter(chapter)
                    return result
                except UnicodeDecodeError as e:
                    continue
                finally :
                    fileInput.close()
        else:
            Log.warn(u'文件[%s]格式错误，预期格式为[txt]'%novel_path)
        return None

    @property
    def volumes(self):
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        self._volumes = volumes

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

class Chapter():

    def __init__(self):
        self._name = None
        self._content = None
        self._sub_chapters = []

    def addChapter(self, chapter):
        self._sub_chapters.append(chapter)

    @property
    def sub_chapters(self):
        return self._sub_chapters

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        self._content = content