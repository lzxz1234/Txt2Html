# -*- coding: utf-8 -*-

import sqlite3
import os

from util.Log import Log

class DB(object):

    db_path = os.path.join(os.path.dirname(__file__), 'repository.sqlite')
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
    def save_novel_portrait(name, portrait):
        cur = DB.conn.cursor()
        cur.execute('SELECT ID FROM NOVEL_INFO WHERE NAME = ?', (name, ))
        target_line = cur.fetchone()
        target_id = target_line and target_line[0] or None
        if target_id:
            cur.execute('UPDATE NOVEL_INFO SET PORTRAIT = ? WHERE ID = ?', (portrait, target_id))
        else:
            cur.execute('INSERT INTO NOVEL_INFO(NAME, PORTRAIT) VALUES(?, ?)', (name, portrait))
        Log.debug(u'小说[%s]的封面路径已更新为[%s]' % (name, portrait))
        cur.close()

    @staticmethod
    def query_novel_portrait(name):
        cur = DB.conn.cursor()
        cur.execute('SELECT PORTRAIT FROM NOVEL_INFO WHERE NAME = ?', (name, ))
        result = cur.fetchone()
        cur.close()
        return result and result[0] or ''

    @staticmethod
    def save_novel_info(name, desc):
        cur = DB.conn.cursor()
        cur.execute('SELECT ID FROM NOVEL_INFO WHERE NAME = ?', (name, ))
        target_line = cur.fetchone()
        target_id = target_line and target_line[0] or None
        if target_id:
            cur.execute('UPDATE NOVEL_INFO SET DESCRIPTION = ? WHERE ID = ?', (desc, target_id))
        else:
            cur.execute('INSERT INTO NOVEL_INFO(NAME, DESCRIPTION) VALUES(?, ?)', (name, desc))
        Log.debug(u'小说[%s]的简介信息已更新为[%s]' % (name, desc))
        cur.close()

    @staticmethod
    def query_novel_info(name):
        cur = DB.conn.cursor()
        cur.execute('SELECT DESCRIPTION FROM NOVEL_INFO WHERE NAME = ?', (name, ))
        result = cur.fetchone()
        cur.close()
        return result and result[0] or ''

if __name__ == '__main__':
    DB().save_novel_info(u'vcs.xml', u'a')