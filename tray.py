import pystray
from PIL import Image, ImageDraw, ImageFont

class Tray:
    def __init__(self, root, frq):
      self.frq = frq
      self.root = root
      self.set_icon()

    def quit_window(self, icon, item):
      icon.stop()
      self.root.destroy()

    def show_window(self, icon, item):
      self.root.after(500, self.root.deiconify)

    def set_icon(self):
      # self.root.withdraw()

      image = self.make_number_icon(self.frq)

      # Создание меню для иконки
      menu = (
          pystray.MenuItem("Открыть", self.show_window, default=True),
          pystray.MenuItem("Выход", self.quit_window)
      )
      # Создание объекта иконки в системном трее
      self.icon = pystray.Icon("name", image, "Auto Screen Frequency", menu)
      self.icon.run()



    def make_number_icon(self, number):
      # draws the number as two digits in red on a transparent background
      img = Image.new('RGBA', (128,128), color=(0,0,0,64))
      font = ImageFont.truetype('impact.ttf', 72)
      d = ImageDraw.Draw(img)

      text = f"{number:02}"
      text_width, text_height = font.getsize(text)
      x = (img.width - text_width) // 2
      y = (img.height - text_height) // 2 - 10
      
      d.text((x, y), f"{number:02}", font=font, fill='#35C47D')

      return img