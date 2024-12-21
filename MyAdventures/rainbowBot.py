import math

class RainbowBot:
    def __init__(self, mc=None):   
        # Si no se pasa el mock de Minecraft, se crea el objeto real
        if mc is None:
            import mcpi.minecraft as minecraft
            self.mc = minecraft.Minecraft.create()
        else:
            self.mc = mc  # Usamos el mock proporcionado para pruebas

    # Función para crear un arcoíris
    def create_rainbow(self):
        rainbow_colors = [14, 1, 4, 5, 3, 11, 10]  # Colores del arcoíris en Minecraft
        radius = 25  # Radio máximo del arcoíris
        layer_height = 2  # Distancia vertical entre las capas del arcoíris

        # Obtener la posición del jugador
        pos = self.mc.player.getTilePos()

        # Calcular la altura base del arcoíris (al menos 5 bloques por encima del jugador)
        base_height = max(self.mc.getHeight(pos.x, pos.z), pos.y + 5)  

        # Crear el arcoíris capa por capa
        for i, color in enumerate(rainbow_colors):
            current_radius = radius - i * layer_height  # Ajusta el radio para cada capa de color

            # Crear cada capa del arcoíris en un semicírculo (0 a 180 grados)
            for angle in range(0, 181, 1):  
                # Calcula las coordenadas (x, y, z) para cada bloque del arcoíris
                x = pos.x + int(current_radius * math.cos(math.radians(angle)))
                y = base_height + int(current_radius * math.sin(math.radians(angle)))  # Curva hacia arriba
                z = pos.z + 10  # Distancia entre el arcoíris y el jugador
                
                # Coloca el bloque en la posición calculada
                self.mc.setBlock(x, y, z, self.mc.block.WOOL.id, color)
