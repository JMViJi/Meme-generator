from QuoteEngine import QuoteModel
from Ingestors.IngestorInt import IngestorInterface


class TextIngestor(IngestorInterface):
    """Return a `QuoteModel` list from a txt file."""
    @classmethod
    def parse(cls, path):
        quotes = []
        try:
            with open(path, "r") as f:
                for line in f:
                    body, author = line.split(" - ")
                    quotes.append(QuoteModel(body, author.strip('\n')))
        except Exception:
            print("Something went wrong when processing .txt file")
        return quotes
