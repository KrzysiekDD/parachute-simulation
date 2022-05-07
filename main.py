import math
import pygame
from TaylorMethod import TaylorMethod


# TODO This class will implement the animation and menu inputs and functionality
class Paratrooper:
    def  __init__(self):
        pygame.init()


    def initialize_game(self):
        screen = pygame.display.set_mode((1920, 1080))




if __name__ == "__main__":
    bibo = Paratrooper()
    metod = TaylorMethod(10, 0.1, 1000) #mass, B, initial height
    metod.numerical_method()