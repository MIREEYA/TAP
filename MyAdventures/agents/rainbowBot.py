import mcpi.minecraft as minecraft
from mcpi import block
import math

# Conectar al mundo de Minecraft
mc = minecraft.Minecraft.create()

# Función para crear un arcoíris
def create_rainbow():
    rainbow_colors = [14, 1, 4, 5, 3, 11, 10]  
    radius = 25
    layer_spacing = 2  
    
    # Obtener la posición del jugador
    pos = mc.player.getTilePos()

    # para que el arcoiris este a nivel de tierra
    base_height = max(mc.getHeight(pos.x, pos.z), pos.y + 5)  # al menos 5 bloques por encima del jugador
    
    for i, color in enumerate(rainbow_colors):
        current_radius = radius - i * layer_spacing

        for angle in range(0, 181, 1):  # Semicírculo (0 to 180 degrees, 1-degree steps)
            x = pos.x + int(current_radius * math.cos(math.radians(angle)))
            y = base_height + int(current_radius * math.sin(math.radians(angle)))  # Curva hacia arriba
            z = pos.z + 10  # distancia entre arcoiris y jugador
            
            mc.setBlock(x, y, z, block.WOOL.id, color)
