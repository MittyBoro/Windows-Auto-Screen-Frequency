from power import Power

from tray import Tray
from frequency import Frequency


class App:
    app_name = "Auto Screen Frequency"

    def __init__(self):
        self.power = Power()
        self.frequency = Frequency()
        self.tray = Tray(self.app_name, self.frequency)

    # def update_data(self):
    #     # меняем инфу в начале
    #     self.type_label.config(text=f"Тип питания: {self.power.text()}")
    #     self.frequency_label.config(text=f"Частота экрана: {self.frequency.current()}Гц")

    #     # меняем частоту экрана, если меняется тип питания
    #     if self.power.is_changed():
    #         self.set_frequency()

    #     self.root.after(2000, self.update_data)

    def set_frequency(self):
        if not self.power.is_plugged():
            self.frequency.set_new(int(self.battery_entry.get()))
        else:
            self.frequency.set_new(int(self.plugged_entry.get()))


app = App()
