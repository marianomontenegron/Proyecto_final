from PyQt5 import QtWidgets, uic, QtCore        
from load.load_regresion import VentanaRegresion
from load.load_integracion import VentanaIntegracion
from load.load_integracion_inversa import VentanaIntegracionInversa
from load.load_programa_4 import VentanaPrograma4

class MenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_menu_principal.ui", self)
        self.showMaximized()

        self.actionRegresi_n_lineal.triggered.connect(self.ingresarRegresion)
        self.actionIntegraci_n_num_rica.triggered.connect(self.ingresarIntegracion)
        self.actionIntegraci_n_Inversa.triggered.connect(self.ingresarIntegracionInversa)
        self.actionPt4.triggered.connect(self.ingresarprograma4)        
        
        self.actionSalir.triggered.connect(self.salir)

    def ingresarRegresion(self):
        regresion = VentanaRegresion()
        regresion.exec()

    def ingresarIntegracion(self):
        integracion = VentanaIntegracion()
        integracion.exec()

    def ingresarIntegracionInversa(self):
        integracioninv = VentanaIntegracionInversa()
        integracioninv.exec()

    def ingresarprograma4(self):
        programa_final = VentanaPrograma4()
        programa_final.exec()

    def salir(self):
        self.close()

