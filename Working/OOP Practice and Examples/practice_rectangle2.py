class Rectangle(object):
    """
    A class representing a rectangle
    """

    def __init__(self, rect_width, rect_height):
        """
        Initialize width and height
        """

        self.width = rect_width
        self.height = rect_height


    def get_area(self):
        """
        Calculate the area of the rectangle
        :param rec: a rectangle object
        :return: area of rec
        """
        return self.width * self.height


def main():
    rect1 = Rectangle(4, 7)
    rect2 = Rectangle(6, 7)
    rect3 = Rectangle(3, 8)

    print("The area of the rectangle is", Rectangle.get_area(rect1))
    print("The area of the rectangle is", Rectangle.get_area(rect2))
    print("The area of the rectangle is", Rectangle.get_area(rect3))


main()