"""
EJERCICIO 1 - VALIDADOR DE NOTAS CON PROMEDIO

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Una o varias notas.

Proceso:
- Validar que cada nota esté entre 0 y 100.
- Guardar solamente las notas válidas.
- Calcular el promedio de las notas guardadas.

Salida:
- True o False al validar una nota.
- Lista de notas válidas.
- Promedio de las notas.

PASO 2 - BOSQUEJO A MANO

Ejemplo:
Notas: 85, 92, 110, 78, -5, 88

85 -> válida
92 -> válida
110 -> no válida
78 -> válida
-5 -> no válida
88 -> válida

Lista final:
[85, 92, 78, 88]

PASO 3 - DESCUBRIR EL PATRÓN

Se repite la validación de cada nota.
Si la nota está entre 0 y 100, se agrega a la lista.

PASO 4 - ESCRIBIR EL CÓDIGO

Se crea la clase Calificador.
Se utiliza una lista para guardar las notas válidas.
El método cargar_notas reutiliza validar_nota.

PASO 5 - VERIFICACIÓN

Entrada:
85, 92, 110, 78, -5, 88

Salida:
[85, 92, 78, 88]
Promedio: 85.75
"""

class Calificador:

    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        if nota >= 0 and nota <= 100:
            return True
        else:
            return False

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)

        return self.notas

    def promedio(self):
        if len(self.notas) == 0:
            return 0

        suma = 0

        for nota in self.notas:
            suma = suma + nota

        return suma / len(self.notas)


calificador = Calificador()

cantidad = int(input("¿Cuántas notas desea ingresar? "))

for i in range(cantidad):
    nota = float(input("Ingrese la nota: "))
    calificador.cargar_notas(nota)

print("Notas válidas:", calificador.notas)
print("Promedio:", calificador.promedio())


"""
EJERCICIO 2 - CONTADOR DE PALABRAS ÚNICAS

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Una o varias palabras.

Proceso:
- Guardar las palabras en un conjunto para evitar duplicados.
- Guardar las palabras en una lista para conservar el orden.
- Contar las palabras únicas.

Salida:
- Cantidad de palabras únicas.

PASO 2 - BOSQUEJO A MANO

Entrada:
hola, mundo, hola

Conjunto:
{"hola", "mundo"}

Lista:
["hola", "mundo"]

Cantidad:
2

PASO 3 - DESCUBRIR EL PATRÓN

El conjunto elimina automáticamente los duplicados.
La lista conserva el orden en que fueron agregadas las palabras.

PASO 4 - ESCRIBIR EL CÓDIGO

Se crea la clase AnalizadorTexto.
Se crean un conjunto y una lista.
agregar_multiples utiliza *args y reutiliza agregar_palabra.

PASO 5 - VERIFICACIÓN

Entrada:
hola, mundo, hola

Salida:
2 palabras únicas.
"""

class AnalizadorTexto:

    def __init__(self):
        self.palabras_unicas = set()
        self.lista_palabras = []

    def agregar_palabra(self, palabra):
        self.palabras_unicas.add(palabra)

        if palabra not in self.lista_palabras:
            self.lista_palabras.append(palabra)

    def contar_palabras(self):
        return len(self.palabras_unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)


analizador = AnalizadorTexto()

cantidad = int(input("¿Cuántas palabras desea ingresar? "))

for i in range(cantidad):
    palabra = input("Ingrese una palabra: ")
    analizador.agregar_palabra(palabra)

print("Palabras:", analizador.lista_palabras)
print("Palabras únicas:", analizador.contar_palabras())


"""
EJERCICIO 3 - GESTOR DE COMPRAS CON TOTALES

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Nombre de artículos.
- Precio de cada artículo.
- Precio mínimo y máximo.

Proceso:
- Guardar nombre y precio en un diccionario.
- Sumar todos los precios.
- Buscar artículos que estén dentro de un rango.

Salida:
- Total del carrito.
- Lista de artículos dentro del rango.

PASO 2 - BOSQUEJO A MANO

pan -> 2.50
leche -> 3.00

Total:
2.50 + 3.00 = 5.50

PASO 3 - DESCUBRIR EL PATRÓN

El diccionario permite relacionar cada artículo con su precio.
Con values() se pueden recorrer los precios.
Con items() se pueden obtener nombre y precio.

PASO 4 - ESCRIBIR EL CÓDIGO

Se crea la clase CarroCompras.
Se utiliza un diccionario llamado articulos.

PASO 5 - VERIFICACIÓN

pan = 2.50
leche = 3.00

Total = 5.50
"""

class CarroCompras:

    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        total = 0

        for precio in self.articulos.values():
            total = total + precio

        return total

    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []

        for nombre, precio in self.articulos.items():
            if precio >= precio_min and precio <= precio_max:
                resultado.append(nombre)

        return resultado


carrito = CarroCompras()

cantidad = int(input("¿Cuántos artículos desea agregar? "))

for i in range(cantidad):
    nombre = input("Nombre del artículo: ")
    precio = float(input("Precio del artículo: "))
    carrito.agregar_articulo(nombre, precio)

print("Artículos:", carrito.articulos)
print("Total:", carrito.total_carrito())

