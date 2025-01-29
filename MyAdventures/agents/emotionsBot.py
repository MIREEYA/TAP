import time
import mcpi.minecraft as minecraft
from .AgentFramework import Agent

# Listas de palabras positivas y negativas
positive_words = ["happy", "okey", "good", "fantastic", "excellent", "great", "excited", "amazing"]
negative_words = ["sad", "bad", "depressed", "bored", "angry", "annoyed", "cooked", "dead"]

class EmotionBot(Agent):  # Hereda de Agent
    def __init__(self, mc):
        super().__init__("EmotionBot")  # Constructor de la clase base
        self.mc = mc
        self.running = False  # Control de ejecución

    def start(self):
        self.running = True
        self.mc.postToChat("EmotionBot is online! Type 'bye' to stop me.")
        self.ask_about_emotion()

    def ask_about_emotion(self):
        self.mc.postToChat("How are you today? (Type something)")
        while self.running:
            # Revisa los mensajes del chat
            chat_messages = self.mc.events.pollChatPosts()

            if chat_messages:
                for event in chat_messages:
                    message = event.message.lower()

                    if message == "bye":
                        self.mc.postToChat("Goodbye! EmotionBot shutting down.")
                        self.stop()
                        return

                    # usar filter para detectar emociones
                    if any(word in message for word in positive_words):
                        self.mc.postToChat("I'm happy for you!")
                    elif any(word in message for word in negative_words):
                        self.mc.postToChat("I'm sorry to hear that.")
                    else:
                        self.mc.postToChat("I don't understand you.")
                    return  # Salir después de la primera respuesta

            time.sleep(2)

    def stop(self):
        self.running = False
