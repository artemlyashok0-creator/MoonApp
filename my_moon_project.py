# Project: My Moon
# Створюємо простір для емоцій та ефективності

import time

def start_interface():
    print("--- Початок ініціалізації системи ---")
    time.sleep(1)
    print("Завантаження модулів... [OK]")
    time.sleep(0.5)
    print("Налаштування зв'язку... [OK]")
    print("\n--- Вітаю у твоєму цифровому просторі ---\n")

if __name__ == "__main__":
    start_interface()
    import random

# Список "теплих" повідомлень для нашої системи
messages = [
    "Світло Місяця сьогодні особливо яскраве.",
    "Не забувай, що навіть маленькі кроки ведуть до великих звершень.",
    "Твоя енергія створює навколо тебе новий простір.",
    "Зроби перерву, ти працюєш краще, ніж будь-хто інший.",
    "Система функціонує в ідеальному ритмі завдяки тобі."
]

def get_thought():
    # Вибираємо випадкове повідомлення для підтримки балансу
    return random.choice(messages)

def run_nexus():
    # Основний робочий цикл нашої програми
    print("\n--- Модуль 'Nexus' активовано ---")
    thought = get_thought()
    print(f"Статус натхнення: {thought}")
    import datetime

def log_session():
    # Записуємо час запуску сесії
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("session.log", "a") as f:
        f.write(f"Session started at: {now}\n")
    print(f"--- Сесію зафіксовано: {now} ---")
if __name__ == "__main__":
    log_session()  # Записуємо початок
    start_interface()
    main_menu()
    print("\n--- Робочу сесію завершено ---")
def main_menu():
    print("\n--- Оберіть режим роботи ---")
    print("1. [Текст] - Отримати натхнення")
    print("2. [Картинка] - Візуалізація настрою")
    
    choice = input("\nВведіть номер (1 або 2): ")
    
    if choice == "1":
        # Логіка тексту
        thought = random.choice(messages)
        print(f"\n[Текст]: {thought}")
        
    elif choice == "2":
        # Логіка картинки (поки що через ASCII)
        print("\n[Картинка]: Генерую візуалізацію...")
        time.sleep(1)
        # Використовуємо tprint, якщо бібліотека art встановлена
        try:
            from art import tprint
            tprint("MOON", font="block")
        except ImportError:
            print("--- [Графічний елемент: МІСЯЦЬ] ---")
    else:
        print("\nПомилка: Невірний вибір.")

# Оновлюємо наш головний блок
if __name__ == "__main__":
    log_session()
    start_interface()
    main_menu()
    print("\n--- Сесію завершено ---")
