
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
            "If you were the trophy at the end of my race, I'd walk backwards",
            "You so stupid you probably think Taco Bell is where you pay your telephone bill.",
            "Don't you have a terribly empty feeling ---- in your skull?"
            "Yo Mama's so fat, when she stepped onto the scale it said 'to infinity and beyond!'",
            "Everyone is entitled to be stupid, but you abuse the privilege.",
            "What's that ugly thing growing out of your neck... Oh... It's your head...",
            "I'm sorry, Talking to you seems as appealing as playing leapfrog with unicorns.",
            "I am not anti-social..I just don't like you",
            "Yo Mama so fat she sat on a rainbow and skittles came out.",
            "Yo Mama so fat she went into a zoo and a zookeeper said: 'Oh boy...another elephant got out!'",
            "Yo Mama is so fat she walked out in high heels and came back in flip flops.",
            "You're a habit I'd like to kick; with both feet.",
            "You're the best at all you do - and all you do is make people hate you.",
            "You're so ugly if my dog looked like you, I'd shave its ass and teach it to walk backwards",
            "You're so ugly when you were born the doctor slapped your mother!",
            "You're so dumb you think manual labor is a Mexican",
            "If you ever tax your brain, don't charge more than a penny."
        ]

        self._running = False 
        self.min_delay = 10
        self.max_delay = 50 

    def insult(self):
        """Elige un insulto aleatorio y lo envía al chat, con serializacion ASCII."""
        insult = random.choice(self.insults)
        safe_insult = insult.encode("ascii", "ignore").decode()  # Elimina caracteres incompatibles
        self.mc.postToChat(safe_insult)

    def run(self):
        """Envia un insulto cada x segundos hasta que se detenga."""
        while self._running:
             # random delay cada ciclo
            delay = random.randint(self.min_delay, self.max_delay)
            time.sleep(delay)
            self.insult()

    def start(self):
        """Inicia el insulto en un ciclo separado."""
        self._running = True
        self.run() 

    def stop(self):
        self._running = False
