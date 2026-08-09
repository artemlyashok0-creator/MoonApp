from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random

class MoonAppUI(BoxLayout):
    def __init__(self, **kwargs):
        super(MoonAppUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        # Список повідомлень для натхнення
        self.messages = [
            "Світло Місяця сьогодні особливо яскраве.",
            "Не забувай, що навіть маленькі кроки ведуть до великих звершень.",
            "Твоя енергія створює навколо тебе новий простір.",
            "Зроби перерву, ти працюєш краще, ніж будь-хто інший.",
            "Система функціонує в ідеальному ритмі завдяки тобі."
        ]

        # Заголовок / текст на екрані
        self.label = Label(
            text="--- Вітаю у твоєму\nцифровому просторі ---",
            font_size='20sp',
            halign='center',
            valign='middle'
        )
        self.label.bind(size=self.label.setter('text_size'))
        self.add_widget(self.label)

        # Кнопка для зміни тексту
        self.btn = Button(
            text="Отримати натхнення",
            font_size='18sp',
            size_hint=(1, 0.3)
        )
        self.btn.bind(on_press=self.update_message)
        self.add_widget(self.btn)

    def update_message(self, instance):
        # Вибираємо випадкове повідомлення при натисканні
        new_thought = random.choice(self.messages)
        self.label.text = f"[Текст]:\n{new_thought}"

class MoonApp(App):
    def build(self):
        self.title = "MoonApp"
        return MoonAppUI()

if __name__ == "__main__":
    MoonApp().run()
