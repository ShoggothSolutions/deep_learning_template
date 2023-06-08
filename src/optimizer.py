# === IMPORTS: THIRD-PARTY ===
from torch.utils.data import DataLoader

# === IMPORTS: LOCAL ===
from src.configs.configs import OptimizerConfig


class Optimizer:
    def __init__(self, config: OptimizerConfig):
        self.config = config

    def get_optimizer(self, model):
        # TODO: implement the method which returns your optimizer
        pass