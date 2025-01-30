import time
import mcpi.minecraft as minecraft
from .AgentFramework import Agent


class OracleBot(Agent):
    def __init__(self, mc):
        super().__init__("OracleBot")  # Call to Agent's constructor
        self.mc = mc
        self.running = False

        self.responses = {
            "hello": "Hi there!",
            "how are you": "I'm doing well, thank you for asking.",
            "what's your name": "I am the OracleBot, wise and all-knowing.",
            "what is the meaning of life": "I'm just a machine.",
            "stupid": "I'm not saying you're stupid, but you make me feel smart.",
            "i love you": "Awww, you're so cute!",
            "what's your favorite animal": "Dolphins, because they're so evil like me >:).",
        }

    def start(self):
        self.running = True
        self.mc.postToChat("OracleBot is online! Type 'bye' to stop me.")
        self.listen_for_questions()

    def listen_for_questions(self, test_mode=False):

        ######################################################
        # para verificar q funcione en el test sin quedarse en el Loop
        if test_mode:
            events = self.mc.events.pollChatPosts()
            for event in events:
                question = event.message.lower()
                if question == "bye":
                    self.mc.postToChat("Goodbye! OracleBot shutting down.")
                    self.stop()
                    return
                response = self.responses.get(question, "I'm sorry, my programmer was too lazy to design a response to that kind of question")
                self.mc.postToChat(response)
        #######################################################
        
        else:
            while self.running:
                events = self.mc.events.pollChatPosts()
                for event in events:
                    question = event.message.lower()
                    if question == "bye":
                        self.mc.postToChat("Goodbye! OracleBot shutting down.")
                        self.stop()
                        return
                    response = self.responses.get(question, "I'm sorry, my programmer was too lazy to design a response to that kind of question")
                    self.mc.postToChat(response)
                time.sleep(1)

    def stop(self):
        self.running = False
