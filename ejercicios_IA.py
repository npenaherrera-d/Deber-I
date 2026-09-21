"""
EJERCICIO SIMILAR 1 - CALCULADOR DE CALIFICACIONES

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Varias calificaciones de estudiantes.

Proceso:
- Validar que cada calificación esté entre 0 y 100.
- Guardar solamente las calificaciones válidas.
- Calcular la calificación más alta.

Salida:
- Lista de calificaciones válidas.
- Calificación más alta.

PASO 2 - BOSQUEJO A MANO

Calificaciones:
80, 95, 110, 70

110 no es válida.

Lista:
[80, 95, 70]

Mayor:
95

PASO 3 - DESCUBRIR EL PATRÓN

Cada calificación debe revisarse antes de almacenarse.
Después se recorren las calificaciones para encontrar la mayor.

PASO 4 - ESCRIBIR EL CÓDIGO

Se crea una clase.
Se utilizan métodos para validar, agregar y encontrar
la calificación más alta.

PASO 5 - VERIFICACIÓN

Entrada:
80, 95, 110, 70

Salida:
[80, 95, 70]
Mayor: 95
"""

class GestorCalificaciones:

    def __init__(self):
        self.calificaciones = []

    def validar(self, nota):
        if nota >= 0 and nota <= 100:
            return True
        else:
            return False

    def agregar(self, nota):
        if self.validar(nota):
            self.calificaciones.append(nota)

    def nota_mas_alta(self):
        if len(self.calificaciones) == 0:
            return 0

        mayor = self.calificaciones[0]

        for nota in self.calificaciones:
            if nota > mayor:
                mayor = nota

        return mayor


gestor = GestorCalificaciones()

cantidad = int(input("¿Cuántas calificaciones desea ingresar? "))

for i in range(cantidad):
    nota = float(input("Ingrese una calificación: "))
    gestor.agregar(nota)

print("Calificaciones válidas:", gestor.calificaciones)
print("Calificación más alta:", gestor.nota_mas_alta())


"""
EJERCICIO SIMILAR 2 - CONTADOR DE PALABRAS REPETIDAS

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Varias palabras.

Proceso:
- Guardar cada palabra.
- Contar cuántas veces aparece cada palabra.
- Mostrar las palabras que aparecen más de una vez.

Salida:
- Diccionario con las frecuencias.

PASO 2 - BOSQUEJO A MANO

Entrada:
sol
luna
sol
mar

Resultado:

sol -> 2
luna -> 1
mar -> 1

PASO 3 - DESCUBRIR EL PATRÓN

El diccionario puede utilizarse para guardar una palabra
y la cantidad de veces que aparece.

PASO 4 - ESCRIBIR EL CÓDIGO

Si la palabra ya existe, se aumenta su contador.
Si no existe, se crea con valor 1.

PASO 5 - VERIFICACIÓN

sol, luna, sol

Resultado:
{'sol': 2, 'luna': 1}
"""

class ContadorPalabras:

    def __init__(self):
        self.palabras = {}

    def agregar_palabra(self, palabra):

        if palabra in self.palabras:
            self.palabras[palabra] = self.palabras[palabra] + 1
        else:
            self.palabras[palabra] = 1

    def palabras_repetidas(self):
        resultado = []

        for palabra, cantidad in self.palabras.items():
            if cantidad > 1:
                resultado.append(palabra)

        return resultado


contador = ContadorPalabras()

cantidad = int(input("¿Cuántas palabras desea ingresar? "))

for i in range(cantidad):
    palabra = input("Ingrese una palabra: ")
    contador.agregar_palabra(palabra)

print("Frecuencias:", contador.palabras)
print("Palabras repetidas:", contador.palabras_repetidas())


"""
EJERCICIO SIMILAR 3 - FILTRO DE PRODUCTOS

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Nombre de productos.
- Precio de cada producto.

Proceso:
- Guardar los productos y sus precios.
- Buscar los productos cuyo precio sea menor o igual
  a un valor determinado.

Salida:
- Lista de productos económicos.

PASO 2 - BOSQUEJO A MANO

pan -> 2
arroz -> 5
carne -> 12

Precio máximo:
5

Resultado:
pan
arroz

PASO 3 - DESCUBRIR EL PATRÓN

Se recorren los elementos del diccionario y se compara
cada precio con el precio máximo.

PASO 4 - ESCRIBIR EL CÓDIGO

Se utiliza un diccionario.
El método productos_economicos devuelve una lista.

PASO 5 - VERIFICACIÓN

pan = 2
arroz = 5
carne = 12

Máximo = 5

Resultado:
['pan', 'arroz']
"""

