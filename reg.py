import winreg
import os


class RegManager:
    def __init__(self):
        self.key_path = r"Software\AutoScreenFrequency"

    def get(self, value_name, key_path=self.key_path):
        try:
            # Открываем ключ реестра
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.key_path, 0, winreg.KEY_READ)
            # Извлекаем значение из реестра
            value, _ = winreg.QueryValueEx(registry_key, value_name)
            # Закрываем ключ реестра
            winreg.CloseKey(registry_key)

            return value
        except FileNotFoundError:
            # Если ключ или значение не найдены, возвращаем 0
            return 0

    def set(self, value_name, value_data, key_path=self.key_path, type=winreg.REG_DWORD):
        try:
            # Создаем ключ реестра
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
            # Записываем значение
            winreg.SetValueEx(key, value_name, 0, type, value_data)
            # Закрываем ключ реестра
            winreg.CloseKey(key)
        except Exception as e:
            raise ValueError("Ошибка при записи значения в реестр:", e)

    def toggle(self, value_name):
        self.set(value_name, 1 - self.get(value_name))

        return bool(self.get(value_name))
