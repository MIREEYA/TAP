import unittest
from unittest.mock import MagicMock
from agents.timeBot import TimeBot
import time

class TestTimeBot(unittest.TestCase):
    def setUp(self):
        """Configura un mock para el objeto Minecraft."""
        self.mc_mock = MagicMock()
        self.bot = TimeBot(self.mc_mock)

    def test_start_sets_running(self):
        """Prueba que `start()` activa el bot."""
        # Mock del método run() para evitar el ciclo infinito
        self.bot.run = MagicMock()  # Mocking run() para evitar el ciclo infinito
        self.bot.start()
        self.assertTrue(self.bot.running)

    def test_stop_sets_running_false(self):
        """Prueba que `stop_timer()` detiene el bot."""
        self.bot.running = True
        self.bot.stop_timer()
        self.assertFalse(self.bot.running)

    def test_run_sends_time_message(self):
        """Prueba que el bot envía el mensaje de tiempo correctamente."""
        # Simulamos el paso del tiempo (2 minutos pasados)
        self.bot.start_time = time.time() - 120  # 2 minutos pasados
        
        # Hacemos mock de `time.sleep` para que no espere realmente
        with unittest.mock.patch('time.sleep', return_value=None):
            self.bot.run(iterations=1)  # Ejecutamos solo 1 iteración

        # Verificamos que `postToChat` fue llamado con el mensaje correcto
        self.mc_mock.postToChat.assert_called_with("Total time played: 2 minutes.")



if __name__ == '__main__':
    unittest.main()
