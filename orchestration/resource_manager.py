class ResourceManager:
    def __init__(self):
        self.resources = {}

    def allocate_resource(self, agent_id, resource_type):
        self.resources[agent_id] = resource_type
        print(f"Allocated {resource_type} to agent {agent_id}.")

    def release_resource(self, agent_id):
        if agent_id in self.resources:
            print(f"Releasing {self.resources[agent_id]} from agent {agent_id}.")
            del self.resources[agent_id]
