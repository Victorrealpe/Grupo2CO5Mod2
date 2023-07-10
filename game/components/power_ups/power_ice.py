from game.components.power_ups.power_up import PowerUp
from game.utils.constants import  ICE, ICE_TYPE


class Ice(PowerUp):
    def __init__(self):
        super().__init__(ICE, ICE_TYPE)