"""
Freefall with air resistance:
    m * (d^2y)/(dt^2) = -m*g + b * (dy/dt)^2
Initial Conditions y(0) = y0, v(0) = y'(0) = 0
    m - mass, b - Stoke's constant, y0 - initial height, yFinal - final height,  g = 9,81 m/s^2
"""


class TaylorMethod:
    G = 9.81
    Y_FINAL = 0
    # Constructor of the TaylorMethod class, the position and velocity have initial conditions
    # so we set them appropriately
    def __init__(self, m: float, b: float, y0: float, H: float):
        self.m = m
        self.b = b
        self.y0 = y0
        self.H = H
        self.y_second_derivative = []
        self.y_first_derivative = []
        self.y_position = []
        self.y_first_derivative.append(-2.0)
        self.y_position.append(self.y0)
    # This method calculates the position, velocity and acceleration using Taylor method for numerical ODE's
    def numerical_method(self):
        i = 0
        while self.y_position[i] >= 0:

            self.y_second_derivative.append(-TaylorMethod.G
            + (self.b / self.m) * self.y_first_derivative[i] * self.y_first_derivative[i])

            self.y_first_derivative.append(self.y_first_derivative[i] + self.H * self.y_second_derivative[i])

            x = self.y_position[i] + self.H * self.y_first_derivative[i] \
            + self.H * self.H * 0.5 * self.y_second_derivative[i]
            if x <= 0:
                i += 1
                break
            else:
                self.y_position.append(x)
            i += 1

        self.y_position.append(0)
        self.y_second_derivative.append(self.y_second_derivative[i-1])
