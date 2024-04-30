#!/usr/bin/env python3
from pathlib import Path
from configparser import ConfigParser

class Config:
    """
    Represents a configuration object that loads settings from a config file.
    
    Args:
        config_file_path (Path): The path to the config file.
    """
    
    def __init__(self, config_file_path: Path) -> None:
        self.config_file_path = config_file_path
        self.load_config(self.config_file_path)  
        
    
    def load_config(self, config_file_path: Path):
        """
        Loads the settings from the config file.
        
        Args:
            config_file_path (Path): The path to the config file.
        """
        config = ConfigParser()
        config.read_file(open(config_file_path))

        for setting, value in config['settings'].items():
            setattr(self, setting, value)
       
        
        
        
    

   
