# encoding: utf-8

import os

class FileUtils:

    @staticmethod
    def exists(path):
        # 应该有更正常点的解决办法，但我不知道
        return FileUtils.__exists__(path, 'gbk') or FileUtils.__exists__(path, 'utf8')

    @staticmethod
    def to_array(path):
        return FileUtils.__to_array__(path, 'gbk') or FileUtils.__to_array__(path, 'utf8')

    @staticmethod
    def __to_array__(path, encode):
        try:
            input = open(path.encode(encode), 'rb')
            result = bytearray(input.read())
            input.close()
            return result
        except Exception as e:
            return None

    @staticmethod
    def __exists__(path, encode):
        try:
            return os.path.exists(path.encode(encode))
        except Exception as e:
            return False