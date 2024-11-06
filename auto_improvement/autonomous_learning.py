class AutonomousLearning:
    def __init__(self, model_manager):
        self.model_manager = model_manager

    def evaluate_and_update(self, agent, data, result):
        if self.is_underperforming(result):
            print(f"Auto-adjustment initiated for agent {agent.id}.")
            self.model_manager.train_and_update(data, result)

    def is_underperforming(self, result):
        return result < 0.75
