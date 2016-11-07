import logging
import sys


class BitmovinObject(object):
    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger(self.__class__.__module__ + "." + self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s')
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
