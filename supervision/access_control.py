class AccessControl:
    def __init__(self):
        self.permissions = {}

    def set_permission(self, agent_id, permission_level):
        self.permissions[agent_id] = permission_level

    def check_permission(self, agent_id, required_level):
        if self.permissions.get(agent_id, 0) >= required_level:
            print(f"Agent {agent_id} has permission level {required_level}.")
            return True
        else:
            print(f"Agent {agent_id} does NOT have permission level {required_level}.")
            return False
