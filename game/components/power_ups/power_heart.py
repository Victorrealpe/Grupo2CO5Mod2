from game.components.power_ups.power_up import PowerUp
from game.utils.constants import  CORAZON, HEART_TYPE


class Heart(PowerUp):
    def __init__(self):
        super().__init__(CORAZON, HEART_TYPE)
    
    