from game.components.power_ups.power_up import PowerUp
from game.utils.constants import  BOMB, BOMB_TYPE


class Bomb(PowerUp):
    def __init__(self):
        super().__init__(BOMB, BOMB_TYPE)