from .base_agent import BaseAgent

class DataAgent(BaseAgent):
    def perform_task(self, data):
        print(f"DataAgent {self.id}: Performing data analysis.")
        return self.model.predict(data)
