import vpython as vp
import numpy as np

class CelestialBody:
    def __init__(self, color_of_body, radius_of_body,position):
        self.body = vp.sphere(color=color_of_body,\
                              radius=radius_of_body, \
                              pos=position, canvas=scene, make_trail=True, retain=10)
        self.position = position
                              











