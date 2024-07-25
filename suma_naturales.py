def sumatoria(n):
    # Caso base
    if n == 0:
        return 0
    # Caso recursivo
    else:
        return n + sumatoria(n - 1)

# Ejemplo de uso
print(sumatoria(3))  # Output: 6

