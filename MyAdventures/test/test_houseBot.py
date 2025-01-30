import unittest
from unittest.mock import MagicMock
from agents.houseBot import HouseBot
import mcpi.block as block

class TestHouseBot(unittest.TestCase):
    def setUp(self):
        """Configura un mock para el objeto Minecraft."""
        self.mc_mock = MagicMock()
        self.bot = HouseBot(self.mc_mock)

    def test_bot_inactive_build_house(self):
        """Prueba que el bot no construya si no está activo."""
        self.bot.running = False
        self.bot.build_house(0, 0, 0)
        self.mc_mock.postToChat.assert_called_with("HouseBot is not active!")

    def test_change_house_material(self):
        """Prueba que el material de la pared cambie correctamente."""
        self.bot.wall = block.WOOD.id  # Inicialmente madera
        self.bot.change_house()
        self.assertEqual(self.bot.wall, block.GLASS.id)  # Debe cambiar a cristal

        self.bot.change_house()
        self.assertEqual(self.bot.wall, block.WOOD.id)  # Debe volver a madera

    def test_start_activates_bot(self):
        """Prueba que `start()` activa correctamente el bot."""
        self.bot.start()
        self.assertTrue(self.bot.running)

    def test_stop_deactivates_bot(self):
        """Prueba que `stop()` detiene el bot."""
        self.bot.running = True
        self.bot.stop()
        self.assertFalse(self.bot.running)

if __name__ == '__main__':
    unittest.main()
