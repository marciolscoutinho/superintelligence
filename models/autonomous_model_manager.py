from auto_improvement.auto_ml_manager import AutoMLManager
from auto_improvement.adaptive_learning import AdaptiveLearning

class AutonomousModelManager:
    def __init__(self, model, auto_ml_manager):
        self.model = model
        self.auto_ml_manager = auto_ml_manager
        self.adaptive_learning = AdaptiveLearning(model)

    def train_and_update(self, data, labels):
        print("Autonomous training initiated.")
        self.model = self.auto_ml_manager.optimize_model(data, labels, validation_data=(data, labels))
        self.adaptive_learning.continuous_learning(data, labels)
        print("Model autonomously updated.")
