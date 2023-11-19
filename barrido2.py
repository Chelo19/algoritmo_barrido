import math
import matplotlib.pyplot as plt

# Función para calcular el ángulo polar entre dos puntos con respecto al depósito
def polar_angle(x, y):
    return math.atan2(y, x)

# Datos de los clientes y el depósito
deposito = (0, 0, 0)
clientes = [
    (-77, -66, 14),
    (16, -24, 21),
    (2, -51, 16),
    (-21, -17, 3),
    (-81, -11, 22),
    (6, -25, 18),
    (9, -74, 19),
    (-63, -44, 1),
    (11, -73, 24),
    (-32, 17, 8)
]

# Calcular ángulos polares de los clientes con respecto al depósito
angles = {}
for i, cliente in enumerate(clientes):
    x, y, demanda = cliente
    angle = polar_angle(x - deposito[0], y - deposito[1])
    angles[i+1] = (angle, demanda)

# Ordenar los clientes según el ángulo polar en sentido horario
sorted_angles = sorted(angles.items(), key=lambda x: x[1][0], reverse=True)

# Obtener coordenadas x, y de los clientes ordenados por ángulo polar
x_coords = [clientes[item[0]-1][0] for item in sorted_angles]
y_coords = [clientes[item[0]-1][1] for item in sorted_angles]

# Graficar los clientes
plt.figure(figsize=(8, 8))
plt.scatter([deposito[0]], [deposito[1]], color='red', label='Depósito')

for i, cliente in enumerate(sorted_angles):
    plt.scatter(x_coords[i], y_coords[i], label=f"Cliente {cliente[0]}")

plt.xlabel('Coordenada x')
plt.ylabel('Coordenada y')
plt.title('Clientes y Depósito')
plt.legend()
plt.grid(True)
plt.show()
