import sys
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
 
servidorUi = uic.loadUiType("servidor2.ui")[0] #Se carga la interfaz de tipo ui del servidor
 
class Servidor(QtGui.QMainWindow, servidorUi):

 	def __init__(self, parent=None):#Constructor de la ventana
 		QtGui.QMainWindow.__init__(self, parent)
 		self.setupUi(self)#Inicializa la interfaz del tipo ui
 		self.tableWidget.horizontalHeader().setResizeMode(QHeaderView.Stretch) #Como su nombre lo dice estira a las columnas horizontales para adaptarse a la widget
 		self.tableWidget.verticalHeader().setResizeMode(QHeaderView.Stretch) #Lo mismo para las verticales
 		self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) #Cuando las celdas son bastantes, la scrollbar aparece, este basicamente las hace desaparecer
 		self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff) #Tambien las verticales (Con las de 20 columnas, 20 filas, aparecía)
 		self.columnas.setMaximum(99) #Ajusta cuantos se puede recibir como maximo en la spinbox para las columnas
 		self.columnas.setMinimum(10) #Ajusta cuantos se puede recibir como minimo en la spinbox para las columnas
 		self.columnas.valueChanged.connect(self.ajustaColumnas) #Conecta los valores de la spinbox al metodo
 		self.filas.setMaximum(99) #Ajusta cuantos se puede recibir como maximo en la spinbox para las filas
 		self.filas.setMinimum(10) #Ajusta cuantos se puede recibir como minimo en la spinbox para las filas
 		self.espera.setMaximum(999)
 		self.espera.setMinimum(10)
 		self.espera.setValue(150)
 		self.filas.valueChanged.connect(self.ajustaRenglones)
 		self.espera.valueChanged.connect(self.speed) #Conecta los valores de la spinbox con el metodo
 		self.tableWidget.setColumnCount(self.columnas.value()) #Inicia las columnas en el minimo de la spinbox
 		self.tableWidget.setRowCount(self.filas.value()) #Inicia las filas en el minimo de la spinbox
 		
 		self.corCabeza = [3,5]
 		self.corCuerpo1 = [3,4]
 		self.corCuerpo2 = [3,3]
 		self.corCuerpo3 = [3, 2]
 		self.corCola = [3,1]
 		self.dire= 1

 		self.tableWidget.keyPressEvent = self.keyPressEvent
 		self.iniciajuego.clicked.connect(self.playGameButton)
 		self.pushButton_2.clicked.connect(self.termina)
 		self.pushButton_2.hide()
 		
 	def ajustaColumnas(self, columnas): #Cambia las columnas cuando se cambia el valor de la spinbox
 		self.tableWidget.setColumnCount(columnas)

 	def ajustaRenglones(self, renglones): #Cambia las filas cuando se cambia el valor de la spinbox
 		self.tableWidget.setRowCount(renglones)

 	def speed(self, velocidad):
 		self.timer.setInterval(velocidad)

 	def matame(self):
 		if self.corCabeza == self.corCola:
 			print("moriste we :v")
 			return True

 		#Inicia el juego
 	def playGameButton(self):
 		if self.iniciajuego.text() == "Inicia Juego":
 			self.cabezaSnake = QTableWidgetItem()
 			self.cuerpoSnake1 = QTableWidgetItem()
 			self.cuerpoSnake2 = QTableWidgetItem()
 			self.cuerpoSnake3 = QTableWidgetItem()
 			self.colaSnake = QTableWidgetItem()
 			self.cabezaSnake.setBackgroundColor(QtGui.QColor(100,100,150))
 			self.cuerpoSnake1.setBackgroundColor(QtGui.QColor(100,100,150))
 			self.cuerpoSnake2.setBackgroundColor(QtGui.QColor(100,100,150))
 			self.cuerpoSnake3.setBackgroundColor(QtGui.QColor(100,100,150))
 			self.colaSnake.setBackgroundColor(QtGui.QColor(100,100,150))
 			self.iniciajuego.setText("Pausar el juego")#Cambia el texto del boton
 			self.tableWidget.setItem(self.corCabeza[0], self.corCabeza[1], self.cabezaSnake)
 			self.tableWidget.setItem(self.corCuerpo1[0], self.corCuerpo1[1], self.cuerpoSnake1)
 			self.tableWidget.setItem(self.corCuerpo2[0], self.corCuerpo2[1], self.cuerpoSnake2)
 			self.tableWidget.setItem(self.corCuerpo3[0], self.corCuerpo3[1], self.cuerpoSnake3)
 			self.tableWidget.setItem(self.corCola[0], self.corCola[1], self.colaSnake)
 			self.pushButton_2.show()
 			self.timer = QTimer()
 			self.timer.timeout.connect(self.condicional)
 			self.timer.start(150)
 			self.espera.setValue(150)
 		elif self.iniciajuego.text() == "Pausar el juego":
 			self.timer.stop()
 			self.iniciajuego.setText("Reanudar juego")
 		else: 
 			self.timer.start(self.espera.value())
 			self.iniciajuego.setText("Pausar el juego")
 

 	def caminaDerecha(self):
 		self.tableWidget.takeItem(self.corCabeza[0], self.corCabeza[1])
 		self.tableWidget.takeItem(self.corCuerpo1[0], self.corCuerpo1[1])
 		self.tableWidget.takeItem(self.corCuerpo2[0], self.corCuerpo2[1])
 		self.tableWidget.takeItem(self.corCuerpo3[0], self.corCuerpo3[1])
 		self.tableWidget.takeItem(self.corCola[0], self.corCola[1])

 		self.cabezaSnake = QTableWidgetItem()
 		self.cuerpoSnake1 = QTableWidgetItem()
 		self.cuerpoSnake2 = QTableWidgetItem()
 		self.cuerpoSnake3 = QTableWidgetItem()
 		self.colaSnake = QTableWidgetItem()

 		self.cabezaSnake.setBackgroundColor(QtGui.QColor(100,100,150))
 		self.cuerpoSnake1.setBackgroundColor(QtGui.QColor(100,100,150))
 		self.cuerpoSnake2.setBackgroundColor(QtGui.QColor(100,100,150))
 		self.cuerpoSnake3.setBackgroundColor(QtGui.QColor(100,100,150))
 		self.colaSnake.setBackgroundColor(QtGui.QColor(100,100,150))

 		self.corCola= self.corCuerpo3
 		self.corCuerpo3 = self.corCuerpo2
 		self.corCuerpo2 = self.corCuerpo1
 		self.corCuerpo1 = self.corCabeza
 		self.corCabeza = [ self.corCabeza[0] , (self.corCabeza[1] + 1)% self.tableWidget.columnCount()]

 		self.tableWidget.setItem(self.corCabeza[0], self.corCabeza[1], self.cabezaSnake)
 		self.tableWidget.setItem(self.corCuerpo1[0], self.corCuerpo1[1], self.cuerpoSnake1)
 		self.tableWidget.setItem(self.corCuerpo2[0], self.corCuerpo2[1], self.cuerpoSnake2)
 		self.tableWidget.setItem(self.corCuerpo3[0], self.corCuerpo3[1], self.cuerpoSnake3)
 		self.tableWidget.setItem(self.corCola[0], self.corCola[1], self.colaSnake)

 	def caminaIzquierda(self):
 		self.tableWidget.takeItem(self.corCabeza[0], self.corCabeza[1])
 		self.tableWidget.takeItem(self.corCuerpo1[0], self.corCuerpo1[1])
 		self.tableWidget.takeItem(self.corCuerpo2[0], self.corCuerpo2[1])
 		self.tableWidget.takeItem(self.corCuerpo3[0], self.corCuerpo3[1])
 		self.tableWidget.takeItem(self.corCola[0], self.corCola[1])

 		self.cabezaSnake = QTableWidgetItem()
 		self.cuerpoSnake1 = QTableWidgetItem()
 		self.cuerpoSnake2 = QTableWidgetItem()
 		self.cuerpoSnake3 = QTableWidgetItem()
 		self.colaSnake = QTableWidgetItem()

 		self.cabezaSnake.setBackgroundColor(QtGui.QColor(100,100,150))
 		self.cuerpoSnake1.setBackgroundColor(QtGui.QColor(100,100,150))
 		self.cuerpoSnake2.setBackgroundColor(QtGui.QColor(100,100,150))
 		self.cuerpoSnake3.setBackgroundColor(QtGui.QColor(100,100,150))
 		self.colaSnake.setBackgroundColor(QtGui.QColor(100,100,150))

 		self.corCola= self.corCuerpo3
 		self.corCuerpo3 = self.corCuerpo2
 		self.corCuerpo2 = self.corCuerpo1
 		self.corCuerpo1 = self.corCabeza
 		self.corCabeza = [ self.corCabeza[0] , (self.corCabeza[1] - 1)% self.tableWidget.columnCount()]

 		self.tableWidget.setItem(self.corCabeza[0], self.corCabeza[1], self.cabezaSnake)
 		self.tableWidget.setItem(self.corCuerpo1[0], self.corCuerpo1[1], self.cuerpoSnake1)
 		self.tableWidget.setItem(self.corCuerpo2[0], self.corCuerpo2[1], self.cuerpoSnake2)
 		self.tableWidget.setItem(self.corCuerpo3[0], self.corCuerpo3[1], self.cuerpoSnake3)
 		self.tableWidget.setItem(self.corCola[0], self.corCola[1], self.colaSnake)

 	def caminaArriba(self):
 		self.tableWidget.takeItem(self.corCabeza[0], self.corCabeza[1])
 		self.tableWidget.takeItem(self.corCuerpo1[0], self.corCuerpo1[1])
 		self.tableWidget.takeItem(self.corCuerpo2[0], self.corCuerpo2[1])
 		self.tableWidget.takeItem(self.corCuerpo3[0], self.corCuerpo3[1])
 		self.tableWidget.takeItem(self.corCola[0], self.corCola[1])

 		self.cabezaSnake = QTableWidgetItem()
 		self.cuerpoSnake1 = QTableWidgetItem()
 		self.cuerpoSnake2 = QTableWidgetItem()
 		self.cuerpoSnake3 = QTableWidgetItem()
 		self.colaSnake = QTableWidgetItem()

 		self.cabezaSnake.setBackgroundColor(QtGui.QColor(100,100,150))
 		self.cuerpoSnake1.setBackgroundColor(QtGui.QColor(100,100,150))
 		self.cuerpoSnake2.setBackgroundColor(QtGui.QColor(100,100,150))
 		self.cuerpoSnake3.setBackgroundColor(QtGui.QColor(100,100,150))
 		self.colaSnake.setBackgroundColor(QtGui.QColor(100,100,150))

 		self.corCola= self.corCuerpo3
 		self.corCuerpo3 = self.corCuerpo2
 		self.corCuerpo2 = self.corCuerpo1
 		self.corCuerpo1 = self.corCabeza
 		self.corCabeza = [ (self.corCabeza[0] - 1) % self.tableWidget.rowCount() , (self.corCabeza[1]) ]

 		self.tableWidget.setItem(self.corCabeza[0], self.corCabeza[1], self.cabezaSnake)
 		self.tableWidget.setItem(self.corCuerpo1[0], self.corCuerpo1[1], self.cuerpoSnake1)
 		self.tableWidget.setItem(self.corCuerpo2[0], self.corCuerpo2[1], self.cuerpoSnake2)
 		self.tableWidget.setItem(self.corCuerpo3[0], self.corCuerpo3[1], self.cuerpoSnake3)
 		self.tableWidget.setItem(self.corCola[0], self.corCola[1], self.colaSnake)

 	def caminaAbajo(self):
 		self.tableWidget.takeItem(self.corCabeza[0], self.corCabeza[1])
 		self.tableWidget.takeItem(self.corCuerpo1[0], self.corCuerpo1[1])
 		self.tableWidget.takeItem(self.corCuerpo2[0], self.corCuerpo2[1])
 		self.tableWidget.takeItem(self.corCuerpo3[0], self.corCuerpo3[1])
 		self.tableWidget.takeItem(self.corCola[0], self.corCola[1])

 		self.cabezaSnake = QTableWidgetItem()
 		self.cuerpoSnake1 = QTableWidgetItem()
 		self.cuerpoSnake2 = QTableWidgetItem()
 		self.cuerpoSnake3 = QTableWidgetItem()
 		self.colaSnake = QTableWidgetItem()

 		self.cabezaSnake.setBackgroundColor(QtGui.QColor(100,100,150))
 		self.cuerpoSnake1.setBackgroundColor(QtGui.QColor(100,100,150))
 		self.cuerpoSnake2.setBackgroundColor(QtGui.QColor(100,100,150))
 		self.cuerpoSnake3.setBackgroundColor(QtGui.QColor(100,100,150))
 		self.colaSnake.setBackgroundColor(QtGui.QColor(100,100,150))

 		self.corCola= self.corCuerpo3
 		self.corCuerpo3 = self.corCuerpo2
 		self.corCuerpo2 = self.corCuerpo1
 		self.corCuerpo1 = self.corCabeza
 		self.corCabeza = [ (self.corCabeza[0] + 1) % self.tableWidget.rowCount() , (self.corCabeza[1]) ]

 		self.tableWidget.setItem(self.corCabeza[0], self.corCabeza[1], self.cabezaSnake)
 		self.tableWidget.setItem(self.corCuerpo1[0], self.corCuerpo1[1], self.cuerpoSnake1)
 		self.tableWidget.setItem(self.corCuerpo2[0], self.corCuerpo2[1], self.cuerpoSnake2)
 		self.tableWidget.setItem(self.corCuerpo3[0], self.corCuerpo3[1], self.cuerpoSnake3)
 		self.tableWidget.setItem(self.corCola[0], self.corCola[1], self.colaSnake)

 	def condicional(self):
 		if self.dire == 1:
 			self.mueveVib(1)
 		elif self.dire == 2:
 			self.mueveVib(2)
 		elif self.dire == 3:
 			self.mueveVib(3)
 		elif self.dire == 0:  
 			self.mueveVib(0)
 		if self.matame():
 			self.termina()

 	def mueveVib(self, dir):
 		if dir == 1:
 			self.caminaDerecha()
 		elif dir == 2:
 			self.caminaIzquierda()
 		elif dir == 3:
 			self.caminaAbajo()
 		elif self.dire == 0:
 			self.caminaArriba()

 	def keyPressEvent(self,event):
 		if event.key() == QtCore.Qt.Key_Left and self.dire != 1:
 			self.dire= 2
 		elif event.key() == QtCore.Qt.Key_Right and self.dire != 2:
 			self.dire= 1
 		elif event.key() == QtCore.Qt.Key_Up and self.dire != 3:
 			self.dire= 0
 		elif event.key() == QtCore.Qt.Key_Down and self.dire != 0:
 			self.dire= 3
 	
 	def termina(self):
 		self.iniciajuego.setText("Inicia Juego")#Cambia el texto del boton
 		self.tableWidget.takeItem(self.corCabeza[0], self.corCabeza[1])
 		self.tableWidget.takeItem(self.corCuerpo1[0], self.corCuerpo1[1])
 		self.tableWidget.takeItem(self.corCuerpo2[0], self.corCuerpo2[1])
 		self.tableWidget.takeItem(self.corCuerpo3[0], self.corCuerpo3[1])
 		self.tableWidget.takeItem(self.corCola[0], self.corCola[1])
 		self.pushButton_2.hide()
 		self.timer.stop()

#Inicia la aplicacion.
def main():
    app = QtGui.QApplication(sys.argv)
    win = Servidor()
    win.show()
    app.exec_()
    
main()
