# timeBot.py

import time
import mcpi.minecraft as minecraft
from .AgentFramework import Agent

class TimeBot(Agent):#heredar de Agent
    def __init__(self, mc):
        super().__init__("TimeBot")  # constructor de Agent
        self.mc = mc
        self.start_time = time.time()  # Coger tiempo inicial
        self.running = False  # bot activado?

    def start(self):
        self.running = True
        self.run()      
   
    def run(self):
        while self.running:  
            seconds = int(time.time() - self.start_time)
            self.mc.postToChat(f"Total time played: {seconds // 60} minutes.")
            time.sleep(60)  # esperar 60 seg

    def stop(self):
        self.running = False
        #self.mc.postToChat("TimeBot stopped.")
