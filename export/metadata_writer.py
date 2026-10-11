from export.export_writer import ExportWriter

class MetaDataWriter(ExportWriter):
    def export(self,data):
        metadata = data['metadata']
        return metadata