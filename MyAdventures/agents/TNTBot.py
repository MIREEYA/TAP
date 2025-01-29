import time
import mcpi.minecraft as minecraft
import mcpi.block as block
from .AgentFramework import Agent

class TNTBot(Agent):  # Hereda de Agent
    def __init__(self, mc):
        super().__init__("TNTBot")  # Llamada al constructor Agent
        self.mc = mc
        self.running = False  
        self.delay = 2  # Tiempo entre la colocación y activación de TNT

    def start(self):
        self.running = True
        #self.run()

    def run(self):
        #while self.running:
            #self.deploy_near_player(count=1)  # 1 TNT a la vez
            time.sleep(5)  # esperar 5 seg

    def stop(self):
        self.running = False

    def place_tnt(self, x, y, z):
        self.mc.setBlock(x, y, z, block.TNT.id)
        self.mc.postToChat(f"TNT placed at ({x}, {y}, {z})!")
        time.sleep(self.delay)
        self.activate_tnt(x, y, z)

    def activate_tnt(self, x, y, z):
        self.mc.setBlock(x, y + 1, z, block.FIRE.id)  # Activa el TNT con fuego
        self.mc.postToChat("Boom!")

    def deploy_near_player(self, count=1):
        pos = self.mc.player.getTilePos()
        self.mc.postToChat("Deploying TNT near the player...")
        for i in range(count):
            offset_x = i * 2
            self.place_tnt(pos.x + offset_x, pos.y, pos.z)
