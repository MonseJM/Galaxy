from tkinter import * 
from tkinter import messagebox, filedialog
from tkinter.filedialog import asksaveasfile
from tkinter import scrolledtext as st
import tkinter as tk

import articulos

class ListaProvedor():
            
    def DataProL():
        ##################################################################################
        articulo1=articulos.Articulos()
        ventana = Tk() #creamos un objeto de la clase tk que nos permite tener todos los metodos de una GUI.

        ventana.geometry('950x550')
        ventana.config(bg='white') #"bg"--> background de color verde, es decir, fondo.
        ventana.title('Lista de Proveedores') #Colocamos titulo a la ventana.
        ventana.resizable(width=False, height=False) #Hacemos que la ventana no sea reducible.
        #-------------------------------------------
        ventana.iconbitmap('Imagenes\logo.png') #Cambiamos el icono de la ventana.
        main_title = Label(text="                          Lista de Proveedores                         ",font=("Bauhaus 93",35),bg="#A3F6C5",fg="black")
        main_title.pack()
        #-------------------------------------------

        scrolledtext1=st.ScrolledText(ventana, width=70, height=17)
        scrolledtext1.place(x=123,y=100)


        #-------------------------------------------


        def Regresar():
            pass #--> Con el pass permites que se ejecute una función sin tomar en cuenta sus sentencias (si tiene o no).
            ventana.destroy()
            from OpcionesProveedores import OpcionesProvee
            #SystemExit()
            OpcionesProvee.elegir3()
 

        imagen2=PhotoImage(file='Imagenes\RegresarPro.png') #Creamos un objeto de la clase PhotoImage que usa etiquetas para imagenes.
        boton_Regresar=Button(ventana, image=imagen2, bg='light gray', command=Regresar) #Creamos un objeto de la clase Button.
        boton_Regresar.config(width=388, height=45)
        boton_Regresar.place(x=27, y=476)
            


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

        def Lista():
            pass #--> Con el pass permites que se ejecute una función sin tomar en cuenta sus sentencias (si tiene o no).
            respuesta=articulo1.recuperar_todos()
            scrolledtext1.delete("1.0", tk.END)        
            for fila in respuesta:
                scrolledtext1.insert(tk.END, "código:"+str(fila[0])+
                                              "\ndescripción:"+fila[1]+
                                              "\nprecio:"+str(fila[2])+"\n\n")


        boton_Guardar=Button(ventana, text='Mostrar la Lista ', bg='light gray', command=Lista, font=('Century Gothic bold', 15)) #Creamos un objeto de la clase Button.
        boton_Guardar.config(width=20, height=1)
        boton_Guardar.place(x=552,y=410)


        ventana.mainloop() #el metodo mantiene la ventana abierta y visible.


