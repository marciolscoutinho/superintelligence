from supervision.feedback_system import FeedbackSystem
from monitoring.performance_monitor import PerformanceMonitor

class AutonomousSupervisor:
    def __init__(self):
        self.feedback_system = FeedbackSystem()
        self.performance_monitor = PerformanceMonitor()

    def audit_agent(self, agent_id, action, context):
        if not self.is_compliant(action, context):
            self.feedback_system.apply_feedback(agent_id, action)
            print(f"Autonomous intervention applied to agent {agent_id}.")

    def is_compliant(self, action, context):
        return action in ["Access Allowed", "Safe Task"]

    def monitor_performance(self, agent_id, metric, value):
        self.performance_monitor.log_performance(agent_id, metric, value)
        if value < 0.8:
            self.feedback_system.adjust_agent_parameters(agent_id)
            print(f"Performance adjustment made for agent {agent_id}.")
