from game.components.power_ups.power_up import PowerUp
from game.utils.constants import  CORAZON, SPACESHIP


class Heart(PowerUp):
    def __init__(self):
        super().__init__(CORAZON, SPACESHIP)
    
    