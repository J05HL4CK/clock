import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
import datetime
from kivy.config import Config


Config.set('graphics', 'height', '600')
Config.set('graphics', 'width', '300')
Config.set('graphics', 'resizable', '0')
Config.write()

class StudyTimer(App):
    pass



if __name__ == "__main__":
    StudyTimer().run()