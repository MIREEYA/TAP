import time
import mcpi.minecraft as minecraft
import mcpi.block as block



class TNTBot:
    def __init__(self, mc=None):
        if mc is None:
            import mcpi.minecraft as minecraft
            self.mc = minecraft.Minecraft.create()
        else:
            self.mc = mc
        

    def place_tnt(self, x, y, z):
        """Coloca TNT en la posición especificada y lo activa."""
        self.mc.setBlock(x, y, z, block.TNT.id)
        self.mc.postToChat(f"TNT placed at ({x}, {y}, {z})!")
        time.sleep(self.delay)
        self.activate_tnt(x, y, z)

    def activate_tnt(self, x, y, z):
        """Activa el TNT colocando fuego encima."""
        self.mc.setBlock(x, y + 1, z, block.FIRE.id)  # Activa el TNT con fuego
        self.mc.postToChat("Boom!")

    def deploy_near_player(self, count=5):
        """Coloca y activa TNT cerca del jugador."""
        pos = self.mc.player.getTilePos()
        self.mc.postToChat("Deploying TNT near the player...")
        for i in range(count):
            offset_x = i * 2
            self.place_tnt(pos.x + offset_x, pos.y, pos.z)

