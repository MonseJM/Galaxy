from tkinter import *
#import tkinter
#from tkinter.tix import IMAGETEXT 

##################################################################################
class OpcionesArticulos():
    
    def elegir():

        ventana = Tk() #creamos un objeto de la clase tk que nos permite tener todos los metodos de una GUI.

        ventana.geometry('950x550')
        ventana.config(bg='white') #"bg"--> background de color verde, es decir, fondo.
        ventana.title('Opciones') #Colocamos titulo a la ventana.
        ventana.resizable(width=False, height=False) #Hacemos que la ventana no sea reducible.
        #-------------------------------------------
        ventana.iconbitmap('Imagenes\logo.png') #Cambiamos el icono de la ventana.
        
        #-------------------------------------------
        main_title = Label(ventana,text="                            Opciones Articulo...                            ",font=("Bauhaus 93",35),bg="#F4A2CE",fg="black")
        main_title.pack()
        Logo1=PhotoImage(file='Imagenes\logoAr.png') #Creamos un objeto de la clase PhotoImage que usa etiquetas para imagenes.
        Label(ventana, image=Logo1).place(x=501,y=105) 
        #-------------------------------------------
        def Registrar():
            pass #--> Con el pass permites que se ejecute una función sin tomar en cuenta sus sentencias (si tiene o no).
            ventana.destroy()
            from AgregarArticulo import AgregarArticulo
            #SystemExit()
            AgregarArticulo.Data() 

        imagen=PhotoImage(file='Imagenes\BotonAr.png') #Creamos un objeto de la clase PhotoImage que usa etiquetas para imagenes.
        boton_Productos=Button(ventana, image=imagen, bg='white', command=Registrar) #Creamos un objeto de la clase Button.
        boton_Productos.config(width=390, height=59)
        boton_Productos.place(x=36, y=92)

        def Borrar():
            pass #--> Con el pass permites que se ejecute una función sin tomar en cuenta sus sentencias (si tiene o no).
            ventana.destroy()
            from BorrarArticulo import BorrarArticulo
            #SystemExit()
            BorrarArticulo.Data2()

        imagen1=PhotoImage(file='Imagenes\BotonArticuloB.png') #Creamos un objeto de la clase PhotoImage que usa etiquetas para imagenes.
        boton_Ventas=Button(ventana, image=imagen1, bg='white', command=Borrar) #Creamos un objeto de la clase Button.
        boton_Ventas.config(width=388, height=58)
        boton_Ventas.place(x=38, y=168)

        def Modificar():
            pass #--> Con el pass permites que se ejecute una función sin tomar en cuenta sus sentencias (si tiene o no).
            ventana.destroy()
            from ModificarArticulo import ModificarArticulo
            #SystemExit()
            ModificarArticulo.Data3()

        imagen2=PhotoImage(file='Imagenes\BotonArticuloM.png') #Creamos un objeto de la clase PhotoImage que usa etiquetas para imagenes.
        boton_Modi=Button(ventana, image=imagen2, bg='white', command=Modificar) #Creamos un objeto de la clase Button.
        boton_Modi.config(width=391, height=63)
        boton_Modi.place(x=38, y=241)

        
        def Consultar():
            pass #--> Con el pass permites que se ejecute una función sin tomar en cuenta sus sentencias (si tiene o no).
            ventana.destroy()
            from ConsultarArticulo import ConsultarArticulo
            #SystemExit()
            ConsultarArticulo.Data4()

        imagen3=PhotoImage(file='Imagenes\BotonArticuloC.png') #Creamos un objeto de la clase PhotoImage que usa etiquetas para imagenes.
        boton_Con=Button(ventana, image=imagen3, bg='white', command=Consultar) #Creamos un objeto de la clase Button.
        boton_Con.config(width=393, height=58)
        boton_Con.place(x=36, y=324)

        def Lista():
            pass #--> Con el pass permites que se ejecute una función sin tomar en cuenta sus sentencias (si tiene o no).
            ventana.destroy()
            from ListaArticulo import ListaArticulo
            #SystemExit()
            ListaArticulo.Data5()

        imagen4=PhotoImage(file='Imagenes\BotonArticuloL.png') #Creamos un objeto de la clase PhotoImage que usa etiquetas para imagenes.
        boton_People=Button(ventana, image=imagen4, bg='white', command=Lista) #Creamos un objeto de la clase Button.
        boton_People.config(width=402, height=61)
        boton_People.place(x=28, y=407)

        def Triangulo():
            pass #--> Con el pass permites que se ejecute una función sin tomar en cuenta sus sentencias (si tiene o no).
            ventana.destroy()
            from Interfaz2 import Loguin
            #SystemExit()
            Loguin.abrir()

        imagen5=PhotoImage(file='Imagenes\logo.png') #Creamos un objeto de la clase PhotoImage que usa etiquetas para imagenes.
        boton_Triangulo=Button(ventana, image=imagen5, bg='light gray', command=Triangulo) #Creamos un objeto de la clase Button.
        boton_Triangulo.config(width=78, height=59)
        boton_Triangulo.place(x=876, y=483)
        #######################################################################
        ventana.mainloop() #el metodo mantiene la ventana abierta y visible.
