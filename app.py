import random
import os
import requests
from flask import Flask, render_template, request
from Ingestors import Ingestor
from MemeEngine import MemeGenerator


app = Flask(__name__)

meme = MemeGenerator('./static')


def setup():
    """ Load all resources """
    quotes = []
    images_path = "./_data/photos/dog/"
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    img = "./tmp/temp_image.jpg"
    allowed_img_extensions = ['.jpeg', '.jpg', '.png']

    url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')
    img_data = requests.get(url).content
    filename, file_extension = os.path.splitext(url)
    if file_extension not in allowed_img_extensions:
        print("Url must contain a valid image")
    else:
        with open(img, 'wb') as handler:
            handler.write(img_data)
        path = meme.make_meme(img, body, author)
        os.remove(img)
        return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
