import mcpi.minecraft as minecraft
from mcpi import block
import math

# Conectar al mundo de Minecraft
mc = minecraft.Minecraft.create()

# Función para crear un arcoíris
def create_rainbow():
    rainbow_colors = [14, 1, 4, 5, 3, 11, 10]  
    radius = 25  # Radio máximo del arcoíris
    layer_height = 2  # Distancia vertical entre las capas del arcoíris

    # Obtener la posición del jugador
    pos = mc.player.getTilePos()

    # Para que el arcoíris esté a nivel de la tierra
    base_height = max(mc.getHeight(pos.x, pos.z), pos.y + 5)  # Al menos 5 bloques por encima del jugador
    
    for i, color in enumerate(rainbow_colors):
        current_radius = radius - i * layer_height  # Ajusta el radio para cada capa de color

        # Crear cada capa del arcoíris en un semicírculo
        for angle in range(0, 181, 1):  # Semicírculo (0 a 180 grados, pasos de 1 grado)
            x = pos.x + int(current_radius * math.cos(math.radians(angle)))
            y = base_height + int(current_radius * math.sin(math.radians(angle)))  # Curva hacia arriba
            z = pos.z + 10  # Distancia entre el arcoíris y el jugador
            
            mc.setBlock(x, y, z, block.WOOL.id, color)

# Llamada para crear el arcoíris
create_rainbow()
