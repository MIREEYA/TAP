import unittest
from unittest.mock import MagicMock
from agents.emotionsBot import EmotionBot

class TestEmotionBot(unittest.TestCase):
    def setUp(self):
        """Configura un mock para el objeto Minecraft."""
        self.mc_mock = MagicMock()
        self.bot = EmotionBot(self.mc_mock)

    def test_positive_emotion(self):
        """Prueba que el bot responde con un mensaje positivo."""
        self.mc_mock.events.pollChatPosts.return_value = [MagicMock(message="I feel fantastic")]
        self.bot.ask_about_emotion()
        
        # Ignorar el primer mensaje del bot
        self.mc_mock.postToChat.assert_any_call("How are you today? (Type something)")
        self.mc_mock.postToChat.assert_any_call("I'm happy for you!")


    def test_negative_emotion(self):
        """Prueba que el bot responde con un mensaje de empatía."""
        self.mc_mock.events.pollChatPosts.return_value = [MagicMock(message="I am very sad")]
        self.bot.ask_about_emotion()

        # Ignorar el primer mensaje del bot
        self.mc_mock.postToChat.assert_any_call("How are you today? (Type something)")
        self.mc_mock.postToChat.assert_called_with("I'm sorry to hear that.")

    def test_unknown_emotion(self):
        """Prueba que el bot responde adecuadamente a palabras desconocidas."""
        self.mc_mock.events.pollChatPosts.return_value = [MagicMock(message="I am confused")]
        self.bot.ask_about_emotion()

        # Ignorar el primer mensaje del bot
        self.mc_mock.postToChat.assert_any_call("How are you today? (Type something)")
        self.mc_mock.postToChat.assert_called_with("I don't understand you.")

    def test_stop_on_bye(self):
        """Prueba que el bot se detiene cuando recibe 'bye'."""
        self.mc_mock.events.pollChatPosts.return_value = [MagicMock(message="bye")]
        self.bot.ask_about_emotion()
        self.assertFalse(self.bot.running)

        # Ignorar el primer mensaje del bot
        self.mc_mock.postToChat.assert_any_call("How are you today? (Type something)")
        self.mc_mock.postToChat.assert_called_with("Goodbye! EmotionBot shutting down.")

if __name__ == '__main__':
    unittest.main()
