import numpy as np
import math

x = np.linspace(0, 10, 500)
y = np.sin(x)
mi0 = 1
p0 = 1
omega = 1
c = 1

def get_E(x, y, z, t):
    r = (x**2 + y**2 + z**2)**0.5
    theta = math.atan2(r, z)
    value = -mi0 * p0 * omega ** 2 / (4 * math.pi) * math.sin(theta) / r * math.cos(omega * (t - r/c))
    # value = 0
    value = value * r
    value_z = math.sin(theta) * value
    value_horizontal = - value * math.cos(theta)
    r_horizontal = (x**2 + y**2)**0.5
    value_x = value_horizontal * x / r_horizontal
    value_y = value_horizontal * y / r_horizontal
    return value_x, value_y, value_z

def get_B(x, y, z, t):
    r = (x**2 + y**2 + z**2)**0.5
    theta = math.atan2(r, z)
    value = -mi0 * p0 * omega ** 2 / (4 * math.pi * c) * math.sin(theta) / r * math.cos(omega * (t - r/c))
    # value = 1
    r_horizontal = (x**2 + y**2)**0.5
    value = value * r_horizontal
    value_z = 0
    value_y = value * x/r_horizontal
    value_x = -value * y/r_horizontal
    return value_x, value_y, value_z

if __name__ == '__main__':
    print(get_B(0, 1, 0, 0))