# Crear un iterador para los numeros impares

#Limite
limit = 10

#Crear iterador
odd_itter = iter(range(1,limit+1,2))

#Usar el iterador
for num in odd_itter:
    print(num)


#Crear un iterador para los numeros Pares

limit = 10

Odd_Itter = iter(range(0,11,2))

for Num in Odd_Itter:
    print(Num)

# Para los que les interesa saber 
# por que escribio 1,limit+1,2 
# en la linea 7 de codigo, asi funciona la syntaxis:

# range(start, stop, step)

#start: por donde empieza

# stop: donde para limit+1 = 10

# step: numero de posiciones que avanza