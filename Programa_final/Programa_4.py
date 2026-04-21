import math
import numpy as np
from Integracion.Integracion import Integracion
from Integracion_inversa.Integracion_inversa import IntegracionInversa
from Regresion_lineal.Caso_de_prueba_1 import RegresionLineal
 
 
class Programa_final(object):
 
    def __init__(self, x: list, y: list, xk: float):
        self.x   = x
        self.y   = y
        self.xk  = xk
        self.n   = len(x)
 
        self.b0  = 0.0
        self.b1  = 0.0
        self.rxy = 0.0
        self.r2  = 0.0
 
        self.t_value   = 0.0
        self.tail_area = 0.0
 
        self.yk       = 0.0
        self.range_70 = 0.0
        self.upi      = 0.0
        self.lpi      = 0.0
 
    def calcular(self):
        self._calcular_regresion()
        self._calcular_significancia()
        self._calcular_prediccion()
 
    def _calcular_regresion(self):
        reg = RegresionLineal(self.x, self.y)
        reg.Calcular()
        self.b0  = reg.B0
        self.b1  = reg.B1
        self.rxy = reg.rxy
        self.r2  = reg.r2
 
    def _calcular_significancia(self):
        r = self.rxy
        n = self.n
 
        if abs(r) >= 1.0:
            self.t_value   = float('inf')
            self.tail_area = 0.0
            return
 
        denom        = math.sqrt(1 - r ** 2)
        self.t_value = r * math.sqrt(n - 2) / denom
 
        dof   = n - 2
        x_abs = abs(self.t_value)
 
        integ = Integracion()
        p = integ.integrar(x_abs, dof)
 
        self.tail_area = 1 - 2 * p
 
    def _calcular_prediccion(self):
        x  = self.x
        y  = self.y
        n  = self.n
        b0 = self.b0
        b1 = self.b1
        xk = self.xk
 
        self.yk = b0 + b1 * xk
 
        suma_error2 = sum((y[i] - b0 - b1 * x[i]) ** 2 for i in range(n))
        s           = math.sqrt(suma_error2 / (n - 2))
 
        x_avg      = sum(x) / n
        suma_diff2 = sum((xi - x_avg) ** 2 for xi in x)
 
        if suma_diff2 == 0:
            raise ValueError(
                "no se puede calcular el intervalo de predicción."
            )
 
        varianza_extra = 1 + 1 / n + (xk - x_avg) ** 2 / suma_diff2
        sigma_total = s * math.sqrt(varianza_extra)
 
        dof = n - 2
        buscador = IntegracionInversa()
        t_35 = buscador.busca_x(0.35, dof)
 
        self.range_70 = t_35 * sigma_total
        self.upi = self.yk + self.range_70
        self.lpi = self.yk - self.range_70