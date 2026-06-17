from abc import ABC, abstractmethod
class ExportWriter(ABC):
    @abstractmethod
    def export(self, data):
        pass