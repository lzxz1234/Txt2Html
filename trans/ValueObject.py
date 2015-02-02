# -*- coding: utf-8 -*-
__author__ = 'lzxz1234@gmail.com'

import os
import re
from codecs import open

from db.SQLites import DB


class Seq():

    seq = 1

    def __init__(self):
        self.seq = str(Seq.seq)
        Seq.seq += 1

class NovelInfo(Seq):

    def __init__(self):
        Seq.__init__(self)
        self._volumes = []
        self._title = None
        self._file = None

    @staticmethod
    def fromFile(novel_path):
        p = re.compile(u'(§+)\s*([^\r\n]+)([^§]+)')
        result = NovelInfo()
        for encode in ['utf8', 'gb2312', 'gb18030']:
            fileInput = open(novel_path, encoding=encode)
            try :
                allText = fileInput.read()
                result._file = os.path.split(novel_path)[1]
                result._title = os.path.basename(novel_path).split('.')[0]
                last_volume = None
                for flag, name, content in p.findall(allText):
                    chapter = Chapter()
                    chapter.name = name
                    chapter.content = content
                    if flag == u"§§":
                        last_volume = chapter
                        result.add_volume(chapter)
                    else:
                        if not last_volume:
                            last_volume = Chapter()
                            chapter.name = result.title
                            result.add_volume(last_volume)
                        last_volume.addChapter(chapter)
                break
            except UnicodeDecodeError as e:
                continue
            finally :
                fileInput.close()
        return result

    @property
    def volumes(self):
        return self._volumes

    @property
    def desc(self):
        desc, portrait = DB.query_novel_info(self.file_name)
        return desc or ''

    def add_volume(self, volume):
        self._volumes.append(volume)

    @property
    def file(self):
        return self._file

    @property
    def file_name(self):
        return os.path.split(self._file)[1]

    @property
    def title(self):
        return self._title

    @property
    def safe_title(self):
        return self.seq

class Chapter(Seq):

    def __init__(self):
        Seq.__init__(self)
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

    @property
    def safe_name(self):
        return self.seq

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        self._content = content