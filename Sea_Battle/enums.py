import enum


class Direction(enum.Enum):
    horizontal = 0
    vertical = 1


class ShootResult(enum.Enum):
    miss = 0
    hit = 1
    kill = 2
