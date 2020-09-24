# ---------------------------------------------------- #
# Dem generator by Makw aka https://vk.com/id264444807 #
#                !!! SHITCODE ALERT !!!                #
# ---------------------------------------------------- #

from PIL import Image, ImageDraw, ImageFont
import textwrap


class Generator:
    def __init__(self):
        self.img = None

    def create(self, img: Image, top_text: str, bottom_text="", copyright_="", max_size: int = 1280,
               min_size: int = 720) -> Image:
        self.img = img.convert("RGBA")
        self.__resize_image(max_size, min_size)
        h, w = self.img.size

        if w > h:
            border_width = round(w * 8 / 100)
            scale = w * 1 / 100
        else:
            border_width = round(h * 8 / 100)
            scale = h * 1 / 100

        top_font, top_multiline_text = self.__wrap_text("fonts/times-new-roman.ttf", round(border_width * 1.5), top_text)
        bottom_font, bottom_multiline_text = self.__wrap_text("fonts/tahoma.ttf", round(border_width * 0.6), bottom_text)

        copyright_font = ImageFont.truetype("fonts/fulbo.otf", round(scale))

        copyright_h, copyright_w = copyright_font.getsize(copyright_)
        top_h, top_w = top_font.getsize_multiline(top_multiline_text)

        bottom_h, bottom_w = bottom_font.getsize_multiline(bottom_multiline_text)

        background = Image.new("RGB", (border_width * 3 + h, w + top_w + bottom_w + border_width * 3))
        background_h, background_w = background.size

        background.paste(self.img, (round((background_h - h) / 2), border_width), self.img)

        d = ImageDraw.Draw(background)

        d.rectangle(((background_h - h) / 2 - (scale * 1.1), border_width - (scale * 1.1),      # Image outline
                    (background_h + h) / 2 + (scale * 1.1), (w + border_width) + (scale * 1.1)),
                    width=round(scale * 42 / 100))

        d.rectangle(((background_h - h) / 2 - copyright_w / 4, (w + border_width),           # Copyright background
                     (background_h - h) / 2 + copyright_h + copyright_w / 4,
                     (w + border_width + copyright_w)), fill=0)

        d.text(((background_h - h) / 2, (w + border_width) + copyright_w / 4),               # Copyright text
               text=copyright_,
               font=copyright_font)

        d.multiline_text(((background_h - top_h) / 2, w + round(border_width * 1.7)),               # Top text
                         text=top_multiline_text,
                         font=top_font,
                         align="center")
        d.multiline_text(((background_h - bottom_h) / 2, w + round(border_width * 2.1) + top_w),   # Bottom text
                         text=bottom_multiline_text,
                         font=bottom_font,
                         align="center")

        return background

    """Proportional resize an image by min & max size"""
    def __resize_image(self, max_size, min_size):
        h, w = self.img.size

        if h > max_size or w > max_size:
            if h > w:
                new_w = round(w / (h / max_size))
                self.img = self.img.resize((max_size, new_w))
            else:
                new_h = round(h / (w / max_size))
                self.img = self.img.resize((new_h, max_size))

        elif h < min_size and w < min_size:
            if h > w:
                new_w = round(w * (min_size / h))
                self.img = self.img.resize((min_size, new_w))
            else:
                new_h = round(h * (min_size / w))
                self.img = self.img.resize((new_h, min_size))

    def __wrap_text(self, font_name: str, font_size: int, text: str):
        font = ImageFont.truetype(font_name, font_size)
        text_height = font.getsize_multiline(text)[0]
        font_size = font.size
        x = 0

        while text_height > self.img.size[0]:
            font_size -= round(font_size * 0.02)
            font = ImageFont.truetype(font_name, font_size)
            text_height = font.getsize_multiline(text)[0]

            if x >= font_size:
                y = text_height / self.img.size[0]
                text = textwrap.fill(text, round(len(text) / y))
                return font, text
            x += 1

        return font, text
