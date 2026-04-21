import math
from Integracion.Integracion import Integracion

class IntegracionInversa:
    def __init__(self, error_aceptable=1e-14):
        self.error_aceptable = error_aceptable
        self.integra = Integracion(1e-14)

    def busca_x(self, p, dof, redondear=True):
        # Fase 1: encontrar rango [lo, hi]
        lo = 0.0
        hi = 1.0
        while self.integra.integrar(hi, dof) < p:
            hi *= 2

        # Fase 2: bisección pura
        for _ in range(300):
            mid = (lo + hi) / 2
            resultado = self.integra.integrar(mid, dof)
            if resultado < p:
                lo = mid
            else:
                hi = mid

        x = (lo + hi) / 2
        return round(x, 5) if redondear else x
