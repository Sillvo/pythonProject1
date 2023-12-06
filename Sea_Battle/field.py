class Field:
    '''Игровое поле для морского боя'''

    def __init__(self):
        '''Создаем пустое поле 10х10'''
        self.__field: list[list[tuple]] = [[(0, 0, True)]*10]*10

    def set_ship(self):
        '''Устанавливаем корабль на поле'''

    def __set_cell(self, row: int, column: int, value):
        '''Меняем значение ячейки'''

    def __check_cell(self, row: int, column: int):
        '''Можно ли туда ставить палубу корабля'''