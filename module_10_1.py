import threading
from datetime import datetime
from time import sleep


# Функция для записи слов в файл с паузами
def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Пауза 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")


# Измерение времени выполнения функций
start_time_functions = datetime.now()

# Запуск функций последовательно
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

end_time_functions = datetime.now()
print(f"Работа функций: {end_time_functions - start_time_functions}")

# Измерение времени выполнения потоков
start_time_threads = datetime.now()

# Создание и запуск потоков
threads = []
for wc, fn in [(10, "example5.txt"), (30, "example6.txt"), (200, "example7.txt"), (100, "example8.txt")]:
    thread = threading.Thread(target=write_words, args=(wc, fn))
    threads.append(thread)
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

end_time_threads = datetime.now()
print(f"Работа потоков: {end_time_threads - start_time_threads}")
