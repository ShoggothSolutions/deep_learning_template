# === IMPORTS: BUILT-IN ===
from dataclasses import dataclass

# === IMPORTS: THIRD-PARTY ===
import torch


@dataclass
class LossConfig:
    param: float = 0.0


@dataclass
class TrainerConfig:
    num_epochs: int = 100
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    folder: str = "trained_models"


@dataclass
class OptimizerConfig:
    lr: float = 1e-3


@dataclass
class ModelConfig:
    device: str = "cuda" if torch.cuda.is_available() else "cpu"


@dataclass
class DataConfig:
    device: str = "cuda" if torch.cuda.is_available() else "cpu"