
import random
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SHIELD, SHIELD_TYPE, CORAZON


class Shield(PowerUp):


    def __init__(self):
        lista_poderes = [SHIELD,CORAZON]
        #lista_naves = [SHIELD_TYPE]
        super().__init__(lista_poderes[random.randint(0,1)], SHIELD_TYPE)
    
    