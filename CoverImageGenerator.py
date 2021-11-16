from PIL import Image, ImageDraw, ImageFont


class CoverImageGenerator:
    def __init__(self, width, height, color_bg, color_fg, emoji):
        self.width = width
        self.height = height
        self.color_fg = color_fg
        self.color_bg = color_bg
        self.emoji = emoji

    def generate(self):
        self.image = Image.new('RGB', (self.width, self.height), self.color_bg)
        self.draw_emoji()
        self.draw_attribution()
        return self.image

    def draw_emoji(self):
        draw = ImageDraw.Draw(self.image)
        font_size = int(self.height / 2)
        font = ImageFont.truetype(
            './fonts/OpenMoji-Black.ttf', font_size, encoding='unic')
        text = self.emoji
        # text_width, text_height = draw.textsize(text)
        # x = int(self.width / 2 - text_width / 2)
        # y = int(self.height / 2 - text_height / 2)
        x = self.width / 2 - font_size / 2
        y = self.height / 2 - font_size / 2
        return draw.text((x, y), text, font=font, fill=self.color_fg)

    def draw_attribution(self):
        draw = ImageDraw.Draw(self.image)
        font_size = 10
        font = ImageFont.truetype(
            './fonts/FiraCode-Regular.ttf', font_size)
        text = 'All emojis designed by OpenMoji - the open-source emoji and icon project. License: CC BY-SA 4.0'
        # text ="© 2021 David Wolf"
        text_width, text_height = draw.textsize(text)
        x = int(self.width / 2 - text_width / 2)
        y = int(self.height - text_height - font_size)
        return draw.text((x, y), text, font=font, fill=self.color_fg)