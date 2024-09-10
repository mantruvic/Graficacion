import tkinter
from tkinter import filedialog
from PIL import Image, ImageTk
import os

#Ventana 
ventana = tkinter.Tk()
ventana.title("Selector de imagen")
ventana.geometry("400x400+100+100")
ventana.configure(bg="#e4e8eb")
ventana.resizable(False,False)

def MostrarImagen():    
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title='Seleccionar Archivo de Imagen',
                                        filetype=(('Archivo PNG', '*.png'),
                                                  ('Archivo JPG', '*.jpg'),
                                                  ('Todos los archivos', '*.*')))
    img= Image.open(filename)
    img = img.resize((310,270))
    img= ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=310,height=270)
    lbl.image=img

#contenedor para boton selecionar imagen
selectimage = tkinter.Frame(ventana,width=340,height=350,bg="#d6dee5")
selectimage.place(x=30,y=20)
#contenedor de la imagen 
lbl = tkinter.Label(selectimage,bg="#d6dee5")
lbl.place(x=15,y=15)

tkinter.Button(selectimage,text="Elige Imagen",width=12,height=1,
               font="arial 14 bold",command=MostrarImagen).place(x=10,y=300)

ventana.mainloop()