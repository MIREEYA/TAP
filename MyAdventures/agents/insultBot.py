import random
import time
import mcpi.minecraft as minecraft
from .AgentFramework import Agent

class InsultBot(Agent):  # hereda de Agent
    def __init__(self, mc):
        super().__init__("InsultBot")  # Llama al constructor de Agent
        self.mc = mc
        self.insults = [
            "You look easy to draw",
            "I've seen dirt blocks more creative than you!",
            "Is that your best effort?",
            "I'm not impressed by your surviving skills",
            "If a zombie was eating your brains, he'd die from starvation",
            "You're about as useful as a stick",
            "I had zero expectations and you still let me down",
            "I'm not saying you're stupid, but you make me feel smart",
            "Ah, so you're the reason we have warning labels on everything",
            "If you're going to be so stupid, why not be a zombie",
            "If you were the trophy at the end of my race, I'd walk backwards"
        ]
        self._running = False  

    def insult(self):
        """Elige un insulto aleatorio y lo envía al chat, asegurando compatibilidad con cp437."""
        insult = random.choice(self.insults)
        safe_insult = insult.encode("ascii", "ignore").decode()  # Elimina caracteres incompatibles
        self.mc.postToChat(safe_insult)

    def run(self):
        """Envia un insulto cada 90 segundos hasta que se detenga."""
        while self._running:
            time.sleep(90) 
            self.insult()

    def start(self):
        """Inicia el insulto en un ciclo separado."""
        self._running = True
        self.run() 

    def stop(self):
        self._running = False
