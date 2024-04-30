# /usr/bin/env python3
from sys import ar
from pathlib import Path


from shield_plex_dbbackup_2_gdrive.config import Config
# from shield_plex_dbbackup_2_gdrive.filesystems.smb import Smb



def main():
    config = Config(config_file_path)
    plex_db_backups = Smb(config)


if __name__ == '__main__':
    main()
