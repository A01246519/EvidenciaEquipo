import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from funpymodeling.exploratory import freq_tbl
import seaborn as sns
import webbrowser as wb
import csv


def marco1():
  imagen1=sg.B("",image_filename="airbnb2.png", key="BTN_IMAGEN_1")#crear un botón no activado con una imagen
  texto_contraseña=sg.Text("Asi se les dice a los Jose ", key="TXT_CONTRASENA1")
  texto_instruccion=sg.Text("Escribe una palabra sin espacio para poder continuar", key="TXT_CONTINUAR")
  input_contraseña=sg.Input("", key="INP_CONTRASENA1") #Espacio donde será colocada la contraseña 
  b2=sg.B("Iniciar sesión", key="BTN_INICIARSESION1") #Botón para iniciar sesión si la contraseña es correcta
  layout=[[texto_instruccion],[texto_contraseña,input_contraseña],[b2],[imagen1]]
 
#layout del primer marco donde en el primer renglón se presenta la instrucción, en el segundo la contraseña a escribir y el espacio para escribirla, después un botón para iniciar sesión y finalmente una imagen.

  marco=sg.Frame("Pantalla de inicio", layout,key="M1")

  return marco

def marco2():
  b3=sg.B(" ",image_filename="base.png",key="BTN_BASEDATOS")
  b4=sg.B(" ",image_filename="Visualizacion.png", key="BTN_REPORTE")
  b8=sg.B(" ",image_filename="mapa.png", key="BTN_Mapa")
  
  
  #Botones que dirigen a todos los marcos del programa, al presionarlos se oculta el marco 2 y se presenta el marco de destino.#

  layout=[[b3,b4,b8]]
  #En el primer renglón se colocan 3 botones, en el segundo una imagen y al final 4 botones.

  marco2=sg.Frame("Ciudad de Mexico", layout,key="M2", visible=False)
  return marco2

def marco3(): #Página de la base de datos original
    renglon=" "
    with open("Mx.csv", newline='') as  csvfile:
        reader = csv.reader(csvfile) #Se asocia al reader con el archivo csvfile
        for row in reader:#Se recorre todo el archivo
            renglon+=str(row)+'\n' #Cada línea del archivo es una lista
            texto_datos=sg.Text(renglon, key="TXT_DATOS")
    
  #Botones y layout 
    btn_regresa=sg.B("Regresa a la página principal", key="Regresa3")
    texto_descripcion=sg.Text("Esta base habla acerca de la ciudad de Mexico \n y sus puntos importantes para airbnb")

    layout=[[texto_descripcion],[btn_regresa],[texto_datos]]
 
    marco3=sg.Frame("Base de datos: Airbnb y como aprovecharlo", layout, visible=False, key="M3")
    return marco3
def marco4():
  b5=sg.B(" ",image_filename="Circulares.png",key="BTN_Circulos")
  b6=sg.B(" ",image_filename="Barras.png", key="BTN_Barras")
  b7=sg.B(" ",image_filename="dispersion.png", key="BTN_Disper")
  layout=[[b5,b6,b7]]
  marco4=sg.Frame("Anlisis descriptivo", layout,key="M4", visible=False)
  return marco4
  

    
    
ventana1=marco1()
ventana2=marco2()
ventana3=marco3()
ventana4=marco4()
layout=[[ventana1,ventana2,ventana3,ventana4]]



window=sg.Window("Análisis de datos de Airbnb en la cdmx",layout)

