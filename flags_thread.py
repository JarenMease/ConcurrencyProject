import os
import time
import requests
from concurrent.futures import ThreadPoolExecutor

start_time = time.perf_counter()

# Create flags directory if it doesn't exist
if not os.path.exists('flags'):
    os.mkdir('flags')

total_bytes = 0
with open('flags.txt', 'r') as f:
    countries = [line.strip() for line in f]


def download_flag(country):
    url = f'https://www.sciencekids.co.nz/images/pictures/flags680/{country.replace(" ", "_")}.jpg'
    response = requests.get(url)
    with open(f'flags/{country}.jpg', 'wb') as f:
        f.write(response.content)
    return len(response.content)


with ThreadPoolExecutor(max_workers=4) as executor:
    bytes_list = list(executor.map(download_flag, countries))
    total_bytes = sum(bytes_list)

elapsed_time = time.perf_counter() - start_time

# Write output to file
with open('flags_thread.out', 'w') as f:
    f.write(f'Elapsed time: {elapsed_time}\n{total_bytes} bytes downloaded')
