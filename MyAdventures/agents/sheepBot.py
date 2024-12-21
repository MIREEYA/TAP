import mcpi.minecraft as minecraft
import time, random
import mcpi.block as block


class SheepBot:
    def __init__(self, mc):
        self.mc = mc

    def spawn_sheep_statue_near_player(self, count=1):
        """Simulates sheep spawning by building a wool statue."""
        player_pos = self.mc.player.getTilePos()

        for _ in range(count):
            # Generate a random offset near the player
            offset_x = random.randint(-5, 5)
            offset_z = random.randint(-5, 5)
            x = player_pos.x + offset_x
            y = player_pos.y
            z = player_pos.z + offset_z

            # Build a simple "sheep" out of wool
            self.mc.setBlock(x, y, z, block.WOOL.id, 0)  # Body
            self.mc.setBlock(x, y + 1, z, block.WOOL.id, 0)  # Head
            self.mc.setBlock(x - 1, y, z, block.WOOL.id, 15)  # Leg 1
            self.mc.setBlock(x + 1, y, z, block.WOOL.id, 15)  # Leg 2
            self.mc.setBlock(x, y, z - 1, block.WOOL.id, 15)  # Leg 3
            self.mc.setBlock(x, y, z + 1, block.WOOL.id, 15)  # Leg 4

            self.mc.postToChat(f"Sheep statue created at ({x}, {y}, {z})!")
            time.sleep(0.5)
