import math
import pygame
"""
TODO this class will implement the differential equation used to determine the trajectory of the paratrooper
and it's derivatives
Freefall with air resistance:
    m * (d^2y)/(dt^2) = -m*g + b * (dy/dt)^2
Initial Conditions y(0) = y0, v(0) = y'(0) = 0
    m - mass, b - Stoke's constant, y0 - initial height, yFinal - final height,  g = 9,81 m/s^2
"""
class TaylorMethod:
    G = 9.81
    Y_FINAL = 0
    H = 0.05
    N = 1000

    def __init__(self, m: float, b: float, y0: float):
        self.m = m
        self.b = b
        self.y0 = y0
        self.y_second_derivative = []
        self.y_first_derivative = []
        self.y_position = []
        #self.y_second_derivative.append(0)
        self.y_first_derivative.append(0)
        self.y_position.append(self.y0)

    def numerical_method(self):
        for i in range(TaylorMethod.N):
            self.y_second_derivative.append(-TaylorMethod.G
            + (self.b/self.m) * self.y_first_derivative[i] * self.y_first_derivative[i])

            self.y_first_derivative.append(self.y_first_derivative[i] + TaylorMethod.H*self.y_second_derivative[i])

            self.y_position.append(self.y_position[i] + TaylorMethod.H*self.y_first_derivative[i]
            + TaylorMethod.H * TaylorMethod.H * 0.5*self.y_second_derivative[i])

        for i in range(TaylorMethod.N):
            print(i, "  ", self.y_position[i], "     ", self.y_first_derivative[i], "     ", self.y_second_derivative[i],
                  sep="")
