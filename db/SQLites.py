# -*- coding: utf-8 -*-

import sqlite3
import os

from util.Log import Log
from util.File import cur_file_dir


class DB(object):

    db_path = os.path.join(cur_file_dir(), 'repository.sqlite')
    conn = sqlite3.connect(db_path)
    conn.isolation_level = None
    conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")
    conn.execute('CREATE TABLE IF NOT EXISTS NOVEL_INFO('
                 'ID INTEGER PRIMARY KEY AUTOINCREMENT, '
                 'NAME VARCHAR(100), '
                 'PORTRAIT VARCHAR(1000), '
                 'DESCRIPTION VARCHAR(2000) )')
    conn.execute('CREATE TABLE IF NOT EXISTS PARAMETER(ID INTEGER PRIMARY KEY '
                 'AUTOINCREMENT, NAME VARCHAR(20), VALUE VARCHAR(100))')

    @staticmethod
    def get_param(name):
        cur = DB.conn.cursor()
        cur.execute('SELECT VALUE FROM PARAMETER WHERE NAME = ?', (name, ))
        target_line = cur.fetchone()
        cur.close()
        return target_line and target_line[0] or ''

    @staticmethod
    def save_param(name, value):
        cur = DB.conn.cursor()
        cur.execute('SELECT ID FROM PARAMETER WHERE NAME = ?', (name, ))
        target_line = cur.fetchone()
        target_id = target_line and target_line[0] or None
        if target_id:
            cur.execute('UPDATE PARAMETER SET VALUE = ? WHERE ID = ?', (value, target_id))
        else:
            cur.execute('INSERT INTO PARAMETER(NAME, VALUE) VALUES(?, ?)', (name, value))
        Log.debug(u'参数[%s]已更新为[%s]' % (name, value))
        cur.close()

    @staticmethod
    def save_novel_info(name, desc, portrait):
        cur = DB.conn.cursor()
        cur.execute('SELECT ID FROM NOVEL_INFO WHERE NAME = ?', (name, ))
        target_line = cur.fetchone()
        target_id = target_line and target_line[0] or None
        if target_id:
            cur.execute('UPDATE NOVEL_INFO SET DESCRIPTION = ?, PORTRAIT = ? WHERE ID = ?', (desc, portrait, target_id))
        else:
            cur.execute('INSERT INTO NOVEL_INFO(NAME, DESCRIPTION, PORTRAIT) VALUES(?, ?, ?)', (name, desc, portrait))
        Log.debug(u'小说[%s]的简介信息已更新为[%s]，封面更新为[%s]' % (name, desc, portrait))
        cur.close()

    @staticmethod
    def query_novel_info(name):
        cur = DB.conn.cursor()
        cur.execute('SELECT DESCRIPTION, PORTRAIT FROM NOVEL_INFO WHERE NAME = ?', (name, ))
        result = cur.fetchone()
        cur.close()
        return result or ('', '')

if __name__ == '__main__':
    DB().save_novel_info(u'vcs.xml', u'a')