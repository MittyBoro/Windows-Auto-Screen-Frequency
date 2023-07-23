import psutil
import win32api


class Frequency:
    values = null
    current = null

    def current(self):
        dm = win32api.EnumDisplaySettings(None, -1)
        return dm.DisplayFrequency

    def set_new(self, rate):
        # if (self.current == rate):
        #     return
        win32api.ChangeDisplaySettings(None, 0)
        win32api.ChangeDisplaySettings(None, 0)
        dm = win32api.EnumDisplaySettings()
        dm.DisplayFrequency = rate
        win32api.ChangeDisplaySettings(dm, 0)

    def available(self):
        if values:
            return values

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

        values = refresh_rates
        return refresh_rates

    def min(self):
        return min(self.available())

    def max(self):
        return max(self.available())
