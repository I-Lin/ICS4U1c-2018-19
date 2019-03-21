class Point(object):

    def __init__(self, x_pos, y_pos):
        """
        Create an instance of a Point
        :param x_pos: x coordinate value
        :param y_pos: y coordinate value
        """
        self.x = x_pos
        self.y = y_pos

    def get_distance(self, other_point):
        """
        Compute the distance between the current object and another Point object
        :param other_point: Point object to find the distance to
        :return: float
        """
        distance = ((self.x - other_point.x)**2 + (self.y - other_point.y)**2) ** 0.5
        return distance


def main():
    """
    Program demonstrating the creation of Point instances and calling class methods
    """
    p1 = Point(1, 1)
    p2 = Point(4, 5)

    print("The distance between the 2 points is", Point.get_distance(p1, p2))


main()