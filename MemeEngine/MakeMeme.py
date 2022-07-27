import os
import random
from PIL import Image, ImageDraw, ImageFont
from QuoteEngine import QuoteModel


class MemeGenerator:

    def __init__(self, out_path):
        self.out_path = out_path
        if not os.path.exists(out_path):
            os.makedirs(out_path)

    def load_image(self, img_path, width):
        """ Loads an image"""
        with Image.open(img_path, "r") as img:
            w, h = img.size
            relation = h/w
            image = img.resize((width, int(width*relation)))
        return image

    def add_quote(self, img, body, author):
        """  Adds Quote text to an image"""
        quote = QuoteModel(body, author)
        draw = ImageDraw.Draw(img)
        text_size = int(img.size[1]/30)
        font = ImageFont.truetype("./_data/Fonts/LilitaOne-Regular.ttf", text_size)
        quote_text = f'"{quote.body}" - {quote.author}'
        draw.text((text_size, img.size[1]*0.92), quote_text, font=font, fill='white')
        return img

    def make_meme(self, img_path, text, author, width=500):
        """ Generate a image with a quote"""
        outfile = os.path.join(self.out_path, f"_new_image{random.randint(0,1000)}.jpeg")
        img_resized = MemeGenerator.load_image(self, img_path, width)
        img_with_quote = MemeGenerator.add_quote(self, img_resized, text, author)
        img_with_quote.save(outfile, "JPEG")
        return outfile
