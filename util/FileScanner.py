# -*- coding: utf-8 -*-

import os


def scan(dir_path):
    # dir_path = str(dir_path)
    result = []
    if os.path.exists(dir_path):
        if os.path.isdir(dir_path):
            os.path.walk(dir_path, __walk__, result)
        else:
            result.extend(dir_path)
    return result


def __walk__(arg, dir_name, names):
    for name in names:
        cur_file = os.path.join(dir_name, name)
        if not os.path.isdir(cur_file):
            arg.append(cur_file)

if __name__ == '__main__':
    for each in scan(u'G:\迅雷下载'):
        print(os.path.basename(each))