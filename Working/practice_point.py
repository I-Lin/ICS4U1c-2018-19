class Point(object):

    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos

    def get_distance(self, other_point):
        distance = ((self.x - other_point.x)**2 + (self.y - other_point.y)**2) ** 0.5
        return distance


def main():
    p1 = Point(1, 1)
    p2 = Point(4, 5)

    print("The distance between the 2 points is", Point.get_distance(p1, p2))


main()