# -*- coding: utf-8 -*-

import time

from Queue import Queue

class Log(object):

    messages = Queue(0)

    @staticmethod
    def debug(text):
        Log.log('DEBUG', text)

    @staticmethod
    def info(text):
        Log.log('INFO', text)

    @staticmethod
    def warn(text):
        Log.log('WARN', text)

    @staticmethod
    def log(level, text):
        time_label = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        format_text = '[<span style="color: blue;">%s</span>]' \
                      '[<span style="color: red;">%s</span>] - ' \
                      '<span style="color: green;">%s</span>' % (time_label, level, text)
        Log.messages.put(format_text)

if __name__ == '__main__':
    Log.log('x', 'a')