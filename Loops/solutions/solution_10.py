# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time

attempts= 1
max_retry=5
wait_time=1

while attempts <= max_retry:
    print(f"Attempt {attempts} - Wait Time {wait_time}")
    # Shut system till waiting time
    time.sleep(wait_time)
    attempts+=1
    # Wait time will be exponential
    wait_time *= 2
    