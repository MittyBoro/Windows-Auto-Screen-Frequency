import psutil
import win32api

class Frequency:

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
