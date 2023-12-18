from enums import Direction, ShootResult

class Field:
    """Игровое поле для морского боя"""

    def __init__(self):
        """Создаем пустое поле 10х10"""
        self.__field: list[list[dict]] = []
        for r in range(10):
            self.__field.append([])
            for c in range(10):
                self.__field[r].append(
                    {
                        "cell_type": 0,
                        "ship_number": 0,
                        "is_live": True
                    }
                )


    def set_ship(self, row: int, column: int, direction: Direction, shiptype: int, shipnumber: int):
        """Устанавливаем корабль на поле"""
        row, column, direction, shiptype = map(int, input("Введите координаты начала корабля, направление и тип: ((2,2,) 0 - горизонтально / 1 - вертикально 1/2/3/4) ").split())
        if direction == Direction.horizontal:
            for i in range(shiptype):
                if self.__check_cell(row, column):
                    self.__field[row][column]["cell_type"] = shiptype
                    self.__field[row][column]["ship_number"] = shipnumber
                else:
                    print("Корабль не может быть установлен")
                    return
        else:
            for i in range(shiptype):
                if self.__check_cell(row, column):
                    self.__field[row][column]["cell_type"] = shiptype
                    self.__field[row][column]["ship_number"] = shipnumber
                else:
                    print("Корабль не может быть установлен")
                    return




    def __set_cell(self, row: int, column: int, value):
        """Меняем значение ячейки"""

    def __check_cell(self, row: int, column: int) -> bool:
        """Можно ли туда ставить палубу корабля True - можно"""
        if 1 <= row <= 10 and 1 <= column <= 10:
            return True
        else:
            return False

    def check_shoot(self, row: int, column: int) -> ShootResult:
        """Проверяем результат выстрела"""
        if self.__field[row][column]["cell_type"] != 0:
            if self.__field[row][column]["is_live"]:
                self.__field[row][column]["is_live"] = False
                return ShootResult.hit
            else:
                return ShootResult.miss
        else:
            return ShootResult.miss




