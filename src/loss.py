# === IMPORTS: THIRD-PARTY ===
from torch import nn

# === IMPORTS: LOCAL ===
from src.configs.configs import LossConfig


class Loss(nn.Module):
    def __init__(self, config: LossConfig):
        self.config = config
        super().__init__()

    def __call__(self):
        # TODO: Implement your loss function
        pass