class Tienda:

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, precio):
        self.productos[nombre] = precio

    def productos_economicos(self, precio_maximo):
        resultado = []

        for nombre, precio in self.productos.items():
            if precio <= precio_maximo:
                resultado.append(nombre)

        return resultado


tienda = Tienda()

cantidad = int(input("¿Cuántos productos desea registrar? "))

for i in range(cantidad):
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))

    tienda.agregar_producto(nombre, precio)

maximo = float(input("Ingrese el precio máximo: "))

print("Productos económicos:",
      tienda.productos_economicos(maximo))


"""
EJERCICIO SIMILAR 4 - ROTADOR DE LISTAS

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Una lista de elementos.

Proceso:
- Mover el último elemento al inicio de la lista.
- Repetir el proceso varias veces si es necesario.

Salida:
- Lista rotada.

PASO 2 - BOSQUEJO A MANO

Lista:
[1, 2, 3, 4]

Una rotación:

[4, 1, 2, 3]

PASO 3 - DESCUBRIR EL PATRÓN

El último elemento debe colocarse en la primera posición.
Los demás elementos mantienen su orden.

PASO 4 - ESCRIBIR EL CÓDIGO

Se utiliza una nueva lista.
Se recorre desde el último elemento.

PASO 5 - VERIFICACIÓN

[1, 2, 3, 4]

Resultado:
[4, 1, 2, 3]
"""

class RotadorLista:

    def rotar_una_vez(self, lista):

        if len(lista) == 0:
            return []

        resultado = []

        resultado.append(lista[len(lista) - 1])

        for i in range(len(lista) - 1):
            resultado.append(lista[i])

        return resultado

    def rotar_multiples(self, lista, veces):

        resultado = lista

        for i in range(veces):
            resultado = self.rotar_una_vez(resultado)

        return resultado


rotador = RotadorLista()

lista = []

cantidad = int(input("¿Cuántos elementos tendrá la lista? "))

for i in range(cantidad):
    elemento = input("Ingrese un elemento: ")
    lista.append(elemento)

veces = int(input("¿Cuántas veces desea rotar? "))

print("Lista original:", lista)
print("Lista rotada:", rotador.rotar_multiples(lista, veces))


"""
EJERCICIO SIMILAR 5 - CLASIFICADOR DE NÚMEROS

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Varios números.

Proceso:
- Determinar si cada número es positivo, negativo o cero.
- Agruparlos según su tipo.

Salida:
- Diccionario con positivos, negativos y ceros.

PASO 2 - BOSQUEJO A MANO

Números:
5, -2, 0, 8, -4

Positivos:
[5, 8]

Negativos:
[-2, -4]

Ceros:
[0]

PASO 3 - DESCUBRIR EL PATRÓN

Se utilizan condiciones if, elif y else.

PASO 4 - ESCRIBIR EL CÓDIGO

Cada número se compara con cero y se coloca
en la lista correspondiente.

PASO 5 - VERIFICACIÓN

5 -> positivo
-2 -> negativo
0 -> cero
"""

class ClasificadorNumeros:

    def __init__(self):
        self.resultado = {
            "positivos": [],
            "negativos": [],
            "ceros": []
        }

    def clasificar(self, numero):

        if numero > 0:
            self.resultado["positivos"].append(numero)

        elif numero < 0:
            self.resultado["negativos"].append(numero)

        else:
            self.resultado["ceros"].append(numero)

    def clasificar_multiples(self, *numeros):

        for numero in numeros:
            self.clasificar(numero)

        return self.resultado


clasificador = ClasificadorNumeros()

cantidad = int(input("¿Cuántos números desea ingresar? "))

numeros = []

for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

print(clasificador.clasificar_multiples(*numeros))


