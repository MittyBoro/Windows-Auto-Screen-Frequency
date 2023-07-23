import pystray
from pystray import Menu, MenuItem as Item
from draw import Draw


class Tray:
    # def __init__(self, app_name, frq):
    def __init__(self):
        self.app_name = "app_name"
        self.frq = 40
        # self.root = root

        self.start()

    def start(self):
        image = Draw().icon(self.frq)

        fq_submenu = Menu(Item("Подменю 1.1", self.quit_window), Item("Подменю 1.2", self.quit_window))

        menu = (
            Item("Автозагрузка ✓", self.quit_window, default=True),
            Item("Автоизменение частоты ✓", self.quit_window),
            Item("Доступные частоты", fq_submenu),
            Item("Сейчас 144гц", False),
            Item("Выход", self.quit_window),
        )
        # Создание объекта иконки в системном трее
        self.icon = pystray.Icon("name", image, self.app_name, menu)
        self.icon.run()

    def quit_window(self, icon, item):
        icon.stop()


app = Tray()
