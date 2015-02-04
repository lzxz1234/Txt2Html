# -*- coding: utf-8 -*-

import os
import shutil

from jinja2 import Environment, FileSystemLoader

from db.SQLites import DB
from util.Log import Log
from util.File import write, cur_file_dir


env = Environment(loader=FileSystemLoader(os.path.join(cur_file_dir(), 'resources')))

def genAll(novels, target_html_dir):
    db = DB()
    for novel in novels:
        Log.info(u'处理文件[%s]'%novel.file)
        novel_cur_dir = os.path.join(target_html_dir, novel.safe_title)
        if not os.path.exists(novel_cur_dir):
            os.mkdir(novel_cur_dir)
        write(novel_cur_dir, 'index.html', genNovelIndex(novel))
        desc, portrait = db.query_novel_info(novel.title)
        if portrait:
            shutil.copy(portrait, os.path.join(novel_cur_dir, 'post.jpg'))
        else:
            Log.warn(u'小说[%s]未找到封面图片'%novel.title)
        for volume in novel.volumes:
            if volume.content:
                write(novel_cur_dir, volume.safe_name+'.html', genChapter(volume, volume))
            for chapter in volume.sub_chapters:
                write(novel_cur_dir, volume.safe_name+'-'+chapter.safe_name+'.html', genChapter(volume, chapter))
    write(target_html_dir, 'index.html', genIndex(novels))

def genIndex(novels):
    return env.get_template('index.html').render(list=novels)

def genNovelIndex(novel):
    return env.get_template('novel-index.html').render(novel=novel)

def genChapter(volume, chapter):
    return env.get_template('chapter.html').render(volume = volume, chapter = chapter)
