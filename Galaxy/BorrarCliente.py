from tkinter import * 
from tkinter import messagebox, filedialog
from tkinter.filedialog import asksaveasfile
import articulos

class BorrarCliente():
            
    def DatacliB():
        ##################################################################################
        articulo1=articulos.Articulos()
        ventana = Tk() #creamos un objeto de la clase tk que nos permite tener todos los metodos de una GUI.

        ventana.geometry('950x550')
        ventana.config(bg='white') #"bg"--> background de color verde, es decir, fondo.
        ventana.title('Borrar el Articulo') #Colocamos titulo a la ventana.
        ventana.resizable(width=False, height=False) #Hacemos que la ventana no sea reducible.
        #-------------------------------------------
        ventana.iconbitmap('Imagenes\logo.png') #Cambiamos el icono de la ventana.
        main_title = Label(text="                            Borrar Cliente                          ",font=("Bauhaus 93",35),bg="#9CD9E2",fg="black")
        main_title.pack()
        #-------------------------------------------
        codigoborra = StringVar()
        #-------------------------------------------
        etiqueta=Label(ventana, text='Codigo:', fg='black', font=("Bauhaus 93",35), bg='white') #Creamos un objeto de la clase etiqueta. --> fg=foreground.
        etiqueta.place(x=123, y=140) #Posicionamos la etiqueta.

        #-------------------------------------------
        campo_nombre=Entry(ventana, textvariable=codigoborra,bg='light gray', bd='8',  font=('Century Gothic bold',10), fg='black') #Creamos un objeto de la clase Entry que nos permite colocar campos de texto.
        campo_nombre.place(x=536, y=140, width=328, height=65)
        #-------------------------------------------
        def Regresar():
            pass #--> Con el pass permites que se ejecute una función sin tomar en cuenta sus sentencias (si tiene o no).
            ventana.destroy()
            from OpcionesClientes import OpcionesCliente
            #SystemExit()
            OpcionesCliente.elegircli()
            

            
        imagen2=PhotoImage(file='Imagenes\RegresarCli.png') #Creamos un objeto de la clase PhotoImage que usa etiquetas para imagenes.
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

        def Borrar():
            pass #--> Con el pass permites que se ejecute una función sin tomar en cuenta sus sentencias (si tiene o no).
            datos=(codigoborra.get(), )
            cantidad=articulo1.baja(datos)
            if cantidad==1:
                messagebox.showwarning("Información", "Se borró el artículo con dicho código")

            else:
                 messagebox.showwarning("Información", "No existe un artículo con dicho código")


        boton_Guardar=Button(ventana, text='Borrar', bg='light gray', command=Borrar, font=('Century Gothic bold', 15)) #Creamos un objeto de la clase Button.
        boton_Guardar.config(width=15, height=1)
        boton_Guardar.place(x=552,y=380)
 


        ventana.mainloop() #el metodo mantiene la ventana abierta y visible.
