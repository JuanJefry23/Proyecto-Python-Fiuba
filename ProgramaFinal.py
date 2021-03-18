#Programa para la venta de pasajes de un avión
#El avión tiene 24 filas y 6 asientos en cada fila
import requests
import json

acum=0
#Asiento totales disponibles en el avion: 24*6
num=144

#Matrices
listaPasajeros=[[""]*3 for j in range(144)]

a=[['Disponible']*6 for i in range(24)]



#---Bloque de la función para la opcion 1 del MENU "Venta de pasajes" + bloque función que verifica la dirección del usuario--
#Funcion que valida la dirección del usuario:
def validarDireccion(pos):

    url="http://servicios.usig.buenosaires.gob.ar/normalizar/?direccion="
    address=input("Ingrese su domicilio: \n>")
    print("\n")
    answer=requests.get(url+address)
    dic=json.loads(answer.content)
    cant_direcciones=len(dic["direccionesNormalizadas"])
    
    if (cant_direcciones>0):
        for i in dic["direccionesNormalizadas"]:
            print(i["nombre_localidad"],i["nombre_partido"])
            print("\n")
            
        res=int(input("Su domicilio esta ubicado dentro de la Ciudad de Buenos aires (CABA) \n1.SI \n2.NO \n>"))
        if (res==1):
            print("""Descuento del 10% a los usuarios que viven dentro de Ciudad de Buenos aires
                     El precio final de su boleto es de : $19800(Pesos Arg)""")
            dirFinal=address+" / " + "CABA"
        if(res==2):
            partido=input("Ingrese el nombre del partido: \n>")
            dirFinal=address+" / "+partido
            
        listaPasajeros[pos][2]=dirFinal
            
                   
    else:
        print("No existe la dirección")
        print("Vuelva a ingresar una dirección valida")
        validarDireccion(pos)


#Funcion que se encarga de la venta de pasajes:

def ventaPasaje():
    #Variable contador
    libre=0
    bandera1=0
    bandera2=0

    for i in range(6):
        print(a)
    
    print("\n")
    opcion=int(input("Presione: \n1.Si desea elegir un asiento disponible \n2.Si desea que el sistema le asigne un asiento disponible al azar\n>"))

    if(opcion==1):
        print("\n")
        #Pregunto al pasajero que fila y asiento desea elegir:
        print("Elija Una fila entre 1 y 24\n Y un asiento entre 1 y 6\n")
        while(bandera1==0):
            fila=(int(input("Que fila desea? \n> ")))-1
            if(fila<1 or fila>24):
                print("Vuelva a ingresar una fila entre 1 y 24")
            else:
                bandera1=1
                
        while(bandera2==0):
            asiento = (int(input("Que asiento de esa fila desea? \n> ")))-1
            if(asiento<1 or asiento>6):
                print("Vuelva a ingresar una asiento entre 1 y 6")
                bandera2=0
            else:
                bandera2=1
            print("\n")
    
        #Hago una validación que dicha eleccion hecha por el pasajero este disponible:
        if(a[fila][asiento]=="Disponible"):
            print("Asiento disponible !")
            print("\n")
            a[fila][asiento]="Ocupado"
            #Guardo su informacion: asiento, nombre, direccion en otra matriz llamada "listaPasajeros"
            for i in range(144):
                if(listaPasajeros[i][0]==""):
                    libre=i
                    break
            
        listaPasajeros[libre][0]= "Fila:"+ str(fila+1)+"|Asiento:"+ str(asiento+1)
        listaPasajeros[libre][1]=input("Ingrese su nombre: \n>")
        validarDireccion(libre)
        
        
    if(opcion==2):
        print("Eligio la opcion 2, el sistema le asignara un asiento disponible")
        r=0
        col=0
        #Busco un asiento disponible:
        for i in range(24):
            for j in range(6):
                if(a[i][j]!="Ocupado"):
                    a[i][j]="Ocupado"
                    r=i
                    col=j
                    break
            break
            
        #Guardo su informacion: asiento, nombre, direccion en otra matriz llamada "listaPasajeros"
        for k in range(144):
            if(listaPasajeros[k][1]==""):
                libre=k
                break
    
        resF=r+1
        resA=col+1
        listaPasajeros[libre][0]= "Fila:"+ str(resF)+"|Asiento:"+ str(resA)
        listaPasajeros[libre][1]=input("Ingrese su nombre: \n>")
        validarDireccion(libre)
    
#-----------------------------------------------------------------------------------------------------------------------------



#----------------------------------Bloque de la función de la opción 2 del MENÚ "Cerrar Vuelo"---------------------------------
def cerrarVuelo(totalP,pOcup):
    
    print("------------------------------------------------------- LISTA DE PASAJEROS ------------------------------------------------------\n")
    print("\t\t\tASIENTO\t\t\t\tNOMBRE\t\t\t\t\t\tDOMICILIO")
    for i in range(144):
        if(listaPasajeros[i][1]!=""):
            print("\t\t\t"+ str(listaPasajeros[i][0]) + "\t\t" + str(listaPasajeros[i][1]) + "\t\t\t" + str(listaPasajeros[i][2]))    
    
    print("\n")
    numVuelo=input("Por favor ingrese el numero de su vuelo: \n>")
    nombre="vuelo"+numVuelo+".txt"
    
    archivo = open(nombre,"w")

    archivo.write("------------------------------------------------------- LISTA DE PASAJEROS ------------------------------------------------------")
    
    archivo.write("\t\t\tASIENTO\t\t\t\tNOMBRE\t\t\t\t\t\tDOMICILIO\n")
    for i in range(144):
        if(listaPasajeros[i][0]!=''):
            archivo.write("\t\t\t"+ str(listaPasajeros[i][0]) + "\t\t" + str(listaPasajeros[i][1]) + "\t\t\t" + str(listaPasajeros[i][2]) + "\n")
    
    archivo.write("\n")
    archivo.write("Total de pasajeros: " + str(totalP) + "\n")
    archivo.write("Porcentaje de ocupación del avión: " + str(pOcup) + "%")
       
    archivo.close()
    
    print("Se generó correctamente el informe de su vuelo !")
    print("\n")
#-----------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------MENU DE OPCIONES------------------------------------------------------------

option=int(input("Elija una opcion: \n1.Vender Pasaje \n2.Cerrar vuelo \n3.Salir del programa \n> "))
if(option==3):
    print("Hasta luego.")
    
while(option!=3):
    if(option==1):
        acum+=1
        print("Elegiste la opción 1")
        ventaPasaje()
    
    porcentajeOcupado="{:.3f}".format((acum*100)/144)
        
        
    if(option==2):
        print("Elegiste la opción 2")
        cerrarVuelo(acum,porcentajeOcupado)
        
    option=int(input("\nElija una opcion: \n1.Vender Pasaje \n2.Cerrar vuelo \n3.Salir del programa \n> "))
    if(option==3):
        print("\n")
        print("HASTA LUEGO.")
        
#-----------------------------------------------------------------------------------------------------------------------------
    
        
          
          
          
          
          
          
          
    