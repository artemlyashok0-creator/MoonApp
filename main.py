import os
import json
import requests

class MoonApp:
    def __init__(self):
        self.assets = "assets"
        self.config_file = "settings.json"
        self.api_key = self.load_api_key()
        self.running = True

    def load_api_key(self):
        try:
            with open(self.config_file, 'r') as f:
                data = json.load(f)
                return data.get("api_key")
        except FileNotFoundError:
            print("Помилка: файл settings.json не знайдено.")
            return None

    def test_connection(self):
        if not self.api_key:
            print("Помилка: API ключ відсутній.")
            return

        url = "https://api.pexels.com/v1/search?query=nature&per_page=1"
        headers = {"Authorization": self.api_key}

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print("--- Зв'язок з API успішний! ---")
            else:
                print(f"Помилка з'єднання: {response.status_code}")
        except Exception as e:
            print(f"Помилка запиту: {e}")

    def start(self):
        if not os.path.exists(self.assets):
            os.makedirs(self.assets)
        print("--- System Online ---")
        self.test_connection()

    def process_visual(self):
        print("Виклик модуля візуалізації...")
        # Тут згодом буде логіка запиту до API для отримання фото

    def run(self):
        while self.running:
            try:
                choice = input("\n[1] Статус API\n[2] Візуалізація\n[0] Вихід: ")
                
                if choice == "1":
                    self.test_connection()
                elif choice == "2":
                    self.process_visual()
                elif choice == "0":
                    self.running = False
                else:
                    print("Невірний запит.")
            except Exception as e:
                print(f"Помилка системи: {e}")

if __name__ == "__main__":
    app = MoonApp()
    app.start()
    app.run()


