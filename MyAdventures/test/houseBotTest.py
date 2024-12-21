import unittest
from unittest.mock import MagicMock
from agents.houseBot import HouseBot 
import mcpi.block as block

class TestHouseBot(unittest.TestCase):
    def setUp(self):
        # Crear un mock de Minecraft para evitar interacciones reales
        self.mc_mock = MagicMock()
        self.bot = HouseBot(self.mc_mock)

    def test_build_house(self):
        # Llamar al método build_house y verificar que se colocan bloques correctamente
        self.bot.build_house(0, 0, 0)
        
        # Verificar que se hayan colocado bloques
        self.assertTrue(self.mc_mock.setBlock.called)
        
        # Obtener los argumentos de la llamada a setBlock
        call_args = self.mc_mock.setBlock.call_args[0]
        
        # Verificar que el bloque colocado es uno de los bloques permitidos (vidrio, madera o piedra)
        block_id = call_args[3]
        self.assertIn(block_id, [block.GLASS.id, block.WOOD.id, block.STONE.id], f"Expected block to be GLASS, WOOD, or STONE, but got {block_id}")
