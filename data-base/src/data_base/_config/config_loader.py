from file_work import File

class JSONConfigLoader:
    def __init__(self, folder: str):
        self.folder = folder

    def load(self, file_name: str, extension: str = "json") -> dict:
        return File.read(file_path=f"{self.folder}/{file_name}.{extension}")
