#importacion de tkinter en su forma mas simple
import tkinter
#Creación del objeto ventana 
ventana = tkinter.Tk()
#definicion del tamano de la ventana
ventana.geometry("800x600")
#titulo de la ventana 
ventana.title("Ventana")
#cambiamos el color de fondo de la ventana 
ventana.config(bg="azure")
#configuracion para cambio de tamaño (recibe dos valores si estan en 0,0 se deshabilita modificar en ancho y alto )
ventana.resizable(0,1)
#icono (usar la ruta absoluta en este ejemplo)
ventana.iconbitmap("C:/Users/Marco/Desktop/marshall.ico")


#Lanza el bucle principal, encargado de gestionar todos los eventos que reciba la aplicación.
ventana.mainloop()