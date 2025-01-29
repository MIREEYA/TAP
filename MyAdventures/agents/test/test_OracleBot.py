# agents/test/OracleBotTest.py
import unittest, pytest
from unittest.mock import MagicMock
from agents.OracleBot import OracleBot  

class TestOracleBot(unittest.TestCase):
    def setUp(self):
        # Crear un mock de Minecraft para evitar interacciones reales
        self.mc_mock = MagicMock()
        self.bot = OracleBot()  # No pasamos el mock aquí
        self.bot.mc = self.mc_mock  # Asignamos manualmente el mock
        

    def test_respond_to_known_question(self):
        question = "hello"
        event = MagicMock()
        event.message = question
        self.mc_mock.events.pollChatPosts = MagicMock(return_value=[event])
        self.bot.listen_and_respond(test_mode=True)
        self.mc_mock.postToChat.assert_any_call("Hi there!")
    
    def test_respond_to_unknown_question(self):
        question = "what is the meaning of life?"
        event = MagicMock()
        event.message = question
        self.mc_mock.events.pollChatPosts = MagicMock(return_value=[event])
        self.bot.listen_and_respond(test_mode=True)
        self.mc_mock.postToChat.assert_any_call("I'm sorry, my programmer was too lazy to design a response to that kind of question ;)")

    def test_multiple_questions(self):
        questions = ["hello", "how are you", "what's your name", "what is the meaning of life?", "bye"]
        for question in questions:
            event = MagicMock()
            event.message = question
            self.mc_mock.events.pollChatPosts = MagicMock(return_value=[event])
            self.bot.listen_and_respond(test_mode=True)
            if question == "hello":
                self.mc_mock.postToChat.assert_any_call("Hi there!")
            elif question == "how are you":
                self.mc_mock.postToChat.assert_any_call("I'm doing well, thank you for asking")
            elif question == "what's your name":
                self.mc_mock.postToChat.assert_any_call("I am the OracleBot, wise and all-knowing")
            else:
                self.mc_mock.postToChat.assert_any_call("I'm sorry, my programmer was too lazy to design a response to that kind of question ;)")

    def test_shutdown_on_bye(self):
        # Simula un mensaje "bye"
        question = "bye"
        
        # Crea un evento de chat simulado
        event = MagicMock()
        event.message = question
        self.mc_mock.events.pollChatPosts = MagicMock(return_value=[event])
        
        # Llama a listen_and_respond con test_mode=True
        self.bot.listen_and_respond(test_mode=True)
        
        # Verifica que se haya enviado el mensaje de despedida
        self.mc_mock.postToChat.assert_any_call("Goodbye!")
        self.mc_mock.postToChat.assert_any_call("OracleBot shutting down. Returning to main menu...")
    

if __name__ == "__main__":
    unittest.main()
