from field import Field
from enums import Direction, ShootResult


class Player:
    """Абстрактный игрок"""

    def __init__(self):
        self.own_field = Field()
        self.opponent_field = Field()

    def place_ships(self, shiptype):
        """ Расставляем корабли на поле
            Пример абстрактного метода. Требует реализации в потомке
        """
        raise NotImplementedError

    def shoot(self) -> tuple[int, int]:
        """Производим выстрел. Возвращаем row и column"""
        raise NotImplementedError

    def check_shoot(self, row: int, column: int) -> ShootResult:
        """Проверяем ячейку в которую произвели выстрел"""
        return self.own_field.check_shoot(row, column)

    def is_killed_all(self) -> bool:
        """Проверяем, что убиты все корабли"""
        return False

class Human(Player):

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def place_ships(self, shiptype: int):
        """Спрашиваем пользователя куда и ставим корабли"""


    def shoot(self) -> tuple[int, int]:
        """Спрашиваем у игрока куда стрелять"""
        try:
            row, col = int(input("Введите координаты для выстрела: (строка, столбец)"))
            return row, col
        except ValueError:
            print("Пожалуйста, введите целые числа.")
            return self.shoot()


class Bot(Player):

    def place_ships(self):
        """Рандомно расставляем корабли"""
        self.own_field.set_ship(1, 2, Direction.vertical)

    def shoot(self) -> tuple[int, int]:
        """Решаем куда выстрелить"""
