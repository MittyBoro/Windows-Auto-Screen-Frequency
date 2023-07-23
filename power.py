import psutil


class Power:
    current = None

    def __init__(self):
        self.current = self.is_plugged()

    def is_plugged(self):
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        return plugged

    def is_changed(self):
        new_value = self.is_plugged()
        if self.current != new_value:
            self.current = new_value
            return True

        return False
