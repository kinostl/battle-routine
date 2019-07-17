from dataclasses import dataclass

from element import Element

@dataclass
class BaseActor:
    #These three must be from Elements
    #If you want a custom Element for flair, extend a color and rename it.
    #For example, Fire extends Red and Grass extends Green.
    weak_against: Element = Element.GRAY
    strong_against: Element = Element.GRAY
    element: Element = Element.GRAY