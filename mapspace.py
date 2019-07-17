from dataclasses import dataclass

from element import Element
from baseactor import BaseActor

@dataclass
class MapSpace:
    x:int=0
    y:int=0
    element: Element = Element.GRAY
    inhabitant: BaseActor = None