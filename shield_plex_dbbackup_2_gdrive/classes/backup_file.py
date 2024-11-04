"""
This module defines the BackupFile class for representing backup files.

Classes:
    BackupFile: A Pydantic BaseModel class for representing backup files.
"""

from pydantic import BaseModel

class BackupFile(BaseModel):
    """
    A Pydantic BaseModel class for representing backup files.

    Attributes:
        file_name (str): The name of the file.
        path (str): The path to the file.
        file_system (str): The file system where the file is stored.
    """

    file_name: str
    path: str
    file_system: str

    def __eq__(self, other: object) -> bool:
        """
        Checks if two BackupFile instances are equal based on their file names.

        Args:
            other (object): The other object to compare.

        Returns:
            bool: True if the file names are equal, False otherwise.
        """
        if not isinstance(other, BackupFile):
            return NotImplemented
        return self.file_name == other.file_name
