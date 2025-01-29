import time
import mcpi.minecraft as minecraft
from mcpi.event import ChatEvent
import mcpi.block as block
import threading


#Framework
from .AgentFramework import AgentFramework, Agent

# Bots
from .insultBot import InsultBot
from .TNTBot import TNTBot
from .OracleBot import OracleBot
from .houseBot import HouseBot
from .welcome import Person
from .emotionsBot import EmotionBot
from .timeBot import TimeBot


class CommandHandler(Agent):
    def __init__(self, mc, framework, ready_event):
        super().__init__("CommandHandler")
        self.mc = mc
        self.framework = framework
        self.commands = {}  # Guarda el mapeo de los comandos
        self.ready_event = ready_event  # Evento de bloqueo para sincronización

        # Bots a registrar
        self.oracle_bot = None
        self.emotion_bot = None

    def register_command(self, name, function, description="No description"):
        """Registra un comando con su función y descripción."""
        self.commands[name] = {"function": function, "description": description}

    def execute_command(self, name, *args):
        """Ejecuta un comando llamando al framework cuando sea necesario."""
        if name in self.commands:
            self.commands[name]["function"](*args)

    def show_help(self):
        self.mc.postToChat("Commands available:")
        for name, details in self.commands.items():
            if name != "--help":
                self.mc.postToChat(f"{name}: {details['description']}")

    def run(self):
        """Escucha los comandos en el chat de Minecraft."""
        while True:
            chat_events = self.mc.events.pollChatPosts()
            for event in chat_events:
                if event.type == ChatEvent.POST:
                    message = event.message.strip().lower()
                    parts = message.split(" ")
                    command_name = parts[0]
                    arguments = parts[1:]
                    self.execute_command(command_name, *arguments)
            time.sleep(1)

    def start_oracle(self):
        """Inicia OracleBot solo si se solicita el comando."""
        if not self.oracle_bot:
            self.oracle_bot = OracleBot(self.mc)
            self.framework.register_agent(self.oracle_bot)
            self.oracle_bot.start()


    def start_emotion(self):
        """Inicia EmotionBot solo si se solicita el comando."""
        if not self.emotion_bot:
            self.emotion_bot = EmotionBot(self.mc)
            self.framework.register_agent(self.emotion_bot)
            self.emotion_bot.start() 
    
    def exit_game(self):
        """Detener todos los agentes y salir del juego."""
        self.mc.postToChat("Shutting down...")
        
        # Detener agentes
        self.framework.stop_agents()  
        
        exit()  # Salir de la ejecución del script
        


# Main
def main():
    
    # Connexion al servidor Minecraft
    mc = minecraft.Minecraft.create()

    # Crear un evento de bloqueo para sincronización
    ready_event = threading.Event()

    # Crear framework
    framework = AgentFramework()

    # welcome
    person_agent = Person(mc, ready_event)
    framework.register_agent(person_agent)
    person_agent.start()  
    ready_event.wait()  # Bloquea hasta que termine
    framework.unregister_agent(person_agent)  

    # Crear los agentes y registrarlos al framework
    time_bot = TimeBot(mc)
    house_bot = HouseBot(mc)
    insult_bot = InsultBot(mc)
    tnt_bot = TNTBot(mc)
    #oracle_bot = OracleBot(mc)
    #emotion_bot = EmotionBot(mc)

    framework.register_agent(time_bot)
    framework.register_agent(house_bot)
    framework.register_agent(insult_bot)
    framework.register_agent(tnt_bot)
    #framework.register_agent(oracle_bot)
    #framework.register_agent(emotion_bot)

    # Registrar comandos
    handler = CommandHandler(mc, framework, ready_event)
    framework.register_agent(handler)

    time.sleep(2)
    # mensaje inicial
    mc.postToChat("Welcome to Minecraft! Type '--help' to see available commands.")

    # handler delega las llamadas a framework
    handler.register_command("--help", handler.show_help)
    handler.register_command("insultbot", lambda: insult_bot.insult(), "Start InsultBot")
    handler.register_command("tntbot", lambda: tnt_bot.deploy_near_player(count=3), "Deploy TNTBot")
    handler.register_command("oraclebot", handler.start_oracle, "Start OracleBot")
    handler.register_command("emotionbot", handler.start_emotion, "Start EmotionBot")
    handler.register_command("changehouse", lambda: house_bot.change_house(), "Change blocks of a house")
    handler.register_command("housebot", lambda: house_bot.build_house(mc.player.getTilePos().x + 2, mc.player.getTilePos().y, mc.player.getTilePos().z + 2), "Create a house")
    handler.register_command("--exit", handler.exit_game, "Remove all agents and exit script")



    # Activar agentes 
    framework.run_agents()



# Ejecutar programa
if __name__ == "__main__":
    main()

