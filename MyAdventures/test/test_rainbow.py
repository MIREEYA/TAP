import unittest
from unittest.mock import MagicMock
import math
import pytest

from MyAdventures.agents.rainbowBot import RainbowBot  # Importación correcta de la clase

# Definimos el test de RainbowBot
class TestRainbowBot(unittest.TestCase):
    def setUp(self):
        # Creamos un mock del objeto Minecraft
        self.mock_mc = MagicMock()
        
        # Creamos el objeto RainbowBot usando el mock
        self.bot = RainbowBot(mc=self.mock_mc)
        
        # Simulamos la posición del jugador
        self.mock_mc.player.getTilePos.return_value = MagicMock(x=0, y=10, z=0)
        
        # Simulamos que la función getHeight siempre retorna 10 para cualquier coordenada (x, z)
        self.mock_mc.getHeight.return_value = 10
        
        # Simulamos que los bloques de la tienda de Minecraft están disponibles
        self.mock_mc.block.WOOL.id = 35  # ID de la lana (wool) en Minecraft

    def test_create_rainbow(self):
        # Llamamos al método que queremos probar
        self.bot.create_rainbow()

        # Verificamos que el método getTilePos fue llamado
        self.mock_mc.player.getTilePos.assert_called_once()
        
        # Verificamos que getHeight fue llamado con las coordenadas correctas
        self.mock_mc.getHeight.assert_called_with(0, 0)
        
        # Comprobamos que se llamaron 7 veces a setBlock (por los 7 colores del arcoíris)
        self.assertEqual(self.mock_mc.setBlock.call_count, 7 * 181)  # 7 colores, 181 bloques por color (0 a 180 grados)

        # Comprobamos que el color de la lana corresponde al primer color (rojo, ID 15)
        first_call_args = self.mock_mc.setBlock.call_args_list[0][0]

        
        # Comprobamos que la posición de los bloques esté calculada correctamente
        # Primero calculamos las coordenadas (x, y, z) para el primer bloque
        angle = 0
        radius = 25  # Radio inicial
        current_radius = radius - 0 * 2  # Para la primera capa (sin cambios en el radio)
        x = 0 + int(current_radius * math.cos(math.radians(angle)))
        
        # La altura base debe ser al menos 15 (10 del jugador + 5 bloques arriba)
        base_height = 15  # Según nuestra simulación de la altura base
        
        y = base_height + int(current_radius * math.sin(math.radians(angle)))  # Curva hacia arriba
        z = 0 + 10  # La distancia entre el arcoíris y el jugador

        # Comprobamos que las coordenadas calculadas coinciden con las primeras coordenadas de setBlock
        first_call_args = self.mock_mc.setBlock.call_args_list[0][0]
        self.assertEqual(first_call_args[0], x)
        self.assertEqual(first_call_args[1], y)  # Ahora y debería ser 15
        self.assertEqual(first_call_args[2], z)

if __name__ == "__main__":
    unittest.main()
