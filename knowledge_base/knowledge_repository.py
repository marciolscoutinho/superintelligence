class KnowledgeRepository:
    def __init__(self):
        self.knowledge_base = {}

    def store_knowledge(self, agent_id, knowledge):
        if agent_id not in self.knowledge_base:
            self.knowledge_base[agent_id] = []
        self.knowledge_base[agent_id].append(knowledge)
        print(f"Knowledge stored by agent {agent_id}.")

    def retrieve_knowledge(self, query):
        results = []
        for agent_id, knowledge_list in self.knowledge_base.items():
            for knowledge in knowledge_list:
                if query in knowledge:
                    results.append((agent_id, knowledge))
        return results