precio_min = float(input("Precio mínimo: "))
precio_max = float(input("Precio máximo: "))

print("Artículos en el rango:")
print(carrito.articulos_por_rango(precio_min, precio_max))


"""
EJERCICIO 4 - INVERSOR DE SECUENCIAS

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Una o varias listas.

Proceso:
- Recorrer una lista desde el último elemento hasta el primero.
- Crear una nueva lista invertida.
- Reutilizar el método para varias listas.

Salida:
- Lista invertida.
- Diccionario con las listas originales y sus listas invertidas.

PASO 2 - BOSQUEJO A MANO

Lista:
[1, 2, 3]

Desde el final:
3
2
1

Resultado:
[3, 2, 1]

PASO 3 - DESCUBRIR EL PATRÓN

Para invertir una lista se puede utilizar un índice que comience
en el último elemento y vaya disminuyendo.

PASO 4 - ESCRIBIR EL CÓDIGO

No se utiliza reversed().
Se utiliza un while para recorrer la lista manualmente.

Como una lista no puede utilizarse directamente como clave de
diccionario, se convierte la lista original en una tupla.

PASO 5 - VERIFICACIÓN

[1, 2, 3] -> [3, 2, 1]
"""

class InversorSecuencia:

    def invertir_lista(self, lista):
        resultado = []
        posicion = len(lista) - 1

        while posicion >= 0:
            resultado.append(lista[posicion])
            posicion = posicion - 1

        return resultado

    def invertir_multiples(self, *listas):
        resultado = {}

        for lista in listas:
            lista_invertida = self.invertir_lista(lista)
            resultado[tuple(lista)] = lista_invertida

        return resultado


inversor = InversorSecuencia()

cantidad = int(input("¿Cuántas listas desea invertir? "))

listas = []

for i in range(cantidad):
    lista = []

    cantidad_elementos = int(input("¿Cuántos elementos tendrá la lista? "))

    for j in range(cantidad_elementos):
        elemento = input("Ingrese un elemento: ")
        lista.append(elemento)

    listas.append(lista)

for lista in listas:
    print("Original:", lista)
    print("Invertida:", inversor.invertir_lista(lista))


"""
EJERCICIO 5 - DETECTOR DE NÚMEROS PARES E IMPARES

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Varios números.

Proceso:
- Comprobar si cada número es par.
- Separar los números pares e impares.
- Contar cuántos hay de cada tipo.

Salida:
- Diccionario con pares e impares.
- Tupla con las cantidades.

PASO 2 - BOSQUEJO A MANO

1 -> impar
2 -> par
3 -> impar
4 -> par
5 -> impar

Pares:
[2, 4]

Impares:
[1, 3, 5]

PASO 3 - DESCUBRIR EL PATRÓN

Un número es par cuando el residuo de dividirlo entre 2 es 0.
Se utiliza el operador %.

PASO 4 - ESCRIBIR EL CÓDIGO

Se crea el método es_par().
El método separar() reutiliza es_par().

PASO 5 - VERIFICACIÓN

Entrada:
1, 2, 3, 4, 5

Salida:
{'pares': [2, 4], 'impares': [1, 3, 5]}
"""

class AnalizadorNumeros:

    def __init__(self):
        self.resultado = {
            "pares": [],
            "impares": []
        }

    def es_par(self, numero):
        if numero % 2 == 0:
            return True
        else:
            return False

    def separar(self, *numeros):
        self.resultado = {
            "pares": [],
            "impares": []
        }

        for numero in numeros:
            if self.es_par(numero):
                self.resultado["pares"].append(numero)
            else:
                self.resultado["impares"].append(numero)

        return self.resultado

    def cantidad_pares_impares(self):
        cantidad_pares = len(self.resultado["pares"])
        cantidad_impares = len(self.resultado["impares"])

        return (cantidad_pares, cantidad_impares)


analizador = AnalizadorNumeros()

cantidad = int(input("¿Cuántos números desea ingresar? "))

for i in range(cantidad):
    numero = int(input("Ingrese un número: "))

    if analizador.es_par(numero):
        analizador.resultado["pares"].append(numero)
    else:
        analizador.resultado["impares"].append(numero)

print(analizador.resultado)
print("Cantidad de pares e impares:",
      analizador.cantidad_pares_impares())


"""
EJERCICIO 6 - ESTADÍSTICAS DE TEMPERATURA

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Una o varias temperaturas.

Proceso:
- Guardar las temperaturas.
- Encontrar la temperatura mínima.
- Encontrar la temperatura máxima.
- Calcular el promedio.

Salida:
- Temperatura mínima.
- Temperatura máxima.
- Promedio.

PASO 2 - BOSQUEJO A MANO

Temperaturas:
20, 25, 18, 30

Mínima = 18
Máxima = 30
Promedio = 23.25

PASO 3 - DESCUBRIR EL PATRÓN

Las temperaturas se guardan en una lista.
Python permite utilizar min() y max() para encontrar extremos.

PASO 4 - ESCRIBIR EL CÓDIGO

Se crea la clase GestorTemperatura.
registrar_multiples() reutiliza registrar_temperatura().

PASO 5 - VERIFICACIÓN

20, 25, 18, 30

Mínima = 18
Máxima = 30
Promedio = 23.25
"""

