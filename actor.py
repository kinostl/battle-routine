from dataclasses import dataclass
from typing import List

from element import Element
from datachip import DataChip
from mapspace import MapSpace

@dataclass
class Actor:
    #These three must be from Elements
    #If you want a custom Element for flair, extend a color and rename it.
    #For example, Fire extends Red and Grass extends Green.
    weak_against: Element = Element.GRAY
    strong_against: Element = Element.GRAY
    element: Element = Element.GRAY

    x: int=0
    y: int=0

    deck: List[DataChip]
    scannedMap: List[List[MapSpace]]

    #Actions include the following. Only one can be taken on a turn.
    #   Gain board state at end of turn
    #   Teleport
    #   Use battle chip
    #   Refresh a battle chip
    #   Convert a tile to a color

    #Must return an action object
    #Loops not suggested
    #Infinite loops will result in doNothing(self,) due to game having a timeOut on calling this function
    def getAction(self):
        raise NotImplementedError
