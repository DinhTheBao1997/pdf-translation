from django.core.files.base import File

class FileUpload:
    file: File
    def __init__(self, FILES) -> None:
        self.file = FILES["file_upload"]