class GestorTemperatura:

    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        if len(self.temperaturas) == 0:
            return None

        return min(self.temperaturas)

    def maxima(self):
        if len(self.temperaturas) == 0:
            return None

        return max(self.temperaturas)

    def promedio(self):
        if len(self.temperaturas) == 0:
            return 0

        suma = 0

        for temperatura in self.temperaturas:
            suma = suma + temperatura

        return suma / len(self.temperaturas)

    def registrar_multiples(self, *temps):
        for temperatura in temps:
            self.registrar_temperatura(temperatura)


temperatura = GestorTemperatura()

cantidad = int(input("¿Cuántas temperaturas desea ingresar? "))

for i in range(cantidad):
    temp = float(input("Ingrese la temperatura: "))
    temperatura.registrar_temperatura(temp)

print("Temperaturas:", temperatura.temperaturas)
print("Mínima:", temperatura.minima())
print("Máxima:", temperatura.maxima())
print("Promedio:", temperatura.promedio())


"""
EJERCICIO 7 - MAPEADOR DE EDADES

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Nombre y edad de cada persona.
- Edad mínima para realizar una búsqueda.

Proceso:
- Guardar nombre y edad en un diccionario.
- Buscar personas cuya edad sea mayor o igual a la indicada.
- Calcular el promedio de las edades.

Salida:
- Lista de personas mayores.
- Promedio de edades.

PASO 2 - BOSQUEJO A MANO

Ana -> 28
Bob -> 17

Buscar mayores de 18:

Ana cumple.
Bob no cumple.

Resultado:
["Ana"]

PASO 3 - DESCUBRIR EL PATRÓN

El diccionario permite relacionar nombre y edad.
Con items() podemos revisar cada persona y su edad.

PASO 4 - ESCRIBIR EL CÓDIGO

Se crea la clase GestorPersonas.
Las personas se guardan en un diccionario.

PASO 5 - VERIFICACIÓN

Ana = 28
Bob = 17

personas_mayores(18)
Resultado: ["Ana"]
"""

class GestorPersonas:

    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        resultado = []

        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)

        return resultado

    def edad_promedio(self):
        if len(self.personas) == 0:
            return 0

        suma = 0

        for edad in self.personas.values():
            suma = suma + edad

        return suma / len(self.personas)


personas = GestorPersonas()

cantidad = int(input("¿Cuántas personas desea ingresar? "))

for i in range(cantidad):
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))

    personas.agregar_persona(nombre, edad)

print("Personas:", personas.personas)

edad_minima = int(input("Edad mínima: "))

print("Personas mayores:",
      personas.personas_mayores(edad_minima))

print("Edad promedio:", personas.edad_promedio())


"""
EJERCICIO 8 - ASIGNADOR DE EQUIPOS

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Nombre de equipos.
- Nombre de jugadores.

Proceso:
- Crear equipos dentro de un diccionario.
- Guardar los jugadores en listas.
- Contar los jugadores de cada equipo.
- Encontrar el equipo con más integrantes.

Salida:
- Nombre del equipo con más jugadores.

PASO 2 - BOSQUEJO A MANO

Equipo A:
Juan
Pedro

Equipo B:
Luis

Equipo A tiene 2 jugadores.
Equipo B tiene 1 jugador.

Resultado:
Equipo A

PASO 3 - DESCUBRIR EL PATRÓN

Se necesita un diccionario donde cada equipo tenga una lista
de jugadores.

PASO 4 - ESCRIBIR EL CÓDIGO

crear_equipo() crea una lista vacía.
agregar_jugador() agrega jugadores a esa lista.

PASO 5 - VERIFICACIÓN

A -> 2 jugadores
B -> 1 jugador

Equipo con más integrantes:
A
"""

class Equipos:

    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        if equipo in self.equipos:
            self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        if len(self.equipos) == 0:
            return None

        equipo_mayor = None
        mayor_cantidad = 0

        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > mayor_cantidad:
                mayor_cantidad = len(jugadores)
                equipo_mayor = equipo

        return equipo_mayor


equipos = Equipos()

cantidad_equipos = int(input("¿Cuántos equipos desea crear? "))

for i in range(cantidad_equipos):
    nombre_equipo = input("Nombre del equipo: ")
    equipos.crear_equipo(nombre_equipo)

for equipo in equipos.equipos:
    cantidad_jugadores = int(
        input("¿Cuántos jugadores tendrá " + equipo + "? ")
    )

    for i in range(cantidad_jugadores):
        jugador = input("Nombre del jugador: ")
        equipos.agregar_jugador(equipo, jugador)

print("Equipos:", equipos.equipos)
print("Equipo con más integrantes:",
      equipos.equipo_mayor_integrantes())