"""
EJERCICIO SIMILAR 6 - REGISTRO DE HUMEDAD

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Varias mediciones de humedad.

Proceso:
- Guardar las mediciones.
- Encontrar la humedad mínima.
- Encontrar la humedad máxima.

Salida:
- Mínima y máxima humedad.

PASO 2 - BOSQUEJO A MANO

Mediciones:
60, 70, 55, 80

Mínima = 55
Máxima = 80

PASO 3 - DESCUBRIR EL PATRÓN

Se utiliza una lista para guardar las mediciones.
Después se recorren para encontrar los extremos.

PASO 4 - ESCRIBIR EL CÓDIGO

Se crean métodos para registrar y buscar los valores.

PASO 5 - VERIFICACIÓN

60, 70, 55, 80

Mínima = 55
Máxima = 80
"""

class GestorHumedad:

    def __init__(self):
        self.humedades = []

    def registrar(self, humedad):
        self.humedades.append(humedad)

    def minima(self):
        if len(self.humedades) == 0:
            return 0

        menor = self.humedades[0]

        for humedad in self.humedades:
            if humedad < menor:
                menor = humedad

        return menor

    def maxima(self):
        if len(self.humedades) == 0:
            return 0

        mayor = self.humedades[0]

        for humedad in self.humedades:
            if humedad > mayor:
                mayor = humedad

        return mayor


gestor = GestorHumedad()

cantidad = int(input("¿Cuántas mediciones desea ingresar? "))

for i in range(cantidad):
    humedad = float(input("Ingrese la humedad: "))
    gestor.registrar(humedad)

print("Humedades:", gestor.humedades)
print("Mínima:", gestor.minima())
print("Máxima:", gestor.maxima())


"""
EJERCICIO SIMILAR 7 - REGISTRO DE EMPLEADOS

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Nombre y salario de cada empleado.

Proceso:
- Guardar cada empleado y su salario.
- Buscar empleados que ganen más de un valor indicado.
- Calcular el salario promedio.

Salida:
- Lista de empleados.
- Salario promedio.
- Empleados que superan el valor indicado.

PASO 2 - BOSQUEJO A MANO

Ana -> 500
Luis -> 800
Pedro -> 600

Buscar mayores de 550:

Luis
Pedro

PASO 3 - DESCUBRIR EL PATRÓN

El diccionario relaciona el nombre con el salario.

PASO 4 - ESCRIBIR EL CÓDIGO

Se recorren los elementos del diccionario para comparar
los salarios.

PASO 5 - VERIFICACIÓN

500, 800, 600

Promedio = 633.33
"""

class GestorEmpleados:

    def __init__(self):
        self.empleados = {}

    def agregar_empleado(self, nombre, salario):
        self.empleados[nombre] = salario

    def empleados_por_salario(self, minimo):
        resultado = []

        for nombre, salario in self.empleados.items():
            if salario >= minimo:
                resultado.append(nombre)

        return resultado

    def salario_promedio(self):
        if len(self.empleados) == 0:
            return 0

        suma = 0

        for salario in self.empleados.values():
            suma = suma + salario

        return suma / len(self.empleados)


empleados = GestorEmpleados()

cantidad = int(input("¿Cuántos empleados desea ingresar? "))

for i in range(cantidad):
    nombre = input("Nombre: ")
    salario = float(input("Salario: "))

    empleados.agregar_empleado(nombre, salario)

print("Empleados:", empleados.empleados)

minimo = float(input("Salario mínimo: "))

print("Empleados encontrados:",
      empleados.empleados_por_salario(minimo))

print("Salario promedio:",
      empleados.salario_promedio())


"""
EJERCICIO SIMILAR 8 - GRUPOS DE ESTUDIANTES

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Nombre de grupos.
- Nombres de estudiantes.

Proceso:
- Crear grupos.
- Agregar estudiantes a cada grupo.
- Encontrar el grupo con menos integrantes.

Salida:
- Grupo con menos integrantes.

PASO 2 - BOSQUEJO A MANO

Grupo A:
Ana
Luis
Pedro

Grupo B:
Carlos

Grupo B tiene menos estudiantes.

PASO 3 - DESCUBRIR EL PATRÓN

Cada grupo necesita una lista de estudiantes.
Un diccionario permite relacionar grupo y lista.

PASO 4 - ESCRIBIR EL CÓDIGO

Se crea el grupo.
Después se agregan estudiantes.

PASO 5 - VERIFICACIÓN

A -> 3
B -> 1

Resultado:
B
"""

