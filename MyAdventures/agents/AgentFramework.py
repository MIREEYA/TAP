import threading
import time
import mcpi.minecraft as minecraft

# AgentFramework.py para controlar el ciclo de vida de los agents
class AgentFramework:
    def __init__(self):
        self.agents = []  # Lista para almacenar los agentes registrados
    
    def register_agent(self, agent):
        """
        Registrar agente en el framework.
        """
        self.agents.append(agent)

    def unregister_agent(self, agent):
        """
        Quitar agente del framework
        """
        self.agents.remove(agent)
    
    def run_agents(self):
        """
        iniciar agents en sus threads separados
        """
        threads = []
        for agent in self.agents:
            thread = threading.Thread(target=agent.start)
            threads.append(thread)
            thread.start()

        # Esperar threads a q acaben
        for thread in threads:
            thread.join()

    def stop_agents(self):
        """
        parar todos los agentes
        """
        for agent in self.agents:
            agent.stop()

class Agent:
    """Contrato de Agentes"""
    def __init__(self, name):
        self.name = name
        self.running = False
    
    def start(self):
        self.running = True
        self.run()

    def run(self):
        while self.running:
            time.sleep(1)  

    def stop(self):
        self.running = False


