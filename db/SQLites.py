# -*- coding: utf-8 -*-

import sqlite3
import os

from util.Log import Log
from util.File import cur_file_dir
from util.Singleton import Singleton


class DB(Singleton):

    def post_construct(self):
        db_path = os.path.join(cur_file_dir(), 'repository.sqlite')
        self.conn = sqlite3.connect(db_path, check_same_thread = False)
        self.conn.isolation_level = None
        self.conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")
        self.conn.execute('CREATE TABLE IF NOT EXISTS NOVEL_INFO('
                     'ID INTEGER PRIMARY KEY AUTOINCREMENT, '
                     'NAME VARCHAR(100), '
                     'PORTRAIT VARCHAR(1000), '
                     'DESCRIPTION VARCHAR(2000) )')
        self.conn.execute('CREATE TABLE IF NOT EXISTS PARAMETER(ID INTEGER PRIMARY KEY '
                     'AUTOINCREMENT, NAME VARCHAR(20), VALUE VARCHAR(100))')

    def get_param(self, name):
        cur = self.conn.cursor()
        cur.execute('SELECT VALUE FROM PARAMETER WHERE NAME = ?', (name, ))
        target_line = cur.fetchone()
        cur.close()
        return target_line and target_line[0] or ''

    def save_param(self, name, value):
        cur = self.conn.cursor()
        cur.execute('SELECT ID FROM PARAMETER WHERE NAME = ?', (name, ))
        target_line = cur.fetchone()
        target_id = target_line and target_line[0] or None
        if target_id:
            cur.execute('UPDATE PARAMETER SET VALUE = ? WHERE ID = ?', (value, target_id))
        else:
            cur.execute('INSERT INTO PARAMETER(NAME, VALUE) VALUES(?, ?)', (name, value))
        Log.debug(u'参数[%s]已更新为[%s]' % (name, value))
        cur.close()

    def save_novel_info(self, name, desc, portrait):
        cur = self.conn.cursor()
        cur.execute('SELECT ID FROM NOVEL_INFO WHERE NAME = ?', (name, ))
        target_line = cur.fetchone()
        target_id = target_line and target_line[0] or None
        if target_id:
            cur.execute('UPDATE NOVEL_INFO SET DESCRIPTION = ?, PORTRAIT = ? WHERE ID = ?', (desc, portrait, target_id))
        else:
            cur.execute('INSERT INTO NOVEL_INFO(NAME, DESCRIPTION, PORTRAIT) VALUES(?, ?, ?)', (name, desc, portrait))
        Log.debug(u'小说[%s]的简介信息已更新为[%s]，封面更新为[%s]' % (name, desc, portrait))
        cur.close()

    def query_novel_info(self, name):
        cur = self.conn.cursor()
        cur.execute('SELECT DESCRIPTION, PORTRAIT FROM NOVEL_INFO WHERE NAME = ?', (name, ))
        result = cur.fetchone()
        cur.close()
        return result or ('', '')

if __name__ == '__main__':
    DB().save_novel_info(u'vcs.xml', u'a')