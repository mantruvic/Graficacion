import tkinter 

ventana = tkinter.Tk()
ventana.geometry("800x600")

boton1 = tkinter.Button(ventana,text="Boton 1",width=10,height=5)
boton2 = tkinter.Button(ventana,text="Boton 2",width=10,height=5)
boton3 = tkinter.Button(ventana,text="Boton 3",width=10,height=5)

boton1.grid(row=0,column=0)
boton2.grid(row=1,column=0)
boton3.grid(row=2,column=0)

ventana.mainloop()