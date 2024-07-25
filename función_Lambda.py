# ¿Cómo utilizar lambda para operaciones básicas?

#Para realizar operaciones sencillas con lambda, 
# no necesitamos especificar el nombre de la función. 
# Solo requerimos parámetros y la operación deseada. 
# Por ejemplo, para sumar dos números, podemos definir una función lambda así:

sumar = lambda a, b: a + b
print(sumar(10, 4))

multiplicar = lambda a, b: a * b
print(multiplicar(80, 4))

#Cuando trabajamos con listas y queremos aplicar una función a cada elemento, 
# map es útil junto con lambda. 
# Por ejemplo, para obtener el cuadrado de los números del 0 al 10:

numeros = list(range(11))
cuadrados = list(map(lambda x: x ** 2, numeros))
print("Cuadrados:", cuadrados)

#Lambda también es útil para filtrar elementos que cumplen ciertas condiciones. 
# Por ejemplo, para obtener los números pares de una lista:

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", numeros_pares)