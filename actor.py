from dataclasses import dataclass
from enum import Enum

class Element(Enum):
    GRAY=0
    YELLOW=1
    RED=2
    BLUE=3
    GREEN=4
    ORANGE=5
    PURPLE=6
    BLACK=7
    WHITE=8

@dataclass
class Actor:
    #These three must be from Elements
    #If you want a custom Element for flair, extend a color and rename it.
    #For example, Fire extends Red and Grass extends Green.
    weak_against: Element
    strong_against: Element
    element: Element

    x: int=0
    y: int=0

    deck: List[DataChip]
    scannedMap: List[MapSpace]

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
