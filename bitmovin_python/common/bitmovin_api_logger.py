import logging
import sys

from bitmovin_python.common.bitmovin_api_logger_base import BitmovinApiLoggerBase


class BitmovinApiLogger(BitmovinApiLoggerBase):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__module__ + "." + self.__class__.__name__)
        self._attach_console_logging_handler_if_not_existing()

    def log(self, message, data=None):
        if data is not None:
            self.logger.debug(message, data)
        else:
            self.logger.debug(message)

    def error(self, message, data=None):
        if data is not None:
            self.logger.error(message, data)
        else:
            self.logger.error(message)

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
