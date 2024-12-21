# Listas de palabras positivas y negativas
positive_words = ["happy", "okey", "good", "fantastic", "excellent", "great", "excited", "amazing"]
negative_words = ["sad", "bad", "depressed", "bored", "angry", "annoyed","cooked","dead"]

class Emotion:
    def __init__(self, mc=None):
        if mc is None:
                import mcpi.minecraft as minecraft
                self.mc = minecraft.Minecraft.create()
        else:
                self.mc = mc
    def ask(self):
        # Pregunta al jugador
        self.mc.postToChat("How are you today? (Type something)")

        # Revisa los mensajes del chat
        chat_messages = self.mc.events.pollChatPosts()

        # Si hay mensajes en el chat, los procesamos
        if chat_messages:
            # Filtrar mensajes positivos
            positive_responses = list(filter(lambda x: any(word in x.message.lower() for word in positive_words), chat_messages))
            negative_responses = list(filter(lambda x: any(word in x.message.lower() for word in negative_words), chat_messages))

            # Si encontramos respuestas positivas
            if positive_responses:
                self.mc.postToChat("I'm happy for you!")

            # Si encontramos respuestas negativas
            elif negative_responses:
                 self.mc.postToChat("I'm sorry to hear that.")
            else:
                self.mc.postToChat("I don't understand you")

