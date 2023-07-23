import pystray
from pystray import Menu, MenuItem as Item
from draw import Draw
from reg import RegManager
import tkinter as tk


class Tray:
    app_name = ""

    def __init__(self, app_name, frequency):
        self.app_name = app_name
        self.reg = RegManager()
        self.frequency = frequency

        self.is_working = self.reg.get("IsWorking")

        self.start()

    def start(self):
        image = self.get_image()
        menu = self.get_menu()

        # Создание объекта иконки в системном трее
        self.icon = pystray.Icon("name", image, self.app_name, menu)
        self.icon.run()

    def restart(self):
        self.icon.stop()
        self.start()

    def get_image(self):
        current_fq = self.frequency.current()
        image = Draw().icon(current_fq)
        return image

    def get_menu(self):
        current_fq = self.frequency.current()

        def make_menu_item_handler(fq):
            def menu_item_handler(item):
                self.set_fq_from_menu(fq)

            return menu_item_handler

        fq_list = self.frequency.available()
        fq_submenu = [Item(f"{fq} гц", make_menu_item_handler(fq)) for fq in fq_list]

        menu = Menu(
            Item("Автоизменение частоты", self.toggle_fq_setter, checked=lambda item: self.is_working),
            Item("Доступные частоты", Menu(*fq_submenu)),
            Item(f"Текущая частота {current_fq} гц", lambda icon, item: None),
            Item("Закрыть", self.quit_window, default=True),
        )

        return menu

    def toggle_fq_setter(self):
        res = self.reg.toggle("IsWorking")
        return res

    def set_fq_from_menu(self, value):
        self.reg.set("IsWorking", 0)
        self.is_working = False
        self.frequency.set(value)
        self.icon.icon = self.get_image()

    def quit_window(self, icon, item):
        icon.stop()
