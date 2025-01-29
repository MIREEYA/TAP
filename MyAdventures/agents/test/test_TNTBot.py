import unittest, pytest
from unittest.mock import MagicMock
from agents.TNTBot import TNTBot

class TestTNTBot(unittest.TestCase):
    def setUp(self):
        # Crear un mock de Minecraft para evitar interacciones reales
        self.mc_mock = MagicMock()
        
        # Simular la posición del jugador
        self.mc_mock.player.getTilePos.return_value = MagicMock(x=10, y=64, z=10)
        
        self.bot = TNTBot(self.mc_mock)

    def test_deploy_near_player(self):
        # Llamar al método deploy_near_player y verificar que se cree TNT en la posición correcta
        self.bot.deploy_near_player(count=3)  # Cambia el count si es necesario

        # Verificar que se haya llamado a setBlock
        self.mc_mock.setBlock.assert_called()

        # Obtener todas las llamadas a setBlock
        calls = self.mc_mock.setBlock.call_args_list
        
        # Imprimir las llamadas para depuración
        for call in calls:
            print(call)

        # Verificar que se colocó TNT en las posiciones esperadas.
        player_position = (10, 64, 10)  # Suponiendo que la posición del jugador sea (10, 64, 10)
        
        # Verifica que las posiciones del TNT sean correctas
        for i in range(3):  # Comprobamos 3 TNT, puedes ajustarlo si usas un count diferente
            expected_position = (player_position[0] + i * 2, player_position[1], player_position[2])
            print(f"Expected Position: {expected_position}")

            # Verificar que se colocó TNT en la posición esperada
            self.mc_mock.setBlock.assert_any_call(*expected_position, 46)  # 46 es el ID de TNT

        # Verificar que se colocó fuego encima de cada TNT
        for i in range(3):
            expected_fire_position = (player_position[0] + i * 2, player_position[1] + 1, player_position[2])
            self.mc_mock.setBlock.assert_any_call(*expected_fire_position, 51)  # 51 es el ID de fuego