"""
EJERCICIO 9 - VALIDADOR DE CARACTERES

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Un texto.

Proceso:
- Recorrer cada carácter.
- Identificar vocales, consonantes y dígitos.
- Guardar el texto más largo analizado.

Salida:
- Diccionario con la cantidad de vocales,
  consonantes y dígitos.

PASO 2 - BOSQUEJO A MANO

Texto:
Hola123

H -> consonante
o -> vocal
l -> consonante
a -> vocal
1 -> dígito
2 -> dígito
3 -> dígito

Resultado:
vocales = 2
consonantes = 2
dígitos = 3

PASO 3 - DESCUBRIR EL PATRÓN

Cada carácter debe clasificarse.
Se puede utilizar lower(), isdigit() y una lista de vocales.

PASO 4 - ESCRIBIR EL CÓDIGO

solo_vocales() verifica si una letra es vocal.
contar_por_tipo() reutiliza ese método.

PASO 5 - VERIFICACIÓN

Hola123

Resultado:
{'vocales': 2, 'consonantes': 2, 'digitos': 3}
"""

class AnalizadorString:

    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        vocales = "aeiouáéíóú"

        if letra.lower() in vocales:
            return True
        else:
            return False

    def contar_por_tipo(self, texto):

        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        resultado = {
            "vocales": 0,
            "consonantes": 0,
            "digitos": 0
        }

        for letra in texto:

            if self.solo_vocales(letra):
                resultado["vocales"] = resultado["vocales"] + 1

            elif letra.isdigit():
                resultado["digitos"] = resultado["digitos"] + 1

            elif letra.isalpha():
                resultado["consonantes"] = resultado["consonantes"] + 1

        return resultado


analizador = AnalizadorString()

texto = input("Ingrese un texto: ")

resultado = analizador.contar_por_tipo(texto)

print("Resultado:", resultado)
print("Texto más largo:", analizador.texto_mas_largo)


"""
EJERCICIO 10 - GESTOR DE TAREAS CON PRIORIDAD

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Descripción de una tarea.
- Prioridad de la tarea.

Proceso:
- Guardar cada tarea como una tupla.
- Filtrar las tareas de prioridad alta.
- Eliminar una tarea completada.

Salida:
- Lista de tareas prioritarias.

PASO 2 - BOSQUEJO A MANO

("Estudiar", "alta")
("Leer", "baja")

Tareas prioritarias:
[("Estudiar", "alta")]

PASO 3 - DESCUBRIR EL PATRÓN

Cada tarea tiene dos datos:
descripción y prioridad.

Una tupla permite guardar ambos datos juntos.

PASO 4 - ESCRIBIR EL CÓDIGO

Se crea una lista de tuplas.
Se recorre la lista para buscar las tareas de prioridad alta.

PASO 5 - VERIFICACIÓN

Estudiar -> alta
Leer -> baja

Resultado:
[("Estudiar", "alta")]
"""

class Tareas:

    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        tarea = (descripcion, prioridad)
        self.tareas.append(tarea)

    def tareas_prioritarias(self):
        resultado = []

        for tarea in self.tareas:
            if tarea[1].lower() == "alta":
                resultado.append(tarea)

        return resultado

    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                return True

        return False


tareas = Tareas()

cantidad = int(input("¿Cuántas tareas desea ingresar? "))

for i in range(cantidad):
    descripcion = input("Descripción de la tarea: ")
    prioridad = input("Prioridad (alta/media/baja): ")

    tareas.agregar_tarea(descripcion, prioridad)

print("Tareas:", tareas.tareas)
print("Tareas prioritarias:", tareas.tareas_prioritarias())

tarea_eliminar = input("Ingrese una tarea completada para eliminar: ")

if tareas.eliminar_completada(tarea_eliminar):
    print("Tarea eliminada.")
else:
    print("La tarea no existe.")

print("Tareas restantes:", tareas.tareas)


"""
EJERCICIO 11 - CONTADOR DE FRECUENCIA

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Elementos que pueden repetirse.

Proceso:
- Guardar cada elemento en un diccionario.
- Aumentar su contador cada vez que aparece.
- Encontrar el elemento más frecuente.

Salida:
- Elemento más frecuente.
- Cantidad de veces que aparece.

PASO 2 - BOSQUEJO A MANO

a
b
a

Diccionario:
a -> 2
b -> 1

Elemento más frecuente:
a

PASO 3 - DESCUBRIR EL PATRÓN

El diccionario puede utilizarse como contador.
La clave es el elemento y el valor es la cantidad.

PASO 4 - ESCRIBIR EL CÓDIGO

Si el elemento no existe, se crea con 1.
Si existe, se aumenta en 1.

PASO 5 - VERIFICACIÓN

a -> 1
b -> 1
a -> 2

Resultado:
a
"""

class ContadorFrecuencia:

    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] = self.frecuencias[elemento] + 1
        else:
            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):
        if len(self.frecuencias) == 0:
            return None

        elemento_mayor = None
        frecuencia_mayor = 0

        for elemento, frecuencia in self.frecuencias.items():
            if frecuencia > frecuencia_mayor:
                frecuencia_mayor = frecuencia
                elemento_mayor = elemento

        return elemento_mayor

    def frecuencia_elemento(self, elemento):
        if elemento in self.frecuencias:
            return self.frecuencias[elemento]
        else:
            return 0


contador = ContadorFrecuencia()

