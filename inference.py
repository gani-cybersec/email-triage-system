import requests
from agent import choose_action, learn

BASE_URL = "http://localhost:8000"

for i in range(10):
    # Step 1: Reset environment
    obs = requests.post(f"{BASE_URL}/reset").json()
    email = obs.get("email")

    # Step 2: Choose action
    action = choose_action(email)

    # Step 3: Send action to server
    result = requests.post(
        f"{BASE_URL}/step",
        json={"action": action}   # ✅ correct format
    ).json()

    # Debug print
    print("Result:", result)

    # Step 4: Get reward
    reward = result.get("reward", 0)

    # Step 5: Learn from reward
    learn(email, action, reward)

    # Output
    print("Email:", email)
    print("Action:", action)
    print("Reward:", reward)
    print("Correct:", result.get("correct_label"))
    print("------")