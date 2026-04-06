from .tasks import get_random_email
from .graders import compute_reward


class EmailTriageEnv:
    def __init__(self):
        self.current_email = None
        self.done = False

    def reset(self):
        self.current_email = get_random_email()
        self.done = False
        
        return {
            "email": self.current_email["text"]
        }

    def step(self, action):
        # safety check
        if self.current_email is None:
            return {
                "error": "Call /reset before /step"
            }

        correct = self.current_email["label"]
        reward = compute_reward(action, correct)

        self.done = True

        return {
            "observation": self.current_email["text"],
            "reward": reward,
            "done": self.done,
            "correct_label": correct,
            "info": {
                "message": "Step completed"
            }
        }
