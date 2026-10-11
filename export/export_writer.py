from abc import ABC, abstractmethod
class ExportWriter(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def export(self, data):
        pass