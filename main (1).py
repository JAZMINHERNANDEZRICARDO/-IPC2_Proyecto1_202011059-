import xml.etree.ElementTree as ET
import graphviz as gv
from graphviz import Digraph, Graph
import graphviz
import xml.dom.minidom as minidom
# C:\Users\krist\OneDrive\Escritorio\Proyecto1_2023_s2\archivoEntrada.xml
class NodoMatriz:
    def __init__(self, fila, columna, dato, datoBinario):
        self.fila = fila
        self.columna = columna
        self.dato = dato
        self.datoBinario = datoBinario
        self.siguiente_fila = None
        self.siguiente_columna = None

class MatrizEnlazada:
    def __init__(self):
        self.primer_nodo = None
        self.lista_agrupada = None  
        self.grupos = None
        self.sumados = None

    def agregar(self, fila, columna, dato,datoBinario):
        nuevo_nodo = NodoMatriz(fila, columna, dato,datoBinario)

        if not self.primer_nodo:
            self.primer_nodo = nuevo_nodo
            return

        nodo_actual = self.primer_nodo
        while nodo_actual.siguiente_fila:
            nodo_actual = nodo_actual.siguiente_fila
        nodo_actual.siguiente_fila = nuevo_nodo

        nodo_actual = self.primer_nodo
        while nodo_actual.siguiente_columna:
            nodo_actual = nodo_actual.siguiente_columna
        nodo_actual.siguiente_columna = nuevo_nodo

        if not self.lista_agrupada:
            self.lista_agrupada = NodoMatriz(fila, columna, dato, datoBinario)
        else:
            nodo_actual = self.lista_agrupada
            while nodo_actual.siguiente_fila:
                nodo_actual = nodo_actual.siguiente_fila
            nodo_actual.siguiente_fila = NodoMatriz(fila, columna, dato, datoBinario)

    def imprimir(self):
        nodo_actual = self.primer_nodo
        while nodo_actual:
            print(f"Fila: {nodo_actual.fila}, Columna: {nodo_actual.columna}, Dato: {nodo_actual.dato}, DatoBinario: {nodo_actual.datoBinario}")
            nodo_actual = nodo_actual.siguiente_fila

        self.suma()
    
    def suma(self):
        max_fila = 0
        nodo_actual = self.primer_nodo

        while nodo_actual:
            if int(nodo_actual.fila) > max_fila:
                max_fila = int(nodo_actual.fila)
            nodo_actual = nodo_actual.siguiente_fila

        for fila in range(1, max_fila + 1):
            nodo_actual = self.primer_nodo

            print(f"Fila: {fila} =>", end=" ")
            a = ""
            while nodo_actual:
                if int(nodo_actual.fila) == fila:
                    print(f"Dato: {nodo_actual.datoBinario}", end=" ")
                    a = a + str(nodo_actual.datoBinario)
                nodo_actual = nodo_actual.siguiente_fila
            print(a)
            
            if not self.lista_agrupada:
                self.lista_agrupada = NodoMatriz(fila, None, None, a)
            else:
                nodo_actual = self.lista_agrupada
                while nodo_actual.siguiente_fila:
                    nodo_actual = nodo_actual.siguiente_fila
                nodo_actual.siguiente_fila = NodoMatriz(fila, None, None, a)
              
            a = ""
            print()

        self.imprimir_lista_agrupada()

    def imprimir_lista_agrupada(self):
        print("Valores de self.lista_agrupada:")
        nodo_lista = self.lista_agrupada
        while nodo_lista:
            if len(str(nodo_lista.datoBinario)) > 1:
                print(f"Fila: {nodo_lista.fila}, DatoBinario: {nodo_lista.datoBinario}")
            nodo_lista = nodo_lista.siguiente_fila

        print()

        self.agregar_a_grupos()

    def agregar_a_grupos(self):
        if not self.lista_agrupada:
            return

        nodo_actual = self.lista_agrupada

        while nodo_actual:
            dato_actual = nodo_actual.datoBinario
            if len(str(dato_actual)) > 1:
                
                grupo_actual = self.grupos
                grupo_anterior = None
                while grupo_actual:
                    if grupo_actual.datoBinario == dato_actual:
                        grupo_actual.fila = str(grupo_actual.fila) + f", {nodo_actual.fila}"
                        break
                    grupo_anterior = grupo_actual
                    grupo_actual = grupo_actual.siguiente_fila

                
                if not grupo_actual:
                    nuevo_grupo = NodoMatriz(nodo_actual.fila, None, None, nodo_actual.datoBinario)
                    if grupo_anterior is None:
                        self.grupos = nuevo_grupo
                    else:
                        grupo_anterior.siguiente_fila = nuevo_grupo

            nodo_actual = nodo_actual.siguiente_fila

        grupo_actual = self.grupos
        while grupo_actual:
            print(f"Grupo en fila {grupo_actual.fila}:\n")
            filas_grupo = str(grupo_actual.fila).split(", ")
            for fila in filas_grupo:
                nodo_actual = self.primer_nodo
                while nodo_actual:
                    if int(nodo_actual.fila) == int(fila):
                        print(f"Fila: {nodo_actual.fila}, Columna: {nodo_actual.columna}, Dato: {nodo_actual.dato}, DatoBinario: {nodo_actual.datoBinario}")
                    nodo_actual = nodo_actual.siguiente_fila
                print()
            grupo_actual = grupo_actual.siguiente_fila

        print("\n\n")

        self.menu = menu_prin()
        self.menu.final()

    
    def agregar_fila_vacia(self, max_columna):
        nueva_fila = NodoMatriz(None, None, None, None)
        
        for columna in range(1, max_columna + 1):
            nueva_fila.siguiente_columna = NodoMatriz(None, columna, 0, None)
            nueva_fila = nueva_fila.siguiente_columna

        return nueva_fila
    


    def convertir_a_binaria(self):
        nodo_actual = self.primer_nodo
        while nodo_actual:
            if int(nodo_actual.dato)== 0:
                print(f"Fila: {nodo_actual.fila}, Columna: {nodo_actual.columna}, Dato: {int(0)}")
                nodo_actual = nodo_actual.siguiente_fila
            else:
                print(f"Fila: {nodo_actual.fila}, Columna: {nodo_actual.columna}, Dato: {int(1)}")
                nodo_actual = nodo_actual.siguiente_fila


