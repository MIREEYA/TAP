import unittest
from unittest.mock import MagicMock, patch
import mcpi.block as block
from agents.TNTBot import TNTBot


class TestTNTBot(unittest.TestCase):
    def setUp(self):
        """Configura un mock para el objeto Minecraft."""
        self.mc_mock = MagicMock()
        self.bot = TNTBot(self.mc_mock)

    def test_place_tnt_places_tnt_block(self):
        """Prueba que `place_tnt()` coloca un bloque de TNT y activa el fuego."""
        # Configura la posición de TNT
        x, y, z = 10, 20, 30
        self.bot.place_tnt(x, y, z)

        # Verificar
        self.mc_mock.setBlock.assert_any_call(x, y, z, block.TNT.id)
        self.mc_mock.setBlock.assert_any_call(x, y + 1, z, block.FIRE.id)

        # Verifica que los mensajes 
        self.mc_mock.postToChat.assert_any_call(f"TNT placed at ({x}, {y}, {z})!")
        self.mc_mock.postToChat.assert_any_call("Boom!")

    @patch.object(TNTBot, 'place_tnt')  # Mockea place_tnt dentro de TNTBot
    def test_deploy_near_player_places_tnt(self, mock_place_tnt):
        """Prueba que `deploy_near_player()` coloca TNT cerca del jugador."""
        # Simula la posición del jugador
        self.mc_mock.player.getTilePos.return_value = MagicMock(x=10, y=20, z=30)

        self.bot.deploy_near_player(count=2)

        # Verifica que `place_tnt()` fue llamada dos veces con las posiciones correctas
        mock_place_tnt.assert_any_call(10, 20, 30)  # Primera posición
        mock_place_tnt.assert_any_call(12, 20, 30)  # Segunda posición (con desplazamiento)

        # Verifica que el mensaje 
        self.mc_mock.postToChat.assert_any_call("Deploying TNT near the player...")

    def test_start_starts_bot(self):
        """Prueba que `start()` activa el bot."""
        self.bot.start()
        self.assertTrue(self.bot.running)

    def test_stop_stops_bot(self):
        """Prueba que `stop()` detiene el bot."""
        self.bot.running = True
        self.bot.stop()
        self.assertFalse(self.bot.running)


if __name__ == '__main__':
    unittest.main()
