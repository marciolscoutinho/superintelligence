class PerformanceMonitor:
    def __init__(self):
        self.performance_log = {}

    def log_performance(self, agent_id, metric, value):
        if agent_id not in self.performance_log:
            self.performance_log[agent_id] = {}
        self.performance_log[agent_id][metric] = value
        print(f"Agent {agent_id} performance logged: {metric} = {value}")

    def generate_kpi_report(self):
        report = {}
        for agent_id, metrics in self.performance_log.items():
            report[agent_id] = metrics
        print("KPI report generated.")
        return report
