import xml.etree.ElementTree as ET

class nota:
  def __init__(self, Tiempoo, Amplitudd, Valorr):
    self.Tiempoo = Tiempoo
    self.Amplitudd = Amplitudd
    self.Valorr = Valorr

class nodo:
  def _init_(self,nota=None, siguiente=None):
    self.nota = nota
    self.siguiente = siguiente

class lista_enlazada:
    def __init__(self):
        self.primero =None

    def insertar (self, nota):
        if self.primero is None:
            self.primero = nodo(nota=nota)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo(nota=nota)

    def recorrer(self):
        actual=self.primero
        while actual != None:
            print("Usuario: ", actual.nota.Tiempo,
                " | Titulo: ", actual.nota.Amplitud)
            actual = actual.siguiente
        print("se carga archivo")


class menu_prin:

    #Menu principal del programa
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
           menu_e.CargarArchivo()

    #Cargar archivo
    def CargarArchivo (self):
        self.tree = ET.parse('archivoEntrada.xml')
        self.root = self.tree.getroot()

        for senal in self.root.findall(".//senal"):
            #-------------------------------------
            nombreAudio = senal.attrib['nombre']
            tiempo = senal.attrib['t']
            amplitud = senal.attrib['A']
            print("Nombre de la señal de audio: ",nombreAudio," Tiempo: ",tiempo," Amplitud: ",amplitud)
            #-------------------------------------

            for dato in senal.findall(".//dato"):
                #-------------------------------------
                PosicionT = dato.attrib['t']
                PosicionA = dato.attrib['A']
                #-------ultimo------
                valor = int(dato.text)
                #-------ultimo------
                print(PosicionT," ",PosicionA,"  ",valor,"Tmax ",tiempo," ",amplitud)
                '''list = lista_enlazada()
                n = nota("123","12","1")
                #n1 = nota(PosicionT,PosicionA,valor)
                list.insertar(n)'''
                if int(PosicionT)<=int(tiempo) and int(PosicionA)<=int(amplitud):
                   
                   
                    
                   
                   print(PosicionT, " es menor o igual ",tiempo)
                   print(PosicionA, " es menor o igual ",amplitud)

                   
                else:
                   print("Error: No prodece ya que el tiempo o amplitud no concuerdan")
                   


        print("se carga archivo")
    def ProcesarArchivo(self):
       
      
       

       ''''def recorrer(self):
        actual=self.primero
        while actual != None:
            print("Usuario: ", actual.nota.Tiempo,
                " | Titulo: ", actual.nota.Amplitud)
            actual = actual.siguiente
        print("se carga archivo")'''
       
       

list = lista_enlazada()
nota1 = nota("123","12","1")
#n1 = nota(PosicionT,PosicionA,valor)
list.insertar(nota1)
menu_e = menu_prin()
menu_e.MenuPrincipal()