
class OracleBot:
    def __init__(self, mc=None):
        if mc is None:
            import mcpi.minecraft as minecraft
            self.mc = minecraft.Minecraft.create()
        else:
            self.mc = mc
        
        # Definir las respuestas conocidas
        self.responses = {
            "hello": "Hi there!",
            "how are you": "I'm doing well, thank you for asking",
            "what's your name": "I am the OracleBot, wise and all-knowing",
            "bye": "Goodbye! OracleBot shutting down. Returning to main menu..."
        }

    def listen_and_respond(self, test_mode=False):
        event = self.mc.events.pollChatPosts()
        if event:
            question = event[0].message
            response = self.responses.get(question, "I'm sorry, my programmer was too lazy to design a response to that kind of question ;)")
            self.mc.postToChat(response)
            if question.lower() == "bye":
                self.mc.postToChat("Goodbye!")
                self.mc.postToChat("OracleBot shutting down. Returning to main menu...")
                return  # Lógica para detener el bot o cambiar estado

