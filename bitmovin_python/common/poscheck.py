class PositionalArgumentsError(Exception):
    def __init__(self, f, n):
        self.f = f
        self.n = n

    def __str__(self):
        if self.n == 0:
            return "%s takes only keyword arguments" % self.f.__name__
        else:
            return "all arguments to %s after the first %s must be keyword arguments" % (
                self.f.__name__, self.n)


def poscheck(f):
    return poscheck_except(0)(f)


def poscheck_except(n):
    def helper(f):
        def checked_f(*args, **kwargs):
            if len(args) > n:
                raise PositionalArgumentsError(f, n)
            return f(*args, **kwargs)
        return checked_f
    return helper
