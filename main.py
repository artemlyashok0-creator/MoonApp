from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation
from plyer import notification
import random

class MoonAppUI(BoxLayout):
    def __init__(self, **kwargs):
        super(MoonAppUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        self.is_dark_theme = True

        self.themes_content = {
            "night": [
                {"text": "Світло Місяця сьогодні особливо яскраве.", "image": "https://images.pexels.com/photos/1168899/pexels-photo-1168899.jpeg"},
                {"text": "Тиша ночі дарує простір для великих думок.", "image": "https://images.pexels.com/photos/3560044/pexels-photo-3560044.jpeg"},
                {"text": "Система функціонує в ідеальному ритмі завдяки тобі.", "image": "https://images.pexels.com/photos/1287145/pexels-photo-1287145.jpeg"}
            ],
            "day": [
                {"text": "Світло нового дня наповнює тебе енергією.", "image": "https://images.pexels.com/photos/210186/pexels-photo-210186.jpeg"},
                {"text": "Зроби перерву, ти працюєш краще, ніж будь-хто інший.", "image": "https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg"},
                {"text": "Маленькі кроки ведуть до великих звершень.", "image": "https://images.pexels.com/photos/1591447/pexels-photo-1591447.jpeg"}
            ]
        }

        with self.canvas.before:
            self.bg_color = Color(0.05, 0.05, 0.08, 1) if self.is_dark_theme else Color(0.95, 0.95, 0.95, 1)
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        current = random.choice(self.themes_content["night"])

        self.img = AsyncImage(source=current["image"], allow_stretch=True, size_hint=(1, 0.65))
        self.img.opacity = 0
        self.add_widget(self.img)

        self.label = Label(
            text="",
            font_size='18sp',
            halign='center',
            valign='middle',
            size_hint=(1, 0.2),
            color=(1, 1, 1, 1) if self.is_dark_theme else (0.1, 0.1, 0.1, 1)
        )
        self.label.opacity = 0
        self.label.bind(size=self.label.setter('text_size'))
        self.add_widget(self.label)

        self.theme_btn_label = Label(
            text="[ Тап — контент | Нижній тап — тема ]",
            font_size='11sp',
            halign='center',
            size_hint=(1, 0.15),
            color=(0.5, 0.5, 0.5, 1)
        )
        self.add_widget(self.theme_btn_label)

        self.full_text = current['text']
        self.current_index = 0
        
        # 1. Запит дозволу на сповіщення одразу при запуску додатку
        self.request_notification_permission()

        self.fade_in_content()
        self.play_background_sound()

        # 2. Запускаємо планувальник для першого рандомного пушу
        self.schedule_random_notification()

    def request_notification_permission(self):
        try:
            # Plyer викликає нативний системний діалог Android на нових версіях
            notification.notify(title="", message="", app_name="MoonApp")
        except Exception:
            pass

    def schedule_random_notification(self):
        # Генеруємо випадковий інтервал (наприклад, від 60 до 180 секунд для тесту; 
        # у реальному житті для довгих проміжків можна ставити більші значення)
        delay = random.randint(60, 180)
        Clock.schedule_once(self.send_random_push, delay)

    def send_random_push(self, dt):
        # Вибираємо випадкову тему та випадкову цитату для пушу
        theme_key = random.choice(["night", "day"])
        random_pair = random.choice(self.themes_content[theme_key])

        notification.notify(
            title="MoonApp Натхнення 🌙",
            message=random_pair['text'],
            app_name="MoonApp"
        )
        
        # Плануємо наступний випадковий пуш знову
        self.schedule_random_notification()

    def _update_bg(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size

    def fade_in_content(self):
        anim_img = Animation(opacity=1, duration=0.5)
        anim_label = Animation(opacity=1, duration=0.5)
        anim_img.start(self.img)
        anim_label.start(self.label)
        self.start_typing_effect()

    def change_content_smoothly(self, new_pair):
        anim_out_img = Animation(opacity=0, duration=0.3)
        anim_out_label = Animation(opacity=0, duration=0.3)

        def load_new_data(*args):
            self.img.source = new_pair["image"]
            self.img.reload()
            self.full_text = new_pair['text']
            self.fade_in_content()

        anim_out_img.bind(on_complete=load_new_data)
        anim_out_img.start(self.img)
        anim_out_label.start(self.label)

    def start_typing_effect(self):
        self.label.text = ""
        self.current_index = 0
        if hasattr(self, 'typing_event') and self.typing_event:
            self.typing_event.cancel()
        self.typing_event = Clock.schedule_interval(self.add_letter, 0.04)

    def add_letter(self, dt):
        if self.current_index < len(self.full_text):
            self.label.text += self.full_text[self.current_index]
            self.current_index += 1
        else:
            return False

    def play_background_sound(self):
        sound_url = "https://actions.google.com/sounds/v1/weather/rain_heavy_loud.ogg"
        self.sound = SoundLoader.load(sound_url)
        if self.sound:
            self.sound.loop = True
            self.sound.volume = 0.5
            self.sound.play()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if touch.y < self.height * 0.15:
                self.toggle_theme()
            else:
                theme_key = "night" if self.is_dark_theme else "day"
                pair = random.choice(self.themes_content[theme_key])
                self.change_content_smoothly(pair)
            return True
        return super(MoonAppUI, self).on_touch_down(touch)

    def toggle_theme(self):
        self.is_dark_theme = not self.is_dark_theme
        if self.is_dark_theme:
            self.bg_color.rgba = (0.05, 0.05, 0.08, 1)
            self.label.color = (1, 1, 1, 1)
            theme_key = "night"
        else:
            self.bg_color.rgba = (0.95, 0.95, 0.95, 1)
            self.label.color = (0.1, 0.1, 0.1, 1)
            theme_key = "day"

        pair = random.choice(self.themes_content[theme_key])
        self.change_content_smoothly(pair)

class MoonApp(App):
    def build(self):
        self.title = "MoonApp"
        return MoonAppUI()

if __name__ == "__main__":
    MoonApp().run()
