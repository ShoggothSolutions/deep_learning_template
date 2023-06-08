# === IMPORTS: THIRD-PARTY ===
from torch import nn

# === IMPORTS: LOCAL ===
from src.configs.configs import ModelConfig


class Model(nn.Module):
    def __init__(self, config: ModelConfig):
        self.config = config
        super().__init__()

    def forward(self):
        # TODO: implement the forward pass of your model
        pass