class GruposEstudiantes:

    def __init__(self):
        self.grupos = {}

    def crear_grupo(self, grupo):
        self.grupos[grupo] = []

    def agregar_estudiante(self, grupo, estudiante):
        if grupo in self.grupos:
            self.grupos[grupo].append(estudiante)

    def grupo_menor(self):

        if len(self.grupos) == 0:
            return None

        grupo_menor = None
        cantidad_menor = None

        for grupo, estudiantes in self.grupos.items():

            if cantidad_menor is None:
                cantidad_menor = len(estudiantes)
                grupo_menor = grupo

            elif len(estudiantes) < cantidad_menor:
                cantidad_menor = len(estudiantes)
                grupo_menor = grupo

        return grupo_menor


grupos = GruposEstudiantes()

cantidad = int(input("¿Cuántos grupos desea crear? "))

for i in range(cantidad):
    grupo = input("Nombre del grupo: ")
    grupos.crear_grupo(grupo)

for grupo in grupos.grupos:

    cantidad_estudiantes = int(
        input("Cantidad de estudiantes para " + grupo + ": ")
    )

    for i in range(cantidad_estudiantes):
        estudiante = input("Nombre del estudiante: ")
        grupos.agregar_estudiante(grupo, estudiante)

print("Grupos:", grupos.grupos)
print("Grupo con menos estudiantes:", grupos.grupo_menor())


"""
EJERCICIO SIMILAR 9 - ANALIZADOR DE TEXTO

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Una oración.

Proceso:
- Contar letras mayúsculas.
- Contar letras minúsculas.
- Contar espacios.

Salida:
- Cantidad de cada tipo de carácter.

PASO 2 - BOSQUEJO A MANO

Texto:
"Hola Mundo"

Mayúsculas:
H, M -> 2

Minúsculas:
o, l, a, u, n, d, o -> 7

Espacios:
1

PASO 3 - DESCUBRIR EL PATRÓN

Se recorre carácter por carácter.
isupper() detecta mayúsculas.
islower() detecta minúsculas.

PASO 4 - ESCRIBIR EL CÓDIGO

Se crea un diccionario para almacenar los contadores.

PASO 5 - VERIFICACIÓN

"Hola Mundo"

Resultado:
mayúsculas = 2
minúsculas = 7
espacios = 1
"""

class AnalizadorCaracteres:

    def contar(self, texto):

        resultado = {
            "mayusculas": 0,
            "minusculas": 0,
            "espacios": 0
        }

        for caracter in texto:

            if caracter.isupper():
                resultado["mayusculas"] += 1

            elif caracter.islower():
                resultado["minusculas"] += 1

            elif caracter == " ":
                resultado["espacios"] += 1

        return resultado


analizador = AnalizadorCaracteres()

texto = input("Ingrese una oración: ")

print(analizador.contar(texto))


"""
EJERCICIO SIMILAR 10 - LISTA DE COMPRAS CON PRIORIDAD

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Nombre de productos.
- Prioridad de compra.

Proceso:
- Guardar cada producto con su prioridad.
- Buscar los productos de prioridad alta.
- Eliminar un producto comprado.

Salida:
- Productos prioritarios.
- Lista actualizada.

PASO 2 - BOSQUEJO A MANO

("Pan", "alta")
("Leche", "baja")
("Arroz", "alta")

Prioritarios:
Pan
Arroz

PASO 3 - DESCUBRIR EL PATRÓN

Cada producto se puede guardar como una tupla.

PASO 4 - ESCRIBIR EL CÓDIGO

Se recorre la lista buscando prioridad alta.
Para eliminar se busca el nombre del producto.

PASO 5 - VERIFICACIÓN

Pan -> alta
Leche -> baja

Resultado:
Pan
"""

class ListaCompras:

    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, prioridad):
        producto = (nombre, prioridad)
        self.productos.append(producto)

    def productos_prioritarios(self):
        resultado = []

        for producto in self.productos:
            if producto[1].lower() == "alta":
                resultado.append(producto)

        return resultado

    def eliminar_producto(self, nombre):

        for producto in self.productos:

            if producto[0] == nombre:
                self.productos.remove(producto)
                return True

        return False


