from dataclasses import dataclass
from typing import List

from element import Element

@dataclass
class DataChip:
    element: Element = Element.GRAY
    damage: int = 0
    shape=List[List[int]]