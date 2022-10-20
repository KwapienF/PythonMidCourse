# import math
#
# print("Podaj współrzędne:")
# x = float(input("Podaj x: "))
# y = float(input("Podaj y: "))
# z = float(input("Podaj z: "))
#
# cosa = (x/(y-x))
# print(cosa)
#
# mat.cos(cosa)
# calc_sphere_cordinates

import math


PI = math.pi
PI_2 = PI / 2

def calc_sphere_coordinates(radius, phi, theta):
    # see: https://stackoverflow.com/a/969880/1230358
    # see: https://stackoverflow.com/q/19673067/1230358
    # see: http://mathinsight.org/spherical_coordinates
    # see: https://en.wikipedia.org/wiki/Spherical_coordinate_system
    # see: http://tutorial.math.lamar.edu/Classes/CalcII/SphericalCoords.aspx

    # φ phi is the polar angle, rotated down from the positive z-axis (slope)
    # θ theta is azimuthal angle, the angle of the rotation around the z-axis (aspect)

    # z
    # |  x
    # | /
    # |/
    # +-------- y

    # both angles need to be in radians, not degrees!
    theta = theta * PI / 180
    phi = phi * PI / 180

    x = radius * math.sin(phi) * math.cos(theta)
    y = radius * math.sin(phi) * math.sin(theta)
    z = radius * math.cos(phi)
    return (x, y, z)

if __name__ == "__main__":

    # calculate point position in hemisphere by rotating down from positive z-axis
    for i in (10, 20, 30, 40, 50, 60, 70 , 80, 90):
        print(calc_sphere_coordinates(10, i, 0))

    print("-"*10)

    # calculate point position in hemisphere by rotating around the z axis
    for i in (10, 20, 30, 40, 50, 60, 70 , 80, 90):
        print(calc_sphere_coordinates(10, 0, i))

    print("-"*10)

    # calculate point position by rotating in both directions
    for i in (10, 20, 30, 40, 50, 60, 70 , 80, 90):
        print(calc_sphere_coordinates(10, i, 90-i))