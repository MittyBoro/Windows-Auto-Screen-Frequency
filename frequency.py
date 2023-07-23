import win32api
import time


class Frequency:
    values = None

    def current(self):
        dm = win32api.EnumDisplaySettings(None, -1)
        rate = dm.DisplayFrequency
        return rate

    def set(self, rate):
        if self.current() == rate:
            return
        win32api.ChangeDisplaySettings(None, 0)
        win32api.ChangeDisplaySettings(None, 0)
        dm = win32api.EnumDisplaySettings()
        dm.DisplayFrequency = rate
        win32api.ChangeDisplaySettings(dm, 0)

    def set_by_power(self, is_plugged=False):
        if is_plugged:
            self.set(self.max())
        else:
            self.set(self.min())

    def available(self):
        if self.values:
            return self.values

        refresh_rates = set()
        device = 0  # Индекс монитора (0 для основного монитора)
        device_name = win32api.EnumDisplayDevices(None, device, 0)

        i = 0
        while True:
            try:
                device_settings = win32api.EnumDisplaySettingsEx(device_name.DeviceName, i)
                refresh_rates.add(device_settings.DisplayFrequency)
                i += 1
            except:
                break

        self.values = refresh_rates
        return sorted(refresh_rates)

    def min(self):
        return min(self.available())

    def max(self):
        return max(self.available())