compras = ListaCompras()

cantidad = int(input("¿Cuántos productos desea agregar? "))

for i in range(cantidad):
    nombre = input("Producto: ")
    prioridad = input("Prioridad: ")

    compras.agregar_producto(nombre, prioridad)

print("Productos:", compras.productos)
print("Productos prioritarios:",
      compras.productos_prioritarios())

eliminar = input("Producto comprado: ")

compras.eliminar_producto(eliminar)

print("Lista actualizada:", compras.productos)


"""
EJERCICIO SIMILAR 11 - FRECUENCIA DE NÚMEROS

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Varios números.

Proceso:
- Contar cuántas veces aparece cada número.
- Buscar el número que aparece menos veces.

Salida:
- Diccionario de frecuencias.
- Número menos frecuente.

PASO 2 - BOSQUEJO A MANO

2, 3, 2, 5, 3

2 -> 2
3 -> 2
5 -> 1

Menos frecuente:
5

PASO 3 - DESCUBRIR EL PATRÓN

Se utiliza un diccionario como contador.

PASO 4 - ESCRIBIR EL CÓDIGO

Se aumenta el valor de la clave cada vez que aparece.

PASO 5 - VERIFICACIÓN

2 aparece 2 veces.
3 aparece 2 veces.
5 aparece 1 vez.

Resultado:
5
"""

class FrecuenciaNumeros:

    def __init__(self):
        self.frecuencias = {}

    def agregar(self, numero):

        if numero in self.frecuencias:
            self.frecuencias[numero] += 1
        else:
            self.frecuencias[numero] = 1

    def menos_frecuente(self):

        if len(self.frecuencias) == 0:
            return None

        numero_menor = None
        frecuencia_menor = None

        for numero, frecuencia in self.frecuencias.items():

            if frecuencia_menor is None:
                frecuencia_menor = frecuencia
                numero_menor = numero

            elif frecuencia < frecuencia_menor:
                frecuencia_menor = frecuencia
                numero_menor = numero

        return numero_menor


frecuencia = FrecuenciaNumeros()

cantidad = int(input("¿Cuántos números desea ingresar? "))

for i in range(cantidad):
    numero = int(input("Número: "))
    frecuencia.agregar(numero)

print("Frecuencias:", frecuencia.frecuencias)
print("Menos frecuente:", frecuencia.menos_frecuente())


"""
EJERCICIO SIMILAR 12 - NÚMEROS DENTRO DE INTERVALOS

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Un intervalo.
- Un número para consultar.
- Varios intervalos.

Proceso:
- Crear intervalos.
- Determinar si un número pertenece al intervalo.

Salida:
- True o False.

PASO 2 - BOSQUEJO A MANO

Intervalo:
10 a 20

Número:
15

15 está dentro.

Resultado:
True

PASO 3 - DESCUBRIR EL PATRÓN

Se compara el número con el inicio y el final.

PASO 4 - ESCRIBIR EL CÓDIGO

Se utilizan tuplas para representar los intervalos.

PASO 5 - VERIFICACIÓN

(10, 20)
15

Resultado:
True
"""

class BuscadorIntervalos:

    def crear_intervalo(self, inicio, fin):
        return (inicio, fin)

    def esta_en_intervalo(self, numero, intervalo):

        inicio = intervalo[0]
        fin = intervalo[1]

        if numero >= inicio and numero <= fin:
            return True
        else:
            return False

    def consultar_multiples(self, numero, *intervalos):

        resultado = []

        for intervalo in intervalos:

            if self.esta_en_intervalo(numero, intervalo):
                resultado.append(intervalo)

        return resultado


buscador = BuscadorIntervalos()

inicio = int(input("Inicio: "))
fin = int(input("Fin: "))

intervalo = buscador.crear_intervalo(inicio, fin)

numero = int(input("Número a consultar: "))

print(
    "¿Está dentro?",
    buscador.esta_en_intervalo(numero, intervalo)
)


