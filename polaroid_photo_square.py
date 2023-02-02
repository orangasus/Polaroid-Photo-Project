from polaroid_photo import Polaroid_Photo
import textwrap
from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw, ImageFont


class Polaroid_Photo_Square(Polaroid_Photo):
    def __init__(self, image, filename):
        super().__init__(image, filename)

        self.crop_image()
        self.resize_image()
        self.apply_filters_to_image()
        self.create_a_border()
        if not self.should_write_date:
            self.write_date_on_picture()
        self.write_title_on_picture()

    def crop_image(self):
        width, height = self.image.size
        if width == height:
            pass
        offset = int(abs(height - width) / 2)
        if width > height:
            self.image = self.image.crop([offset, 0, width - offset, height])
        else:
            self.image = self.image.crop([0, offset, width, height - offset])

    def resize_image(self):
        total_width, total_height = 1080, 1290
        new_width, new_height = round(total_width * 0.92), round(total_width * 0.92)
        self.image = ImageOps.contain(self.image, (new_width, new_height))

    def create_a_border(self):
        total_width, total_height = 1080, 1290
        new_width, new_height = self.image.width, self.image.height
        offset_y, offset_x = round(total_height * 0.07), round((total_width - new_width) // 2)

        border = Image.new("RGB", size=(total_width, total_height), color=(255, 255, 255))
        border.paste(self.image, (offset_x, offset_y))
        self.image = border

    def write_title_on_picture(self):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype(r"C:\Users\Gleb\PycharmProjects\Polaroid_Photo\fonts\patrick-hand.ttf", size=50)
        symbols_in_line = 40

        list_of_lines = textwrap.wrap(self.name, symbols_in_line)
        formatted_text = ""
        for i in range(len(list_of_lines) - 1):
            formatted_text += list_of_lines[i] + "\n"
        formatted_text += list_of_lines[len(list_of_lines) - 1]

        center_x, center_y = self.image.width // 2, round(self.image.width * 0.92 + self.image.height * 0.07
                                                          + (self.image.height - (self.image.width * 0.92
                                                                                  + self.image.height * 0.07)) // 2)
        draw.multiline_text(anchor='mm', xy=(center_x, center_y), text=formatted_text, align='center', font=font,
                            fill=(0, 0, 0))

    def write_date_on_picture(self):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype(r"C:\Users\Gleb\PycharmProjects\Polaroid_Photo\fonts\patrick-hand.ttf", size=35)
        text = f"{self.date}"
        text_length = draw.textlength(text, font)
        offset_x, offset_y = self.image.width * 0.96 - text_length, self.image.height * 0.95
        draw.text(text=text, xy=(offset_x, offset_y), fill=(0, 0, 0), font=font)

    def apply_filters_to_image(self):
        new_image = self.image.convert('P', palette=Image.ADAPTIVE, colors=256)
        new_image = new_image.convert('RGB')
        col_ehc = ImageEnhance.Color(new_image)
        bright_ehc = ImageEnhance.Brightness(new_image)
        new_image = col_ehc.enhance(1.4)
        new_image = bright_ehc.enhance(1.15)
        new_image = new_image.filter(ImageFilter.GaussianBlur(1.15))
        self.image = new_image
