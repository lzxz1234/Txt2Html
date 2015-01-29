# -*- coding: utf-8 -*-

import os


def scan(dir_path):
    result = []
    if os.path.exists(dir_path):
        for root, dirs, files in os.walk(dir_path):
            for dir in dirs:
                result.extend(scan(os.path.join(root, dir)))
            for file in files:
                result.append(os.path.join(root, file))
    return result

if __name__ == '__main__':
    print(len(scan(u'G:\迅雷下载')))