"""
EJERCICIO SIMILAR 13 - MEZCLADOR DE LISTAS

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Dos listas.

Proceso:
- Unir las dos listas.
- Evitar que existan elementos repetidos.

Salida:
- Una nueva lista sin duplicados.

PASO 2 - BOSQUEJO A MANO

Lista 1:
[1, 2, 3]

Lista 2:
[3, 4, 5]

Resultado:
[1, 2, 3, 4, 5]

PASO 3 - DESCUBRIR EL PATRÓN

Se puede utilizar un conjunto para controlar duplicados.
Después se convierte nuevamente en lista.

PASO 4 - ESCRIBIR EL CÓDIGO

Se recorren las dos listas y se agregan los elementos
a un conjunto.

PASO 5 - VERIFICACIÓN

[1, 2, 3] + [3, 4, 5]

Resultado:
[1, 2, 3, 4, 5]
"""

class MezcladorListas:

    def unir_sin_repetir(self, lista1, lista2):

        elementos = set()

        for elemento in lista1:
            elementos.add(elemento)

        for elemento in lista2:
            elementos.add(elemento)

        resultado = list(elementos)

        return resultado


mezclador = MezcladorListas()

lista1 = []
lista2 = []

cantidad = int(input("Elementos de la primera lista: "))

for i in range(cantidad):
    elemento = input("Elemento: ")
    lista1.append(elemento)

cantidad = int(input("Elementos de la segunda lista: "))

for i in range(cantidad):
    elemento = input("Elemento: ")
    lista2.append(elemento)

print("Resultado:",
      mezclador.unir_sin_repetir(lista1, lista2))


"""
EJERCICIO SIMILAR 14 - REGISTRO DE ESTUDIANTES

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Nombre y edad de estudiantes.

Proceso:
- Guardar los estudiantes.
- Buscar estudiantes mayores de cierta edad.
- Encontrar al estudiante de menor edad.

Salida:
- Lista de estudiantes mayores.
- Estudiante de menor edad.

PASO 2 - BOSQUEJO A MANO

Ana -> 20
Luis -> 18
Pedro -> 22

Menor:
Luis -> 18

PASO 3 - DESCUBRIR EL PATRÓN

Se utiliza un diccionario para relacionar nombre y edad.

PASO 4 - ESCRIBIR EL CÓDIGO

Se recorre el diccionario para buscar el menor.

PASO 5 - VERIFICACIÓN

20, 18, 22

Menor:
Luis
"""

class RegistroEstudiantes:

    def __init__(self):
        self.estudiantes = {}

    def registrar(self, nombre, edad):
        self.estudiantes[nombre] = edad

    def mayores_de(self, edad_minima):

        resultado = []

        for nombre, edad in self.estudiantes.items():

            if edad >= edad_minima:
                resultado.append(nombre)

        return resultado

    def estudiante_menor(self):

        if len(self.estudiantes) == 0:
            return None

        nombre_menor = None
        edad_menor = None

        for nombre, edad in self.estudiantes.items():

            if edad_menor is None or edad < edad_menor:
                edad_menor = edad
                nombre_menor = nombre

        return (nombre_menor, edad_menor)


registro = RegistroEstudiantes()

cantidad = int(input("¿Cuántos estudiantes? "))

for i in range(cantidad):

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))

    registro.registrar(nombre, edad)

print("Estudiantes:", registro.estudiantes)

edad = int(input("Edad mínima: "))

print("Mayores:",
      registro.mayores_de(edad))

print("Estudiante menor:",
      registro.estudiante_menor())


"""
EJERCICIO SIMILAR 15 - NÚMEROS PRIMOS

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Un número.

Proceso:
- Buscar si el número tiene divisores diferentes de 1 y él mismo.
- Determinar si es primo.
- Analizar varios números.

Salida:
- True o False.
- Diccionario con resultados.

PASO 2 - BOSQUEJO A MANO

Número:
7

Divisores:
1 y 7

Es primo:
True

Número:
8

Divisores:
1, 2, 4, 8

Es primo:
False

PASO 3 - DESCUBRIR EL PATRÓN

Un número primo solamente tiene dos divisores positivos:
1 y el propio número.

PASO 4 - ESCRIBIR EL CÓDIGO

Se recorre desde 2 hasta el número anterior.
Si existe un divisor exacto, no es primo.

PASO 5 - VERIFICACIÓN

7 -> True
8 -> False
"""

