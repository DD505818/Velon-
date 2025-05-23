import os
import time

def run_agent():
    print("[AGENT] DeepAgent INIT")
    print("Mode:", os.getenv("AGENT_MODE"))
    print("Execution:", os.getenv("AGENT_EXECUTION_MODEL"))
    while True:
        print("[AGENT] Scanning market with", os.getenv("STRATEGY_ENGINE"))
        time.sleep(5)

if __name__ == "__main__":
    run_agent()
