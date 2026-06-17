from export_writer import ExportWriter

class ChessNotationWriter(ExportWriter):
    def export(self,seznam_tahu):
        pgn = ""
        for i, tah in enumerate(seznam_tahu):
            pgn += f"{i + 1}. {tah}\n"
