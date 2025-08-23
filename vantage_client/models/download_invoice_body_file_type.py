from enum import Enum


class DownloadInvoiceBodyFileType(str, Enum):
    CSV = "csv"
    PDF = "pdf"

    def __str__(self) -> str:
        return str(self.value)
