# Importamos los módulos necesarios
import os  # Para poder usar os.system() y limpiar la pantalla
import math  # Para realizar operaciones matemáticas como la raíz cuadrada

# Limpiamos la pantalla
os.system("cls")

# Solicitamos al usuario los coeficientes de la ecuación cuadrática
a = int(input("Digite el coeficiente a: "))  # Coeficiente 'a'
b = int(input("Digite el coeficiente b: "))  # Coeficiente 'b'
c = int(input("Digite el coeficiente c: "))  # Coeficiente 'c'

# Calculamos el discriminante de la ecuación cuadrática (b^2 - 4ac)
imaginario = (b ** 2) - (4 * a * c)

# Verificamos si el discriminante es mayor o igual a 0 (raíz real)
if imaginario >= 0:
    # Si el discriminante es no negativo, calculamos las raíces reales
    x1 = ((-b) + math.sqrt(imaginario)) / (2 * a)  # Primera solución
    x2 = ((-b) - math.sqrt(imaginario)) / (2 * a)  # Segunda solución
    
    # Imprimimos las soluciones reales
    print("Las soluciones de X son \n", "X1 =", x1, "\n", "X2 =", x2)
else:
    # Si el discriminante es negativo, calculamos las raíces imaginarias
    Ima = math.sqrt(imaginario * (-1))  # Parte imaginaria de la solución
    variable = "i"  # Usamos 'i' para representar la parte imaginaria
    
    # Calculamos la parte real de la solución
    x1 = (-b) / (2 * a)  # Parte real de la primera solución
    x2 = (-b) / (2 * a)  # Parte real de la segunda solución
    
    # Imprimimos las soluciones imaginarias
    print("Las soluciones de X son: \n",
          "X1 =", x1, "+", Ima, variable, "\n",
          "X2 =", x2, "-", Ima, variable)