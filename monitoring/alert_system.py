class AlertSystem:
    def __init__(self):
        self.alerts = []

    def raise_alert(self, message):
        self.alerts.append(message)
        print(f"Alert: {message}")

    def get_all_alerts(self):
        return self.alerts
