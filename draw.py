import pystray
from PIL import Image, ImageDraw, ImageFont


class Draw:
    def icon(self, number, is_watch, is_plugged):
        size = (128, 128)
        background = (22, 22, 22, 230)
        corner_radius = 40

        font_family = "./src/impact.ttf"
        font_size = 72
        color = "#999"

        if is_watch:
            if is_plugged == True:
                color = "#35C47D"
            else:
                color = "#C44D35"

        # Create a transparent background
        img = Image.new("RGBA", size, color=(0, 0, 0, 0))

        # Create a rounded rectangle as the background
        rounded_rect = Image.new("RGBA", img.size)
        draw = ImageDraw.Draw(rounded_rect)
        draw.rounded_rectangle([(0, 0), rounded_rect.size], corner_radius, fill=background)

        img.paste(rounded_rect, (0, 0), mask=rounded_rect)

        font = ImageFont.truetype(font_family, font_size)
        d = ImageDraw.Draw(img)

        text = f"{number:02}"
        text_width, text_height = font.getsize(text)
        x = (img.width - text_width) // 2
        y = (img.height - text_height) // 2 - 10

        # Create a transparent text label
        text_img = Image.new("RGBA", img.size)
        text_draw = ImageDraw.Draw(text_img)
        text_draw.text((x, y), f"{number:02}", font=font, fill=color)

        # Combine the text label with the rounded-corner background
        img = Image.alpha_composite(img, text_img)

        return img
