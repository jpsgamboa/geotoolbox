import math

class Point:
    def __init__(self, x, y, name=""):
        self.X, self.Y, self.name = x, y, name

    def add(self, other):
        return Point(self.X + other.X, self.Y + other.Y)

    def __sub__(self, other):
        """subtract a point, list or scalar"""
        other = to_point(other)
        return Point(self.X - other.X, self.Y - other.Y)

    def angle(self):
        """angle in degrees from origin (0,0)"""
        return math.degrees( math.atan2(self.Y, self.X) )

    def __repr__(self):
        """return a point as a string: called by the repr() and str()."""
        return '[%s,%s]' % (self.X, self.Y)

    def println(self):
        print "(%d, %d)" % (self.X, self.Y)

    def distance_from(self, other):
        import math
        lat1 = self.X * math.pi / 180
        lat2 = other.X * math.pi / 180
        lon1 = self.Y * math.pi / 180
        lon2 = other.Y * math.pi / 180

        cosX = math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)

        try:
            return 6371 * math.acos(cosX)
        except ValueError:
            # If the error is occurring because cosX is nearing 1, then return 0
            if round(cosX, 2) - 1.0 == 0:  # Round is used because 1.00000000000001 == 1.00 for our purposes.
                return 0
            else:
                import sys
                return sys.maxint

    def is_near_to(self, other, radius):
        if radius < 10:
            if abs(other.Y - self.Y) > 0.0001:
                return False
            if abs(other.X - self.X) > 0.0001:
                return False

        if self.distance_from(other) < radius:
          return True
        return False


def to_point(other):
    '''converts a list/tuple to a point'''
    if isinstance(other, Point):
        return other
    else:
        return Point(other)