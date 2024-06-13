import numpy as np

class ExchangeEconomyClass:
    def __init__(self):
        self.alpha = 1/3
        self.beta = 2/3
        self.omega_A1 = 0.8
        self.omega_A2 = 0.3
        self.omega_1bar = 1.0
        self.omega_2bar = 1.0
        self.p2 = 1  # Numeraire

    def uA(self, x1, x2):
        return (x1**self.alpha) * (x2**(1-self.alpha))

    def uB(self, x1, x2):
        return (x1**self.beta) * (x2**(1-self.beta))

    def demand_A(self, p1):
        xA1 = self.alpha * ((p1 * self.omega_A1 + self.p2 * self.omega_A2) / p1)
        xA2 = (1 - self.alpha) * ((p1 * self.omega_A1 + self.p2 * self.omega_A2) / self.p2)
        return xA1, xA2

    def demand_B(self, p1):
        omega_B1 = 1 - self.omega_A1
        omega_B2 = 1 - self.omega_A2
        xB1 = self.beta * ((p1 * omega_B1 + self.p2 * omega_B2) / p1)
        xB2 = (1 - self.beta) * ((p1 * omega_B1 + self.p2 * omega_B2) / self.p2)
        return xB1, xB2

    def utility_A(self, xA1, xA2):
        return self.uA(xA1, xA2)

    def utility_B(self, xB1, xB2):
        return self.uB(xB1, xB2)