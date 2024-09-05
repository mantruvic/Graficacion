import tkinter
import tkinter.messagebox

ventana = tkinter.Tk()
ventana.geometry("800x600")

def saludo(saludo):
    print("Hola " + saludo)
    tkinter.messagebox.showinfo(message="¡Hola, mundo!" + saludo, title="Saludo")

def textoDelaCaja():
    TextoCaja = cajaTexto.get()
    etiqueta["text"] = TextoCaja    

## boton mandando mensaje en funcion con parametros 
boton1 = tkinter.Button(ventana, text="Presiona" , padx=15,pady=8, command=lambda:saludo("python"))
##comamnd = lambda: saludo("python")
## lambda: print("Hola")
boton1.pack()

###Etiqueta
etiqueta = tkinter.Label(ventana)
etiqueta.pack()
##caja texto con fuente personalizada
cajaTexto = tkinter.Entry(ventana, font="Helvetica 20")
cajaTexto.pack()
#boton usando el tecto escrito en un textbox 
boton2 = tkinter.Button(ventana, text="Presiona",command=textoDelaCaja)
boton2.pack()

ventana.mainloop()