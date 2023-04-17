import os
import requests
import time
import multiprocessing


def download_flag(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    return len(response.content)


def download_all_flags(country_list):
    if not os.path.exists('flags'):
        os.makedirs('flags')
    total_bytes = 0
    for name in country_list:
        url = f'https://www.sciencekids.co.nz/images/pictures/flags680/{name}.jpg'
        filename = f'flags/{name}.jpg'
        total_bytes += download_flag(url, filename)
    return total_bytes


if __name__ == '__main__':
    with open('flags.txt') as f:
        country_list = f.read().splitlines()

    start_time = time.perf_counter()
    with multiprocessing.Pool() as pool:
        total_bytes = sum(pool.map(download_all_flags, [country_list]))

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    with open('flags_smp.out', 'w') as f:
        f.write(f'Elapsed time: {elapsed_time:.8f}\n{total_bytes} bytes downloaded\n')
