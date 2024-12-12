import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0  # Инициализация баланса
        self.lock = threading.Lock()  # Создание объекта блокировки

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Генерация случайного числа для пополнения
            self.balance += amount  # Увеличение баланса
            print(f"Пополнение: {amount}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():  # Проверка условия для разблокировки
                self.lock.release()  # Разблокировка потока
            time.sleep(0.001)  # Имитация скорости выполнения

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Генерация случайного числа для снятия
            print(f"Запрос на {amount}")
            if amount <= self.balance:  # Проверка возможности снятия
                self.balance -= amount  # Уменьшение баланса
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()  # Блокировка потока

# Создание объекта класса Bank
bk = Bank()

# Создание и запуск потоков
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

# Вывод итогового баланса
print(f'Итоговый баланс: {bk.balance}')