while True:
  #use the window.read method to catch any button pressed 
  event,values= window.read()
  #end program if user closes window 
  if event==sg.WIN_CLOSED:
    break;
  if event=="BTN_SALIR":
    break; 

  if event=="BTN_INICIARSESION1":
    pepe=values["INP_CONTRASENA1"]
    resultado='pepe'
    if resultado==pepe:
      window["M1"].update(visible=False)
      window["M2"].update(visible=True)

  #Botones de salida
  if event==sg.WIN_CLOSED:
    break;

  if event=="BTN_BASEDATOS":
    window["M2"].update(visible=False)
    window["M3"].update(visible=True)
    
  if event=="BTN_Mapa":
      wb.open('https://www.google.com.mx/maps/dir/Ciudad+de+M%C3%A9xico,+CDMX/Buenos+Aires,+Argentina/@-7.0045569,-100.6863919,4z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x85ce0026db097507:0x54061076265ee841!2m2!1d-99.133208!2d19.4326077!1m5!1m1!1s0x95bcca3d05457fbb:0xe160f4fce7f7c017!2m2!1d-58.4401655!2d-34.6143048?entry=ttu',new=1,autoraise=True)

  if event=="BTN_REPORTE":
    window["M2"].update(visible=False)
    window["M4"].update(visible=True)

  if event=="BTN_Circulos":
      mm=pd.read_csv('Mexa.csv')
      mm1=mm[['has_availability']]

      mm2=pd.read_csv('Buenos.csv')
      mm23=mm2[['has_availability']]
      colores=["#6495ED", "#FFEBCD","#F0F8FF"]

      plt.subplot(121)
      rm=freq_tbl(mm1["has_availability"])
      Filtro_index3=rm.set_index('has_availability')
      Filtro_index3["frequency"].plot(kind="pie",figsize=(10,5), shadow=True, autopct="%.1f%%")
      plt.title('Disponibilidad de airbnb en Mexico')

      plt.subplot(122)
      yy=freq_tbl(mm23["has_availability"])
      Filtro_index190=yy.set_index('has_availability')
      Filtro_index190["frequency"].plot(kind="pie",figsize=(10,5), shadow=True, autopct="%.1f%%")
      plt.title("disponibilidad Buenos Aires")
      plt.show()
 
  if event=="BTN_Barras":
     tt=pd.read_csv('Mexa.csv')
     tt1=tt[['room']]

     tt2=pd.read_csv('Buenos.csv')
     tt3=tt2[['room_type']]


     plt.subplot(121)
     fred=freq_tbl(tt1)
     fred1=fred[['room','frequency']]
     fredinde=fred1.set_index('room')
     fredinde["frequency"].plot(kind="bar",figsize=(10,5),color='orange')
     plt.title('Tipo de inmueble Mexico')

     plt.subplot(122)
     fredi=freq_tbl(tt3)
     fredi1=fredi[['room_type','frequency']]
     frediinde=fredi1.set_index('room_type')
     frediinde["frequency"].plot(kind="bar",figsize=(10,5),color='darkblue')
     plt.title('tiempo de inmueble Argentina')     
     plt.show()
  if event=="BTN_Disper":
      
       dd=pd.read_csv('Mexa.csv')
       tt4=pd.read_csv('Buenos.csv')

       wn=dd[['location']]
       wn1=dd[['comunication']]
       wn2=dd[['clean']]
       wf=pd.concat([wn,wn1,wn2],axis=1)

       bm=tt4[['review_scores_location']]
       bm1=tt4[['review_scores_communication']]
       bm2=tt4[['review_scores_cleanliness']]
       vm= pd.concat([bm,bm1,bm2], axis=1)

       plt.subplot(221)
       plt.hist(wf, color=['lightblue','darkblue','green'])
       plt.xlabel('Azul cielo=ubicacion\n Azul Oscuro= comunicacion\n Verde=Limpieza')


       plt.subplot(222)
       plt.hist(vm, color=['lightblue','darkblue','green'])
       plt.xlabel('Azul cielo=ubicacion\n Azul Oscuro= comunicacion\n Verde=Limpieza')

       plt.subplot(223)
       plt.boxplot(dd[['price']])

       plt.subplot(224)
       plt.boxplot(tt4[['price']])

       plt.show()

  if event=="Regresa3":
    #Clave del botón regresar que está al final
    window["M3"].update(visible=False)
    window["M2"].update(visible=True)   
window.close()



