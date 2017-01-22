"""
Class file that holds system wide information. It does not hold any information
about the bodies.
"""


class StarSystem:
    def __init__(self):
        # the name of the star system
        self.name = ''
        # the strength of gravity
        self.G = 9.8  # m/s^2
        # the star map background, should be a 2d array of squares, measured in
        # degrees
        self.star_map = []
        # Either the central most body or the barycenter of the system.
        self.head = None
        return
