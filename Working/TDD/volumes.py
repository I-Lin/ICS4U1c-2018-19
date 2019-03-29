import math


def get_cube_vol(side_length):
    """
    Compute the volume of a cube
    :param side_length: length of a side of the cube
    :return: volume of cube
    """
    return side_length**3


def get_sphere_vol(radius):
    """
    Compute the volume of a sphere
    :param radius: radius of the sphere
    :return: volume of sphere
    """
    return int(4/3 * math.pi * radius**3 * 100) / 100


def get_cylinder_vol(radius, height):
    return 3.14