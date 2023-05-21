from tkinter import *
from tkinter import messagebox
import mysql.connector
import articulos
#import tkinter


##################################################################################
class Loguin():
    
    def abrir():


        ventana = Tk() #creamos un objeto de la clase tk que nos permite tener todos los metodos de una GUI.

        ventana.geometry('950x550')
        ventana.config(bg='white') #"bg"--> background de color verde, es decir, fondo.
        ventana.title('Tienda Galaxy') #Colocamos titulo a la ventana.
        ventana.resizable(width=False, height=False) #Hacemos que la ventana no sea reducible.
        #-------------------------------------------
        ventana.iconbitmap('Imagenes\logo.png') #Cambiamos el icono de la ventana.
        #-------------------------------------------
        main_title = Label(text="                            Tienda Galaxy                          ",font=("Bauhaus 93",35),bg="#9F9FE5",fg="black")
        main_title.pack()
        #-------------------------------------------
        imagen1=PhotoImage(file='Imagenes\icon.png') #Creamos un objeto de la clase PhotoImage que usa etiquetas para imagenes.
        Label(ventana, image=imagen1).place(x=513,y=133)
        #---------------------------------------------------------------------------------------------------------------------
        def Articulos():
            pass #--> Con el pass permites que se ejecute una función sin tomar en cuenta sus sentencias (si tiene o no).
            ventana.destroy()
            from OpcionesArticulos import OpcionesArticulos
            #SystemExit()
            OpcionesArticulos.elegir() 

        imagen=PhotoImage(file='Imagenes\BotonArticulo.png') #Creamos un objeto de la clase PhotoImage que usa etiquetas para imagenes.
        boton_Productos=Button(ventana, image=imagen, bg='white', command=Articulos) #Creamos un objeto de la clase Button.
        boton_Productos.config(width=357, height=89)
        boton_Productos.place(x=68, y=118)

        def Clientes():
            pass #--> Con el pass permites que se ejecute una función sin tomar en cuenta sus sentencias (si tiene o no).
            ventana.destroy()
            from OpcionesClientes import OpcionesCliente
            #SystemExit()
            OpcionesCliente.elegircli() 

        imagen2=PhotoImage(file='Imagenes\BotonClientes.png') #Creamos un objeto de la clase PhotoImage que usa etiquetas para imagenes.
        boton_Clientes=Button(ventana, image=imagen2, bg='white', command=Clientes) #Creamos un objeto de la clase Button.
        boton_Clientes.config(width=353, height=92)
        boton_Clientes.place(x=72, y=239)

        def Proveedores():
            pass #--> Con el pass permites que se ejecute una función sin tomar en cuenta sus sentencias (si tiene o no).
            ventana.destroy()
            from OpcionesProveedores import OpcionesProvee
            #SystemExit()
            OpcionesProvee.elegir3() 

        imagen3=PhotoImage(file='Imagenes\BotonProvee.png') #Creamos un objeto de la clase PhotoImage que usa etiquetas para imagenes.
        boton_Provee=Button(ventana, image=imagen3, bg='white', command=Proveedores) #Creamos un objeto de la clase Button.
        boton_Provee.config(width=356, height=92)
        boton_Provee.place(x=68, y=363)


        #######################################################################
        ventana.mainloop() #el metodo mantiene la ventana abierta y visible.
    abrir()