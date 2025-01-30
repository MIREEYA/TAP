import time
import mcpi.minecraft as minecraft
from .AgentFramework import Agent

# Listas de palabras positivas y negativas
positive_words = ["happy", "okey", "good", "fantastic", "excellent", "great", "excited", "amazing"]
negative_words = ["sad", "bad", "depressed", "bored", "angry", "annoyed", "cooked", "dead"]

class EmotionBot(Agent):  # Hereda de Agent
    def __init__(self, mc, test_mode=False):
        super().__init__("EmotionBot")  # Constructor de la clase base
        self.mc = mc
        self.running = False  # Control de ejecución
        self.test_mode = test_mode  # Modo de prueba

    def start(self):
        self.running = True
        self.mc.postToChat("EmotionBot is online! Type 'bye' to stop me.")
        self.ask_about_emotion()

    def ask_about_emotion(self):
        """Verifica el estado emocional del usuario basándose en el chat."""
        self.mc.postToChat("How are you today? (Type something)")

        ###################################
        if self.test_mode:
            # Procesa solo un mensaje y sale
            self.process_chat_messages()
            self.running = False 
            return  
        ###################################

        # Modo normal: loop mientras el bot esté activo
        while self.running:
            self.process_chat_messages()
            time.sleep(2)

    def process_chat_messages(self):
        """Procesa los mensajes del chat y responde según la emoción detectada."""
        chat_messages = self.mc.events.pollChatPosts()

        if chat_messages:
            for event in chat_messages:
                message = event.message.lower()

                if message == "bye":
                    self.mc.postToChat("Goodbye! EmotionBot shutting down.")
                    self.stop()
                    return

                if any(word in message for word in positive_words):
                    self.mc.postToChat("I'm happy for you!")
                elif any(word in message for word in negative_words):
                    self.mc.postToChat("I'm sorry to hear that.")
                else:
                    self.mc.postToChat("I don't understand you.")

                ##########################################
                if self.test_mode:  # Salir inmediatamente en test_mode
                    self.running = False
                    return  
                ##########################################

    def stop(self):
        self.running = False