cantidad = int(input("¿Cuántos elementos desea ingresar? "))

for i in range(cantidad):
    elemento = input("Ingrese un elemento: ")
    contador.agregar_elemento(elemento)

print("Frecuencias:", contador.frecuencias)
print("Elemento más frecuente:",
      contador.elemento_mas_frecuente())

buscar = input("¿Qué elemento desea consultar? ")

print("Frecuencia:",
      contador.frecuencia_elemento(buscar))


"""
EJERCICIO 12 - SELECTOR DE RANGO CON TUPLAS

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Inicio y fin de un rango.
- Varios rangos.

Proceso:
- Crear rangos representados como tuplas.
- Combinar los elementos de varios rangos.
- Eliminar duplicados utilizando un conjunto.

Salida:
- Tupla con los números de un rango.
- Lista con los elementos únicos de varios rangos.

PASO 2 - BOSQUEJO A MANO

Rango 1:
(1, 3) -> 1, 2, 3

Rango 2:
(2, 4) -> 2, 3, 4

Combinación:
1, 2, 3, 2, 3, 4

Sin duplicados:
1, 2, 3, 4

PASO 3 - DESCUBRIR EL PATRÓN

Los conjuntos permiten eliminar automáticamente los duplicados.

PASO 4 - ESCRIBIR EL CÓDIGO

crear_rango() devuelve una tupla.
elementos_en_multiples_rangos() recibe varias tuplas con *rangos.

PASO 5 - VERIFICACIÓN

(1,3), (2,4)

Resultado:
[1, 2, 3, 4]
"""

class SelectorRango:

    def crear_rango(self, inicio, fin):
        resultado = []

        for numero in range(inicio, fin + 1):
            resultado.append(numero)

        return tuple(resultado)

    def elementos_en_multiples_rangos(self, *rangos):
        elementos = set()

        for rango in rangos:
            inicio = rango[0]
            fin = rango[1]

            for numero in range(inicio, fin + 1):
                elementos.add(numero)

        resultado = list(elementos)
        resultado.sort()

        return resultado


selector = SelectorRango()

inicio = int(input("Inicio del rango: "))
fin = int(input("Fin del rango: "))

print("Rango:", selector.crear_rango(inicio, fin))

cantidad = int(input("¿Cuántos rangos desea combinar? "))

rangos = []

for i in range(cantidad):
    inicio = int(input("Inicio del rango: "))
    fin = int(input("Fin del rango: "))

    rangos.append((inicio, fin))

print("Elementos sin duplicados:",
      selector.elementos_en_multiples_rangos(*rangos))


"""
EJERCICIO 13 - COMBINADOR DE LISTAS

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Dos o más listas.

Proceso:
- Tomar un elemento de la primera lista.
- Tomar un elemento de la segunda lista.
- Alternarlos.
- Repetir hasta terminar las listas.

Salida:
- Una lista intercalada.

PASO 2 - BOSQUEJO A MANO

Lista 1:
[1, 2]

Lista 2:
[3, 4]

Intercalando:
1, 3, 2, 4

Resultado:
[1, 3, 2, 4]

PASO 3 - DESCUBRIR EL PATRÓN

Se utilizan índices para acceder a cada posición.
Si una lista es más larga, sus elementos restantes también se agregan.

PASO 4 - ESCRIBIR EL CÓDIGO

Se crea intercalar() para dos listas.
intercalar_multiples() reutiliza intercalar() para varias listas.

PASO 5 - VERIFICACIÓN

[1, 2] y [3, 4]

Resultado:
[1, 3, 2, 4]
"""

class CombinadorListas:

    def intercalar(self, lista1, lista2):
        resultado = []

        posicion = 0

        while posicion < len(lista1) or posicion < len(lista2):

            if posicion < len(lista1):
                resultado.append(lista1[posicion])

            if posicion < len(lista2):
                resultado.append(lista2[posicion])

            posicion = posicion + 1

        return resultado

    def intercalar_multiples(self, *listas):

        if len(listas) == 0:
            return []

        resultado = listas[0]

        posicion = 1

        while posicion < len(listas):
            resultado = self.intercalar(
                resultado,
                listas[posicion]
            )

            posicion = posicion + 1

        return resultado


combinador = CombinadorListas()

lista1 = []
lista2 = []

cantidad1 = int(input("Elementos de la primera lista: "))

for i in range(cantidad1):
    elemento = input("Elemento: ")
    lista1.append(elemento)

cantidad2 = int(input("Elementos de la segunda lista: "))

for i in range(cantidad2):
    elemento = input("Elemento: ")
    lista2.append(elemento)

print("Lista 1:", lista1)
print("Lista 2:", lista2)

print("Lista intercalada:",
      combinador.intercalar(lista1, lista2))


