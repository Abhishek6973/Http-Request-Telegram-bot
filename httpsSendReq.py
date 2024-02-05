import requests
import time
import os

if __name__ == "__main__":
    target_url = os.getenv("LIVE_URL")
    next_target_url = os.getenv("SEC_LIVE_URL")
    no = 1
    while True:
        requests.get(target_url)
        ak = requests.get(next_target_url)
        print(ak.text)
        print("Success No:-",no)
        no += 1
        time.sleep(50)  # Sleep for 60 seconds (1 minute)
