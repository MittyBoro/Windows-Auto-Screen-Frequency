import time
import threading

from frequency import Frequency
from power import Power
from tray import Tray


class App:
    app_name = "Auto Screen Frequency"

    def __init__(self):
        self.frequency = Frequency()
        self.power = Power()
        self.tray = Tray(self.app_name, self.frequency, self.power)

        self.tray_thread = threading.Thread(target=self.start_tray, args=(self.tray,))

        self.tray_thread.start()

        self.watch()

    def start_tray(self, tray):
        tray.run()

    def watch(self):
        time.sleep(1)  # дать время для tray.icon.visible
        while self.tray.icon.visible:
            if self.tray.is_watch:
                self.runIteration()

            time.sleep(2)

    def runIteration(self):
        if self.power.is_changed():
            self.tray.update(True)


app = App()
