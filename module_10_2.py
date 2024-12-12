import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.enemies_left = 100  # Каждый рыцарь имеет свои враги

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies_left > 0:
            time.sleep(1)  # Задержка в 1 секунду (1 день)
            self.days += 1
            self.enemies_left -= self.power

            if self.enemies_left < 0:
                self.enemies_left = 0

            # Синхронизированный вывод
            with lock:
                print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies_left} воинов.")

        # Синхронизированный вывод сообщения о победе
        with lock:
            print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Блокировка для синхронизации вывода
lock = threading.Lock()

# Создание объектов класса Knight
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения обоих потоков
first_knight.join()
second_knight.join()

# Вывод строки об окончании битв
with lock:
    print("Все битвы закончились!")
