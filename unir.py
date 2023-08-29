import xml.etree.ElementTree as ET
import graphviz as gv
from graphviz import Digraph, Graph
import graphviz

class NodoMatriz:
    def __init__(self, fila, columna, dato):
        self.fila = fila
        self.columna = columna
        self.dato = dato
        self.siguiente_fila = None
        self.siguiente_columna = None

class MatrizEnlazada:
    def __init__(self):
        self.primer_nodo = None

    def agregar(self, fila, columna, dato):
        nuevo_nodo = NodoMatriz(fila, columna, dato)

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

    def imprimir(self):
        nodo_actual = self.primer_nodo
        while nodo_actual:
            print(f"Fila: {nodo_actual.fila}, Columna: {nodo_actual.columna}, Dato: {nodo_actual.dato}")
            nodo_actual = nodo_actual.siguiente_fila

    def convertir_a_binaria(self):
        nodo_actual = self.primer_nodo
        while nodo_actual:
            if int(nodo_actual.dato)== 0:
                print(f"Fila: {nodo_actual.fila}, Columna: {nodo_actual.columna}, Dato: {int(0)}")
                nodo_actual = nodo_actual.siguiente_fila
            else:
                print(f"Fila: {nodo_actual.fila}, Columna: {nodo_actual.columna}, Dato: {int(1)}")
                nodo_actual = nodo_actual.siguiente_fila

        




    def sumar_filas_seleccionadas(self, filas_a_sumar):
        fila_sums = {}  # Diccionario para almacenar las sumas de las filas seleccionadas

        nodo_actual = self.primer_nodo
        while nodo_actual:
            fila = nodo_actual.fila
            dato = nodo_actual.dato
            if fila in filas_a_sumar:
                if fila in fila_sums:
                    fila_sums[fila] += dato
                else:
                    fila_sums[fila] = dato
            nodo_actual = nodo_actual.siguiente_fila

        return fila_sums
    


class menu_prin:
    dot = graphviz.Digraph(comment='Mi Gráfico Dirigido')
    nombreAudio=""
    tiempo =""
    amplitud=""
    valor=0
    anterior=0
    contador=0
    lista_e = MatrizEnlazada()
    matrizbinaria =MatrizEnlazada()
    def MenuPrincipal (self):
        Opcion = input("--------------------------------"+"\n"+
                        "        MENU PRINCIPAL          "+"\n"+
                        "--------------------------------"+"\n"+
                        "1. Cargar archivo"+"\n"+
                        "2. Procesar archivo"+"\n"+
                        "3. Escribir archivo salida"+"\n"+
                        "4. Mostrar datos del estudiante"+"\n"+
                        "5. Generar gráfica"+"\n"+
                        "6. Inicializar sistema"+"\n"+
                        "7. Salida"+"\n")
        if int(Opcion)==1:
           print("OPCION "+Opcion)
           menu_e = menu_prin()
           menu_e.CargarArchivo()

        elif int(Opcion)==2:
           print("OPCION "+Opcion)
           menu_e = menu_prin()
           menu_e.ProcesarArchivo()
    def CargarArchivo (self):
        ruta_archivo = input("Ingrese la ruta del archivo XML: ")
        try:
            #C:\Users\krist\OneDrive\Escritorio\Proyecto1_2023_s2\archivoEntrada.xml
            self.tree = ET.parse(ruta_archivo)
            self.root = self.tree.getroot()
        

            for senal in self.root.findall(".//senal"):
              #-------------------------------------
                self.nombreAudio = senal.attrib['nombre']
                self.tiempo = senal.attrib['t']
                self.amplitud = senal.attrib['A']

            
                for dato in senal.findall(".//dato"):
                    self.anterior=self.valor
                    #-------------------------------------
                    PosicionT = dato.attrib['t']
                    PosicionA = dato.attrib['A']
                
                

                
                    #-------ultimo------
                    self.valor = int(dato.text)
                    #-------ultimo------
                    print( int(PosicionT),int(self.tiempo),int(PosicionA),int(self.amplitud))
                    if int(PosicionT)<=int(self.tiempo) and int(PosicionA)<=int(self.amplitud):
                        self.contador=self.contador+1
                        self.lista_e.agregar(PosicionT,PosicionA,self.valor)
                    
                    else:
                        print("Error: No prodece ya que el tiempo o amplitud no concuerdan")
            
            
            
                self.lista_e.imprimir()


                print("SE GUARDAN DATOS")  
                print("") 
                print("")  
                menu_e = menu_prin()
                menu_e.MenuPrincipal()
        except FileNotFoundError:
            print("Archivo no encontrado.")
            self.MenuPrincipal()
            
    def ProcesarArchivo(self):
      
      print("Matriz")
      
      self.lista_e.convertir_a_binaria()
    def Graficar(self):
        
        self.tree = ET.parse('archivoEntrada.xml')
        self.root = self.tree.getroot()
        
        
        for senal in self.root.findall(".//senal"):
            #-------------------------------------
            self.nombreAudio = senal.attrib['nombre']
            self.tiempo = senal.attrib['t']
            self.amplitud = senal.attrib['A']
            self.dot.node('A',self.nombreAudio)
            
            
            for dato in senal.findall(".//dato"):
                self.anterior=self.valor
                #-------------------------------------
                PosicionT = dato.attrib['t']
                PosicionA = dato.attrib['A']
                
                

                
                #-------ultimo------
                self.valor = int(dato.text)
                #-------ultimo------
                print( int(PosicionT),int(self.tiempo),int(PosicionA),int(self.amplitud))
                if int(PosicionT)<=int(self.tiempo) and int(PosicionA)<=int(self.amplitud):
                    self.contador=self.contador+1
                    self.lista_e.agregar(PosicionT,PosicionA,self.valor)
                    
               


                    if int(self.contador)<=int(self.amplitud):
                        

                        
                        self.dot.node(str(self.contador),str(self.valor))
                        self.dot.edge('A',str(self.contador))
                        print(str(self.valor),"--------------------------------------------------------")

                    else:
                        print (str(self.anterior),"__________________________________________________________-")
                        print(self.valor,"  dosssss  ",self.anterior,PosicionT+"    "+PosicionA)
                        
                        self.dot.node(str(self.contador),str(self.valor))
                        self.dot.edge(str(self.contador-int(self.amplitud)),str(self.contador))
                        print("")

                    




                else:
                   print("Error: No prodece ya que el tiempo o amplitud no concuerdan")
            
            
            
            self.lista_e.imprimir()
            self.dot.node('C',"A= "+self.amplitud)
            self.dot.node('D',"T= "+self.tiempo)

            self.dot.edge('A','C')
            self.dot.edge('A','D')

            self.dot.render('Prueba.gv', format='png', view=True)
            print("SE GUARDAN DATOS")  
            print("") 
            print("")  
            menu_e = menu_prin()
            menu_e.MenuPrincipal()
            
            
            self.dot.render('graph', format='png', view=True)




lis_e = menu_prin()
lis_e.MenuPrincipal()
