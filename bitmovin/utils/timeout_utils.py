import time
from bitmovin.errors import TimeoutError


class TimeoutUtils:

    @classmethod
    def raise_error_if_timeout_reached(cls, start_time_in_seconds, timeout_in_seconds):
        if start_time_in_seconds is None:
            raise TimeoutError('Invalid usage: start_time_in_seconds needs to be a number')

        if timeout_in_seconds is None:
            raise TimeoutError('Invalid usage: timeout_in_seconds needs to be a number')

        if timeout_in_seconds == -1:
            return

        now = time.time()
        max_time = start_time_in_seconds + timeout_in_seconds
        timeout_reached = now > max_time

        if timeout_reached:
            raise TimeoutError('Timeout of {} reached.'.format(timeout_in_seconds))
