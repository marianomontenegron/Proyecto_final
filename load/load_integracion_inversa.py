from PyQt5 import QtWidgets, uic
from Integracion_inversa.Integracion_inversa import IntegracionInversa

class VentanaIntegracionInversa(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/ventana_integracion_inversa.ui', self)
        self.pushButton.clicked.connect(self.botonCalc)

    def botonCalc(self):
        try:
            p = float(self.lineEdit_p.text())
            dof = int(self.lineEdit_dof.text())
            calcularinv = IntegracionInversa()
            x = calcularinv.busca_x(p, dof)
            self.label_resultado.setText(str(x))
        except:
            self.label_resultado.setText("ERROR")