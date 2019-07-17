from dataclasses import dataclass

from baseactor import BaseActor

from element import Element
from datadeck import DataDeck
from gamemap import GameMap

@dataclass
class Actor(BaseActor):
    #XY left out on purpose
    #If you want them, add them to your extended Actor
    #Get them from a map scan.

    deck: DataDeck = None
    scannedMap: GameMap = None

    #Must return an action object
    #Loops not suggested
    #Infinite loops will result in doNothing(self,) due to game having a timeOut on calling this function
    def getAction(self):
        raise NotImplementedError
