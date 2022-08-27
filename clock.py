from kivy.app import App
from time import strftime
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.audio import SoundLoader

Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '300')
Config.set('graphics', 'resizable', '0')
Config.write()

class StudyClock(App):

    default_period = 1500
    focus_period = default_period
    break_period = 300
    rest_period = 900
    timer_on = False


    def format_time(self):
        """return formatted string of mins and secs"""
        self.mins, self.secs = divmod(self.focus_period,60)
        time = f"{self.mins}:{self.secs}"
        return(time)


    def toggle_state(self):
        """Toggle the state of timer/btn on/off"""
        if self.timer_on:
            self.root.ids.start_button.text =  "Start"
        else:
            self.root.ids.start_button.text = "Stop"
        self.timer_on =  not self.timer_on


    def reset(self):
        """Timer off and period reset to default"""
        self.timer_on = False
        self.focus_period = self.default_period
        self.root.ids.counter.text = strftime('25:00')


    def update_time(self,delta):
        self.root.ids.time.text = strftime('[b]%I:%M[/b]:%S %p')
        if self.timer_on and self.focus_period > 0:
            self.focus_period -= delta
            mins, secs = divmod(self.focus_period,60)
            self.root.ids.counter.text = f'{int(mins):02}:{int(secs):02}'
        elif self.focus_period == 0:
            self.timer_On = False


    def on_start(self):
        Clock.schedule_interval(self.update_time, 0)



if __name__ == '__main__':
    from kivy.core.window import Window
    from kivy.utils import get_color_from_hex    
    Window.clearcolor = get_color_from_hex('#010101')    
    StudyClock().run()

