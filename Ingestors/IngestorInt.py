from abc import ABC, abstractmethod

extensions = ['.txt', '.csv', '.pdf', '.docx']


class IngestorInterface(ABC):

    @classmethod
    def can_ingest(cls, path: str):
        return path in extensions

    @abstractmethod
    def parse(cls, path: str):
        pass
