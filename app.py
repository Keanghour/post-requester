import requests
import time
import logging

# ========== Configuration ==========
# URL = "https://example.com/api"  # TODO: Replace with your actual endpoint
# JSON_BODY = {
#     "key1": "value1",
#     "key2": "value2"
# }
# HEADERS = {
#     "Content-Type": "application/json",
#     "User-Agent": "MyRequestScript/1.0"
# }

# ========== Configuration ==========
URL = "https://httpbin.org/post"
JSON_BODY = {
    "name": "Alice",
    "email": "alice@example.com",
    "message": "Hello, this is a test!"
}
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "DemoTestBot/1.0 (+mailto:your.email@example.com)"
}


MAX_ATTEMPTS = 100
DELAY_SECONDS = 1
TIMEOUT_SECONDS = 10

# ========== Logging Setup ==========
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

# ========== Core Request Function ==========
def send_post_request(url, data, headers):
    try:
        response = requests.post(url, json=data, headers=headers, timeout=TIMEOUT_SECONDS)
        return response
    except requests.exceptions.Timeout:
        logging.warning("Request timed out.")
    except requests.exceptions.ConnectionError:
        logging.error("Connection error occurred.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Unhandled exception: {e}")
    return None

# ========== Main Loop ==========
def main():
    attempt = 0

    while attempt < MAX_ATTEMPTS:
        attempt += 1
        logging.info(f"Sending attempt #{attempt}...")

        response = send_post_request(URL, JSON_BODY, HEADERS)

        if response is None:
            logging.warning("No response received. Retrying after delay...")
            time.sleep(DELAY_SECONDS)
            continue

        logging.info(f"Received status code: {response.status_code}")

        if response.status_code == 403:
            logging.error("Received 403 Forbidden. Stopping...")
            break
        elif response.status_code == 200:
            logging.info("Request successful. Status 200 OK.")
        else:
            logging.warning(f"Unexpected status code: {response.status_code}")
            # Optionally print response text for debug:
            # logging.debug(f"Response body: {response.text}")

        time.sleep(DELAY_SECONDS)

    logging.info("Finished sending requests.")

# ========== Entry Point ==========
if __name__ == "__main__":
    main()