class AnalizadorPrimos:

    def es_primo(self, numero):

        if numero < 2:
            return False

        for divisor in range(2, numero):

            if numero % divisor == 0:
                return False

        return True

    def analizar_multiples(self, *numeros):

        resultado = {}

        for numero in numeros:
            resultado[numero] = self.es_primo(numero)

        return resultado


primos = AnalizadorPrimos()

cantidad = int(input("¿Cuántos números desea analizar? "))

numeros = []

for i in range(cantidad):
    numero = int(input("Número: "))
    numeros.append(numero)

print(primos.analizar_multiples(*numeros))


"""
EJERCICIO SIMILAR 16 - CODIFICADOR DE TEXTO

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Una palabra.
- Un desplazamiento.

Proceso:
- Cambiar cada letra por otra letra.
- Mantener los espacios.
- Guardar el resultado.

Salida:
- Texto codificado.

PASO 2 - BOSQUEJO A MANO

abc

Desplazamiento:
1

a -> b
b -> c
c -> d

Resultado:
bcd

PASO 3 - DESCUBRIR EL PATRÓN

Cada letra tiene una posición dentro del alfabeto.
Se aumenta esa posición según el desplazamiento.

PASO 4 - ESCRIBIR EL CÓDIGO

Se crea un método para una letra y otro para toda la palabra.

PASO 5 - VERIFICACIÓN

abc + 1 = bcd
"""

class CodificadorTexto:

    def __init__(self):
        self.historial = []

    def cambiar_letra(self, letra):

        if letra.isalpha() == False:
            return letra

        if letra == "z":
            return "a"

        if letra == "Z":
            return "A"

        return chr(ord(letra) + 1)

    def cambiar_texto(self, texto):

        resultado = ""

        for letra in texto:
            resultado = resultado + self.cambiar_letra(letra)

        self.historial.append(resultado)

        return resultado


codificador = CodificadorTexto()

texto = input("Ingrese un texto: ")

print("Texto original:", texto)
print("Texto codificado:",
      codificador.cambiar_texto(texto))

print("Historial:", codificador.historial)


"""
EJERCICIO SIMILAR 17 - CLASIFICADOR DE ALTURAS

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Varias alturas en centímetros.

Proceso:
- Clasificar cada persona:
  baja, media o alta.
- Agrupar las alturas.

Salida:
- Diccionario con las categorías.

PASO 2 - BOSQUEJO A MANO

150 -> baja
170 -> media
190 -> alta

PASO 3 - DESCUBRIR EL PATRÓN

Se utilizan condiciones para determinar la categoría.

Menos de 160:
baja

160 a 179:
media

180 o más:
alta

PASO 4 - ESCRIBIR EL CÓDIGO

El método clasificar_altura determina la categoría.
El método agrupar utiliza ese método.

PASO 5 - VERIFICACIÓN

150 -> baja
170 -> media
190 -> alta
"""

class AgrupadorAlturas:

    def __init__(self):
        self.grupos = {
            "baja": [],
            "media": [],
            "alta": []
        }

    def clasificar_altura(self, altura):

        if altura < 160:
            return "baja"

        elif altura < 180:
            return "media"

        else:
            return "alta"

    def agrupar(self, *alturas):

        for altura in alturas:

            categoria = self.clasificar_altura(altura)

            self.grupos[categoria].append(altura)

        return self.grupos


alturas = AgrupadorAlturas()

cantidad = int(input("¿Cuántas alturas desea ingresar? "))

lista = []

for i in range(cantidad):
    altura = float(input("Altura en cm: "))
    lista.append(altura)

print(alturas.agrupar(*lista))


"""
EJERCICIO SIMILAR 18 - DISTANCIA ENTRE PUNTOS

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Dos puntos en un plano.

Proceso:
- Obtener las coordenadas.
- Calcular la distancia entre los puntos.

Salida:
- Distancia euclidiana.

PASO 2 - BOSQUEJO A MANO

Punto A:
(1, 2)

Punto B:
(4, 6)

Fórmula:

d = √((x2-x1)² + (y2-y1)²)

PASO 3 - DESCUBRIR EL PATRÓN

Se utiliza la fórmula matemática de distancia euclidiana.

PASO 4 - ESCRIBIR EL CÓDIGO

Se utiliza math.sqrt().
Cada punto se guarda como una tupla.

PASO 5 - VERIFICACIÓN

A = (1,2)
B = (4,6)

Distancia:
5
"""

