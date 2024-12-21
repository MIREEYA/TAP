import mcpi.minecraft as minecraft
import time

class OracleBot:
    def __init__(self, mc):
        self.mc = mc
        self.responses = {
            "hello": "Hi there!",
            "how are you": "I'm doing well, thank you for asking",
            "what's your name": "I am the OracleBot, wise and all-knowing",
        }

    def listen_and_respond(self):
        self.mc.postToChat("Oracle is active, ask me a question! If you want to leave, just type 'bye'")
        chat_events = ""
        while chat_events != "bye":
            # Obtener eventos del chat
            chat_events = self.mc.events.pollChatPosts()
            for event in chat_events:
                question = event.message.lower() 

                if question == "bye":
                    self.mc.postToChat("Goodbye!")
                    self.mc.postToChat("OracleBot shutting down. Returning to main menu...")
                    return 

                #buscar la respuesta en self.response
                response = self.responses.get(question, "I'm sorry, my programmer was too lazy to design a response to that kind of question ;)")
                self.mc.postToChat(response)
            time.sleep(1)
