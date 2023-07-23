import psutil


class Power:
    def __init__(self):
        self.old_value = self.is_plugged()

    def is_plugged(self):
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        return plugged

    def text(self):
        if self.is_plugged():
            return 'От сети'
        else:
            return 'От батареи'

    def is_changed(self):
        result = self.old_value is not 0 and self.old_value != self.is_plugged()
        self.old_value = self.is_plugged()
        return result
