#import unittest
#from unittest.mock import MagicMock
#from MyAdventures.agents.insultBot import InsultBot 
#import pytest


#class TestInsultBot(unittest.TestCase):
  #  def setUp(self):
   #     # Crear un mock de Minecraft para evitar interacciones reales
    #    self.mc_mock = MagicMock()
     #   self.bot = InsultBot(self.mc_mock)

    #def test_insult(self):
        # Simular la llamada al método insult y verificar que el insulto se elige de la lista
     #   self.bot.insult()  
      #  insult = self.bot.mc.postToChat.call_args[0][0]  # Obtener el argumento pasado a postToChat
       # self.assertIn(insult, self.bot.insults)  # Asegurarnos de que el insulto está en la lista de insultos

    #def test_start_insulting(self):
        # Probar el comportamiento de start_insulting que genera múltiples insultos
     #   self.bot.start_insulting(count=2)
      #  self.assertEqual(self.mc_mock.postToChat.call_count, 2)  # Verificamos que se hayan enviado dos insultos
        
