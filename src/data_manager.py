# === IMPORTS: THIRD-PARTY ===
from torch.utils.data import DataLoader

# === IMPORTS: LOCAL ===
from src.configs.configs import DataConfig


class DataManager:
    def __init__(self, config: DataConfig):
        self.config = config

    def get_data(self) -> DataLoader:
        # TODO: implement the method which returns your DataLoader
        pass