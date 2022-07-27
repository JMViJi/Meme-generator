import subprocess
import os
from typing import List
from QuoteEngine import QuoteModel
from Ingestors.IngestorInt import IngestorInterface


class PDFIngestor(IngestorInterface):
    """Return a `QuoteModel` list from a pdf file."""
    @classmethod
    def parse(cls, path):
        quotes = []
        try:
            temp_file = './PDFtoText.txt'
            subprocess.call(['pdftotext', path, temp_file])
            file_ref = open(temp_file, "r")
            for line in file_ref.readlines():
                line = line.strip('\n').strip()
                if len(line) > 0:
                    body, author = line.split(' - ')
                    quotes.append(QuoteModel(body.strip('"'), author))

            file_ref.close()
            os.remove(temp_file)
        except Exception:
            print("Something went wrong when processing .pdf file")
        return quotes
