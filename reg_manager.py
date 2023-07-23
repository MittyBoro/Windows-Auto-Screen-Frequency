import winreg

class RegManager:
    def __init__(self):
        self.key_path = r"Software\ScreenFrequency"

    def get(self, value_name):
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

    def set(self, value_name, value_data):
        try:
            # Создаем ключ реестра
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, self.key_path)
            # Записываем значение
            winreg.SetValueEx(key, value_name, 0, winreg.REG_DWORD, value_data)
            # Закрываем ключ реестра
            winreg.CloseKey(key)
        except Exception as e:
            raise ValueError("Ошибка при записи значения в реестр:", e)