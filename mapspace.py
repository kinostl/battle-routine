from element import Element
from actor import Actor

class MapSpace:
    x=0
    y=0
    element = Element.GRAY
    inhabitant = None

    def __init__(self,x,y):
        self.x = x
        self.y = y