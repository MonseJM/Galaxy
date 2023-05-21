from tkinter import * 
from tkinter import messagebox, filedialog
from tkinter.filedialog import asksaveasfile
import articulos

class AgregarCliente():
            
    def DatacliA():
        ##################################################################################
        articulo1=articulos.Articulos()
        ventana = Tk() #creamos un objeto de la clase tk que nos permite tener todos los metodos de una GUI.

        ventana.geometry('950x550')
        ventana.config(bg='white') #"bg"--> background de color verde, es decir, fondo.
        ventana.title('Resgistrar el Articulo') #Colocamos titulo a la ventana.
        ventana.resizable(width=False, height=False) #Hacemos que la ventana no sea reducible.
        #-------------------------------------------
        ventana.iconbitmap('Imagenes\logo.png') #Cambiamos el icono de la ventana.
        main_title = Label(text="                            Agregar Clientes                          ",font=("Bauhaus 93",35),bg="#9CD9E2",fg="black")
        main_title.pack()
        #-------------------------------------------
        descripcioncarga = StringVar()
        preciocarga = StringVar()
        #-------------------------------------------
        etiqueta=Label(ventana, text='Nombre:', fg='black', font=("Bauhaus 93",35), bg='white') #Creamos un objeto de la clase etiqueta. --> fg=foreground.
        etiqueta.place(x=123, y=140) #Posicionamos la etiqueta.

        etiqueta1=Label(ventana, text='Telefono:', fg='black', font=("Bauhaus 93",35), bg='white') #Creamos un objeto de la clase etiqueta. --> fg=foreground.
        etiqueta1.place(x=123, y=243) #Posicionamos la etiqueta.

        #-------------------------------------------
        campo_nombre=Entry(ventana, textvariable=descripcioncarga,bg='light gray', bd='8', font=('Century Gothic bold',20), fg='black') #Creamos un objeto de la clase Entry que nos permite colocar campos de texto.
        campo_nombre.place(x=536, y=140, width=328, height=65)

        campo_precio=Entry(ventana, textvariable=preciocarga,bg='light gray', bd='8', font=('Century Gothic bold',20), fg='black') #Creamos un objeto de la clase Entry que nos permite colocar campos de texto.
        campo_precio.place(x=536, y=243, width=328, height=65)
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

        def Guardar():
            pass #--> Con el pass permites que se ejecute una función sin tomar en cuenta sus sentencias (si tiene o no).
            datos=(descripcioncarga.get(),preciocarga.get())
            articulo1.altaCliente(datos)
            descripcioncarga.set("")
            preciocarga.set("")

            messagebox.showwarning('Aviso.', '''DATOS GUARDADOS CORRECTAMENTE EN NUESTRA BASE DE DATOS.''')

        boton_Guardar=Button(ventana, text='GUARDAR.', bg='light gray', command=Guardar, font=('Century Gothic bold', 15)) #Creamos un objeto de la clase Button.
        boton_Guardar.config(width=15, height=1)
        boton_Guardar.place(x=552,y=380)


        ventana.mainloop() #el metodo mantiene la ventana abierta y visible.
