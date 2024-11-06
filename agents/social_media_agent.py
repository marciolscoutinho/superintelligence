from .base_agent import BaseAgent

class SocialMediaAgent(BaseAgent):
    def perform_task(self, social_data):
        print(f"SocialMediaAgent {self.id}: Analyzing social media data.")
        return self.model.predict(social_data)
