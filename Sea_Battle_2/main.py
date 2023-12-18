import random

# Размер поля
FIELD_SIZE = 10

# Типы кораблей
SHIP_TYPES = [
    ("линкор", 4),
    ("крейсер", 3),
    ("эсминец", 2),
    ("подлодка", 1),
]

# Класс корабля
class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.hits = 0
        self.place = None
        self.player = None

    def hit(self):
        self.hits += 1

    @property
    def sunk(self):
        return self.hits == self.length

    def is_placed_correctly(self):
        for other_ship in self.player.ships:
            if other_ship != self:
                if self.overlaps(other_ship):
                    return False
        return True

    def overlaps(self, other_ship):
        return self.place == other_ship.place or (
            self.place[0] == other_ship.place[0] and abs(self.place[1] - other_ship.place[1]) == self.length
        ) or (
            self.place[1] == other_ship.place[1] and abs(self.place[0] - other_ship.place[0]) == self.length
        )

# Класс игрока
class Player:
    def __init__(self):
        self.ships = []
        self.field = [["." for i in range(FIELD_SIZE)] for j in range(FIELD_SIZE)]

    def place_ships(self):
        while not self.ships:
            for ship_type, length in SHIP_TYPES:
                while True:
                    x, y = input(f"Введите координаты начала корабля {ship_type} (длина {length}): ").split()
                    x = int(x)
                    y = int(y)
                    direction = input("Введите направление корабля (горизонтально или вертикально): ")
                    ship = Ship(ship_type, length)
                    if self.can_place_ship(x, y, length, direction):
                        ship.player = self
                        self.ships.append(ship)
                        break
                    else:
                        print("Корабль нельзя разместить в этом месте")

    def can_place_ship(self, x, y, length, direction):
        if direction == "h":
            for i in range(length):
                if self.field[y][x + i] != ".":
                    return False
        elif direction == "v":
            for i in range(length):
                if self.field[y + i][x] != ".":
                    return False
        for other_ship in self.ships:
            if other_ship != ship:
                if self.overlaps(other_ship):
                    return False
        return True
