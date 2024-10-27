from pydantic import BaseModel


class BackupFile(BaseModel):
    file_name: str
    path: str
    file_system: str
