import docx
from QuoteEngine import QuoteModel
from Ingestors.IngestorInt import IngestorInterface


class DocxIngestor(IngestorInterface):
    """Return a `QuoteModel` list from a docx file."""
    @classmethod
    def parse(cls, path):
        quotes = []
        try:
            with open(path, "rb") as f:
                doc = docx.Document(f)
                for rows in doc.paragraphs:
                    data2 = rows.text.split(' - ')
                    if data2[0] == "":
                        break
                    else:
                        quotes.append(QuoteModel(data2[0].strip('"'), data2[1]))
        except Exception:
            print("Something went wrong when processing .docx file")
        return quotes
