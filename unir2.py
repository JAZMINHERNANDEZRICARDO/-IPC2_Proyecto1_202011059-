import xml.etree.ElementTree as ET

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

    def agrupar_filas_iguales(self):
        fila_igual = {}

        nodo_actual = self.primer_nodo
        while nodo_actual:
            fila = nodo_actual.fila
            dato = nodo_actual.dato
            if fila in fila_igual:
                fila_igual[fila].append(dato)
            else:
                fila_igual[fila] = [dato]
            nodo_actual = nodo_actual.siguiente_fila

        grupos = {}

        for fila, datos in fila_igual.items():
            ceros = [int(d != 0) for d in datos]
            ceros_str = ''.join(map(str, ceros))
            if ceros_str in grupos:
                grupos[ceros_str].append(fila)
            else:
                grupos[ceros_str] = [fila]

        for grupo, filas in grupos.items():
            print(f"Grupo de filas con ceros iguales ({grupo}): {filas}")
            self.sumar_filas_seleccionadas(filas)

    def sumar_filas_seleccionadas(self, filas_a_sumar):
        suma_por_columna = {}

        for fila in filas_a_sumar:
            nodo_actual = self.primer_nodo
            while nodo_actual:
                if nodo_actual.fila == fila:
                    columna = nodo_actual.columna
                    dato = nodo_actual.dato
                    if columna in suma_por_columna:
                        suma_por_columna[columna] += dato
                    else:
                        suma_por_columna[columna] = dato
                nodo_actual = nodo_actual.siguiente_fila

        print("Suma por columna:")
        for columna, suma in suma_por_columna.items():
            print(f"Columna {columna}: {suma}")
    
class menu_prin:


    def __init__(self):
        self.senales = {}


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
            #menu_e.ProcesarArchivo()
            for nombreAudio, lista_senal in self.senales.items():
                print(f"Procesando señal {nombreAudio}:")
                lista_senal.convertir_a_binaria()
                print("\n\n")
                lista_senal.agrupar_filas_iguales()
    
    def CargarArchivo(self):
        ruta_archivo = input("Ingrese la ruta del archivo XML: ")
        try:
            self.tree = ET.parse(ruta_archivo)
            self.root = self.tree.getroot()

            for senal in self.root.findall(".//senal"):
                nombreAudio = senal.attrib['nombre']
                tiempo = senal.attrib['t']
                amplitud = senal.attrib['A']

                lista_senal = MatrizEnlazada()

                for dato in senal.findall(".//dato"):
                    PosicionT = dato.attrib['t']
                    PosicionA = dato.attrib['A']
                    valor = int(dato.text)

                    if int(PosicionT) <= int(tiempo) and int(PosicionA) <= int(amplitud):
                        lista_senal.agregar(PosicionT, PosicionA, valor)
                    else:
                        print("Error: No procede ya que el tiempo o amplitud no concuerdan")

                print(f"Señal {nombreAudio} cargada:")
                lista_senal.imprimir()
                self.senales[nombreAudio] = lista_senal
                print("SE GUARDAN DATOS")
                print("")
                print("")

            print("Todas las señales han sido cargadas.\n")
            self.MenuPrincipal()

        except FileNotFoundError:
            print("Archivo no encontrado.")
            self.MenuPrincipal()


lis_e = menu_prin()
lis_e.MenuPrincipal()