#Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
def make_readable(seconds):
    # Do something
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    str = '{:02d}:{:02d}:{:02d}'.format(h, m, s)
    return str
