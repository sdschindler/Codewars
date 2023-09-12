import math
def circle_area(r):
    if r <= 0:
        raise ValueError('Work with Positive Numbers Only')
    else:
        return math.pi * r**2
