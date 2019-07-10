#from abc import ABC, abstractmethod
from enum import Enum

class Elements(Enum):
    Gray=0
    Yellow=1
    Red=2
    Blue=3
    Green=4
    Orange=5
    Purple=6
    Black=7
    White=8

class Actor():
    #These three must be from Elements
    #If you want a custom Element for flair, extend a color and rename it.
    #For example, Fire extends Red and Grass extends Green.
    Weakness=0
    Strength=0
    Element=0

    x=0
    y=0
    deck=[]
    scannedMap=[]

    #Actions include the following. Only one can be taken on a turn.
    #   Gain board state at end of turn
    #   Teleport
    #   Use battle chip
    #   Refresh a battle chip
    #   Convert a tile to a color

    #These should probably all be objects. Only functions in here should be things that update the stats of the Actor
    def teleportTo(x,y):
        pass

    def convertPanel(x,y,color,currentMap):
        pass

    def useChip(chip):
        pass

    def refreshChip(chip):
        pass

    def scanMap(newMap):
        pass

    #Must return an action object
    #Loops not suggested
    #Infinite loops will result in doNothing() due to game having a timeOut on calling this function
    def run():
        pass
