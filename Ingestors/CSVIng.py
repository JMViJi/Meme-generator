from QuoteEngine import QuoteModel
from Ingestors.IngestorInt import IngestorInterface
import csv


class CSVIngestor(IngestorInterface):
    """Return a `QuoteModel` list from a csv file."""
    @classmethod
    def parse(cls, path):
        quotes = []
        try:
            with open(path, "r") as infile:
                reader = csv.reader(infile)
                next(reader)
                for row in reader:
                    quotes.append(QuoteModel(row[0], row[1]))
        except Exception:
            print("Something went wrong when processing .csv file")
        return quotes
