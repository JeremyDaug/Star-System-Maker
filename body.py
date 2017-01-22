"""
File for the Body class, contains everything a body needs and does all the
calculations that are needed. For it's children.
"""


class Body:
    def __init__(self):
        # body name
        self.name = ''
        # body mass and unit
        # S for sun, J for Jupiter, E for earth, K for kilogram
        self.mass = (1, 'S')
        # placeholder for surface map
        # self.map = None
        # Day length (from noon to noon)
        # Y for year (earth) year, M for month, D for day, H for hour
        # m for minute, s for second
        self.day = (1, 'D')
        # Calendar listing should be in tuple form of (name, length)
        self.calendar = []
        # leap day shift the month number that any leap days are added to.
        self.leap_shift = 0
        # number of days in a week.
        self.week = []

        # children bodies (planets and moons)
        self.children = []
        return
