import requests
import time
import os

if __name__ == "__main__":
    target_url = "https://formatconverterbot-multifunctional-tg-ak.onrender.com/5504002265:AAG1pUCPJXiU9N6-r0-fOEnaJ_cZ9wZQ3Dc"
    no = 1
    while True:
        requests.get(target_url)
        print("Success No:-",no)
        no += 1
        time.sleep(50)  # Sleep for 60 seconds (1 minute)
