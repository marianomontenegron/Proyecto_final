from PyQt5 import QtWidgets, uic
from Integracion.Integracion import Integracion

class VentanaIntegracion(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_integracion_numerica.ui", self)
        self.show()
        self.botonCalcular.clicked.connect(self.botonCalcularClick)

    def botonCalcularClick(self):
        try:
            x = float(self.lineEdit_x.text())
            dof = int(self.lineEdit_dof.text())
        except ValueError:
            self.label_resultado.setText("Error")
            return

        if dof < 1:
            self.label_resultado.setText("dof debe de ser ≥ 1")
            return

        integracion = Integracion()
        resultado = integracion.integrar(x, dof)
        self.label_resultado.setText(str(resultado))