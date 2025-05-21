from ai_text_summariser.constants import * 
from ai_text_summariser.utils.common import read_yaml, create_directories
from ai_text_summariser.logging import logger
from ai_text_summariser.entity import (DataIngestionConfig)

from pathlib import Path

class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = Path(r"D:\projects\AI-Tex-Summraiser\config\config.yaml"),
        params_filepath: Path = Path(r"D:\projects\AI-Tex-Summraiser\params.ymal")
    ):
        print("Reading config from:", config_filepath)
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
