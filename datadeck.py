from dataclasses import dataclass
from typing import List

from datachip import DataChip

@dataclass
class DataDeck:
    deck: List[DataChip]