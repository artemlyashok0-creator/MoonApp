from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.core.audio import SoundLoader
import random

class MoonAppUI(BoxLayout):
    def __init__(self, **kwargs):
        super(MoonAppUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        self.content_pairs = [
            {
                "text": "Світло Місяця сьогодні особливо яскраве.",
                "image": "https://images.pexels.com/photos/1168899/pexels-photo-1168899.jpeg"
            },
            {
                "text": "Не забувай, що навіть маленькі кроки ведуть до великих звершень.",
                "image": "https://images.pexels.com/photos/210186/pexels-photo-210186.jpeg"
            },
            {
                "text": "Твоя енергія створює навколо тебе новий простір.",
                "image": "https://images.pexels.com/photos/3560044/pexels-photo-3560044.jpeg"
            },
            {
                "text": "Зроби перерву, ти працюєш краще, ніж будь-хто інший.",
                "image": "https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg"
            },
            {
                "text": "Система функціонує в ідеальному ритмі завдяки тобі.",
                "image": "https://images.pexels.com/photos/1287145/pexels-photo-1287145.jpeg"
            }
        ]

        current = random.choice(self.content_pairs)

        self.img = AsyncImage(source=current["image"], allow_stretch=True, size_hint=(1, 0.75))
        self.add_widget(self.img)

        self.label = Label(
            text=current['text'],
            font_size='18sp',
            halign='center',
            valign='middle',
            size_hint=(1, 0.25)
        )
        self.label.bind(size=self.label.setter('text_size'))
        self.add_widget(self.label)

        # Запускаємо фонову музику (тут використано приклад аудіо з відкритих джерел)
        self.play_background_sound()

    def play_background_sound(self):
        # Приклад посилання на розслаблюючий звук (можна замінити на своє або локальний файл)
        sound_url = "https://actions.google.com/sounds/v1/weather/rain_heavy_loud.ogg"
        
        self.sound = SoundLoader.load(sound_url)
        if self.sound:
            self.sound.loop = True  # Робимо зациклення, щоб шум грав постійно
            self.sound.volume = 0.5 # Гучність (від 0.0 до 1.0)
            self.sound.play()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            pair = random.choice(self.content_pairs)
            self.img.source = pair["image"]
            self.img.reload()
            self.label.text = pair['text']
            return True
        return super(MoonAppUI, self).on_touch_down(touch)

class MoonApp(App):
    def build(self):
        self.title = "MoonApp"
        return MoonAppUI()

if __name__ == "__main__":
    MoonApp().run()
