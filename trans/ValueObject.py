# -*- coding: utf-8 -*-
__author__ = 'lzxz1234@gmail.com'

import os
import re
from codecs import open

from db.SQLites import DB


class NovelInfo():

    seq = 1

    def __init__(self):
        self._seq = str(NovelInfo.seq)
        NovelInfo.seq += 1
        self._title = None
        self._file_path = None
        self._file_name = None
        self.db = DB()

    @staticmethod
    def fromFile(novel_path):
        result = NovelInfo()
        result._file_path = novel_path
        result._file_name = os.path.split(novel_path)[1]
        result._title = os.path.basename(novel_path).split('.')[0]
        return result

    @property
    def volumes(self):
        volumes = []
        seq = 1
        p = re.compile(u'(§+)\s*([^\r\n]+)([^§]+)')
        for encode in ['utf8', 'gb2312', 'gb18030']:
            fileInput = open(self._file_path, encoding=encode)
            try :
                allText = fileInput.read()
                last_volume = None
                for flag, name, content in p.findall(allText):
                    chapter = Chapter()
                    chapter._name = name
                    chapter._safe_name = str(seq)
                    seq += 1
                    chapter._content = content
                    if flag == u"§§":
                        last_volume = chapter
                        volumes.append(chapter)
                    else:
                        if not last_volume:
                            last_volume = Chapter()
                            chapter._name = self.title
                            volumes.append(last_volume)
                        last_volume.addChapter(chapter)
                break
            except UnicodeDecodeError:
                continue
            finally :
                fileInput.close()
        return volumes

    @property
    def desc(self):
        desc, portrait = self.db.query_novel_info(os.path.split(self._file_name)[1])
        return desc or ''

    @property
    def file_name(self):
        return self._file_name

    @property
    def title(self):
        return self._title

    @property
    def safe_title(self):
        return self._seq

class Chapter():

    def __init__(self):
        self._name = None
        self._content = None
        self._sub_chapters = []
        self._safe_name = None

    def addChapter(self, chapter):
        self._sub_chapters.append(chapter)

    @property
    def sub_chapters(self):
        return self._sub_chapters

    @property
    def name(self):
        return self._name

    @property
    def safe_name(self):
        return self._safe_name

    @property
    def content(self):
        return self._content