# -*- coding: utf-8 -*-

import os
import sys

from codecs import open

def scan(dir_path):
    result = []
    if os.path.exists(dir_path):
        for root, dirs, files in os.walk(dir_path):
            for dir in dirs:
                result.extend(scan(os.path.join(root, dir)))
            for file in files:
                result.append(os.path.join(root, file))
    return result

def read(file_path):
    file_in = open(file_path, 'rb')
    try:
         return file_in.read()
    finally:
         file_in.close( )

def write(dir, file_name, file_content):
    input = open(os.path.join(dir, file_name), 'w', 'utf8')
    input.write(file_content)
    input.close()

def cur_file_dir():
    path = unicode(sys.path[0], 'gbk')
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

if __name__ == '__main__':
    print(len(scan(u'G:\迅雷下载')))