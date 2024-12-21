import time
import mcpi.minecraft as minecraft
from mcpi.event import ChatEvent

# Bots
from .insultBot import InsultBot
from .TNTBot import TNTBot
from .OracleBot import OracleBot
from .followBot import BlockFollowerBot  # Cambiado para reflejar el nuevo bot
from .rainbowBot import create_rainbow
from .houseBot import HouseBot


class CommandHandler:
    def __init__(self, mc):
        """
        Initializes the CommandHandler with a Minecraft connection.
        
        Parameters:
        mc (Minecraft): Connection to the Minecraft server.
        """
        self.mc = mc
        self.commands = {}  # guarda el mapeo de los comandos

    def register_command(self, name, function, description="No description"):
        """
        Registers a command with its corresponding function and description.
        """
        self.commands[name] = {"function": function, "description": description}

    def execute_command(self, name, *args):
        """
        Executes a command by name with optional arguments.
        """
        command = self.commands.get(name)
        if command:
            command["function"](*args)
        #else:
            #self.mc.postToChat(f"Unknown command: {name}. Type '--help' for a list of commands.")

    def show_help(self):
        """
        Displays all available commands.
        """
        self.mc.postToChat("Commands available:")
        for name, details in self.commands.items():
            if name != "--help":
                self.mc.postToChat(f"{name}: {details['description']}")


# Main
def main():
    # Connexion al servidor Minecraft
    mc = minecraft.Minecraft.create()

    # Crear instancia del CommandHandler
    handler = CommandHandler(mc)

    # Registrar comandos
    handler.register_command("--help", handler.show_help)
    handler.register_command("insultbot", lambda: InsultBot(mc).start_insulting(1), "Start InsultBot")
    handler.register_command("tntbot", lambda: TNTBot(mc).deploy_near_player(count=10), "Deploy TNTBot")
    handler.register_command("oraclebot", lambda: OracleBot(mc).listen_and_respond(), "Start OracleBot")
    handler.register_command("rainbowbot", lambda: create_rainbow(), "Create a rainbow")
    handler.register_command("housebot", lambda: HouseBot(mc).build_house(mc.player.getTilePos().x + 2, 
                                                                          mc.player.getTilePos().y, 
                                                                          mc.player.getTilePos().z + 2), 
                             "Create a house")

    # mensaje inicial
    mc.postToChat("Welcome to Minecraft! Type '--help' to see available commands.")

    while True:

        chat_events = mc.events.pollChatPosts()

        for event in chat_events:
            if event.type == ChatEvent.POST:
                # extraer comando y argumentos
                message = event.message.strip().lower()
                parts = message.split(" ")
                command_name = parts[0]
                arguments = parts[1:]

                # ejecutar comanda
                handler.execute_command(command_name, *arguments)

        time.sleep(1)


# Ejecutar programa
if __name__ == "__main__":
    main()
