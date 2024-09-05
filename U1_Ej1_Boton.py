import tkinter
import tkinter.messagebox

ventana = tkinter.Tk()
ventana.geometry("800x600")

#Funcion saludo 
def saludo():
    print("Hola")
#la impresion se refleja en la consola 

def saludar():
    tkinter.messagebox.showinfo(message="¡Hola, mundo!", title="Saludo")
    
#Creacion de Boton 
boton1 = tkinter.Button(ventana, text="Presiona" , padx=10,pady=30)
#se ubica el boton en un lugar especifico 
boton1.place(x=50,y=50)
#Segundo boton con llamada a una funcion 
boton2 = tkinter.Button(ventana, text="Presiona" , padx=50,pady=80,command=saludo,bg="blue",fg="white")
boton2.pack()
#Tercer boton con llamada a una funcion usando otro elemento 
boton3 = tkinter.Button(ventana, text="Presiona" , padx=10,pady=40,command=saludar)
#Fondo a boton (una manera)
boton3.configure(bg="Red")
boton3.pack()
###Etiqueta
etiqueta = tkinter.Label(ventana)
etiqueta.pack()

ventana.mainloop()