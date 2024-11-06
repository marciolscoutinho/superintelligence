from .base_agent import BaseAgent

class InteractionAgent(BaseAgent):
    def perform_task(self, user_input):
        print(f"InteractionAgent {self.id}: Processing user interaction.")
        return self.model.predict(user_input)
