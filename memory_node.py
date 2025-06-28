class MemoryManager:
    def __init__(self):
        self.memory = {
            "Scientist": [],
            "Philosopher": []
        }

    def update_memory(self, agent, argument):
        """Add argument to that agent’s memory"""
        if agent in self.memory:
            self.memory[agent].append(argument)

    def get_memory(self, agent):
        """Return only that agent’s memory"""
        return self.memory.get(agent, [])
