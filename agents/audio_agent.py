from .base_agent import BaseAgent

class AudioAgent(BaseAgent):
    def perform_task(self, audio_data):
        print(f"AudioAgent {self.id}: Processing audio data.")
        return self.model.predict(audio_data)
