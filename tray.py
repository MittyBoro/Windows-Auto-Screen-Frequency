import pystray
from pystray import Menu, MenuItem as Item
from draw import Draw
from reg import RegManager
from power import Power


class Tray:
    app_name = ""
    current_fq = 0

    def __init__(self, app_name, frequency):
        self.app_name = app_name
        self.reg = RegManager()
        self.frequency = frequency

        self.is_watch = self.reg.get("Watch")
        self.current_fq = self.frequency.current()

        self.start()

    def start(self):
        image = self.get_image()
        menu = self.get_menu()

        # Создание объекта иконки в системном трее
        self.icon = pystray.Icon(self.app_name, image, self.app_name, menu)
        self.icon.run()

    def restart(self):
        self.current_fq = self.frequency.current()
        self.icon.icon = self.get_image()

    def get_image(self):
        image = Draw().icon(self.current_fq, self.is_watch, Power().is_plugged())
        return image

    def get_menu(self):
        def make_menu_item_handler(fq):
            def menu_item_handler(item):
                self.set_fq_from_menu(fq)

            return menu_item_handler

        def get_menu_item_handler(item):
            return

        fq_list = self.frequency.available()
        fq_submenu = [
            Item(
                f"{fq} гц",
                make_menu_item_handler(fq),
                checked=lambda item: item.text.find(str(self.current_fq)) == 0,
                radio=True,
            )
            for fq in fq_list
        ]

        menu = Menu(
            Item("Автоизменение частоты", self.toggle_setter, checked=lambda item: self.is_watch, default=True),
            Menu.SEPARATOR,
            *fq_submenu,
            Menu.SEPARATOR,
            Item("Закрыть", self.quit_window),
        )

        return menu

    def toggle_setter(self):
        res = self.reg.toggle("Watch")
        self.is_watch = res
        self.frequency.set(int(Power().is_plugged()))
        self.restart()

    def set_fq_from_menu(self, value):
        self.reg.set("Watch", 0)
        self.is_watch = False
        self.frequency.set(value)
        self.restart()

    def quit_window(self, icon, item):
        icon.stop()
