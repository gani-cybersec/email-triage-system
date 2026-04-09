import requests
import time
import os

# ✅ IMPORTANT: dynamic base URL
BASE_URL = os.environ.get("BASE_URL", "http://localhost:8000")


def wait_for_server():
    for _ in range(10):
        try:
            r = requests.get(f"{BASE_URL}/health")
            if r.status_code == 200:
                return True
        except:
            pass
        time.sleep(1)
    return False


def run():
    try:
        if not wait_for_server():
            raise Exception("Server not ready")

        # RESET
        r = requests.post(f"{BASE_URL}/reset")
        r.raise_for_status()
        data = r.json()

        email = data["observation"]["email"]

        # Valid action
        action = "High"

        # STEP → triggers LLM
        r = requests.post(
            f"{BASE_URL}/step",
            json={"action": action}
        )
        r.raise_for_status()
        result = r.json()

        print("[START] task=email_triage")
        print(f"[STEP] step=1 reward={result['reward']}")
        print(f"[END] task=email_triage score={result['reward']} steps=1")

    except Exception as e:
        print("ERROR:", str(e))
        print("[START] task=email_triage")
        print("[STEP] step=1 reward=0.0")
        print("[END] task=email_triage score=0.0 steps=1")


if __name__ == "__main__":
    for _ in range(3):
        run()
