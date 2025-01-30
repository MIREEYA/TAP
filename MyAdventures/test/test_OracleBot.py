from unittest.mock import MagicMock
import unittest
from MyAdventures.agents.OracleBot import OracleBot

class TestOracleBot(unittest.TestCase):
    def setUp(self):
        # Mocking Minecraft instancia
        self.mc_mock = MagicMock()
        self.mc_mock.events.pollChatPosts.return_value = [] 
        self.bot = OracleBot(self.mc_mock)

    def test_respond_to_known_question(self):
        # Simular
        event = MagicMock()
        event.message = "hello"
        self.mc_mock.events.pollChatPosts = MagicMock(return_value=[event])

        # metodo
        self.bot.listen_for_questions(test_mode=True)

        # Verificar
        self.mc_mock.postToChat.assert_any_call("Hi there!")

    def test_respond_to_unknown_question(self):
        # Simular pregunta que no sabe el bot
        event = MagicMock()
        event.message = "what is the meaning of life?"
        self.mc_mock.events.pollChatPosts = MagicMock(return_value=[event])

        # metodo
        self.bot.listen_for_questions(test_mode=True)

        # Verificar
        self.mc_mock.postToChat.assert_any_call("I'm sorry, my programmer was too lazy to design a response to that kind of question")

    def test_shutdown_on_bye(self):
        # Simular bye
        event = MagicMock()
        event.message = "bye"
        self.mc_mock.events.pollChatPosts = MagicMock(return_value=[event])

        # metodo
        self.bot.listen_for_questions(test_mode=True)

        # Verificar
        self.mc_mock.postToChat.assert_any_call("Goodbye! OracleBot shutting down.")
