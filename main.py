from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import Config

Config.set('kivy', 'keyboard_mode', 'systemanddock')

Window.size = (500, 670) # выбор разрешения окна


class Container(GridLayout):
    def convert(self):
        try:
            number = int(self.text_input.text)
        except:
            number = 0
            self.text_input.text = "ошибочка"

        self.label_hours.text = str(number * 24)
        self.label_minutes.text = str(number * 1440)
        self.label_seconds.text = str(number * 86400)
        self.label_miliseconds.text = str(number * 24 * 60 * 60 * 60)  # heh))

        try:
            self.label_weeks.text = str("%.2f" % round(number / 7, 2))
        except Exception:
            self.label_weeks.text = "ошибочка"


class HourtoApp(MDApp):

    def build(self):
        self.title = "🕓・Day To"
        self.theme_cls.theme_style = "Light"
        self.icon = "assets/whitenet.png"
        return Container()


if __name__ == "__main__":
    HourtoApp().run()
