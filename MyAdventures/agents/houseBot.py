import mcpi.minecraft as minecraft
import mcpi.block as block
from .AgentFramework import Agent
import time


class HouseBot(Agent): #heredar de Agent
    def __init__(self, mc, wall=block.WOOD.id):
        super().__init__("HouseBot")  # Llamar al constructor de Agent
        self.mc = mc
        self.wall = wall
        self.running = False  # agente activo?  

    def start(self):
        self.running = True
        self.run()
    
    def run(self):
        #while self.running:
            #self.mc.postToChat("HouseBot is ready to build!")
            time.sleep(10)  # Mensaje cada 10 segundos para simular actividad

    def stop(self):
        self.running = False

    def build_house(self, x, y, z, width=7, height=5, length=5):
         if not self.running:
            self.mc.postToChat("HouseBot is not active!")
            return
         else:
            # Outer walls
            for i in range(height):
                for j in range(width):
                    for k in range(length):
                        # Build the walls
                        if (j == 0 or j == width - 1 or k == 0 or k == length - 1) and not (j == width // 2 and k == length - 1 and i < 2):  # espacio para la puerta
                            self.mc.setBlock(x + j, y + i, z + k, self.wall)
            
            # Roof
            for j in range(width):
                for k in range(length):
                    self.mc.setBlock(x + j, y + height, z + k, block.GLASS.id)

            # Floor
            for j in range(width):
                for k in range(length):
                    self.mc.setBlock(x + j, y - 1, z + k, block.STONE.id)

            # Door
            self.mc.setBlock(x + width // 2, y, z + length - 1, block.WOOL.id)
            self.mc.setBlock(x + width // 2, y + 1, z + length - 1, block.WOOL.id)

            # Windows
            for i in range(2):
                self.mc.setBlock(x + 1, y + i + 1, z, block.GLASS.id)
                self.mc.setBlock(x + width - 2, y + i + 1, z, block.GLASS.id)

            self.mc.postToChat("House complete!")

    def change_house(self):
        # Obtener el material actual usando reflexión
        current_material = getattr(self, "wall")
        self.mc.postToChat(f"Current material: { current_material }")

        # Cambiar entre WOOD y GLASS 
        if current_material == block.WOOD.id:
            self.mc.postToChat("Antes: madera")
            new_material = block.GLASS.id
        else:
            self.mc.postToChat("Antes: crsital")
            new_material = block.WOOD.id

        setattr(self, "wall", new_material)

        # Mostrar mensaje de confirmación en el chat
        self.mc.postToChat(f"HouseBot material changed to {'GLASS' if new_material == block.GLASS.id else 'WOOD'}.")
