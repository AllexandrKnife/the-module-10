import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_time = time.time() - start_time
    print(f"{linear_time} (линейный)")

    # Многопроцессный вызов с ограничением количества процессов
    start_time = time.time()
    with Pool(processes=4) as pool:  # Укажите количество процессов
        pool.map(read_info, filenames)
    multiprocess_time = time.time() - start_time
    print(f"{multiprocess_time} (многопроцессный)")
