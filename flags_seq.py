import os
import time
import requests

start_time = time.perf_counter()

# Create flags directory if it doesn't exist
if not os.path.exists('flags'):
    os.mkdir('flags')

total_bytes = 0
with open('flags.txt', 'r') as f:
    for line in f:
        country = line.strip()
        url = f'https://www.sciencekids.co.nz/images/pictures/flags680/{country.replace(" ", "_")}.jpg'
        response = requests.get(url)
        with open(f'flags/{country}.jpg', 'wb') as f:
            f.write(response.content)
        total_bytes += len(response.content)

elapsed_time = time.perf_counter() - start_time

# Write output to file
with open('flags_seq.out', 'w') as f:
    f.write(f'Elapsed time: {elapsed_time}\n{total_bytes} bytes downloaded')
