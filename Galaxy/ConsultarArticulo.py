from tkinter import * 
from tkinter import messagebox, filedialog
from tkinter.filedialog import asksaveasfile
import articulos

class ConsultarArticulo():
            
    def Data4():
        ##################################################################################
        articulo1=articulos.Articulos()
        ventana = Tk() #creamos un objeto de la clase tk que nos permite tener todos los metodos de una GUI.

        ventana.geometry('950x550')
        ventana.config(bg='white') #"bg"--> background de color verde, es decir, fondo.
        ventana.title('Modificar el Articulo') #Colocamos titulo a la ventana.
        ventana.resizable(width=False, height=False) #Hacemos que la ventana no sea reducible.
        #-------------------------------------------
        ventana.iconbitmap('Imagenes\logo.png') #Cambiamos el icono de la ventana.
        main_title = Label(text="                           Consultar Articulo                          ",font=("Bauhaus 93",35),bg="#F4A2CE",fg="black")
        main_title.pack()
        #-------------------------------------------
        codigo = StringVar()
        descripcion = StringVar()
        precio = StringVar()
        #-------------------------------------------
        etiqueta=Label(ventana, text='Codigo:', fg='black', font=("Bauhaus 93",30), bg='white') #Creamos un objeto de la clase etiqueta. --> fg=foreground.
        etiqueta.place(x=130, y=136) #Posicionamos la etiqueta.

        etiqueta=Label(ventana, text='Nombre:', fg='black', font=("Bauhaus 93",30), bg='white') #Creamos un objeto de la clase etiqueta. --> fg=foreground.
        etiqueta.place(x=130, y=215) #Posicionamos la etiqueta.

        etiqueta1=Label(ventana, text='Precio:', fg='black', font=("Bauhaus 93",30), bg='white') #Creamos un objeto de la clase etiqueta. --> fg=foreground.
        etiqueta1.place(x=130, y=294) #Posicionamos la etiqueta.

        #-------------------------------------------
        Campo_Codigo=Entry(ventana, textvariable=codigo,bg='light gray', bd='8', font=('Century Gothic bold',8), fg='black' ) #Creamos un objeto de la clase Entry que nos permite colocar campos de texto.
        Campo_Codigo.place(x=511, y=136, width=330, height=44)

        campo_nombre=Entry(ventana, textvariable=descripcion,bg='light gray', bd='8', font=('Century Gothic bold',8), fg='black') #Creamos un objeto de la clase Entry que nos permite colocar campos de texto.
        campo_nombre.place(x=511, y=215, width=330, height=44)

        campo_edad=Entry(ventana, textvariable=precio,bg='light gray', bd='8', font=('Century Gothic bold',8), fg='black') #Creamos un objeto de la clase Entry que nos permite colocar campos de texto.
        campo_edad.place(x=511, y=294, width=330, height=44)

        #-------------------------------------------
        def Regresar():
            pass #--> Con el pass permites que se ejecute una función sin tomar en cuenta sus sentencias (si tiene o no).
            ventana.destroy()
            from OpcionesArticulos import OpcionesArticulos
            #SystemExit()
            OpcionesArticulos.elegir()
        imagen2=PhotoImage(file='Imagenes\Regresar.png') #Creamos un objeto de la clase PhotoImage que usa etiquetas para imagenes.
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

        def Consultar():

            pass #--> Con el pass permites que se ejecute una función sin tomar en cuenta sus sentencias (si tiene o no).
            datos=(codigo.get(), )
            respuesta=articulo1.consulta(datos)
            if len(respuesta)>0:
              descripcion.set(respuesta[0][0])
              
              precio.set(respuesta[0][1])
            else:
              descripcion.set('')
              precio.set('')
              messagebox.showwarning("Información", "No existe un artículo con dicho código")
            

        boton_Guardar=Button(ventana, text='Consultar', bg='light gray', command=Consultar, font=('Century Gothic bold', 15)) #Creamos un objeto de la clase Button.
        boton_Guardar.config(width=10, height=1)
        boton_Guardar.place(x=552,y=380)


        ventana.mainloop() #el metodo mantiene la ventana abierta y visible.
