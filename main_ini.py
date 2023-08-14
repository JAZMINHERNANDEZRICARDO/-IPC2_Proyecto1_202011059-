import xml.etree.ElementTree as ET

class nota:
  def __init__(self, Tiempoo, Amplitudd, Valorr):
    self.Tiempoo = Tiempoo
    self.Amplitudd = Amplitudd
    self.Valorr = Valorr


class nodo:
  def __init__(self,nota=None, siguiente=None):
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
      print("Tiempoo: ", actual.nota.Tiempoo,
            " | Amplitudd: ", actual.nota.Amplitudd,
            " | Valorr: ", actual.nota.Valorr)
      actual = actual.siguiente

class menu_prin:
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
    def CargarArchivo (self):
        self.tree = ET.parse('archivoEntrada.xml')
        self.root = self.tree.getroot()
        for senal in self.root.findall(".//senal"):
            #-------------------------------------
            nombreAudio = senal.attrib['nombre']
            tiempo = senal.attrib['t']
            amplitud = senal.attrib['A']
            
            for dato in senal.findall(".//dato"):
                #-------------------------------------
                PosicionT = dato.attrib['t']
                PosicionA = dato.attrib['A']
                #-------ultimo------
                valor = int(dato.text)
                #-------ultimo------
                
                if int(PosicionT)<=int(tiempo) and int(PosicionA)<=int(amplitud):
                    n1 = nota(PosicionT,PosicionA,valor)
                    lista_e = lista_enlazada()
                    lista_e.insertar(n1)
                    lista_e.recorrer()

                   
                else:
                   print("Error: No prodece ya que el tiempo o amplitud no concuerdan")
                   

lis_e = menu_prin()
lis_e.MenuPrincipal()

