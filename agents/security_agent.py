from .base_agent import BaseAgent

class SecurityAgent(BaseAgent):
    def perform_task(self, system_logs):
        print(f"SecurityAgent {self.id}: Monitoring system logs.")
        return self.model.predict(system_logs)
