from tkinter import ttk
from tkinter import *
import math
from datetime import date
from datetime import datetime

window = Tk()
#Tamaño del caudro.
ancho =600
alto =300
window.geometry(str(ancho)+"x"+str(alto))
window.title("Examen Final")
lbl25 = Label(window, text="Bienvenido")

lbl25.grid(column=1, row=0)

lbl5 = Label(window, text="Nombre")

lbl5.grid(column=0, row=1)

txt5 = Entry(window,width=10)

txt5.grid(column=1, row=1)

lbl10 = Label(window, text="Apellido")

lbl10.grid(column=0, row=2)

txt10 = Entry(window,width=10)

txt10.grid(column=1, row=2)

lbl15 = Label(window, text="Día")

lbl15.grid(column=0, row=3)

txt15 = Entry(window,width=10)

txt15.grid(column=1, row=3)

lbl20 = Label(window, text="Mes")

lbl20.grid(column=0, row=4)

txt20 = Entry(window,width=10)

txt20.grid(column=1, row=4)

lbl25 = Label(window, text="Año")

lbl25.grid(column=0, row=5)

txt25 = Entry(window,width=10)

txt25.grid(column=1, row=5)

#Muestra el resultado segun la función.
labelText = StringVar()
labelText.set("Aca se verá el resultado de las funciones")
lbl30 = Label(window, textvariable=labelText)
lbl30.grid(column=0, row=7)

#Función que convierte las fechas en código hexadecimal.
def codigo_hexadecimal():
    dia =hex(int( txt15.get()))
    mes =hex(int( txt20.get()))
    año =hex(int( txt25.get()))
    resultado = dia+"/"+mes+"/"+año
    labelText.set(str(resultado))

btn6 = Button(window, text="funcion 1", command=codigo_hexadecimal)

btn6.grid(column=1, row=6)

#Función que muestra las horas vividas.
def vida_en_horas():
    dia =int( txt15.get())
    mes =int( txt20.get())
    año =int( txt25.get())
    fecha_cad1 =str(dia)+"-"+str(mes)+"-"+str(año)
    hoy= datetime.today()
    fecha1 = datetime.strptime(fecha_cad1, '%d-%m-%Y')
    tiempo = hoy-fecha1
    numeroDias=tiempo.days*24
    labelText.set("Usted nacio el "+ str(dia)+"/"+str(mes)+"/"+str(año)+" y ha vivido "+str(numeroDias)+" horas")
btn7 = Button(window, text="funcion 2", command=vida_en_horas)

btn7.grid(column=2, row=6)

#Finción que indica si su nombre y apellido es par o impar.
def letras_par_o_impar():

    nombre=txt5.get()
    apellido=txt10.get()
    todo= nombre+apellido  
    todo2= nombre+" "+apellido 
    suma=  len(todo)
    respuesta="impar"
    if suma%2==0:
        respuesta="par"
    labelText.set(todo2+" su nombre y su apellido es "+respuesta)
btn8 = Button(window, text="funcion 3", command=letras_par_o_impar)

btn8.grid(column=3, row=6)

#Función que muestra cuantas vocales y consonantes tiene su nombre.
def vocales_y_consonantes():
    nombre=str(txt5.get())
    apellido=str(txt10.get())
    Suma = 0
    for voc in nombre:
        if voc == 'a' or voc =='A' or voc =='e' or voc =='E' or voc =='i' or voc =='I' or voc =='o' or voc =="O" or voc =="u" or voc =="U":
            Suma += 1
    for voc in apellido:
        if voc == 'a' or voc =='A' or voc =='e' or voc =='E' or voc =='i' or voc =='I' or voc =='o' or voc =="O" or voc =="u" or voc =="U":
            Suma += 1
    Conso1=len(nombre)
    Conso2=len(apellido)
    SalidaConso=Conso1+Conso2-Suma

    labelText.set(nombre + " " + apellido + ' tiene {} vocales y {} consonantes.'.format(Suma,SalidaConso))
    
btn9 = Button(window, text="funcion 4", command=vocales_y_consonantes)

btn9.grid(column=4, row=6)

#Función que coloca su nombre y apellido al revés.
def nombre_y_apellido_al_reves():
    text40 = txt5.get()+" "+txt10.get()
    text40 = text40[::-1]
    labelText.set(txt5.get()+""+ txt10.get()+"su nombre y apellido al revés es:" + text40) 
btn10 = Button(window, text="funcion 5", command=nombre_y_apellido_al_reves)

btn10.grid(column=5, row=6)

window.mainloop()
