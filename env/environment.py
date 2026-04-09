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
            "observation": self.current_email.get("text", "")
        }

    def state(self):
        return {
            "observation": self.current_email.get("text", "") if self.current_email else ""
        }

    def step(self, action):
        try:
            if self.current_email is None:
                return "", 0.0, True, {}

            email_text = self.current_email.get("text", "")
            correct_label = self.current_email.get("label", "Low")

            reward = compute_reward(action, correct_label)

            self.done = True

            return email_text, float(reward), True, {}

        except Exception:
            return "", 0.0, True, {}
