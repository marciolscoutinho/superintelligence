from .base_agent import BaseAgent

class ScienceAgent(BaseAgent):
    def perform_task(self, scientific_data):
        print(f"ScienceAgent {self.id}: Conducting scientific research.")
        return self.model.predict(scientific_data)
