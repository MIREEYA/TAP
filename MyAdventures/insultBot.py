import random, time
import mcpi.minecraft as minecraft


# Clase InsultBot
class InsultBot:
    def __init__(self, mc):
        if mc is None:
            self.mc = minecraft.Minecraft.create()
        else:
            self.mc = mc
        self.mc = mc

        self.insults = [
            "You look easy to draw",
            "I've seen dirt blocks more creative than you!",
            "Is that your best effort?",
            "I'm not impressed by your surviving skills",
            "If a zombie was eating your brains, he'd die from starvation",
            "You're about as useful as a stick",
            "I had zero expectations and you still let me down",
            "I’m not saying you’re stupid, but you make me feel smart",
            "Ah, so you're the reason we have warning labels on everything",
            "If you're going to be so stupid, why not be a zombie",
            "If you were the trophy at the end of my race, I'd walk backwards"
        ]

    def insult(self):
        # Elegir un insulto al azar y enviarlo al chat
        insult = random.choice(self.insults)
        self.mc.postToChat(insult)

    def start_insulting(self, count=5):
        for _ in range(count):
            self.insult()
            time.sleep(3) 
