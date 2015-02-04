# -*- coding: utf-8 -*-

import threading


class Singleton(object):

    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with cls._instance_lock:
                if not hasattr(cls, "_instance"):
                    impl = cls.configure() if hasattr(cls, "configure") else cls
                    instance = super(Singleton, cls).__new__(impl, *args, **kwargs)
                    if not isinstance(instance, cls):
                        instance.__init__(*args, **kwargs)
                    instance.post_construct() if hasattr(cls, "post_construct") else None
                    cls._instance = instance
        return cls._instance