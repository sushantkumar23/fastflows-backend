from enum import Enum


class Orientation(Enum):
    TB = "TB"
    TD = "TD"
    BT = "BT"
    RL = "RL"
    LR = "LR"


class NodeShape(Enum):
    rectangle = "rectangle"  # process
    round = "round"  # alternate process
    stadium = "stadium"  # start/end
    subroutine = "subroutine"  # sub-process
    cylinder = "cylinder"  # database
    circle = "circle"  # on-page connector
    rhombus = "rhombus"  # decision
    hexagon = "hexagon"  # preparation
    parallelogram = "parallelogram"  # input/output
    trapezoid_alt = "trapezoid_alt"  # manual operation
    """
    TODO: Add more shapes - 
    1. Storage - documents, multiple documents, data storage, internal storage, tape data, paper tape
    2. Input/Output - display, manual input, delay
    3. Connecting Symbols - merge, off-page connector
    """
