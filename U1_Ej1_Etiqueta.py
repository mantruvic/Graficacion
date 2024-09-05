import tkinter

#Creación del objeto ventana 
ventana = tkinter.Tk()
#definicion del tamano de la ventana
ventana.geometry("800x600")

#Creación de Etiqueta Simple y fuente personalizada 
etiqueta = tkinter.Label(ventana,text="Hola Mundo",font="Helvetica 20")
etiqueta.pack()
#Creación de Etiqueta con fondo y expansion en eje Y
etiqueta = tkinter.Label(ventana, text = "Hola Mundo", bg="blue")
etiqueta.pack(fill=tkinter.Y , expand=1)
#otra forma de declarar una etiqueta 
etiqueta2 = tkinter.Label(text="Hola Mundo").pack

#Lanza el bucle principal, encargado de gestionar todos los eventos que reciba la aplicación.
ventana.mainloop()