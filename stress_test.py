import requests
import time
from concurrent.futures import ThreadPoolExecutor

URL = "http://localhost:8080/visit"
NUM_REQUESTS = 1000
CONCURRENT_WORKERS = 100

def hit_api():
    try:
        response = requests.post(URL)
        return response.status_code
    except:
        return "error"

start = time.time()
with ThreadPoolExecutor(max_workers=CONCURRENT_WORKERS) as executor:
    results = list(executor.map(lambda _: hit_api(), range(NUM_REQUESTS)))

end = time.time()
print(f"Total requests: {len(results)}")
print(f"Successful: {results.count(200)}")
print(f"Failed: {results.count('error')}")
print(f"Time taken: {end - start:.2f} seconds")