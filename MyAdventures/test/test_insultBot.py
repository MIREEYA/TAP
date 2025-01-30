import unittest
from unittest.mock import MagicMock
from MyAdventures.agents.insultBot import InsultBot

class TestInsultBot(unittest.TestCase):
    def setUp(self):
        """Configura un mock para el objeto Minecraft."""
        self.mc_mock = MagicMock()
        self.bot = InsultBot(self.mc_mock)

    def test_insult_sends_message(self):
        """Prueba que `insult()` envía un mensaje al chat."""

        self.bot.insult()
        
        # postToChat ha sido llamado ?
        self.mc_mock.postToChat.assert_called_once()

    def test_insult_message_is_valid(self):
        """Prueba que el insulto enviado es un string válido de la lista."""
        self.bot.insult()
        insult_sent = self.mc_mock.postToChat.call_args[0][0]  # Obtiene el primer argumento de la llamada
        self.assertIn(insult_sent, self.bot.insults)

    def test_start_sets_running(self):
        """Prueba que `start()` activa el bot."""
        # Parar ciclo infinito con mock de run() para evitar loop
        self.bot.run = MagicMock()  # Mocking run() 
        self.bot.start()
        self.assertTrue(self.bot._running)

    def test_stop_sets_running_false(self):
        """Prueba que `stop()` detiene el bot."""
        self.bot._running = True
        self.bot.stop()
        self.assertFalse(self.bot._running)

if __name__ == '__main__':
    unittest.main()