"""
EJERCICIO 14 - MAPEO DE ESTUDIANTES A NOTAS

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Nombre del estudiante.
- Nota.
- Nota mínima para aprobar.

Proceso:
- Guardar estudiante y nota en un diccionario.
- Buscar estudiantes aprobados.
- Encontrar el estudiante con mayor nota.

Salida:
- Lista de estudiantes aprobados.
- Tupla con nombre y nota del mejor estudiante.

PASO 2 - BOSQUEJO A MANO

Ana -> 95
Bob -> 70

Mejor estudiante:
("Ana", 95)

PASO 3 - DESCUBRIR EL PATRÓN

El diccionario permite relacionar cada estudiante con su nota.
items() permite recorrer nombre y nota al mismo tiempo.

PASO 4 - ESCRIBIR EL CÓDIGO

Se crea RegistroNotas.
registrar() almacena los datos.
estudiantes_aprobados() filtra.
mejor_estudiante() compara.

PASO 5 - VERIFICACIÓN

Ana = 95
Bob = 70

Mejor:
("Ana", 95)
"""

class RegistroNotas:

    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        resultado = []

        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                resultado.append(estudiante)

        return resultado

    def mejor_estudiante(self):
        if len(self.notas) == 0:
            return None

        mejor_nombre = None
        mejor_nota = -1

        for estudiante, nota in self.notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante

        return (mejor_nombre, mejor_nota)


registro = RegistroNotas()

cantidad = int(input("¿Cuántos estudiantes desea registrar? "))

for i in range(cantidad):
    estudiante = input("Nombre del estudiante: ")
    nota = float(input("Nota: "))

    registro.registrar(estudiante, nota)

print("Registro:", registro.notas)

nota_minima = float(input("Nota mínima para aprobar: "))

print("Estudiantes aprobados:",
      registro.estudiantes_aprobados(nota_minima))

print("Mejor estudiante:",
      registro.mejor_estudiante())


"""
EJERCICIO 15 - DIVISORES DE UN NÚMERO

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Uno o varios números.

Proceso:
- Buscar todos los números que dividen exactamente al número.
- Determinar si un número es perfecto.
- Reutilizar encontrar_divisores() para varios números.

Salida:
- Tupla con divisores.
- True o False para saber si es perfecto.
- Diccionario de números y sus divisores.

PASO 2 - BOSQUEJO A MANO

Número:
12

Divisores:
1, 2, 3, 4, 6, 12

Tupla:
(1, 2, 3, 4, 6, 12)

PASO 3 - DESCUBRIR EL PATRÓN

Si numero % divisor == 0, entonces el divisor divide exactamente
al número.

PASO 4 - ESCRIBIR EL CÓDIGO

Se crea encontrar_divisores().
es_perfecto() suma los divisores excepto el propio número.
encontrar_multiples_divisores() reutiliza encontrar_divisores().

PASO 5 - VERIFICACIÓN

12:
(1, 2, 3, 4, 6, 12)

6:
1 + 2 + 3 = 6

Por lo tanto, 6 es perfecto.
"""

class DivisorFinder:

    def encontrar_divisores(self, numero):
        divisores = []

        for divisor in range(1, numero + 1):
            if numero % divisor == 0:
                divisores.append(divisor)

        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)

        suma = 0

        for divisor in divisores:
            if divisor != numero:
                suma = suma + divisor

        if suma == numero:
            return True
        else:
            return False

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}

        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)

        return resultado


divisor = DivisorFinder()

numero = int(input("Ingrese un número: "))

print("Divisores:", divisor.encontrar_divisores(numero))
print("¿Es perfecto?:", divisor.es_perfecto(numero))

cantidad = int(input("¿Cuántos números desea analizar? "))

numeros = []

for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

print("Divisores:",
      divisor.encontrar_multiples_divisores(*numeros))


"""
EJERCICIO 16 - CODIFICADOR / DECODIFICADOR CESAR

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Una letra o palabra.
- Un desplazamiento del 1 al 25.

Proceso:
- Convertir la letra a un código numérico.
- Aplicar el desplazamiento.
- Utilizar el operador % para mantener el resultado dentro
  del alfabeto.
- Guardar las codificaciones en un diccionario.

Salida:
- Letra o palabra codificada.

PASO 2 - BOSQUEJO A MANO

Palabra:
hola

Desplazamiento:
3

h -> k
o -> r
l -> o
a -> d

Resultado:
krod

PASO 3 - DESCUBRIR EL PATRÓN

Cada letra puede convertirse con ord() y volver a convertirse
a letra con chr().

El operador % permite volver al inicio del alfabeto.

PASO 4 - ESCRIBIR EL CÓDIGO

codificar_letra() trabaja con una letra.
codificar_palabra() reutiliza codificar_letra().

PASO 5 - VERIFICACIÓN

hola + 3 = krod
"""

class CodificadorCesar:

    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):

        if letra.isalpha() == False:
            return letra

        if letra.islower():
            inicio = ord("a")
        else:
            inicio = ord("A")

        posicion = ord(letra) - inicio

        nueva_posicion = (posicion + desplazamiento) % 26

        nueva_letra = chr(inicio + nueva_posicion)

        return nueva_letra

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra:
            resultado = resultado + self.codificar_letra(
                letra,
                desplazamiento
            )

        self.historial[palabra] = resultado

        return resultado


codificador = CodificadorCesar()

palabra = input("Ingrese una palabra: ")
desplazamiento = int(input("Ingrese el desplazamiento: "))

resultado = codificador.codificar_palabra(
    palabra,
    desplazamiento
)

