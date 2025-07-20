import requests
import time
import logging

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
# DELAY_SECONDS = 1
DELAY_SECONDS = 0.1
TIMEOUT_SECONDS = 10
SHOW_RESPONSE = False  # Set to True to print response body

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
        start = time.time()
        response = requests.post(url, json=data, headers=headers, timeout=TIMEOUT_SECONDS)
        duration = time.time() - start
        return response, duration
    except requests.exceptions.Timeout:
        logging.warning("⏱️ Request timed out.")
    except requests.exceptions.ConnectionError:
        logging.error("🔌 Connection error occurred.")
    except requests.exceptions.RequestException as e:
        logging.error(f"⚠️ Unhandled exception: {e}")
    return None, None

# ========== Main Execution ==========
def main():
    attempt = 0
    success_count = 0
    failure_count = 0
    total_start_time = time.time()

    while attempt < MAX_ATTEMPTS:
        attempt += 1
        logging.info(f"🚀 Attempt #{attempt}...")

        response, duration = send_post_request(URL, JSON_BODY, HEADERS)

        if response is None:
            failure_count += 1
            logging.warning(f"❌ No response. Retrying after delay...")
            time.sleep(DELAY_SECONDS)
            continue

        status_code = response.status_code
        if status_code == 200:
            success_count += 1
            logging.info(f"✅ Success [200 OK] in {duration:.2f}s.")
        elif status_code == 403:
            failure_count += 1
            logging.error(f"🛑 Forbidden [403] in {duration:.2f}s. Stopping...")
            break
        else:
            failure_count += 1
            logging.warning(f"⚠️ Unexpected status: {status_code} in {duration:.2f}s.")

        if SHOW_RESPONSE:
            logging.info(f"📦 Response Body: {response.text}")

        time.sleep(DELAY_SECONDS)

    total_duration = time.time() - total_start_time
    logging.info("\n====== ✅ Test Summary ======")
    logging.info(f"🔁 Total attempts: {attempt}")
    logging.info(f"✅ Successful:     {success_count}")
    logging.info(f"❌ Failed:         {failure_count}")
    logging.info(f"⏱️ Total duration:  {total_duration:.2f}s")
    logging.info("🧼 Finished sending requests.")

# ========== Entry Point ==========
if __name__ == "__main__":
    main()
