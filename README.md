# Meme generator

The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote. 

## Description
* Module for reading quotes from files with various formats. (.docx, .txt, .csv, .pdf)
* Module for generating memes 
* Creation of memes, with the option of random meme or customized, through: 
    * Command line.
    * Web app


## Getting Started

### Dependencies

All required dependencies can be installed with pip:
```
pip install -r requirements.txt
```
### Installing
A copy of the project is accessible via this link:
```
git clone https://github.com/jmvj/meme_generator.git
```

### Executing program

#### Command line
* Run meme.py from command line
* Arguments can be passed to generate a custom meme, otherwise a random meme is generated from a collection of images and quotes.


```
python meme.py [-h] [--body BODY] [--author AUTHOR] [--path PATH]


Arguments:
  -h, --help       help message 
  --body BODY      quote text
  --author AUTHOR  quote author
  --path PATH      path to the image 
```

#### Flask

* Run app.py from command line
* Take the url generated and paste it on a browser.
* Open a web browser and paste the url generated while running the app.py
* Two options ares presented to the users:
  * Generate a random meme.
  * Create a meme with custom image, quote and author.
* Result is showed on screen.

```
python app.py
```

