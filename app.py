import tkinter as tk

from power import Power
from tray import Tray
from frequency import Frequency
from form_values import FormValues


class App:
    def __init__(self):
        
        self.power = Power()
        self.frequency = Frequency()

        self.set_form()

        self.update_data()
        self.set_frequency()

        # self.set_tray()
        # self.root.protocol('WM_DELETE_WINDOW', self.set_tray)
        
        self.root.resizable(width=False, height=False)

        # self.root.iconbitmap("favicon.ico")
        self.root.mainloop()

    def set_tray(self):
        Tray(self.root, self.frequency.current())
    
    def set_form(self):
        # заголовок окна
        self.root = tk.Tk()
        self.root.title("Auto Screen Frequency")
        self.root.resizable(0, 0)
        
        # текст с информацией
        self.type_label = tk.Label(self.root, width=30)
        self.type_label.pack(padx=10, pady=[15, 5])
        self.frequency_label = tk.Label(self.root)
        self.frequency_label.pack(padx=10, pady=[0, 10])
        
        # данные
        self.battery_label = tk.Label(self.root, text="Частота экрана в режиме батареи:")
        self.battery_label.pack(padx=10, pady=5)
        self.battery_entry = tk.Entry(self.root, width=25)
        self.battery_entry.pack(padx=10, pady=5)
        
        self.plugged_label = tk.Label(self.root, text="Частота экрана в режиме питания:")
        self.plugged_label.pack(padx=10, pady=5)
        self.plugged_entry = tk.Entry(self.root, width=25)
        self.plugged_entry.pack(padx=10, pady=5)

        self.form_values = FormValues(self.battery_entry, self.plugged_entry)

        self.save_button = tk.Button(self.root, text="Сохранить", command=self.click_save_button)
        self.save_button.pack(padx=10, pady=[10, 15])


    
    def update_data(self):
        # меняем инфу в начале
        self.type_label.config(text=f"Тип питания: {self.power.text()}")
        self.frequency_label.config(text=f"Частота экрана: {self.frequency.current()}Гц")
        
        # меняем частоту экрана, если меняется тип питания
        if self.power.is_changed():
            self.set_frequency()
        
        self.root.after(2000, self.update_data)

    def set_frequency(self):
        if not self.power.is_plugged():
            self.frequency.set_new(int(self.battery_entry.get()))
        else:
            self.frequency.set_new(int(self.plugged_entry.get()))

    def click_save_button(self): 
        self.form_values.save_registry_values()
        self.set_frequency()



app = App()