import math


class DistanciaPuntos:

    def calcular(self, punto1, punto2):

        x1 = punto1[0]
        y1 = punto1[1]

        x2 = punto2[0]
        y2 = punto2[1]

        resultado = math.sqrt(
            (x2 - x1) ** 2 +
            (y2 - y1) ** 2
        )

        return resultado


distancia = DistanciaPuntos()

x1 = float(input("X del punto A: "))
y1 = float(input("Y del punto A: "))

x2 = float(input("X del punto B: "))
y2 = float(input("Y del punto B: "))

punto1 = (x1, y1)
punto2 = (x2, y2)

print("Distancia:",
      distancia.calcular(punto1, punto2))


"""
EJERCICIO SIMILAR 19 - CONTROL DE STOCK MÍNIMO

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Productos.
- Cantidades disponibles.
- Cantidad mínima.

Proceso:
- Guardar el inventario.
- Buscar productos que tengan una cantidad igual
  o menor al mínimo.

Salida:
- Lista de productos que necesitan reposición.

PASO 2 - BOSQUEJO A MANO

pan -> 5
arroz -> 20
leche -> 3

Mínimo:
5

Resultado:
pan
leche

PASO 3 - DESCUBRIR EL PATRÓN

Se recorre el diccionario y se compara cada cantidad
con el límite establecido.

PASO 4 - ESCRIBIR EL CÓDIGO

Se utiliza un diccionario para almacenar productos y cantidades.

PASO 5 - VERIFICACIÓN

pan = 5
arroz = 20
leche = 3

Mínimo = 5

Resultado:
['pan', 'leche']
"""

class ControlStock:

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, cantidad):
        self.productos[nombre] = cantidad

    def productos_reponer(self, minimo):

        resultado = []

        for producto, cantidad in self.productos.items():

            if cantidad <= minimo:
                resultado.append(producto)

        return resultado


stock = ControlStock()

cantidad = int(input("¿Cuántos productos desea registrar? "))

for i in range(cantidad):

    nombre = input("Producto: ")
    cantidad_producto = int(input("Cantidad: "))

    stock.agregar_producto(
        nombre,
        cantidad_producto
    )

minimo = int(input("Cantidad mínima: "))

print("Inventario:", stock.productos)

print("Productos que necesitan reposición:",
      stock.productos_reponer(minimo))


"""
EJERCICIO SIMILAR 20 - AGRUPADOR DE PALABRAS POR LONGITUD

PASO 1 - ENTENDER EL PROBLEMA

Entrada:
- Una oración.

Proceso:
- Separar la oración en palabras.
- Obtener la longitud de cada palabra.
- Agrupar las palabras que tengan la misma longitud.
- Eliminar palabras repetidas.

Salida:
- Diccionario agrupado por longitud.
- Conjunto de palabras únicas.

PASO 2 - BOSQUEJO A MANO

Texto:
"sol luna sol mar"

Longitudes:

sol -> 3
luna -> 4
sol -> 3
mar -> 3

Agrupación:

3 -> [sol, sol, mar]
4 -> [luna]

Palabras únicas:

sol
luna
mar

PASO 3 - DESCUBRIR EL PATRÓN

len() permite conocer la longitud.
Un diccionario permite agrupar por longitud.
Un conjunto permite eliminar duplicados.

PASO 4 - ESCRIBIR EL CÓDIGO

Se separa el texto con split().
Se crea una lista para cada longitud cuando es necesaria.

PASO 5 - VERIFICACIÓN

Texto:
"sol luna sol mar"

Resultado:

{
    3: ["sol", "sol", "mar"],
    4: ["luna"]
}

Palabras únicas:
{"sol", "luna", "mar"}
"""

class AgrupadorPalabras:

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

        resultado = set()

        for palabra in palabras:
            resultado.add(palabra)

        return resultado


agrupador = AgrupadorPalabras()

texto = input("Ingrese una oración: ")

print("Palabras agrupadas por longitud:")

print(
    agrupador.agrupar_por_longitud(texto)
)

print("Palabras únicas:")

print(
    agrupador.palabras_unicas(texto)
)