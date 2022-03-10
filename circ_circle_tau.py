#!/usr/bin/env python3

# Created By: Nicolas Riscalas

# Date: 03-9-2022

# Calculates the area and perimeter of a square


import math
import constants


def main():
    r = float(input("Enter the radius of a circle:\n"))
    perimeter = constants.TAU * r
    print("Perimeter of a circle = %.2f" % perimeter, "m")


if __name__ == "__main__":
    main()