print("Palabra original:", palabra)
print("Palabra codificada:", resultado)
print("Historial:", codificador.historial)


"""
EJERCICIO 17 - GRUPO DE EDADES

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Varias edades.
- Una categoría para consultar.

Proceso:
- Clasificar cada edad.
- Agrupar las edades según su categoría.
- Calcular el promedio de una categoría.

Categorías:
0 a 11 -> niño
12 a 17 -> adolescente
18 a 64 -> adulto
65 o más -> mayor

Salida:
- Diccionario con las edades agrupadas.
- Promedio de una categoría.

PASO 2 - BOSQUEJO A MANO

5 -> niño
15 -> adolescente
30 -> adulto
70 -> mayor

Resultado:
{
    "niño": [5],
    "adolescente": [15],
    "adulto": [30],
    "mayor": [70]
}

PASO 3 - DESCUBRIR EL PATRÓN

Se utilizan condiciones if y elif para determinar la categoría.

PASO 4 - ESCRIBIR EL CÓDIGO

clasificar_edad() determina la categoría.
agrupar_por_categoria() reutiliza clasificar_edad().

PASO 5 - VERIFICACIÓN

5 -> niño
15 -> adolescente
30 -> adulto
70 -> mayor
"""

class AgrupadorEdades:

    def __init__(self):
        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

    def clasificar_edad(self, edad):

        if edad >= 0 and edad <= 11:
            return "niño"

        elif edad >= 12 and edad <= 17:
            return "adolescente"

        elif edad >= 18 and edad <= 64:
            return "adulto"

        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):

        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.grupos[categoria].append(edad)

        return self.grupos

    def edad_promedio_categoria(self, categoria):

        if categoria not in self.grupos:
            return 0

        if len(self.grupos[categoria]) == 0:
            return 0

        suma = 0

        for edad in self.grupos[categoria]:
            suma = suma + edad

        return suma / len(self.grupos[categoria])


edades = AgrupadorEdades()

cantidad = int(input("¿Cuántas edades desea ingresar? "))

lista_edades = []

for i in range(cantidad):
    edad = int(input("Ingrese una edad: "))
    lista_edades.append(edad)

print("Grupos:",
      edades.agrupar_por_categoria(*lista_edades))

categoria = input(
    "¿Qué categoría desea consultar? "
)

print("Promedio:",
      edades.edad_promedio_categoria(categoria))


"""
EJERCICIO 18 - MATRIZ DE DISTANCIAS

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Dos puntos representados por tuplas (x, y).
- Un punto de referencia.
- Varios puntos.

Proceso:
- Calcular la distancia euclidiana.
- Guardar las distancias calculadas en una lista.
- Comparar las distancias para encontrar el punto más cercano.

Salida:
- Distancia entre dos puntos.
- Punto más cercano.

PASO 2 - BOSQUEJO A MANO

Punto 1:
(0, 0)

Punto 2:
(3, 4)

Fórmula:

d = √((x2-x1)² + (y2-y1)²)

d = √(3² + 4²)
d = √25
d = 5

PASO 3 - DESCUBRIR EL PATRÓN

Para cada punto se calcula una distancia.
Después se comparan las distancias para encontrar la menor.

PASO 4 - ESCRIBIR EL CÓDIGO

Se utiliza math.sqrt().
Las coordenadas se guardan como tuplas.

PASO 5 - VERIFICACIÓN

(0,0) y (3,4)

Distancia = 5.0
"""

import math


class CalculadorDistancia:

    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):

        x1 = p1[0]
        y1 = p1[1]

        x2 = p2[0]
        y2 = p2[1]

        distancia = math.sqrt(
            (x2 - x1) ** 2 +
            (y2 - y1) ** 2
        )

        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):

        if len(puntos) == 0:
            return None

        punto_cercano = puntos[0]

        distancia_menor = self.distancia_euclidiana(
            referencia,
            puntos[0]
        )

        for punto in puntos[1:]:

            distancia = self.distancia_euclidiana(
                referencia,
                punto
            )

            if distancia < distancia_menor:
                distancia_menor = distancia
                punto_cercano = punto

        return punto_cercano


calculador = CalculadorDistancia()

x1 = float(input("X del primer punto: "))
y1 = float(input("Y del primer punto: "))

x2 = float(input("X del segundo punto: "))
y2 = float(input("Y del segundo punto: "))

p1 = (x1, y1)
p2 = (x2, y2)

print("Distancia:", calculador.distancia_euclidiana(p1, p2))

cantidad = int(input("¿Cuántos puntos desea comparar? "))

puntos = []

for i in range(cantidad):

    x = float(input("X del punto: "))
    y = float(input("Y del punto: "))

    puntos.append((x, y))

print("Punto más cercano:",
      calculador.punto_mas_cercano(p1, *puntos))

print("Distancias calculadas:",
      calculador.distancias)


