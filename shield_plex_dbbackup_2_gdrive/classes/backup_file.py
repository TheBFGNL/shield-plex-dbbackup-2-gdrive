from pydantic import BaseModel


class BackupFile(BaseModel):
    file_name: str
    path: str
    file_system: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BackupFile):
            return NotImplemented
        return self.file_name == other.file_name
