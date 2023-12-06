from field import Field

class Player:
    '''Абстрактный игрок'''

    def __init__(self):
        self.own_field = Field()
        self.opponent_field = Field()