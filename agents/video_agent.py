from .base_agent import BaseAgent

class VideoAgent(BaseAgent):
    def perform_task(self, video_data):
        print(f"VideoAgent {self.id}: Analyzing video data.")
        return self.model.predict(video_data)
