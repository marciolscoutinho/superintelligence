from .base_agent import BaseAgent
from auto_improvement.autonomous_learning import AutonomousLearning
from monitoring.alert_system import AlertSystem

class AutonomousAgent(BaseAgent):
    def __init__(self, model, agent_id, autonomous_learning, alert_system):
        super().__init__(model, agent_id)
        self.autonomous_learning = autonomous_learning
        self.alert_system = alert_system
        self.task_queue = []

    def perform_task(self, data):
        result = self.model.predict(data)
        print(f"Autonomous Agent {self.id}: Task executed.")
        self.autonomous_learning.evaluate_and_update(self, data, result)
        return result

    def add_task(self, task):
        self.task_queue.append(task)
        self.task_queue.sort(key=lambda x: x.priority, reverse=True)

    def execute_tasks(self):
        while self.task_queue:
            task = self.task_queue.pop(0)
            try:
                task.run()
                print(f"Task {task['name']} successfully executed by Autonomous Agent {self.id}")
            except Exception as e:
                self.alert_system.raise_alert(f"Error executing task {task['name']}: {e}")
