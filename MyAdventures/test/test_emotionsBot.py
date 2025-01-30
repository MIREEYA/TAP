import unittest
from unittest.mock import MagicMock
from agents.emotionsBot import EmotionBot 

class TestEmotionBot(unittest.TestCase):
    def setUp(self):
        """Configura un mock de Minecraft y una instancia de EmotionBot en test_mode."""
        self.mc_mock = MagicMock()
        self.bot = EmotionBot(self.mc_mock, test_mode=True)

    def test_positive_emotion(self):
        """Prueba que el bot responde con un mensaje positivo cuando detecta palabras positivas."""
        self.mc_mock.events.pollChatPosts.return_value = [MagicMock(message="I'm feeling good!")]
        self.bot.ask_about_emotion()
        self.mc_mock.postToChat.assert_any_call("I'm happy for you!")

    def test_negative_emotion(self):
        """Prueba que el bot responde con empatía cuando detecta palabras negativas."""
        self.mc_mock.events.pollChatPosts.return_value = [MagicMock(message="I'm very sad today.")]
        self.bot.ask_about_emotion()
        self.mc_mock.postToChat.assert_any_call("I'm sorry to hear that.")

    def test_unknown_emotion(self):
        """Prueba que el bot responde adecuadamente a palabras desconocidas."""
        self.mc_mock.events.pollChatPosts.return_value = [MagicMock(message="I like pizza!")]
        self.bot.ask_about_emotion()
        self.mc_mock.postToChat.assert_any_call("I don't understand you.")

    def test_stop_on_bye(self):
        """Prueba que el bot se detiene cuando recibe 'bye'."""
        self.mc_mock.events.pollChatPosts.return_value = [MagicMock(message="bye")]
        self.bot.ask_about_emotion()
        self.mc_mock.postToChat.assert_any_call("Goodbye! EmotionBot shutting down.")
        self.assertFalse(self.bot.running)

if __name__ == "__main__":
    unittest.main()
