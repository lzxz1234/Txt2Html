# -*- coding: utf-8 -*-

import os
from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))
def genIndex(novels):
    return env.get_template('index.html').render(list=novels)

def genNovelIndex(novel):
    return env.get_template('novel-index.html').render(novel=novel)

def genChapter(volume, chapter):
    return env.get_template('chapter.html').render(volume = volume, chapter = chapter)
