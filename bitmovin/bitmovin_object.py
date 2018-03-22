import logging
import sys


class BitmovinObject(object):
    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger(self.__class__.__module__ + "." + self.__class__.__name__)
        self._attach_console_logging_handler_if_not_existing()

    def _attach_console_logging_handler_if_not_existing(self):
        handlers = self.logger.handlers
        handler_already_exists = any(handler.name == 'bitmovin_console_handler' for handler in handlers)

        if handler_already_exists:
            return

        self.logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.name = 'bitmovin_console_handler'
        formatter = logging.Formatter('%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s')
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
