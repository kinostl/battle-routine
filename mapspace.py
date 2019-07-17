from dataclasses import dataclass

from element import Element
from baseactor import BaseActor

@dataclass
class MapSpace:
    x:int=0
    y:int=0
    element: Element = Element.GRAY
    inhabitant: BaseActor = None

    def __str__(self):
        if self.inhabitant is not None:
            return "A"

        if self.element is not Element.GRAY:
            return "C"
        return str(self.x * self.y)