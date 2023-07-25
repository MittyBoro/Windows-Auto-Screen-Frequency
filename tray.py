import pystray
from pystray import Menu, MenuItem as Item
from draw import Draw
from reg import RegManager
import os


class Tray:
    current_fq = 0

    def __init__(self, frequency, power):
        self.reg = RegManager()
        self.frequency = frequency
        self.power = power

        self.is_watch = self.reg.get("Watch")
        self.current_fq = self.frequency.current()

        image = self.get_image()
        menu = self.get_menu()
        self.icon = pystray.Icon(os.getenv("APP_NAME"), image, os.getenv("APP_NAME"), menu)

    def run(self):
        self.icon.run()

    def update(self, power_is_changed=False):
        if power_is_changed:
            self.frequency.set_by_power(self.power.is_plugged())

        self.current_fq = self.frequency.current()
        self.icon.icon = self.get_image()

    def get_image(self):
        image = Draw().icon(self.current_fq, self.is_watch, self.power.is_plugged())
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
        self.is_watch = bool(res)
        self.update(self.is_watch)

    def set_fq_from_menu(self, value):
        self.reg.set("Watch", 0)
        self.is_watch = False
        self.frequency.set(value)
        self.update()

    def quit_window(self, icon, item):
        icon.stop()
        icon.visible = False
