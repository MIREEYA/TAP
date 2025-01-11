import unittest
from unittest.mock import MagicMock
from MyAdventures.agents.emotionsBot import Emotion  # Asegúrate de importar correctamente tu clase Emotion


class TestEmotion(unittest.TestCase):
    def setUp(self):
        # Inicializamos el mock para la conexión de Minecraft
        self.mc_mock = MagicMock()
        
        # Creamos una instancia de la clase Emotion, pasando el mock de Minecraft
        self.emotion = Emotion(self.mc_mock)

        # Configuramos los valores que se van a usar en las pruebas
        self.delay = 2  # Tiempo entre la colocación y la activación

    def test_positive_response(self):
        # Creamos un mensaje simulado que contiene una palabra positiva
        message = MagicMock()
        message.message = "I feel fantastic today!"
        
        # Simulamos que este mensaje es recibido en el chat
        self.mc_mock.events.pollChatPosts = MagicMock(return_value=[message])

        # Llamamos al método ask() que debería responder al mensaje
        self.emotion.ask()

        # Verificamos que se haya enviado la respuesta "I'm happy for you!"
        self.mc_mock.postToChat.assert_any_call("I'm happy for you!")

    def test_negative_response(self):
        # Creamos un mensaje simulado que contiene una palabra negativa
        message = MagicMock()
        message.message = "I feel bad today."
        
        # Simulamos que este mensaje es recibido en el chat
        self.mc_mock.events.pollChatPosts = MagicMock(return_value=[message])

        # Llamamos al método ask() que debería responder al mensaje
        self.emotion.ask()

        # Verificamos que se haya enviado la respuesta "I'm sorry to hear that."
        self.mc_mock.postToChat.assert_any_call("I'm sorry to hear that.")

    def test_neutral_response(self):
        # Creamos un mensaje que no contiene palabras positivas ni negativas
        message = MagicMock()
        message.message = "Just here."
        
        # Simulamos que este mensaje es recibido en el chat
        self.mc_mock.events.pollChatPosts = MagicMock(return_value=[message])

        # Llamamos al método ask() que debería responder al mensaje
        self.emotion.ask()

        # Verificamos que se haya enviado la respuesta "I don't understand you"
        self.mc_mock.postToChat.assert_any_call("I don't understand you")

    def test_no_message(self):
        # Simulamos que no hay mensajes en el chat
        self.mc_mock.events.pollChatPosts = MagicMock(return_value=[])

        # Llamamos al método ask() que debería enviar solo la pregunta
        self.emotion.ask()

        # Verificamos que se haya enviado solo la pregunta
        self.mc_mock.postToChat.assert_any_call("How are you today? (Type something)")


if __name__ == '__main__':
    unittest.main()
