class BaseAgent:
    def __init__(self, model, agent_id):
        self.model = model
        self.id = agent_id

    def perform_task(self, data):
        raise NotImplementedError("Subclasses must implement the perform_task method")
