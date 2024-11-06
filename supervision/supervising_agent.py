class SupervisingAgent:
    def __init__(self, rules):
        self.rules = rules

    def audit_action(self, agent_id, action):
        if action in self.rules:
            print(f"Agent {agent_id} action is compliant.")
        else:
            print(f"Agent {agent_id} action violates compliance rules.")
            self.intervene(agent_id)

    def intervene(self, agent_id):
        print(f"Intervention applied to agent {agent_id}")
