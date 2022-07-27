import os

from Ingestors.CSVIng import CSVIngestor
from Ingestors.DocxIng import DocxIngestor
from Ingestors.PDFIng import PDFIngestor
from Ingestors.TextIng import TextIngestor
from Ingestors.IngestorInt import IngestorInterface


class Ingestor(IngestorInterface):

    @classmethod
    def parse(cls, path):
        filename, file_extension = os.path.splitext(path)
        if not cls.can_ingest(file_extension):
            print(f"File extension {file_extension} not allowed")
        if file_extension == ".txt":
            return TextIngestor.parse(path)
        if file_extension == ".docx":
            return DocxIngestor.parse(path)
        if file_extension == ".pdf":
            return PDFIngestor.parse(path)
        if file_extension == ".csv":
            return CSVIngestor.parse(path)
