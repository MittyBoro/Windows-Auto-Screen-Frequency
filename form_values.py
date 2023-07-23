import tkinter as tk
from tkinter import messagebox
from reg_manager import RegManager


class FormValues:
    def __init__(self, battery_entry, plugged_entry):
        self.reg = RegManager()

        self.battery_entry = battery_entry
        self.plugged_entry = plugged_entry

        self.set_form_values()

    def save_registry_values(self):
        try:
            battery_frequency = int(self.battery_entry.get())
            plugged_frequency = int(self.plugged_entry.get())

            self.reg.set("BatteryFrequency", battery_frequency)
            self.reg.set("PluggedFrequency", plugged_frequency)

            self.set_form_values()

            messagebox.showinfo("Успешно", "Данные успешно сохранены!")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при сохранении данных: {str(e)}")

    def set_form_values(self):
        battery_frequency_value = self.reg.get("BatteryFrequency")
        plugged_frequency_value = self.reg.get("PluggedFrequency")

        self.battery_entry.delete(0, tk.END)
        self.plugged_entry.delete(0, tk.END)
        self.battery_entry.insert(tk.END, battery_frequency_value)
        self.plugged_entry.insert(tk.END, plugged_frequency_value)
