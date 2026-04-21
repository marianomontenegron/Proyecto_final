import numpy as np

class RegresionLineal:
    def __init__(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)
        self.xk = 0

    def Calcular(self):
        self.xk = 386
        
        self.xavg = np.average(self.x)
        self.yavg = np.average(self.y)
        self.n = len(self.x)

        self.sumx = sum(self.x)
        self.sumy = sum(self.y)

        self.B1_num = sum(self.x*self.y) - (self.n*self.xavg*self.yavg)
        self.B1_denom = sum(np.pow(self.x,2)) - self.n*(self.xavg**2)

        self.r_num = self.n*(sum(self.x*self.y)) - (self.sumx*self.sumy)
        self.r_denom = (self.n*sum(np.pow(self.x,2)) - (self.sumx**2)) * ((self.n*sum(np.pow(self.y,2))) - (self.sumy**2))

        self.B1 = self.B1_num/self.B1_denom
        self.B0 = self.yavg - self.B1 * self.xavg
        self.rxy = self.r_num/np.sqrt(self.r_denom)
        self.r2 = self.rxy**2
        self.Yk = self.B0 + self.B1 * self.xk