class menu_prin:
    def __init__(self):
        self.nombreAudio=""

    dot = graphviz.Digraph(comment='Mi Gráfico Dirigido')
    
    tiempo =""
    amplitud=""
    valor=0
    anterior=0
    contador=0
    lista_e = MatrizEnlazada()
    
    
    def MenuPrincipal (self):
        Opcion = input("--------------------------------"+"\n"+
                        "        MENU PRINCIPAL          "+"\n"+
                        "--------------------------------"+"\n"+
                        "1. Cargar archivo"+"\n"+
                        "2. Procesar archivo"+"\n"+
                        "3. Escribir archivo salida"+"\n"+
                        "4. Mostrar datos del estudiante"+"\n"+
                        "5. Generar gráfica"+"\n"+
                        "7. Salida"+"\n")
        if int(Opcion)==1:
           print("OPCION "+Opcion)
           menu_e = menu_prin()
           menu_e.CargarArchivo()

        elif int(Opcion)==2:
           print("OPCION "+Opcion)
           menu_e = menu_prin()
           menu_e.ProcesarArchivo()

        elif int(Opcion)==3:
            self.generar_xml()
            self.MenuPrincipal()
        elif int(Opcion)==4:
            print("Datos de estudiante"+"\n"+
                  ">Kristel Jazmin Hernandez Ricardo"+"\n"+
                  ">202011059"+"\n"+
                  ">Introducción a la programación y computacion 2 Sección N"+"\n"+
                  ">Ingenieria en Ciencias y Sistemas"+"\n"+
                  ">4 Semestre")
            self.MenuPrincipal()
        elif int(Opcion)==5:
            self.Graficar()
            self.MenuPrincipal()

        elif int(Opcion)==7:
            print(" :) ")
        elif int(Opcion)>7 or int(Opcion)==0:
            print("No es una opcion del programa, ingrese nuevamente la opcion deseada")
            self.MenuPrincipal()
           
    def CargarArchivo(self):
        ruta_archivo = input("Ingrese la ruta del archivo XML: ")
        try:
            self.tree = ET.parse(ruta_archivo)
            self.root = self.tree.getroot()

            contador_señales = 0

            print("Señales disponibles:")
            for senal in self.root.findall(".//senal"):
                contador_señales += 1
                nombre_senal = senal.attrib['nombre']
                print(f"{contador_señales}. {nombre_senal}")

            seleccion = int(input("Seleccione el número de la señal que desea ver: "))
            
            contador_señales = 0
            for senal in self.root.findall(".//senal"):
                contador_señales += 1
                if contador_señales == seleccion:
                    self.MostrarSenal(senal)
                    
                    break

        except FileNotFoundError:
            print("Archivo no encontrado.")
            self.MenuPrincipal()

    def MostrarSenal(self, senal):
        nombre_senal = senal.attrib['nombre']
        print(f"Mostrando señal: {nombre_senal}")
        self.nombreAudio = nombre_senal
        self.dot.node('A',self.nombreAudio)
        
        self.tiempo = senal.attrib['t']
        self.amplitud = senal.attrib['A']

        for dato in senal.findall(".//dato"):
            PosicionT = dato.attrib['t']
            PosicionA = dato.attrib['A']

            self.valor = int(dato.text)

            if int(PosicionT) <= int(self.tiempo) and int(PosicionA) <= int(self.amplitud):
                self.contador = self.contador + 1
                
                if self.valor==0:
                    self.lista_e.agregar(PosicionT, PosicionA, self.valor,0) 
                elif self.valor!=0:
                    self.lista_e.agregar(PosicionT, PosicionA, self.valor,1)

                if int(self.contador)<=int(self.amplitud):
                    
                    self.dot.node(str(self.contador),str(self.valor))
                    self.dot.edge('A',str(self.contador))
                  
                else:
                
                    self.dot.node(str(self.contador),str(self.valor))
                    self.dot.edge(str(self.contador-int(self.amplitud)),str(self.contador))
                    

            else:
                print("Error: No procede ya que el tiempo o amplitud no concuerdan")
        
        self.dot.node('C',"A= "+self.amplitud)
        self.dot.node('D',"T= "+self.tiempo)

        self.dot.edge('A','C')
        self.dot.edge('A','D')
        self.MenuPrincipal()

        self.lista_e.imprimir()

        print("SE GUARDAN DATOS")
        print("")
        print("")
        menu_e = menu_prin()
        menu_e.MenuPrincipal()
            
    def ProcesarArchivo(self):
      
        print("Matriz")
      
        self.lista_e.convertir_a_binaria()
        self.lista_e.imprimir()
        
        self.MenuPrincipal()

    def final(self):
        if not self.lista_e.grupos:
            print("No hay grupos para sumar.")
            return

        max_fila = 0
        nodo_actual = self.lista_e.primer_nodo

        while nodo_actual:
            if int(nodo_actual.fila) > max_fila:
                max_fila = int(nodo_actual.fila)
            nodo_actual = nodo_actual.siguiente_fila

        nodo_grupo = self.lista_e.grupos
        while nodo_grupo:
            filas_grupo = str(nodo_grupo.fila).split(", ")
            suma_grupo = NodoMatriz(nodo_grupo.fila, None, None, 0)

            for fila in filas_grupo:
                nodo_actual = self.lista_e.primer_nodo
                while nodo_actual:
                    if int(nodo_actual.fila) == int(fila):
                        if suma_grupo.dato is None:
                            suma_grupo.dato = int(nodo_actual.dato)
                        else:
                            suma_grupo.dato += int(nodo_actual.dato)
                    nodo_actual = nodo_actual.siguiente_fila

            print(f"Grupo en fila {nodo_grupo.fila}:")
            print(f"Suma: {suma_grupo.dato}")

            nodo_grupo = nodo_grupo.siguiente_fila




    def Graficar(self):
        print("entra a graficar")
        self.dot.render('graph', format='png', view=True)

    def generar_xml(self):
        senales_reducidas = ET.Element("senalesReducidas")
        senal = ET.SubElement(senales_reducidas, "senal", nombre=self.nombreAudio, A="4")

        # Aquí puedes definir la cantidad de grupos que deseas
        """      numero_de_grupos = 3

        for g in range(1, numero_de_grupos + 1):
            grupo = ET.SubElement(senal, "grupo", g=str(g))
            tiempos = ET.SubElement(grupo, "tiempos")
            tiempos.text = ",".join([str(i) for i in range(1, g + 2)])
            datos_grupo = ET.SubElement(grupo, "datosGrupo")

            for i in range(1, 5):
                dato = ET.SubElement(datos_grupo, "dato", A=str(i))
                dato.text = str(i * g - 1)"""

        # Crear un objeto minidom para dar formato al XML
        xml_string = ET.tostring(senales_reducidas, encoding="utf-8")
        xml_pretty = minidom.parseString(xml_string)

        # Escribir el archivo de salida con formato
        with open("archivoSalida.xml", "wb") as f:
            f.write(xml_pretty.toprettyxml(indent="    ", encoding="utf-8"))


        
lis_e = menu_prin()
lis_e.MenuPrincipal()