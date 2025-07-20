# post-requester
A simple Python script to send repeated POST requests with JSON data for API testing, monitoring, and light load checking.



````markdown
# Demo POST Request Script

A Python script to send repeated POST requests with JSON data to an API endpoint.  
Ideal for **functional testing**, **basic API monitoring**, and **light load checking**.

---

## What Is This For?

- Verify your API endpoint handles requests correctly  
- Monitor API status and responses over multiple attempts  
- Perform simple stability or light load tests with configurable delay  
- Log detailed info including response codes and timing  

*Not intended for heavy load testing or unauthorized attacks.*

---

## Requirements

- Python 3.6+  
- `requests` library (`pip install requests`)

---

## Configuration

Adjust these variables in the script:

- `URL`: API endpoint URL  
- `JSON_BODY`: JSON payload to send  
- `HEADERS`: HTTP headers (e.g., Content-Type, User-Agent)  
- `MAX_ATTEMPTS`: Number of requests to send  
- `DELAY_SECONDS`: Seconds to wait between requests  
- `TIMEOUT_SECONDS`: Request timeout in seconds  
- `SHOW_RESPONSE`: Set to `True` to print response body  

---

## Usage

Run the script:

```bash
python your_script_name.py
````

The script logs each request’s status, timing, and a summary at the end.

---

## Notes

* Use responsibly and only on APIs you own or have permission to test
* Adjust delay to avoid rate limits or server overload
* For heavy load tests, consider tools like Locust or JMeter

---

## License

MIT License

---

## Contact

[phokeanghour12@gmail.com](phokeanghour12@gmail.com)

```
