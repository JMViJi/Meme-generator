import os

from Ingestors.CSVIng import CSVIngestor
from Ingestors.DocxIng import DocxIngestor
from Ingestors.PDFIng import PDFIngestor
from Ingestors.TextIng import TextIngestor
from Ingestors.IngestorInt import IngestorInterface
from Ingestors.ingestor import Ingestor


# class Ingestor(IngestorInterface):
#     @classmethod
#     def parse(cls, path):
#         extension = os.path.splitext(path)
#         if extension[1] not in extensions:
#             print(f"Extension {extension[1]} not allowed")
#         elif extension[1] == extensions[0]:
#             return TextIngestor.parse(path)
#         elif extension[1] == extensions[1]:
#             return CSVIngestor.parse(path)
#         elif extension[1] == extensions[2]:
#             return PDFIngestor.parse(path)
#         elif extension[1] == extensions[3]:
#             return DocxIngestor.parse(path)
