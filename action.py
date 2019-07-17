from enum import Enum
from dataclasses import dataclass

from element import Element

#Actions include the following. Only one can be taken on a turn.
#   Gain board state at end of turn
#   Teleport
#   Use battle chip
#   Refresh a battle chip
#   Convert a tile to a color

class ActionType(Enum):
    UPDATE_BOARD=0
    TELEPORT=1
    USE_CHIP=2
    REFRESH_CHIP=3
    CONVERT_TILE=4
    DO_NOTHING=5

@dataclass
class Action:
    actionType: ActionType = ActionType.DO_NOTHING

@dataclass
class doNothing(Action):
    actionType: ActionType = ActionType.DO_NOTHING

@dataclass
class updateBoard(Action):
    actionType: Action = ActionType.UPDATE_BOARD

@dataclass
class teleport(Action):
    actionType: Action = ActionType.TELEPORT
    x: int=0
    y: int=0

@dataclass
class useChip(Action):
    actionType: Action = ActionType.USE_CHIP
    chipId: int=0

@dataclass
class refreshChip(Action):
    actionType: Action = ActionType.REFRESH_CHIP
    chipId: int=0

@dataclass
class convertTile(Action):
    actionType: Action = ActionType.CONVERT_TILE
    x: int=0
    y: int=0
    element: Element = Element.GRAY