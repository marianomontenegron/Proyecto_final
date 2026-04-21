from PyQt5 import QtWidgets, uic, QtCore
from Programa_final.Programa_4 import Programa_final

class VentanaPrograma4(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_programa_final.ui", self)
        self.show()

        self.pushButton.clicked.connect(self.caso1)
        self.pushButton_2.clicked.connect(self.caso2)


    def caso1(self):
            x  = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
            y  = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
            xk = 386

            prog = Programa_final(x, y, xk)
            prog.calcular()

            self.resRxy.setText(f"{prog.rxy:.9f}")
            self.resR2.setText(f"{prog.r2:.9f}")
            self.resB0.setText(f"{prog.b0:.9f}")
            self.resB1.setText(f"{prog.b1:.9f}")

            
            self.resTail.setText(f"{prog.tail_area:.5E}")

            self.resYk.setText(f"{prog.yk:.7f}")
            self.resRange.setText(f"{prog.range_70:.7f}")
            self.resUpi.setText(f"{prog.upi:.7f}")
            self.resLpi.setText(f"{prog.lpi:.7f}")

    def caso2(self):
            x  = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
            y  = [15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2]
            xk = 386

            prog = Programa_final(x, y, xk)
            prog.calcular()

            self.resRxy.setText(f"{prog.rxy:.9f}")
            self.resR2.setText(f"{prog.r2:.9f}")
            self.resB0.setText(f"{prog.b0:.9f}")
            self.resB1.setText(f"{prog.b1:.9f}")

            
            self.resTail.setText(f"{prog.tail_area:.5E}")

            self.resYk.setText(f"{prog.yk:.7f}")
            self.resRange.setText(f"{prog.range_70:.7f}")
            self.resUpi.setText(f"{prog.upi:.7f}")
            self.resLpi.setText(f"{prog.lpi:.7f}")


