import unittest
from unittest.mock import MagicMock, patch
from MyAdventures.agents.timeBot import TimeBot

class TestTimeBot(unittest.TestCase):
    def setUp(self):
        self.mc_mock = MagicMock()
        self.bot = TimeBot(self.mc_mock)
    
    def test_initial_state(self):
        self.assertFalse(self.bot.running)
        self.assertIsInstance(self.bot.start_time, float)
    
    def test_stop(self):
        #ponemos true para simular que esta en ejecucion
        self.bot.running = True
        self.bot.stop()
        self.assertFalse(self.bot.running)

if __name__ == '__main__':
    unittest.main()
