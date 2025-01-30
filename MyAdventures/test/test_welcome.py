import unittest
from unittest.mock import MagicMock
import mcpi.minecraft as minecraft
from agents.welcome import Person

class TestPerson(unittest.TestCase):
    def test_welcome_asks_for_name(self):
        # Crear un mock para minecraft y el evento
        mc_mock = MagicMock(spec=minecraft.Minecraft)
        
        # Crear un mock para events y asignarlo al mc_mock
        events_mock = MagicMock()
        mc_mock.events = events_mock
        
        ready_event_mock = MagicMock() 
        # Crear instancia de Person usandomocks
        person = Person(mc_mock, ready_event_mock)
        
        # Simular 
        events_mock.pollChatPosts.return_value = [MagicMock(message="John")]
        
        person.welcome()
        
        ready_event_mock.set.assert_called_once()  # Verifica que el set() se haya llamado una vez
        mc_mock.postToChat.assert_any_call("Hello, John!")  # Verifica que el saludo se haya enviado al chat

if __name__ == '__main__':
    unittest.main()
