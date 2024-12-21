import mcpi.minecraft as minecraft
import mcpi.block as block

class HouseBot:
    def __init__(self, mc):
        self.mc = mc

    def build_house(self, x, y, z, width=7, height=5, length=5):
        # Outer walls
        for i in range(height):
            for j in range(width):
                for k in range(length):
                    # Build the walls
                    if (j == 0 or j == width - 1 or k == 0 or k == length - 1) and not (j == width // 2 and k == length - 1 and i < 2):  # espacio para la puerta
                        self.mc.setBlock(x + j, y + i, z + k, block.WOOD.id)
        
        # Roof
        for j in range(width):
            for k in range(length):
                self.mc.setBlock(x + j, y + height, z + k, block.GLASS.id)

        # Floor
        for j in range(width):
            for k in range(length):
                self.mc.setBlock(x + j, y - 1, z + k, block.STONE.id)

        # Door
        self.mc.setBlock(x + width // 2, y, z + length - 1, block.AIR.id)
        self.mc.setBlock(x + width // 2, y + 1, z + length - 1, block.AIR.id)

        # Windows
        for i in range(2):
            self.mc.setBlock(x + 1, y + i + 1, z, block.GLASS.id)
            self.mc.setBlock(x + width - 2, y + i + 1, z, block.GLASS.id)

        self.mc.postToChat("House complete!")