"""
EJERCICIO 19 - INVENTARIO DE PRODUCTOS

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Producto y cantidad.
- Producto y cantidad que se desea retirar.
- Cantidad mínima de stock.

Proceso:
- Guardar productos en un diccionario.
- Aumentar el stock.
- Comprobar si existe suficiente stock antes de restar.
- Buscar productos que tengan menos del mínimo.

Salida:
- True o False al retirar productos.
- Lista de productos con bajo stock.

PASO 2 - BOSQUEJO A MANO

pan -> 50

Restar:
30

Stock:
20

Si mínimo = 25:

20 < 25

Entonces:
["pan"]

PASO 3 - DESCUBRIR EL PATRÓN

El diccionario funciona como una pequeña base de datos.
La clave es el producto y el valor es su cantidad.

PASO 4 - ESCRIBIR EL CÓDIGO

agregar_stock() guarda o aumenta cantidades.
restar_stock() comprueba si existe suficiente.
productos_bajo_stock() filtra los productos.

PASO 5 - VERIFICACIÓN

pan = 50
restar 30

Resultado:
True

Stock final:
20

Con mínimo 25:
["pan"]
"""

class Inventario:

    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):

        if producto in self.stock:
            self.stock[producto] = (
                self.stock[producto] + cantidad
            )
        else:
            self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):

        if producto in self.stock:

            if self.stock[producto] >= cantidad:
                self.stock[producto] = (
                    self.stock[producto] - cantidad
                )

                return True

        return False

    def productos_bajo_stock(self, minimo):

        resultado = []

        for producto, cantidad in self.stock.items():

            if cantidad < minimo:
                resultado.append(producto)

        return resultado


inventario = Inventario()

cantidad = int(input("¿Cuántos productos desea registrar? "))

for i in range(cantidad):

    producto = input("Nombre del producto: ")
    cantidad_producto = int(
        input("Cantidad: ")
    )

    inventario.agregar_stock(
        producto,
        cantidad_producto
    )

print("Inventario:", inventario.stock)

producto_restar = input(
    "¿Qué producto desea retirar? "
)

cantidad_restar = int(
    input("¿Cuánto desea retirar? ")
)

resultado = inventario.restar_stock(
    producto_restar,
    cantidad_restar
)

print("¿Se pudo realizar la operación?:", resultado)
print("Inventario actualizado:", inventario.stock)

minimo = int(input("Stock mínimo: "))

print("Productos bajo stock:",
      inventario.productos_bajo_stock(minimo))


"""
EJERCICIO 20 - ANALIZADOR DE PATRONES EN TEXTOS

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Un texto.
- Un patrón de búsqueda.

Proceso:
- Separar el texto utilizando split().
- Buscar palabras que comiencen con el patrón.
- Agrupar las palabras según su longitud.
- Utilizar un conjunto para eliminar palabras duplicadas.

Salida:
- Lista de palabras que comienzan con el patrón.
- Diccionario de palabras agrupadas por longitud.
- Conjunto de palabras únicas.

PASO 2 - BOSQUEJO A MANO

Texto:
"el gato está aquí"

Palabras:
el
gato
está
aquí

Longitudes:

el -> 2
gato -> 4
está -> 4
aquí -> 4

Diccionario:
{
    2: ["el"],
    4: ["gato", "está", "aquí"]
}

IMPORTANTE:
La guía muestra dos claves 5 en su ejemplo, pero un diccionario
no puede tener dos claves iguales. Por eso las palabras que tienen
la misma longitud deben estar juntas en la misma lista.

PASO 3 - DESCUBRIR EL PATRÓN

split() separa el texto en palabras.
startswith() permite saber si una palabra comienza con un patrón.
len() permite obtener la longitud de cada palabra.
set() permite eliminar duplicados.

PASO 4 - ESCRIBIR EL CÓDIGO

encontrar_palabras() busca palabras por patrón.
agrupar_por_longitud() crea el diccionario.
palabras_unicas() utiliza un conjunto.

PASO 5 - VERIFICACIÓN

Texto:
"el gato está aquí"

Patrón:
"ga"

Resultado de encontrar_palabras():
["gato"]

Resultado de palabras_unicas():
{"el", "gato", "está", "aquí"}
"""

class AnalizadorPatrones:

    def __init__(self):
        self.texto = ""

    def encontrar_palabras(self, texto, patron):

        palabras = texto.split()
        resultado = []

        for palabra in palabras:

            if palabra.startswith(patron):
                resultado.append(palabra)

        return resultado

    def agrupar_por_longitud(self, texto):

        palabras = texto.split()
        resultado = {}

        for palabra in palabras:

            longitud = len(palabra)

            if longitud not in resultado:
                resultado[longitud] = []

            resultado[longitud].append(palabra)

        return resultado

    def palabras_unicas(self, texto):

        palabras = texto.split()

        conjunto = set()

        for palabra in palabras:
            conjunto.add(palabra)

        return conjunto


analizador = AnalizadorPatrones()

texto = input("Ingrese un texto: ")

patron = input(
    "Ingrese el patrón que desea buscar: "
)

print("Palabras que comienzan con el patrón:")

print(
    analizador.encontrar_palabras(
        texto,
        patron
    )
)

print("Palabras agrupadas por longitud:")

print(
    analizador.agrupar_por_longitud(
        texto
    )
)

print("Palabras únicas:")

print(
    analizador.palabras_unicas(
        texto
    )
)