# Operadores Lógicos y de comparación, estructuras de control
a = 50
b = 10
c = 2

if ((a < b) | (b < c)):
    print(f'Camino Verdadero')
else:
    print(f'Camino Falso')

if not ((a < b) | (b < c)):
    print(f'Camino Verdadero')
else:
    print(f'Camino Falso')