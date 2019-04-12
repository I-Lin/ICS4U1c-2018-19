class Rectangle(object):
    """
    A class representing a rectangle
    """

    def __init__(self):
        """
        Initialize width and height
        """

        self.width = 0
        self.height = 0


def get_area(rec):
    """
    Calculate the area of the rectangle
    :param rec: a rectangle object
    :return: area of rec
    """
    return rec.width * rec.height


def main():
    rect1 = Rectangle()

    rect1.width = int(input("Enter width: "))
    rect1.height = int(input("Enter height: "))

    print("The area of the rectangle is", get_area(rect1))


main()