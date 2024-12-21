import mcpi.minecraft as minecraft
import time

# Conexión a Minecraft
mc = minecraft.Minecraft.create()

# Listas de palabras positivas y negativas
positive_words = ["happy", "okey", "good", "fantastic", "excellent", "great", "excited", "amazing"]
negative_words = ["sad", "bad", "depressed", "bored", "angry", "annoyed","cooked","dead"]

class Animo:
    def ask(self):
        # Pregunta al jugador
        mc.postToChat("How are you today? (Type something)")

        while True:  # Bucle infinito esperando respuesta
            # Revisa los mensajes del chat
            chat_messages = mc.events.pollChatPosts()

            # Si hay mensajes en el chat, los procesamos
            if chat_messages:
                # Filtrar mensajes positivos
                positive_responses = list(filter(lambda x: any(word in x.message.lower() for word in positive_words), chat_messages))
                negative_responses = list(filter(lambda x: any(word in x.message.lower() for word in negative_words), chat_messages))

                # Si encontramos respuestas positivas
                if positive_responses:
                    mc.postToChat("I'm happy for you!")
                    break  # Termina la función después de responder

                # Si encontramos respuestas negativas
                elif negative_responses:
                    mc.postToChat("I'm sorry to hear that.")
                    break  # Termina la función después de responder
                else
                    mc.postToChat("I don't understand you")

            time.sleep(1)  # Espera un segundo antes de revisar nuevamente

# Crear una instancia de la clase y llamar a la función
animo = Animo()
animo.ask()
