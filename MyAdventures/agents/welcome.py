import time
import mcpi.minecraft as minecraft
from mcpi.event import ChatEvent
from .AgentFramework import Agent

class Person(Agent):
    def __init__(self, mc, ready_event):
        super().__init__("Person")  # Llamar al constructor de Agent 
        self.mc = mc  
        self.name = None 
        self._running = False  
        self.ready_event = ready_event  # Sincronizar con el evento

    def start(self):
        self._running = True
        self.welcome()

    def stop(self):
        self._running = False

    def run(self):
        while self._running:
            time.sleep(0.5)

    def welcome(self):
        self.mc.postToChat("Welcome! What's your name?")

        while True:
            events = self.mc.events.pollChatPosts()  
            if events:
                self.name = events[0].message  # Asigna el nombre del jugador
                break
            time.sleep(0.5)

        # Llamar al método greet
        self.greet(self.name)
        
        # Evento acabado
        self.ready_event.set()
        self.stop()

    def greet(self, name):
        """Da la bienvenida al jugador por su nombre."""
        self.mc.postToChat(f"Hello, {name}!")
