#/usr/bin/env python3
from smbclient import register_session, listdir
from filesystem import FileSystem

class Smb(FileSystem):
    def __init__(self, 
                 username: str,
                 path: str,
                 password: str) -> None:
        super().__init__(username, path)
        self.password = password

    def list_files(self):
        register_session(self.path, username=self.username, password=self.password)
        return listdir(self.path)

    def __str__(self) -> str:
        return f"Smb: {self.path}"
